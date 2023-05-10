from dotenv import load_dotenv

import os

load_dotenv()

if __name__ == '__main__':
    print("hello world")
    print('My API key is:', os.environ.get('OPENAI_API_KEY'))