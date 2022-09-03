import sys
import schedule
import time
import LoyalFollowersUses as Lfs

Lfs.login_local(sys.argv[1])

schedule.every(2).days.at("21:02").do(Lfs.simp_main_account, user=sys.argv[1], target="main")
schedule.every(21).hours.do(Lfs.upload_story, user=sys.argv[1])

while True:
    schedule.run_pending()
    time.sleep(1)
