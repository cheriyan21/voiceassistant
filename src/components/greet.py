import datetime
import random


def wishMe():
    hour = int(datetime.datetime.now().hour)
    wish = ""
    if hour >= 0 and hour < 12:
        wish = "Good Morning!"
    elif hour >= 12 and hour < 18:
        wish = "Good Afternoon!"
    else:
        wish = "Good Evening!"

    return f"{wish} I am your assistant, How can I help you?" #instead we can give name to the bot to introduce itself


statements = [
    wishMe(),
    "Welcome back. Please let me know how can I help You.",
    "Good to see you! Please tell me if I can help you.",
    "Hello! please say what you need, I will try to help you as much as I can.",
    #we can add as much statements as we like it will be the welcoming msg 
]


def greetings():
    return random.choice(statements)
