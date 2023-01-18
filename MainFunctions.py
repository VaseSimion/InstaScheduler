import ImageManagement as Im
import GraphApiUses as Gau
import Config as Cfg
import os


def upload_picture_on_account_using_api(main_account_used=False):
    response_code = 400
    error_count = 0
    print("\n*******************     New run happened    *******************")

    while True:
        if Gau.get_used_quota(main_account_used) >= 24:
            print("The upload quota has been reached, please try later")
            break

        photo_folder = Cfg.get_parameters()['photo_folder']
        try:
            image_location = Im.get_image_path(photo_folder)
            while not Im.check_if_valid_ratio(image_location):
                os.remove(image_location)
                image_location = Im.get_image_path(photo_folder)
            link = Im.img_bb_image_upload(image_location)
            print("Image is here:", link)
            caption = Im.generate_image_caption(image_location)
            response = Gau.image_upload(link, caption, main_account=main_account_used)
            response_code = response.status_code
            if response_code == 200:
                print("Photo has been uploaded successfully!")
                os.remove(image_location)
                break
        except:
            error_count += 1
            print("Some error happened, error count is ", error_count)

        if error_count > 10:
            print("Tried 10 times, I give up")
            break


if __name__ == "__main__":
    upload_picture_on_account_using_api(True)