import os

class Config(object):
       API_ID=int(os.environ.get("API_ID"))    # Get from https://my.telegram.org/apps
       API_HASH=os.environ.get("API_HASH")     # Get from https://my.telegram.org/apps
       BOT_TOKEN=os.environ.get("BOT_TOKEN")   # Get from https://t.me/BotFather
       AUTH_USERS=os.environ.get("AUTH_USERS") # User ids of those who can use bot anywhere without limit
       GROUPS=os.environ.get("GROUPS")         # Chat ids where you wan't many to use the bot
