import schedule
import time
import MainFunctions as Mf

print("Started the main script")
schedule.every(1).day.at("18:35").do(Mf.upload_picture_on_account_using_api, main_account_used=False)

while True:
    schedule.run_pending()
    time.sleep(1)
