import time, os
from subprocess import Popen
import writeLED

#add actions to be done on wakeup here
def onWakeUp():
	i = 1 
	while i < 255:
		i = i*1.1
		writeLED.writeLED_PWM("r", int(i))
		writeLED.writeLED_PWM("g", int(i))
		writeLED.writeLED_PWM("b", int(i))
		time.sleep(0.2)
	Popen(["mplayer", "http://http-live.sr.se/p3-mp3-192"])
	if os.path.isfile("computers.wol"):	
		Popen(["wakeonlan", "-f computers.wol"])

#cleanup action to do after wakeup
def afterWakeUp():
	#turn of music
	Popen(["killall", "mplayer"])
	writeLED.writeLED_PWM("r", 0)
	writeLED.writeLED_PWM("g", 0)
	writeLED.writeLED_PWM("b", 0)

if __name__ == "__main__":
	onWakeUp()
	time.sleep(10)
	afterWakeUp()
