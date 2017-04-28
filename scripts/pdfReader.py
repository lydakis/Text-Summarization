import urlparse
import urllib2
import os
import datetime
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print "[*] Please download and install Beautiful Soup first!"
    sys.exit(0)

yearValue = 2007
list = []
while (yearValue < datetime.datetime.now().year):
    print datetime.datetime.now().year
    startValue = 0
    counter = True
    while counter:
        url = "http://nemertes.lis.upatras.gr/jspui/simple-search?query=&filter_field_1=dateIssued&filter_type_1=equals&filter_value_1=%d&sort_by=score&order=desc&rpp=10&etal=0&start=%d" % (
        yearValue, startValue)

        request = urllib2.Request(url, None)
        html = urllib2.urlopen(request)
        soup = BeautifulSoup(html.read())  # to parse the website

        #print soup
        divValue = soup.find("div", {"class": "alert alert-info"}).getText()
        #print divValue
        divTextArray = []
        divTextArray = divValue.split(" ")
        recordValue = divTextArray[1].split("-");
        #print recordValue[1]
        #print divTextArray[3]
        #print recordValue
        #divTextArray
        #print recordValue[1].strip() == divTextArray[3].strip()
        startValue += 10
        if (recordValue[1].strip() == divTextArray[3].strip()):
            counter = False
        for tag in soup.findAll('a', href=True):  # find <a> tags with href in it so you know it is for urls
            # so that if it doesn't contain the full url it can the url itself to it for the download
            tag['href'] = urlparse.urljoin(url, tag['href'])
            # print tag['href']
            if "10889" in tag['href']:
                #print tag['href'].split("10889/", 1)[1]
                list.append(tag['href'].split("10889/", 1)[1])
    yearValue += 1
print list
print len(list)
