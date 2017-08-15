#!/usr/bin/python
#-*- coding:utf-8 -*-

from downloader import download
import re
import urlparse
import Queue 
from sql_test import sqlwrite
import argparse

def link_crawler(seed_url, link_regex='', max_depth=2):
    crawler_queue = Queue.deque([seed_url])
    seen = {seed_url: 0}
    while crawler_queue:
        url = crawler_queue.pop()
        depth = seen[url]
        if depth != max_depth:
            html = download(url)
#            print html
            if html:
                for link in get_links(html):
                    if re.match(link_regex, link):
                        print ("match-> %s, %s" %(link, link_regex))
                        link = urlparse.urljoin(seed_url, link)
                        if link not in seen:
                            seen[link] = depth + 1
                            crawler_queue.append(link)
                            sqlwrite(get_domain(link)[0])


def get_links(html):
    """return a list of links from html
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](http://[^/]*?/)["\']',re.IGNORECASE)
    print(webpage_regex.findall(html))
    return webpage_regex.findall(html)

def get_domain(link):
    """return a domain without 'http://' and '/'
    """
    domain_regex = re.compile('http://(.*?)/', re.IGNORECASE)
    return domain_regex.findall(link)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--seed', type=str, default=None)
    parser.add_argument('--regex', type=str, default='')
    parser.add_argument('--deepth', type=int, default=2)

    args = parser.parse_args()

    link_crawler(args.seed, args.regex, args.deepth)
