#! C:\python27
#TODO//Add error checking for JavaScript and cycles...

import re, urllib

tf = file('results.txt','wt')
print "Enter the URL you wish to crawl in Double Quotes("")..."
print 'Example  - "http://www.google.com" '
input_url = input("#>> ")

#Use some regex to parse urls and write all scrawled urls using DFS to a text file
for link in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(input_url).read(), re.I):
        print link 
        for found_link in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(link).read(), re.I):
                print found_link
                tf.write(found_link + '\n')
tf.close()
