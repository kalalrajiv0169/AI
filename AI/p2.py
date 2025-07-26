# Simple chatbot with loop
#Design a simple rule-based chatbot using if-else conditions (min 7 responses).
while True:
    user_input = input("you: ").lower()

    if user_input == "hello":
        print("Bot: Hi there!")
    elif user_input == "how are you?":
        print("Bot: I'm a bot, I'm always good.")
    elif user_input == "bye":
        print("Bot: Goodbye! Take care!")
    elif user_input == "what is ai?":
        print("Bot: AI stands for Artificial Intelligence.")
    elif user_input == "who created you?":
        print("Bot: I was created by a student.")
    elif user_input == "what is name": 
        print("Bot: my name is Kalal Rajiv.")
    elif user_input == "exit":
        print("Bot: Exiting... Have a great day!")
        break  # Exit the loop
    else:
        print("Bot: Sorry, I don't understand.")