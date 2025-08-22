# Extended Rule-Based Chatbot

def chatbot():
        print("Chatbot: Hello! Type 'bye' to exit.")
        
        while True:
                user_input = input("You: ").lower().strip()
                
                if user_input == "hello":
                        print("Chatbot: Hi there!")
                elif user_input == "how are you":
                        print("Chatbot: I'm fine, thanks! How about you?")
                elif user_input in ["i'm fine", "i am fine", "good", "great"]:
                        print("Chatbot: Glad to hear that!")
                elif user_input in ["what is your name", "who are you"]:
                        print("Chatbot: I'm a simple chatbot created in Python.")
                elif user_input in ["thank you", "thanks"]:
                        print("Chatbot: You're welcome!")
                elif user_input == "bye":
                        print("Chatbot: Goodbye! Have a nice day.")
                        break
                else:
                        print("Chatbot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
