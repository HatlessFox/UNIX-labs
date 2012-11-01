#!/usr/local/bin/python3

import re
import urllib.request
import collections
import sys

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:15.0) Gecko/20100101 Firefox/15.0.1"

req = urllib.request.Request(url="http://www.google.com/search?q=" + urllib.request.quote(sys.argv[1]))
req.add_header('User-Agent', user_agent)
resp = urllib.request.urlopen(req);

content = resp.read().decode("UTF8")
url_regex = re.compile(r"<cite(.*?)>(.*?)</cite>")

domain_gr_index = 2
domain_regex = re.compile(r"([\w]+://)?([^/]+?\.)*(.*?)/")
stat = collections.defaultdict(int)

for match in url_regex.finditer(content):
  url = re.sub(r"<.*?>", "", match.groups()[1])
  url = re.sub(r"[\s]*&rsaquo;[\s]*", "/", url)
  domain = domain_regex.search(url)
  if domain: stat[domain.groups()[domain_gr_index]] += 1

for d, cnt in sorted(stat.items(), key = lambda entry: entry[1], reverse = True):
 print("{0} listed {1} times".format(d, cnt))