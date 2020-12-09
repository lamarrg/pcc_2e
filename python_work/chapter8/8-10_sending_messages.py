# Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

texts = ['Hey, give me a call', 'Remember to get milk', 'Don\'t you dare hang up on me!!!']

sent_messages = []


def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(texts)

print(f'The original array is {texts}')
print(f'This is the sent list... {sent_messages}')







