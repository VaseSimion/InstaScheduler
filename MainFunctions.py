import ImageManagement as Im
import GraphApiUses as Gau
import os


def upload_picture_on_second_account():
    response_code = 400
    error_count = 0
    print("\n*******************     New run happened    *******************")

    while response_code != 200 and error_count < 10:
        photo_folder = "D:\\Exported photos\\Instagram"
        image_location = Im.get_image_path(photo_folder)
        try:
            while not Im.check_if_valid_ratio(image_location):
                image_location = Im.get_image_path(photo_folder)
            link = Im.img_bb_image_upload(image_location)
            print("Image is here:", link)
            caption = Im.generate_image_caption(image_location)
            response = Gau.image_upload(link, caption, main_account=False)
            response_code = response.status_code
        except:
            error_count += 1
            print("Some error happened, error count is ", error_count)
        if response_code == 200:
            print("Photo has been uploaded successfully!")
            os.remove(image_location)
