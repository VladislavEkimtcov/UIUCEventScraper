"""
UIUC calendar scraper
By: Vladislav Ekimtcov
"""

import sys
import os
import lxml.html as h
import urllib.request
import shutil
import docx


def legal_characters(line2check: str):
    line2check = line2check.replace("<", " ")
    line2check = line2check.replace(">", " ")
    line2check = line2check.replace('"', " ")
    line2check = line2check.replace("/", " ")
    line2check = line2check.replace('\\', " ")
    line2check = line2check.replace("|", " ")
    line2check = line2check.replace("?", "")
    line2check = line2check.replace("*", " ")
    return line2check


# feign a browser
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for i in range(0, 10000):
    url = "https://calendars.illinois.edu/list/" + str(i)
    print("Checking " + url)
    try:
        urllib.request.urlretrieve(url, "DownloadedCal.html")
        # scrape the text
        xslt_root = h.parse("DownloadedCal.html")
        title_string = xslt_root.xpath("//title/text()")[0]
        # if we got here, there was no 404 and we can check if food is mentioned

        FoodUpperCase = xslt_root.xpath('.//p[contains(text(),"Food")]')
        FoodLowerCase = xslt_root.xpath('.//p[contains(text(),"food")]')
        PizzaUpperCase = xslt_root.xpath('.//p[contains(text(),"Pizza")]')
        PizzaLowerCase = xslt_root.xpath('.//p[contains(text(),"pizza")]')
        BarbecueUpperCase = xslt_root.xpath('.//p[contains(text(),"Barbecue")]')
        BarbecueLowerCase = xslt_root.xpath('.//p[contains(text(),"barbecue")]')
        SnackLowerCase = xslt_root.xpath('.//p[contains(text(),"Snack")]')
        SnackUpperCase = xslt_root.xpath('.//p[contains(text(),"snack")]')

        if len(FoodUpperCase) > 0 or len(FoodLowerCase) > 0 or len(PizzaUpperCase) > 0 or len(
                PizzaLowerCase) > 0 or len(BarbecueUpperCase) > 0 or len(BarbecueLowerCase) > 0:
            print("Food found! Downloading " + title_string + ".ics")
            urllib.request.urlretrieve("https://calendars.illinois.edu/ical/" + str(i) + ".ics",
                                       "Calendars/" + legal_characters(title_string) + ".ics")
        else:
            print("No food found with " + title_string)
    except urllib.error.HTTPError:
        print("Calendar ID " + str(i) + " is either private or does not exist")
    except:
        print("Unhandled exception!")
os.remove("DownloadedCal.html")
