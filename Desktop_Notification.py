from plyer import notification
import  time

if __name__=='__main__':
    while True:
        notification.notify(
            title="*** TAKE REST ***",
            message="Rest is important factor for health",
            # app_icon="C:/Users/Dell/OneDrive/Pictures/Saved Pictures/l5.jpg",
            timeout=5)
        time.sleep(20)