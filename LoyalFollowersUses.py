from instagrapi import Client
from instagrapi.types import StoryLink
import ImageManagement as Im
import Config as Cfg
from pathlib import Path
import random
import os
import time
import platform


def login_local(user, enable_delay=True):
    if enable_delay:
        time.sleep(3600 * random.random())

    params = Cfg.get_parameters("test")
    if user == "basic_bot":
        USERNAME = params['userrc']
        PASSWORD = params['passrc']
    elif user == "nusuntbot":
        USERNAME = params['usernsb']
        PASSWORD = params['passnsb']
    elif user == "sunsetbob":
        USERNAME = params['usersb']
        PASSWORD = params['passsb']
    elif user == "fete":
        USERNAME = params['userfr']
        PASSWORD = params['passfr']
    elif user == "catsfromnet":
        USERNAME = params['usercfn']
        PASSWORD = params['passcfn']
    elif user == "treesdenmark":
        USERNAME = params['usertdk']
        PASSWORD = params['passtdk']
    else:
        USERNAME = params['userlp']
        PASSWORD = params['passlp']

    cl = Client()

    if platform.system() == "Windows":
        try:
            cl.load_settings(Path("Logins/" + user + ".json"))
        except:
            pass
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(Path("Logins/" + user + ".json"))
        return cl
    else:
        try:
            cl.load_settings(Path("/home/vase/TheInstaScript/InstaScheduler/Logins/" + user + ".json"))
        except:
            pass

        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(Path("/home/vase/TheInstaScript/InstaScheduler/Logins/" + user + ".json"))
        return cl


def simp_main_account(user, target):
    comment_text = Im.generate_simp_comment("@vase.simion")
    cl = login_local(user)
    try:
        if target == "main":
            for element in cl.user_medias(2373550137, amount=1):
                id_last_post = element.dict()['id']
                # print(id_last_post)
                comment = cl.media_comment(id_last_post, comment_text)
                # print(comment.dict())
                cl.media_like(media_id=id_last_post)
        else:
            for element in cl.user_medias(54354195189, amount=1):
                id_last_post = element.dict()['id']
                # print(id_last_post)
                comment = cl.media_comment(id_last_post, comment_text)
                # print(comment.dict())
                cl.media_like(media_id=id_last_post)
        print("Comment succesfuly uploaded, from", user)
    except Exception as error:
        print("An exception occurred:", error, user)


def upload_story(user, folder):
    cl = login_local(user)
    try:
        subfolder = "/home/vase/Pictures/" + folder
        file_name = random.choice(os.listdir(subfolder))
        image_location = subfolder + "/" + file_name

        post_story = True
        if post_story:
            cl.photo_upload_to_story(
                image_location,
                "Wanna see more?",
                links=[StoryLink(webUri='https://www.youtube.com/watch?v=CQRy_ygDF4o&list=RDtYdbcwTb8Es&index=13')]
            )
    except Exception as error:
        print("An exception occurred:", error, user)


def upload_photo(user, folder):
    cl = login_local(user)
    try:
        subfolder = "/home/vase/Pictures/" + folder
        file_name = random.choice(os.listdir(subfolder))
        image_location = subfolder + "/" + file_name

        if user == "fete":
            cl.photo_upload(
                image_location,
                Im.generate_ai_portrait_text()
            )
        else:
            cl.photo_upload(
                image_location,
                "Lovely picture made by " + file_name.split("-")[0].title() + " " + file_name.split("-")[1].title()
                # usertags = [Usertag(user=adw0rd, x=0.5, y=0.5)],
                # location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
            )
        os.remove(image_location)
    except Exception as error:
        print("An exception occurred:", error, user)


def simp_specific_user(user, targeted_user, photo_content="Landscape"):
    comment_text = Im.generate_simp_comment(targeted_user, photo_content)
    cl = login_local(user, enable_delay=False)
    if cl.account_info().dict()['username'] == targeted_user:
        print("Won't simp it's own account")
        return 0
    else:
        target_info = cl.user_info_by_username(targeted_user).dict()
        try:
            for element in cl.user_medias(target_info['pk'], amount=1):
                id_last_post = element.dict()['id']
                cl.media_comment(id_last_post, comment_text)
                cl.media_like(media_id=id_last_post)
            print("Comment succesfuly uploaded, from", user)
        except Exception as error:
            print("An exception occurred:", error, user)


def bomb_someone(targeted_user, content):
    list_of_followers = ["basic_bot", "nusuntbot", "catsfromnet", "treesdenmark", "lingeriepro", "sunsetbob", "fete"]
    for user in list_of_followers:
        cl = login_local(user, enable_delay=False)
        if cl.account_info().dict()['username'] == targeted_user:
            print("Simping only other accounts")
            continue
        target_info = cl.user_info_by_username(targeted_user).dict()
        try:
            for element in cl.user_medias(target_info['pk'], amount=1):
                id_last_post = element.dict()['id']
                comment_text = Im.generate_simp_comment("@" + targeted_user, content)
                comment = cl.media_comment(id_last_post, comment_text)
                cl.media_like(media_id=id_last_post)
            print("Comment succesfuly uploaded, from", user)
        except Exception as error:
            print("An exception occurred:", error, user)
        time.sleep(1)


def mass_follow_someone(targeted_user):
    list_of_followers = ["basic_bot", "nusuntbot", "catsfromnet", "treesdenmark", "lingeriepro", "sunsetbob", "fete"]
    for user in list_of_followers:
        cl = login_local(user, enable_delay=False)
        if cl.account_info().dict()['username'] == targeted_user:
            print("Simping only other accounts")
            continue
        target_info = cl.user_info_by_username(targeted_user).dict()
        try:
            cl.user_follow(target_info['pk'])
            print("Dude followed by", user)
        except Exception as error:
            print("An exception occurred:", error, user)
    time.sleep(1)


if __name__ == "__main__":
    simp_specific_user("basic_bot", "feteromanesti", "Portrait")
    pass
