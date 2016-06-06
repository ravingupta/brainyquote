#!/usr/bin/python

import requests
from lxml import html
import time
import string

def get_authors():
    baseUrl = 'http://www.brainyquote.com'
    urlString = 'http://www.brainyquote.com/authors/'
    authorsUrl = [urlString + x for x in list(string.lowercase[:26])]
    
    urlsList = [] # authors list page urls
    print ""
    print "Scanning Started for page links"
    print ""
    for url in authorsUrl:
        print "Scanning URL: %s"%url
        urlsList.append(url)
        urlsList.extend(pagination(url, False))

    authorsList = []
    print ""
    print "Scanning Started for Author Pages"
    print ""
    for url in urlsList:
        print "Scanning URL: %s"%url
        authorsList.extend(get_authors_links(url))
    # Write all authors links
    authorsFile = open("authors.txt","a+")
    for urls in authorsList:
        authorsFile.write(baseUrl + urls.encode('utf-8') + "\n")
    authorsFile.close()

    quoteLinks = []
    # Write all authors links
    print ""
    print "Scanning Started for Quote Page Links"
    print ""
    for url in authorsList:
        newUrl = (baseUrl + url)
        print "Scanning URL: %s"%newUrl
        quoteLinks.append(newUrl)
        arr = pagination(newUrl, True)
        quoteLinks.extend(arr)
    # Write all quotes link
    linksFile = open("quotes_links.txt","a+")
    for url in quoteLinks:
        linksFile.write(url.encode('utf-8') + "\n")
    linksFile.close()

    print ""
    print "Scanning Started for fetching quotes"
    print ""
    # Write all quotes
    quotesFile = open("quotes.csv","a+")
    for url in quoteLinks:
        quote_details = fetch_quote(url)
        quotesFile.write(quote_details.encode('utf-8') + "\n")

    print ""
    print "All Done \nThanks for using it...!!!"
    print ""

def get_authors_links(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    arr = tree.xpath('//table[@class="table table-hover table-bordered sticky_adzone"]//td/a/@href')
    return arr

def fetch_quote(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    quotes = tree.find_class('bqQt')
    tempString = ""
    for q in quotes:
        tempString += ("\"%s\","%next(q.find_class('bqQuoteLink')[0].iter('a')).text)
        tempString += ("%s,"%next(q.find_class('bq-aut')[0].iter('a')).text)
        for element in q.find_class('bqBlackLink')[0].iter('a'):
            tempString += "%s;"%element.text
        tempString += "\n"
    return tempString

def pagination(url, htmlPage): # .html or not - htmlPage True or False
    arr = []
    page = requests.get(url)
    tree = html.fromstring(page.text)
    end = tree.xpath('//div[@class="row paginationContainer"]//nav//ul/li[last()-1]/a/text()')
    if len(end):
        if(htmlPage):
            url = url.split('.html')[0]
            for count in range(2, int(end[0])+1):
                arr.append(url+"%s.html"%(count))
        else:
            for count in range(2, int(end[0])+1):
                arr.append(url+"%s"%(count))
    return  arr

if __name__ == '__main__':
    get_authors()