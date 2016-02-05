# -*- coding: utf-8 -*-
from lxml import html
from lxml import etree
import requests
import re
import urllib2
import urlparse


def get_html(url):
    redirect_re = re.compile('<meta[^>]*?url=(.*?)["\']', re.IGNORECASE)
    hops = []
    while url:
        if url in hops:
            url = None
        else:
            hops.insert(0, url)
            response = urllib2.urlopen(url)
            if response.geturl() != url:
                hops.insert(0, response.geturl())
            # check for redirect meta tag
            html = response.read()
            match = redirect_re.search(html)
            if match:
                url = urlparse.urljoin(url, match.groups()[0].strip())
            else:
                url = None
    return html


def get_abstract(pnum):
    url_format = 'http://patft1.uspto.gov/netacgi/nph-Parser?patentnumber='+pnum;
    html = get_html(url_format)
    xml = etree.HTML(html)
    abstract = xml.xpath('/html/body/p[1]/text()')[0].decode('string_escape')
    return abstract


