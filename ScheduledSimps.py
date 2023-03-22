import sys
import schedule
import time
import LoyalFollowersUses as Lfs
import sys

# The way you call this is: python ./ScheduleSimps.py which_account_is_active at_which_time_to_like_comm Photo_folder
print("Simp", sys.argv[1], "is running")
schedule.every(1).day.at(sys.argv[2]).do(Lfs.simp_main_account, user=sys.argv[1], target="main")
schedule.every(int(sys.argv[4])).hours.do(Lfs.upload_photo, user=sys.argv[1], folder=sys.argv[3])
schedule.every(int(sys.argv[5])).hours.do(Lfs.upload_story, user=sys.argv[1], folder=sys.argv[3])

Lfs.login_local(sys.argv[1])

while True:
    schedule.run_pending()
    time.sleep(1)
