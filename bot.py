from pyrogram import Client, filters

from time import sleep

api_id = <YOUR_API_ID>

api_hash = '<YOUR_API_HASH>'

bot_token = '<YOUR_BOT_TOKEN>'

group_id = '<YOUR_GROUP_ID>'

# Create the Pyrogram client

app = Client("delete_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Filter to handle incoming messages in the group

@ app.on_message(filters.group & ~filters.edited)

def delete_messages(client, message):

    # Delete the message

    client.delete_messages(chat_id=group_id, message_ids=message.message_id)

# Start the bot

app.start()

# Run a loop to continuously delete messages every 3 seconds

while app.is_running:

    app.idle()

    sleep(3)

# Stop the bot gracefully

app.stop()

