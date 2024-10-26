import openai
import os
import src.twitch_functions
import src.openAI_functions
from twitchAPI.twitch import Twitch
from dotenv import load_dotenv


# Environment variables for openai and twitch api
load_dotenv()

# OpenAI setup
openai.api_key = os.getenv('OPENAI_API_KEY')

# Twitch Setup
client_id = os.getenv('TWITCH_CLIENT_ID')
client_secret = os.getenv('TWITCH_CLIENT_SECRET')
oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')

# Twitch authentication (UNDER CONSTRUCTION WILL BE MOVED TO TWITCH FUNCTIONS)
twitch = Twitch(client_id, client_secret)
twitch.authenticate_app([])
user_info = twitch.get_users(logins='channel_name')
print(user_info)