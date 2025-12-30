import time
with open(r"C:\Users\creat\coding karenge\99startup.log", "a") as f:
    f.write("Script started\n")
def Notification():
    from winotify import Notification

    toast = Notification(
        app_id="PAUSE BRO",
        title="Drink Water",
        msg="Take a break , grab a kitkat",
        duration="short")
    toast.show()

while True:
    time.sleep(15)
    Notification()
    time.sleep(3600)