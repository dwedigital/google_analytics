#!/usr/bin/env python
import re
import urllib.request
import sys

def main():
	#When running the script in command enter the file name in the command line
    file= input("Enter the name & path of the text file > ")
    with open(file) as f:
        for line in f:
            getSite(line)


def getSite (site):

        print ('{}\n'.format(site))
        siteOpen = urllib.request.urlopen(site)
        siteContent = siteOpen.read()

        # Find the location of "UA-[4-10 digits]-[1-4 digits]" in a variable
        # based on a regex

        # The 'r' states it is regex
        if re.search(b"UA-\d{4,10}-\d{1,4}", siteContent):
            print ("\t**Google Analytics is installed**\n")
        else:
            print ("\t**No Google Analytics found**\n")


if __name__ == "__main__":
    main()
