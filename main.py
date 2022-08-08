import test as ts
import schedule
import time
import MainFunctions as Mf

#schedule.every().day.at("20:00").do(Mf.upload_picture_on_second_account)
schedule.every(1).minute.do(Mf.upload_picture_on_second_account)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
