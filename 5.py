# pip install chatterbot,chatterbot_corpus
from Chatterbot import ChatBot
from chatterbot.trainer import ListTrainer

chatbot=chatBot('DailyLifeBot')
conversation=[
    "Hi","Hello!",
    "Hello","Hii there!",
    "How are you?","I am good! how about you?",
    "Good Morning","Morning! Have a nice day.",
    "Good neight","Sweet Dreams!",
    "Bye","GoodBye!",
    "what your name?","I am Daily life chatBot",
    "Thank you","you are welcome",
]
trainer=ListTrainer(chatbot)
trainer.train(conversation)

def daily_life_chatbot():
    print("hello ! I am Daily life chatbot chatwith(type exit to leave)")
    while True:
        user_input=input("You:")
        if(user_input.lower()=='exit'):
            print("DailyLifeBot:Bye! Have a good Day")
            break
        response=chatbot.get_response(user_input)
        print(f"DailyLifeBot:{response}")
daily_life_chatbot()