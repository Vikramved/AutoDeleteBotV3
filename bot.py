import asyncio

from os import environ

from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))

API_HASH = environ.get("API_HASH")

BOT_TOKEN = environ.get("BOT_TOKEN")

SESSION = environ.get("SESSION")

TIME = int(environ.get("TIME"))

GROUPS = [int(grp) for grp in environ.get("GROUPS", "").split()]

ADMINS = [int(usr) for usr in environ.get("ADMINS", "").split()]

START_MSG = "<b>Hello {}!\n\nI only support the</b> <a href='https://t.me/+9CKK8DlZlgUxOTE9'><b>Movie Boss</b></a> <b>group.\n\nI perform group automatic cleaning every 30 minutes.</b>"

User = Client(
    "user-account",

    session_string=SESSION,

    api_id=API_ID,

    api_hash=API_HASH,

    workers=300

)

Bot = Client(
    "auto-delete",

    api_id=API_ID,

    api_hash=API_HASH,

    bot_token=BOT_TOKEN,

    workers=300

)

@Bot.on_message(filters.command('start') & filters.private)

async def start(bot, message):

    await message.reply_text(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))

async def delete(user, message):

    try:

        if message.from_user.id in ADMINS:

            return

        else:

            await asyncio.sleep(TIME)

            await Bot.delete_messages(message.chat.id, message.message_id)

    except Exception as e:

        print(e)

async def main():

    User.start()

    print("User Account Started!")

    await Bot.start()

    print("Bot Started!")

    await idle()

    await User.stop()

    print("User Account Stopped!")

    await Bot.stop()

    print("Bot Stopped!")

if __name__ == '__main__':

    asyncio.run(main())

