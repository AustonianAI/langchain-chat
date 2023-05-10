from dotenv import load_dotenv

import os

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()


def main():
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        raise Exception("OPENAI_API_KEY is not set")
    else:
        print("OPENAI_API_KEY is set")

    llm = ChatOpenAI()
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(),
        verbose=True
    )

    print("Hello, I am a helpful CLI assistant. How can I help you?")

    while True:
        user_input = input("> ")

        ai_response = conversation.predict(input=user_input)

        print("\nAssistant:\n " + ai_response + "\n")


if __name__ == '__main__':
    main()
