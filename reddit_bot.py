import praw
import config
import time
import os

def bot_login():
    print "Logging in..."
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "WSB to the moon bot v0.1")
    print "Logged in!"
    return r

def run_bot(r, comments_replied_to):
    print "Obtaining 5 comments..."

   

    for comment in r.subreddit('test').comments(limit=5):
        if "dog" in comment.body and comment_id not in comments_replied_to and not comment_author == r.user.me():
            print "String found!"
            comment.reply("I also love dogs!")
            print "Replied to comment" + comment.id

            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print "Sleeping for 10 seconds..."
    #Sleep for 10 seconds...
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt")
        comments_replied_to = []
    else:
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to - comments_replied_to.split("\n")
        comments_replied_to = filter(None, comments_replied_to)

r = bot_login()
comments_replied_to = []

while True:
run_bot(r, comments_replied_to)





# Stonks going down
# "up": [
# https://giphy.com/gifs/dvZSDOywoCM4Sro65Q/html5
# https://giphy.com/gifs/qBykyt7AiTOgM/html5
# https://giphy.com/gifs/MEq4za8poCEOfdY5Pr/html5
# https://giphy.com/gifs/l0HlDDyxBfSaPpU88/html5
# https://giphy.com/gifs/3orieVe5VYqTdT16qk/html5
# https://giphy.com/gifs/ToMjGppB1bJC04ESjyE/html5
# https://giphy.com/gifs/LkuPxRS0F6gmc/html5
# https://giphy.com/gifs/Js7cqIkpxFy0bILFFA/html5
# https://giphy.com/gifs/l4pTky87QVuvbzwnS/html5
#],


#Stonks going up
# "down": [
# https://giphy.com/gifs/f7GQKWSKo5ekWPUNnC/html5
# https://giphy.com/gifs/AgHBbekqDik0g/html5
# https://giphy.com/gifs/a8yevb0iMyaYw/html5
# https://giphy.com/gifs/TKveuw4x6cXolE7reg/html5
# https://giphy.com/gifs/jQWJUET9SPFxRINeMP/html5
# https://giphy.com/gifs/xT1Ra4EJbNSDf1CmAM/html5
# https://giphy.com/gifs/IhPXkHVji28ACMNEnG/html5
# https://giphy.com/gifs/KB1CEBi2DapSDzfYV7/html5
# ]