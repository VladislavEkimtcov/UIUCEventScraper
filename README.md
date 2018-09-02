# UIUCEventScraper research
Are you the type of person who signs up for 50 RSOs during Quad Day? Are you the type of person with -$78 in liqud assets? Are you just hungry? Why not check out some (or all) UIUC events?

## Motivation
I'm really hungry and want to score some free pizza. After looking for some UIUC events, I noticed that UIUC has moved on to a global calendar system as seen athttps://illinois.edu/resources/calendars.html. Further research revealed that:

* All calendars are numbered: https://calendars.illinois.edu/list/2463
* All calendars come in a downloadable *.ics format: https://calendars.illinois.edu/ical/2463.ics
* This numbering is consistent between the /list/ view and *.ics download
* "site:calendars.illinois.edu/list/" query yields 2,560 results; however, there are calendar IDs such as 5753, meaning that many calendars are non-public. 

## Code plan
The program will do the following:
* Loop through https://calendars.illinois.edu/list/%ID%, where %ID% is between 0 and 9999
* If it gets redirected to a page with a header with "404" in it, that means that the calendar is either private or does not exits
* If there's no redirect, we can make a https://calendars.illinois.edu/ical/%ID%.ics request and save that on a local machine. 

When the loop is finished, we can merge the ICS files together and import to any calendar tool. [ICSMERGER](http://www.tobias-schlegel.de/?page_id=902&lang=en) turned out to be a perfect tool and is included with the distribution.

## Outcome
Some issues were encountered during this project:
* Some calendar names included illegal characters (slashes, for example). Code was added to eliminate those.
* Many calendars were empty or corrupted. Plus, very few included food events. Additional ahndling was included to search for pages that mention "Pizza", "Food", "Snack", or "Barbecue"
* Different departments turned out to participate in the exact same events, resulting in duplicates.

[ICS duplicate remover](https://github.com/VladislavEkimtcov/PythonICSDuplicateRemover) seemed like a good solution and is included with the distribution.