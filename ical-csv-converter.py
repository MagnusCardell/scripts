import icalendar
import csv

# pip install icalendar

path = "data/birthdays.ics"
with open(path,  encoding='utf-8') as f:
    cal = icalendar.Calendar.from_ical(f.read())

with open("data/birthdays.csv", 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(['title', 'date'])

    for event in cal.walk("VEVENT"):
        #print(event.get("SUMMARY"), event.decoded("DTSTART"))
        writer.writerow([event.get("SUMMARY"), event.decoded("DTSTART")])