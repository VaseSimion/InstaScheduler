from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import ImageManagement as Im
import Config as Cfg


def login(user):
    params = Cfg.get_parameters("test")
    if user == "basic_bot":
        USERNAME = params['userrc']
        PASSWORD = params['passrc']
    else:
        USERNAME = params['userusc']
        PASSWORD = params['passusc']

    cl = Client()
    cl.login(USERNAME, PASSWORD)
    return cl


def simp_main_account(cl: Client, target):
    comment_text = "Amazing, love you so much"
    if target != "main":
        for element in cl.user_medias(54354195189, amount=1):
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


def upload_story(cl: Client):
    notabot = cl.user_info_by_username('simion.vase.not.a.bot')
    photo_folder = "D:\\Exported photos\\Instagram"
    image_location = photo_folder + "\\" + Im.get_image_path(photo_folder)
    post_story = True
    if post_story:
        cl.photo_upload_to_story(
            image_location,
            "Just using this with the Instagrapi",
            mentions=[StoryMention(user=notabot, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
            links=[StoryLink(webUri='https://www.youtube.com/watch?v=CQRy_ygDF4o&list=RDtYdbcwTb8Es&index=13')]
            #hashtags=[StoryHashtag(hashtag="#Boss", x=0.23, y=0.32, width=0.5, height=0.22)]
        )


if __name__ == "__main__":
    upload_story(login("other"))

