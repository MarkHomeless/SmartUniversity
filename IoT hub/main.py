from message_handler import MessageHandler
import time

if __name__ == '__main__':
    message_handler = MessageHandler('test')
    while True:
        message_handler.get_message()
        time.sleep(1)