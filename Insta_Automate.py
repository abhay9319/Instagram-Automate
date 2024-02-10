from instabot import Bot

bot = Bot()
bot.login(username="abhi__v8", password="********")
bot.follow("virat.kohli")
bot.upload_photo("C:/Users\Abhay Dhiman/PycharmProjects/Python_Projects/Python.png", caption="I love Python")
bot.unfollow("virat.kohli")
bot.send_message("I love python",["wscubetechindia"])
followers = bot.get_user_followers("abhi__v8")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("abhi__v8")
for Following in following:
    print(bot.get_user_info(Following))