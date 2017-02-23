# Python 2.7 Google Analytics Checker

### A python tool to quickly check multiple sites / pages for Google Analytics

## Instructions for use:
In order to use ensure you have python 2.7

* Create a text file containing all the URLs you want to check
  * Each URL needs to be on a new line
* At the command line run the script and enter the path of the text file
  * e.g. ` > python ga_check.py example.txt `

The script will then run in your command line and go through each line in the
text file checking for Google Analytics and print out:

* Google Analytics is installed
* No Google Analytics found
