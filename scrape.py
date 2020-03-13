from time import sleep
import sys
import os
from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options


if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} [series_url] [output_directory]")

series_url = sys.argv[1]
output_directory = sys.argv[2]

firefoxProfile = FirefoxProfile()
firefoxProfile.set_preference("browser.download.folderList", 2)
firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
firefoxProfile.set_preference("browser.download.dir", os.path.abspath(output_directory))
firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
firefoxProfile.set_preference("pdfjs.disabled", True)
firefoxProfile.set_preference("plugin.scan.Acrobat", "99.0")
firefoxProfile.set_preference("plugin.scan.plid.all", False)

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, firefox_profile=firefoxProfile)

login = "--login" in sys.argv
failed = []

try:

    if login:
        username = input("Username: ")
        password = getpass()
        print("Logging in")
        driver.get(series_url)
        sleep(5)
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password, Keys.ENTER)
        sleep(5)

    book_pages = []

    driver.get(series_url)

    while True:
        print("Retrieving books")
        try:
            books = driver.find_elements_by_xpath("//ol[@id='results-list']/li/div[2]/h2/a")
            book_pages.extend([b.get_attribute("href") for b in books])
            driver.find_element_by_xpath("//a[@class='next']").click()
        except Exception:
            break

    pdfs = []
    n = len(book_pages)
    nl = len(str(n))

    for i, p in book_pages:
        print(f"[ {i+1:{nl}d} / {n} ] Downloading {p}")
        try:
            driver.get(p)
            driver.find_element_by_link_text("Download book PDF").click()

            
        except Exception:
            print(f"Couldn't download {p}")
            failed.append(p)

except Exception:
    pass

driver.close()

with open("failed.txt", "w") as f:
    f.write("\n".join(failed))