from dotenv import load_dotenv

load_dotenv()

from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import openai
import os
import utils
from tools import tools

load_dotenv()

file = os.path.join("data", "ai-description.txt")
context = utils.readfile(file)
memory = ChatMemoryBuffer.from_defaults(token_limit=1500)


def main():
    openai.api_key = os.environ.get("KEY")
    llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context, memory=memory)

    while (prompts := input("Enter a prompt (q to quit): ")) != "q":
        try:
            conversation_history = memory.get_all()
            # Combine all messages into a single string
            conversation_text = ""
            for message in conversation_history:
                conversation_text += message.content + "\n"

            resultOfAgentReact = agent.query(conversation_text + "\n" + prompts)
            print(resultOfAgentReact)
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            memory.put(ChatMessage(role="system", context=resultOfAgentReact))
            memory.put(ChatMessage(role="user", context=prompts))


if __name__ == "__main__":
    main()
