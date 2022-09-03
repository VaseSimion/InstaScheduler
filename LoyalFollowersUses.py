from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import ImageManagement as Im
import Config as Cfg
from pathlib import Path


def login_local(user):
    params = Cfg.get_parameters("test")
    if user == "basic_bot":
        USERNAME = params['userrc']
        PASSWORD = params['passrc']
    else:
        USERNAME = params['userusc']
        PASSWORD = params['passusc']

    cl = Client()

    try:
        cl.load_settings(Path("/../Logins/" + user + ".json"))
    except:
        pass

    cl.login(USERNAME, PASSWORD)
    print(cl.get_timeline_feed())  # check session
    cl.dump_settings(Path("/Logins/" + user + ".json"))
    return cl


def simp_main_account(user, target):
    comment_text = Im.generate_simp_caption()
    cl = login_local(user)
    try:
        if target == "main":
            for element in cl.user_medias(2373550137, amount=1):
                id_last_post = element.dict()['id']
                print(id_last_post)
                comment = cl.media_comment(id_last_post, comment_text)
                print(comment.dict())
                cl.media_like(media_id=id_last_post)
        else:
            for element in cl.user_medias(54354195189, amount=1):
                id_last_post = element.dict()['id']
                print(id_last_post)
                comment = cl.media_comment(id_last_post, comment_text)
                print(comment.dict())
                cl.media_like(media_id=id_last_post)
    except:
        print("Some error happened!")


def upload_story(user):
    cl = login_local(user)
    try:
        notabot = cl.user_info_by_username('simion.vase')
        print(notabot)
        photo_folder = Cfg.get_parameters()['photo_folder']
        image_location = Im.get_image_path(photo_folder)
        post_story = True
        if post_story:
            cl.photo_upload_to_story(
                image_location,
                "Just using this with the Instagrapi",
                mentions=[StoryMention(user=notabot, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
                links=[StoryLink(webUri='https://www.youtube.com/watch?v=CQRy_ygDF4o&list=RDtYdbcwTb8Es&index=13')]
                #hashtags=[StoryHashtag(hashtag="#Boss", x=0.23, y=0.32, width=0.5, height=0.22)]
            )
    except:
        print("Something was not right")


if __name__ == "__main__":
    simp_main_account("basic_bot", "main")