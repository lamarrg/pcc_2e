# Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

texts = ['Hey, give me a call', 'Remember to get milk', 'Don\'t you dare hang up on me!!!']

sent_messages = []


def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(texts[:])

print(f'The original array is {texts}')
print(f'This is the sent list... {sent_messages}')







