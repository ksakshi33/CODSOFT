# Simple Rule-Based Chatbot in Python

# Define a dictionary with intents and responses
chatbot_rules = {
    "hello": "Hello! How can I help you today?",
    "hi":"Hello! How can I help you today?",
    "hey":"Hello! How can I help you today?",
    "how are you doing":"Hello! How can I help you today?",
    "how are you": "I'm a bot, so I'm always doing great. How about you?",
    "bye": "Goodbye! Have a nice day!",
    "Thank You": "Goodbye! Have a nice day!",
    "help me": "Sure, I'm here to help. What do you need assistance with?",
    "what is your name": "My name is Chatbot. Nice to meet you!",
    "default": "I'm sorry, I didn't understand that. Can you rephrase your question?"
}

# Function to get a response based on rules
def get_bot_response(user_input):
    user_input = user_input.lower()  
    
    # Check if the user input matches any of the intents
    for intent, response in chatbot_rules.items():
        if intent in user_input:
            return response
    
   
    return chatbot_rules["default"]

# Chatbot loop
def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    while True:
        user_input = input("You:")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
