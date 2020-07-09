from instapy import InstaPy

# username: carbot_88
# password: instagrambot56
# email: rayle88@outlook.com
# name: Rain Cowd

user = InstaPy(username="carbot_88", password="instagrambot56")
user.login()
user.set_do_follow(True, percentage=100)
user.set_dont_like(["nsfw"])
user.set_comments(["Nice", "I like it"])
user.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
user.clarifai_check_img_for(["nsfw"])

user.like_by_tags(["ferrari", "mclaren", "ducati"], amount=5)
user.do_comment(True, percentage=50)
# close, save logs and prints a report
user.set_use_clarifai(enabled=True, api_key="6edc5260228d44a382a0c29cc4bc0fef")
user.end()
