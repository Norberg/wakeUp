import time
import writeLED

for i in xrange(255):
	writeLED.writeLED_PWM("w", i)
	time.sleep(0.2)

