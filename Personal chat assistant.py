# Rule based AI python Chatbot

import datetime

# Greeting based on time
name = input("Welcome, Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon", name)
elif 17 <= presentHour <= 20:
    print("Good evening", name)
else:
    print("Good night", name)

print("Namaste! Welcome to rule based chatbot")
print("You can ask me basic questions. Type 'Bye' to exit the bot.")

# Chatbot memory creation [dictionary of responses]
responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you!",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "Keep going! Every challenge makes you stronger and sharper.",
    "good morning": "Good morning! Wishing you a productive and happy day ahead.",
    "good night": "Good night! Sleep well and recharge for tomorrow.",
    "thank you": "You’re most welcome! Happy to help anytime.",
    "bye": "Goodbye! Take care and see you soon.",
    "tell me a joke": "Sure! Why don’t programmers like nature? Too many bugs!",
    "what is your name": "I’m your friendly AI chatbot, here to make life easier.",
    "i am sad": "I’m here for you. Remember, tough times don’t last, but tough people do.",
    "study tips": "Break your study into small chunks, take short breaks, and revise regularly.",
    "weather": "I can check the latest weather for you if you’d like!",
    "time": "I can tell you the current time whenever you ask.",
    "what's up": "All good here! How’s your day going?",
    "good afternoon": "Good afternoon! Hope your day is going smoothly.",
    "good evening": "Good evening! Relax and enjoy your time.",
    "i am bored": "Let’s do something fun! Want me to tell you a riddle or a fact?",
    "tell me a fact": "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey still edible!",
    "tell me a riddle": "Here’s one: What has to be broken before you can use it? (Answer: An egg!)",
    "i am hungry": "Grab a snack! Healthy food keeps your energy up.",
    "i am tired": "Take a short break or power nap. You’ll feel refreshed!",
    "i am happy": "That’s wonderful! Happiness looks great on you.",
    "sing a song": "🎵 La la la… I can’t sing, but I can share lyrics or recommend songs!",
    "study with me": "Sure! Let’s focus together. What subject are you working on?",
    "give me advice": "Always stay consistent. Small steps daily lead to big achievements.",
    "tell me something new": "Here’s something cool: Octopuses have three hearts!",
    "i am stressed": "Take a deep breath. You’re stronger than you think.",
    "play with me": "I can play word games, riddles, or quizzes with you!",
    "what is python": "Python is a high-level programming language known for its simplicity and readability.",
    "define variable": "A variable is a container used to store data values in Python.",
    "what is a function": "A function is a block of reusable code defined with 'def' in Python.",
    "what is a loop": "Loops are used to repeat actions. Python has 'for' and 'while' loops.",
    "what is a list": "A list is a collection of items in Python, written inside square brackets [].",
    "what is a dictionary": "A dictionary stores data as key-value pairs, written inside curly braces {}.",
    "what is indentation": "Indentation in Python defines code blocks. Without proper indentation, code won’t run.",
    "what is tuple": "A tuple is like a list but immutable, meaning its values cannot be changed.",
    "what is set": "A set is a collection of unique items in Python, written inside curly braces {}.",
    "what is module": "A module is a Python file containing code that can be imported into other programs.",
    "what is package": "A package is a collection of modules organized together in directories.",
    "what is exception": "Exceptions are errors in Python. They are handled using try-except blocks.",
    "what is class": "A class is a blueprint for creating objects in Python, used in OOP.",
    "what is object": "An object is an instance of a class, representing real-world entities in code.",
    "what is docstring": "A docstring is a string literal used to document functions, classes, or modules."
}

# Method/Function to get response of chatbot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "Sorry, I am not able to tell that yet. I am still in learning mode."

# Take user input
while True:
    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot response:", reply)

    if "bye" in userInput.lower():
        break