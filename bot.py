from pyrogram import Client, filters

from time import sleep

API_ID = "15428219"

API_HASH = "0042e5b26181a1e95ca40a7f7c51eaa7"

BOT_TOKEN = "5429880614:AAGomxybHKTYLRHNxomJOBsfe6azogCa9S0"

GROUP_ID = "-1001397638909"

# Create the Pyrogram client

app = Client("delete_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Filter to handle incoming messages in the group

@ app.on_message(filters.group & ~filters.edited)

def delete_messages(client, message):
    if not message.edited:
# Delete the message
        client.delete_messages(chat_id=GROUP_ID, message_ids=message.message_id)

# Start the bot

app.start()

# Run a loop to continuously delete messages every 3 seconds

while app.is_running:

    app.idle()

    sleep(3)

# Stop the bot gracefully

app.stop()

