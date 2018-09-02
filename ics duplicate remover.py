from ics import Calendar
# your file here
with open("Calendars/ok.ics", encoding="utf8") as f:
    UncleanCalendar = Calendar(f.read())

#create the new calendar class + UID tracker
NewCal = Calendar()
UIDs = []
searchstrings = ['food', 'pizza', 'barbecue', 'snack']

print("Processing " + str(len(UncleanCalendar.events)) + " events from the original file...")
#another food check
for ev in UncleanCalendar.events:
    if ev.uid not in UIDs:
        for word in searchstrings:
            if word in ev.description.lower():
                NewCal.events.add(ev)
                UIDs.append(ev.uid)
                break

print("Generating new file with " + str(len(NewCal.events)) + " events...")

with open("Calendars/NewCal.ics", "w", encoding="utf8") as f:
    f.writelines(NewCal)