import nltk
from nltk.chat.util import Chat, reflections
from textblob import TextBlob

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing fine, thanks for asking.']),
    (r'what is your name?', ['You can call me Chatbot.', 'I am just a humble chatbot.']),
    (r'quit', ['Bye, take care!', 'Goodbye!']),
    (r'(.) good(.)', ['That sounds great!', 'I am glad to hear that!']),
    (r'(.) bad(.)', ['I am sorry to hear that.', 'Is there anything I can do to help?']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm a simple chatbot. You can start a conversation with me. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    
    # Perform basic sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    
    if sentiment > 0.5:
        response = "That sounds really positive!"
    elif sentiment < -0.5:
        response = "I'm sorry to hear that you're feeling so negative."
    else:
        response = chatbot.respond(user_input)
    
    print("Chatbot:", response)
    
    if user_input.lower() == 'quit':
        break
