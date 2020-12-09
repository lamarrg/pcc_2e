# Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)


texts = ['Hey, give me a call', 'Remember to get milk', 'Don\'t you dare hang up on me!!!']


show_messages(texts)

