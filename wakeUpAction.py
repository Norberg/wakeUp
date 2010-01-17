import time
import writeLED

#add actions to be done on wakeup here
def onWakeUp():
	for i in xrange(255):
		writeLED.writeLED_PWM("w", i)
		time.sleep(0.2)

#cleanup action to do after wakeup
def afterWakeUp():
	writeLED.writeLED_PWM("w", 0)
