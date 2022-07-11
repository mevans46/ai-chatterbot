
# import the chatterbot package
# This is the chatbot engine we will use
from chatterbot import ChatBot

# Give our chatbot a name
chatbot = ChatBot("HAL 9000")

# Packages used to Train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Add a new personality about Mars here
# Just using a python list
# Format should be question from the user and the response from chatbot
personality_mars = [
    "What is your favorite planet?",
    "My favorite planet is Mars, that is why I live there.",
    "What is your favorite color?",
    "My favorite color is Red, like the Planet Mars.",
    "What is your favorite color?",
    "My favorite color is Red, like the Dust on the Planet Mars.",
    "What is your favorite color?",
    "My favorite color is Red, like the rocks on Planet Mars.",
    "What is your favorite planet?",
    "My favorite planet is Mars, that is why I bought a home there.",
     "What is your favorite planet?",
    "My favorite planet is Mars, because it is so close."
]

personality_snow = [
    "Do like snow?",
    "I think snow is wonderful!"
]

# Set the trainers we want train
trainer_personality_snow=ListTrainer(chatbot)
trainer_personality_mars= ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)

# Now here we actually train our chatbot on the corpus
# This is what gives our chatbot its personality 
# Train the personality you want to override should come first

# Standard personality chatterbot comes with
trainer.train('chatterbot.corpus.english')
trainer_personality_mars.train(personality_mars)
trainer_personality_snow.train(personality_snow)

''' ******************* GUI Below Engine Above **************** '''
# Import for the GUI 
from chatbot_gui import ChatbotGUI

# create the chatbot app
"""
    Options
    - title: App window title.
    - gif_path: File Path to the ChatBot gif.
    - show_timestamps: If the chat has time-stamps.
    - default_voice_options: The voice options provided to the text-to-speech engine by default if not specified
                             when calling the send_ai_message() function.
"""
app = ChatbotGUI(
    title="H E L L O  H U M A N  - Your bot name here",
    gif_path="ChatbotFemale.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    }
)


# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    """
    This is where you can add chat bot functionality!

    You can use chat.send_ai_message(text, callback, voice_options) to send a message as the AI.
        params:
            - text: the text you want the bot to say
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    You can use chat.start_gif() and chat.stop_gif() to start and stop the gif.
    You can use chat.clear() to clear the user and AI chat boxes.

    You can use chat.process_and_send_ai_message to offload chatbot processing to a thread to prevent the GUI from
    freezing up.
        params:
            - ai_response_generator: A function which takes a string as it's input (user message) and responds with
                                     a string (AI's response).
            - text: The text that the ai is responding to.
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    :param chat: The chat box object.
    :param text: Text the user has entered.
    :return:
    """
    # this is where you can add chat bot functionality!
    # text is the text the user has entered into the chat
    # you can use chat.send_ai_message("some text") to send a message as the AI, this will do background
    # you can use chat.start_gif() and chat.stop_gif() to start and stop the gif
    # you can use chat.clear() to clear the user and AI chat boxes

    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
    output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        # define a callback which will close the application
        def close():
            chat.exit()

        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("It has been good talking with you. Have a great day! Later!", callback=close)
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)


# run the chat bot application
app.run()
