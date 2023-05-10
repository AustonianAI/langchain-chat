from dotenv import load_dotenv

import os

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

load_dotenv()


def main():
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        raise Exception("OPENAI_API_KEY is not set")
    else:
        print("OPENAI_API_KEY is set")

    llm = ChatOpenAI(model_name='gpt-4')
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationEntityMemory(llm=llm,),
        # verbose=True,
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    )

    print("GPT-4 CLI Go!")

    while True:
        user_input = input("> ")

        ai_response = conversation.predict(input=user_input)

        print("\n\nAI:\n " + ai_response + "\n")


if __name__ == '__main__':
    main()
