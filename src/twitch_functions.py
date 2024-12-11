from src.utilities import chat_message_queue, openai_response_queue
from twitchio.ext import commands
# Initialize the empty variable as a string


# Function to initialize the Twitch bot
def initialize_bot(oauthtoken, client_id, client_secret, channel_name):
    bot = commands.Bot (
        token = oauthtoken, 
        client_id = client_id, 
        prefix = '!', 
        secret = client_secret, 
        initial_channels = [channel_name]
        )
    return bot


# Receives message from Twitch chat and stores message as a string.
async def process_twitch_message(message):

    # If @tihfbot is mentioned in the twitch chat, store it in the queue.
    if '@tihfbot' in message.content.lower():

        # Put the message in the queue. Print a statement saying that the message has been added to queue.
        await chat_message_queue.put(message.content)
        print(f'Message added to queue: {message.content}')

# TODO: Create a function that automatically renews the oauth token.
async def renew_oath_token(oauthtoken):
    pass

# Receives message from openAI's chatbot and sends it to twitch chat
async def send_generated_response(bot, channel_name):
    while True:
        # Receive the openai response from utilities.py and send the message to twitch
        openai_response = await openai_response_queue.get()
        print(f'Sending response to twitch chat:  {openai_response}')
        channel = bot.get_channel(channel_name)
        if channel:
            await channel.send(openai_response)