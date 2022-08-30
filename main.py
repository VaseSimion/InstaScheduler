import random
import schedule
import time
import MainFunctions as Mf
import LoyalFollowersUses as Lfs


client_one = Lfs.login("basic_bot")
time.sleep(random.randint(100, 180))
client_two = Lfs.login("usc")

schedule.every(2).days.at("21:00").do(Mf.upload_picture_on_account_using_api, main_account_used=True)
schedule.every(4).hours.do(Mf.upload_picture_on_account_using_api, main_account_used=True)

schedule.every(2).days.at("21:02").do(Lfs.simp_main_account, cl=client_one, target="main")
schedule.every(2).days.at("21:01").do(Lfs.simp_main_account, cl=client_two, target="main")

schedule.every(21).hours.do(Lfs.upload_story, cl=client_one)
schedule.every(23).hours.do(Lfs.upload_story, cl=client_two)

#Mf.upload_picture_on_second_account()

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
