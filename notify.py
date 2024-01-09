import pyinotify
import RPi.GPIO as GPIO
import time

# Use physical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up header pin 11 (GPIO11) as an input
print "Setup Pin 4"
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_ACCESS #This monitors any access on files and folders in the dir

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_ACCESS(self, event):
        print "Accessed:", event.pathname

#Lights on n off at varied intervals 
        var=1
        while var==1 :
          print "Set Output False"
          GPIO.output(27, True)
          
          time.sleep(1)
          print "Set Output False"
          GPIO.output(27, False)
          GPIO.output(4, True)
          time.sleep(1)
          GPIO.output(4, False)
          break

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

#Folder to monitor
wdd = wm.add_watch('/media/pi/Server/Emby Stream', mask, rec=True)

notifier.loop()
