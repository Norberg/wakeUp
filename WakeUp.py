#!/usr/bin/python

import vobject, datetime, os, sys
from time import sleep

import retrive_iCal, wakeUpAction


class WakeUp:
	def __init__(self):
		self.lastParsed = 0
		self.lastRetrived = datetime.datetime.fromtimestamp(0);
		self.wakeUpTimes = []
		self.alarmActive = False

	def getWakeUpTimes(self):
		retrive_iCal.retrive()
		self.lastRetrived = datetime.datetime.now()
		if os.path.exists("calender.ical") and \
		   self.lastParsed == os.path.getmtime("calender.ical"):
			return
		else:
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
				#Reacuring event
				if event.rruleset:
					print "reacuring event.. not handeld"
					#for date in event.rruleset:
						
				tz = event.dtstart.value.tzinfo
				start = event.dtstart.value.utctimetuple()
				end = event.dtend.value.utctimetuple()
				now = datetime.datetime.utcnow().utctimetuple()
				#only append if alarm havent allready gone off
				if end > now:
					self.wakeUpTimes.append([start, end])

	def mainLoop(self):
 		oneHourAgo = datetime.datetime.now()-datetime.timedelta(1/24.0)
		if (self.lastRetrived  < oneHourAgo):
			self.getWakeUpTimes()
			self.lastRetrived = datetime.datetime.now()
			
		for alarm in self.wakeUpTimes:
			utcnow = datetime.datetime.utcnow().utctimetuple()
			if alarm[0] < utcnow and alarm[1] > utcnow: 
				if not self.alarmActive:
					wakeUpAction.onWakeUp()
					self.alarmActive = True
				return
		if self.alarmActive:
			wakeUpAction.afterWakeUp()
			self.alarmActive = False

	def run(self):
		while 1:
			sys.stdout.write(".")
			sys.stdout.flush()
			self.mainLoop()
			sleep(30)

if __name__ == "__main__":
	w = WakeUp()
	w.run()
