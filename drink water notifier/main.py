from plyer import notification 

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/HP/Desktop/python projects/drink water notifier/icon.ico",
        timeout = 5,
  )

if__name__ = "__main__"
notifyMe("**Arjita,Drink Water Now!!", "Drinking Water helps to burn fat, and helps to maintain the balance of Body Fluids.") 