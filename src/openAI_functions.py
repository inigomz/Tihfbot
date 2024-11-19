from openai import OpenAI
client = OpenAI()
from src.utilities import chat_message_queue, openai_response_queue
async def process_message_from_queue():
    while True:
        # Wait for a message to be available in the queue
        message = await chat_message_queue.get()
        print(f"Processing message from queue: {message}")

        # Interact with OpenAI's API
        response = OpenAI.Completion.create(
            engine="text-davinci-003",
            prompt=f"Respond to this Twitch message: {message}",
            max_tokens=50
        )
        openai_response = response.choices[0].txt

        await openai_response_queue.put(openai_response)
        print(f"OpenAI response: {openai_response}")