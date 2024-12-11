# Main folder for anything sending and receiving related for debugging.
# Maily utilized for a lot of the JSON folders during testing.
# For the final release, a direct-approach will be implemented, cutting the middle-man JSON file.
# I just need to check how resource intensitive this program is.
# Also will be using this for initializing varibles shared across different python files.
# TODO: Create a backlog for all the print statements & store it in a JSON file.
import asyncio

chat_message_queue = asyncio.Queue()
openai_response_queue = asyncio.Queue()