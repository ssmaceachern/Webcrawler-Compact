#! C:\python27
#TODO//Add error checking for JavaScript

import re, urllib

textfile = file('depth_1.txt','wt')
print "Enter the URL you wish to crawl..."
print 'Usage  - "http://www.google.com" <-- With the double quotes'
input_url = input("#>> ")

#Use some regex to parse urls and write all scrawled urls () to a text file
for link in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(input_url).read(), re.I):
        print link 
        for found_link in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(link).read(), re.I):
                print found_link
                textfile.write(found_link + '\n')
textfile.close()
