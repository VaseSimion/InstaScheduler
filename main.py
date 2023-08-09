import schedule
import time
import MainFunctions as Mf

print("Started the main script")
schedule.every(2).days.at("19:25").do(Mf.upload_picture_on_account_using_api, account="main")

while True:
    schedule.run_pending()
    time.sleep(1)
