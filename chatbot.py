from datetime import datetime

# Chatbot conversation

Bot_name = "Nova"

conversation_count = 0

# Helper fuctions

def normalize_input(users_input):
    """
    cleans the users input by"
    -  removing extra space
    -  converting text to lowecase
    """
    return user_input.strip().lower()

def show_help():
    "display available commands."
    print("\n Nova: Here are some thing you can ask me")
    print(" * hello/ hi/ hey")
    print(" * how are you?")
    print(" * what's your name?")
    print(" * who created you?")
    print(" * what can you do?")
    print(" * what time is it?")
    print(" * what is today's date?")
    print(" * help")
    print(" * bye/ exit/ quit")

def show_time():
    " display the current time."
    current_time = datetime.now().strftime("%I:%M %P")
    print(f"Nova:The current time is {current_time}.")

def show_date():
    "Display today's date."
    current_date = datetime.now().strftime("%d %B %Y")
    print(f"Nova: Today's date is {current_date}.") 

def show_status():
    "display chat conversation information"
    print(
        f"Nova: we have exchanged"
        f"{conversation_count} message(s) so far"
    )

# welcome msj
print("=" * 45)
print(" NOVA AI_Chatbot")
print("=" * 45)

print("Nova: Hello")
print("Nova: i'm Nova, a rule based AI_Chatbot.")
print("Nova: type 'help' to see what I can do.")
print("Nova: type 'bye', 'exit', 'quit', 'to leave'.")

#Main Chatbot
while True:

    user_input = input("you:")

    user_input = normalize_input(user_input)

    conversation_count += 1

# Exit Commands
    if user_input in ["bye", "exit", "quit"]:

        print("Nova: Goodbye!")
        print("Nova: Thanks for chatting with me.")
        break

# Greetings
    

    elif user_input in ["hello", "hi", "hey"]:

        print("Nova: Hello!  Nice to meet you.")


    elif user_input in [
        "good morning",
        "good afternoon",
        "good evening"
    ]:

        if user_input == "good morning":
            print("Nova: Good morning!")

        elif user_input == "good afternoon":
            print("Nova: Good afternoon!")

        else:
            print("Nova: Good evening!")

# Basic Conversation

    elif user_input in [
        "how are you",
        "how are you doing"
    ]:

        print(
            "Nova: I'm doing great! "
            "Thanks for asking."
        )


    elif user_input in [
        "what is your name",
        "your name"
    ]:

        print(f"Nova: My name is {Bot_name}.")


    elif user_input in [
        "who are you",
        "what are you"
    ]:

        print(
            "Nova: I am a rule-based AI chatbot "
            "created using Python."
        )


    elif user_input in [
        "who created you",
        "who made you"
    ]:

        print(
            "Nova: I was created as a Python "
            "rule-based chatbot project."
        )

# Chatbot Capabilities

    elif user_input in [
        "what can you do",
        "what do you do",
        "your abilities"
    ]:

        print("Nova: I can:")
        print("  • Respond to greetings")
        print("  • Answer predefined questions")
        print("  • Tell you the current time")
        print("  • Tell you today's date")
        print("  • Show conversation information")
        print("  • Provide a list of commands")

# Utility Commands

    elif user_input in [
        "what time is it",
        "current time",
        "time"
    ]:

        show_time()


    elif user_input in [
        "what is today's date",
        "what is todays date",
        "today's date",
        "todays date",
        "date"
    ]:

        show_date()


    elif user_input in [
        "conversation count",
        "how many messages",
        "message count"
    ]:

        show_status()

# Help Command 

    elif user_input in ["help", "commands"]:

        show_help()

# Simple Positive Responses

    elif user_input in [
        "thank you",
        "thanks",
        "thankyou"
    ]:

        print(
            "Nova: You're welcome!"
        )

# Unknown Input

    
    else:

        print(
            "Nova: Hmm... I don't have a rule "
            "for that yet."
        )

        print(
            "Nova: Try typing 'help' to see "
            "the commands I understand."
        )

# Program Finished

print("\nChatbot session ended.")   