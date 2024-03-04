from dotenv import load_dotenv

from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer

load_dotenv()

import os
import utils
from llama_index.core.chat_engine.context import ContextChatEngine
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import openai
from tools import tools

file = os.path.join("data", "ai-description.txt")
context = utils.readfile(file)

prefix_messages = [ChatMessage(role="system", content=context)]

memory = ChatMemoryBuffer.from_defaults(token_limit=1500)


def main():
    openai.api_key = os.environ.get("KEY")
    llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, prefix_messages=prefix_messages, memory=memory)

    while (prompts := input("Enter a prompt (q to quit): ")) != "q":
        result = agent.query(prompts)
        print(result)


if __name__ == '__main__':
    main()
