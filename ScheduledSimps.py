import sys
import schedule
import time
import LoyalFollowersUses as Lfs
import sys

print("Simp", sys.argv[1], "is running")
schedule.every(1).day.at(sys.argv[2]).do(Lfs.simp_main_account, user=sys.argv[1], target="main")
schedule.every(32).hours.do(Lfs.upload_photo, user=sys.argv[1], folder=sys.argv[3])

Lfs.login_local(sys.argv[1])

while True:
    schedule.run_pending()
    time.sleep(1)
