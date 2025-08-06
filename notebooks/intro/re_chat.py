import re

def chatbot_response(user_input):
    # Define patterns and responses
    patterns = {
        r'hi|hello|hey': "Hello! How can I help you today?",
        r'how are you': "I'm just a computer program, but thanks for asking!",
        r'what is your name': "I'm a chatbot created to assist you.",
        r'help|support': "Sure! What do you need help with?",
        r'bye|exit|quit': "Goodbye! Have a great day!",
        r'\d+': "I see you mentioned a number. Can you tell me more about it?",
        r'.*': "I'm not sure how to respond to that. Can you ask something else?"
    }

    # Check each pattern and return the corresponding response
    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|exit|quit', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()



# Example interaction 
"""
Welcome to the chatbot! Type 'bye' to exit.
You: hi
Chatbot: Hello! How can I help you today?
You: What is your name?
Chatbot: I'm a chatbot created to assist you.
You: Can you help me?
Chatbot: Sure! What do you need help with?
You: 123
Chatbot: I see you mentioned a number. Can you tell me more about it?
You: bye
Chatbot: Goodbye! Have a great day!

"""