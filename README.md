# springer_series_scraper

Download all the books in Springer book series. 

## Requirements

Python 3.6, Firefox, and Selenium (with Firefox driver)

## How to use

First, find a Springer book series. You can do this by searching 
[here](https://link.springer.com/search?query=&facet-content-type=%22BookSeries%22) on the Springer Link
website. For example, [this](https://link.springer.com/search?facet-series=%22666%22&facet-content-type=%22Book%22)
is the link for the Undergraduate Text in Mathematics series.
The easiest way to use this script it to be on your institution's network, as, at least in my case,
you don't need to sign in via your institution's SSO to access all the resources on Springer Link. That is,
if you can access all the resources on link.springer.com without sigining in, then you can start the script 
as:

> python scrape.py [series_url] [output_directory]

If you don't, then your library might have an SSO to access Springer Link via a proxy. For 
example, [this](https://libguides.colorado.edu/25295783) is the University of Colorado Boulder's SSO page 
for Springer Link. Find the link to the series through the proxy. For example, [this](https://link-springer-com.colorado.idm.oclc.org/search?facet-series=%22666%22&facet-content-type=%22Book%22)
is the link for the Undergraduate Text in Mathematics series on CU's proxy. Then, start the script as 

> python scrape.py [series_url] [output_directory] --login

A prompt for a username and password will appear. This is not guaranteed to work on any SSO, but should 
work for CU's SSO.
