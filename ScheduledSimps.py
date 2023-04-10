import sys
import schedule
import time
import LoyalFollowersUses as Lfs
import sys
import random

""" The way you call this is: python ./ScheduleSimps.py which_account_is_active at_which_time_to_like_comm Photo_folder
Arguments:
1 - which user runs the script - it has to be in LoyalFollowers and loads from Config
2 - at what time to simp the main account hh:mm
3 - In which folder are the pictures /home/Pictures/folder
4 - how often it should upload photos - frequency of hours
5 - how often it should upload stories - frequency of hours
6 - how often to simp a specific account - frequency of hours
7 - which account to target - without @
8 - What content is in targeted pictures 
9 - Simping other accounts from main account
"""
print("Simp", sys.argv[1], "is running")

time.sleep(random.randint(1, 300))

if sys.argv[9] == "True":
    schedule.every(2).days.at(sys.argv[2]).do(Lfs.simp_main_account, user=sys.argv[1], target="main")
    schedule.every(int(sys.argv[6])).hours.do(Lfs.simp_specific_user, user=sys.argv[1], targeted_user=sys.argv[7], photo_content=sys.argv[8])

schedule.every(int(sys.argv[4])).hours.do(Lfs.upload_photo, user=sys.argv[1], folder=sys.argv[3])
schedule.every(int(sys.argv[5])).hours.do(Lfs.upload_story, user=sys.argv[1], folder=sys.argv[3])
Lfs.login_local(sys.argv[1])

while True:
    schedule.run_pending()
    time.sleep(1)
