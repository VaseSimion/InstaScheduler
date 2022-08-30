import schedule
import time
import LoyalFollowersUses as Lfs
import random

client_one = Lfs.login("basic_bot")

schedule.every(2).days.at("21:02").do(Lfs.simp_main_account, cl=client_one, target="main")
schedule.every(21).hours.do(Lfs.upload_story, cl=client_one)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
