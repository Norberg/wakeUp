import vobject, datetime
import wakeUp

iCalFile = open("calender.ical")
parsedCal = vobject.readOne(iCalFile)
for event in parsedCal.vevent_list:
	try:
		event.categories.value
	except:
		continue

	if event.categories.value == [u'WakeUp']:
		tz = event.dtstart.value.tzinfo
		if event.dtstart.value < datetime.datetime.now(tz) and \
		   event.dtend.value > datetime.datetime.now(tz): 
			print "wakeUp"
