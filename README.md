# azcam-webpages

*azcam-webpages* is an *azcam* extension which adds certain web pages to the default *azcam* web server.

## Installation

Download the code (usually into the *azcam* root folder such as `c:\azcam`) and install.

```shell
cd /azcam
git clone https://github.com/mplesser/azcam-webpages
cd azcam-webpages
pip install -e .
```

# Web Pages

The are static web pages, located for example at:

http://localhost:2403/exposure.

## /exposure

Control an exposure.

## /status

Display the status of exposures.

## /queue

Control an observing queue (not complete).
