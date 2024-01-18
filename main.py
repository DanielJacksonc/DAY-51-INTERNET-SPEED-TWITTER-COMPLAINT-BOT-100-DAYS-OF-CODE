from _datetime import *
import datetime
TIME = datetime.datetime.now().time()
Daily_5PM = time(16,40,00)
from internetspeedtwitter import InternetSpeedTwitterBot
import os
import time


TIME_FUNCTION = time.time() +10
my_schedule = TIME == Daily_5PM


while my_schedule:
    print("still here.......")
    TIME_FUNCTION
    PROMISED_DOWN = 150
    PROMISED_UP = 10
    TWITTER_EMAIL = os.environ["TWITTER"]
    TWITTER_PASSWORD = os.environ["PASSWORD"]

    speed_check = InternetSpeedTwitterBot()
    up = speed_check.up
    down = speed_check.down


    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    if up < PROMISED_UP or down < PROMISED_DOWN:
        print("Network sucks!! Now tweeting.....")
        time.sleep(4)
        bot.tweet_at_provider(TWITTER_EMAIL,TWITTER_PASSWORD)
else:
    print(f"time is: -----{TIME}----- You scheduled to run at ----{Daily_5PM}----",)
