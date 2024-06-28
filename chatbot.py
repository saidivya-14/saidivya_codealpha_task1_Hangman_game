import nltk
from nltk.chat.util import Chat, reflections

# Define pairs and responses for the chatbot
pairs = [
    ['my name is (.*)', ['Hello %1, how can I help you today?']],
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['what is your name?', ['I am a chatbot.']],
    ['how are you?', ['I am good, thank you!']],
    ['quit', ['Bye! Take care.']],
]

def basic_chatbot():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == '__main__':
    basic_chatbot()