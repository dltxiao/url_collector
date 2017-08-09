import urllib2
import gzip
import StringIO

def download(url, user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36', num_retries=1):
    print('Downloading: ', url)
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        try:
            data = urllib2.urlopen(request, timeout=30).read()
            data = StringIO.StringIO(data)
            html = gzip.GzipFile(fileobj=data).read()
        except:
            html = urllib2.urlopen(request, timeout=30).read()
    except:
#        print 'Download Error: ', e.reason
        html = None
        if num_retries > 0 :
#            if hasattr(e, 'code') and 500 <= e.code < 600:
            return download(url, user_agent ,num_retries-1)
    return html

