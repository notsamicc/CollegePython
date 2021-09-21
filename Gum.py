import time
import winsound

print("What do you call a bear with no teeth?")
#waits X seconds before printing punchline
winsound.Beep(1500, 2000)
time.sleep(2)
winsound.Beep(1500, 2000)
print("A gummy bear!")

winsound.Beep(1500, 2000)
#waits Y seconds before "laughing" every Z seconds
time.sleep(3)
while True:
    time.sleep(.1)
    winsound.Beep(1500, 100)
    print("haha")
