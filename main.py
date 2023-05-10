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

    chat = ChatOpenAI(
        temperature=0.5,
        # model_name="gpt-4"
    )

    messages = [
        SystemMessage(content="You are a helpful assistant"),
    ]

    print("Hello, I am a helpful CLI assistant. How can I help you?")

    while True:
        user_input = input("> ")

        messages.append(HumanMessage(content=user_input))

        ai_response = chat(messages)

        messages.append(AIMessage(content=ai_response.content))

        print("\nAssistant:\n", ai_response.content)


if __name__ == '__main__':
    main()
