#!/usr/bin/env python
import re
from urllib2 import urlopen
import sys

def main():
	#When running the xcript in command enter the file name in the command line
    file= str(sys.argv[1])
    with open(file) as f:
        for line in f:
            getSite(line)


def getSite (site):

        print "%s\n" % site
        siteOpen = urlopen(site)
        siteContent = siteOpen.read()

        # Find the location of "UA-[4-10 digits]-[1-4 digits]" in a variable
        # based on a regex

        # The 'r' states it is regex
        if re.search(r"\bUA-\d{4,10}-\d{1,4}\b", siteContent):
            print "\t**Google Analytics is installed**\n"
        else:
            print "\t**No Google Analytics found**\n"


if __name__ == "__main__":
    main()
