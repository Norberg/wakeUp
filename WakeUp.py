import vobject, datetime, os
from time import sleep

import retrive_iCal

class WakeUp:
	def __init__(self):
		self.lastParsed = 0
		self.wakeUpTimes = []

	def getWakeUpTimes(self):
		if os.path.exists("calender.ical") and \
		   self.lastParsed == os.path.getmtime("calender.ical"):
			return
		else:
			retrive_iCal.retrive()		
			self.lastParsed = os.path.getmtime("calender.ical")

		self.wakeUpTimes = []
		iCalFile = open("calender.ical")
		parsedCal = vobject.readOne(iCalFile)
		for event in parsedCal.vevent_list:
			try:
				event.categories.value
			except:
				continue

			if event.categories.value == [u'WakeUp']:
				tz = event.dtstart.value.tzinfo
				self.wakeUpTimes.append([event.dtstart.value.utctimetuple(),
						         event.dtend.value.utctimetuple()])

	def mainLoop(self):
		self.getWakeUpTimes()
		for alarm in self.wakeUpTimes:
			if alarm[0]<datetime.datetime.now().utctimetuple() and\
			alarm[1] > datetime.datetime.now().utctimetuple(): 
				print "wakeUp"
			else:
				print "dont wakeUp"
		


if __name__ == "__main__":
	w = WakeUp()
	while 1:
		w.mainLoop()
		print ".",
		sleep(1)
