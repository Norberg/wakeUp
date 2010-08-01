import time
from subprocess import Popen
import writeLED

#add actions to be done on wakeup here
def onWakeUp():
	#toke to much cpu :(
	#os.popen("play ~/music/*.wav fade h 60 &> /dev/null")
	Popen(["mplayer", "http://http-live.sr.se/p3-mp3-192"])
	print "next"
#	for i in xrange(255):
#		#writeLED.writeLED_PWM("w", i)
#		time.sleep(0.4)
#	os.popen("alsaplayer ~/music/*.au &> /dev/null")

#cleanup action to do after wakeup
def afterWakeUp():
	#turn of musixc
	Popen(["killall", "mplayer"])
	#writeLED.writeLED_PWM("w", 0)

if __name__ == "__main__":
	onWakeUp()
