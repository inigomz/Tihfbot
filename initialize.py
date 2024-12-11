import openai
import os
from dotenv import load_dotenv
from src.twitch_functions import initialize_bot, send_generated_response, process_twitch_message
from src.openAI_functions import process_message_from_queue
from src.utilities import chat_message_queue, openai_response_queue


# Environment variables for openai and twitch api
load_dotenv()

# OpenAI setup
openai.api_key = os.getenv('OPENAI_API_KEY')

# Twitch Setup (DO NOT EDIT THIS. EDIT THE .ENV FILE INSTEAD. IT'S FOR YOUR OWN PRIVACY)
oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')
client_id = os.getenv('TWITCH_CLIENT_ID')
client_secret = os.getenv('TWITCH_CLIENT_SECRET')
channel_name = os.getenv('TWITCH_CHANNEL_NAME')

# Function that initialized the twitch bot. Info about this file can be found in /src/twitch_functions.py.
bot = initialize_bot(oauthtoken=oauth_token, client_id=client_id, client_secret=client_secret, channel_name=channel_name)

# Other initializers for the twitch bot
@bot.event
async def event_ready():
    print(f"logged in as {bot.nick}")
    bot.loop.create_task(process_message_from_queue()) # openAI_functions.py function
    bot.loop.create_task(send_generated_response(bot, channel_name)) # twitch_functions.py function

@bot.event
async def event_message(message):
    # handle commands
    await bot.handle_commands(message)
    await process_twitch_message(message)

# ----------------------- TEMP LAUNCH ---------------------------
if __name__ == "__main__":
    bot.run()