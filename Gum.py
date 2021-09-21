import time

print("What do you call a bear with no teeth?")
#waits X seconds before printing punchline
time.sleep(2)
print("A gummy bear!")

#waits Y seconds before "laughing" every Z seconds
time.sleep(3)
while True:
    time.sleep(.1)
    print("haha")
