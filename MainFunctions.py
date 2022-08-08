import ImageManagement as Im
import GraphApiUses as Gau
import random


def upload_picture_on_second_account():
    try:
        photo_folder = "D:\\Exported photos\\Instagram"
        print("\n*******************     New run happened    *******************")
        image_location = photo_folder + "\\" + Im.get_image_path(photo_folder)
        while not Im.check_if_valid_ratio(image_location):
            image_location = photo_folder + "\\" + Im.get_image_path(photo_folder)
        link = Im.img_bb_image_upload(image_location)
        print("Image is here:", link)
        caption = random.choice(["This is part of the bigger picture", "I am not a bot uploading random photos", "69"])
        response = Gau.image_upload(link, caption, main_account=False)
        print(response)
    except:
        print("Some error happened")
