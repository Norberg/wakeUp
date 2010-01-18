import time, os
import writeLED

#add actions to be done on wakeup here
def onWakeUp():
	#os.popen("play ~/music/* fade h 60 &> /dev/null")
	for i in xrange(255):
		writeLED.writeLED_PWM("w", i)
		time.sleep(0.2)

#cleanup action to do after wakeup
def afterWakeUp():
	#turn of musix
	#os.popen("killall play")
	writeLED.writeLED_PWM("w", 0)

if __name__ == "__main__":
	onWakeUp()
