import schedule
import time
import MainFunctions as Mf

print("Started the main script")
schedule.every(1).day.at("19:25").do(Mf.upload_picture_on_account_using_api, main_account_used=True)

while True:
    schedule.run_pending()
    time.sleep(1)
