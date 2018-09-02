from ics import Calendar
# your file here
with open("Calendars/ok.ics", encoding="utf8") as f:
    UncleanCalendar = Calendar(f.read())

#create the new calendar class + UID tracker
NewCal = Calendar()
UIDs = []

print("Processing " + str(len(UncleanCalendar.events)) + " events from the original file...")
for ev in UncleanCalendar.events:
    if ev.uid not in UIDs and:
        NewCal.events.add(ev)
        UIDs.append(ev.uid)

print("Generating new file with " + str(len(NewCal.events)) + " events...")

with open("Calendars/NewCal.ics", "w", encoding="utf8") as f:
    f.writelines(NewCal)