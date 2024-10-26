import src.utilities
import twitchio
from twitchio.ext import commands
# Initialize the empty variable as a string
last_message = ''

# Function to initialize the Twitch bot
def initialize_bot(token, client_id, channel_name):
    bot = commands.Bot(
        token=token,
        client_id=client_id,
        prefix='!',
        initial_channels=[channel_name]
    )
    return bot
# Receives message from Twitch chat and stores message as a string.
def RecieveTwitchMsg(message_content):
    global last_message
    last_message = message_content
    print(f'stored message {last_message}')

async def CatchEventMessage(message):
    if "@tihfbot" in message.content.lower():
        RecieveTwitchMsg(message.content)