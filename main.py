from dotenv import load_dotenv
from llama_index.core.base.llms.types import ChatMessage

load_dotenv()
from llama_index.core.memory import ChatMemoryBuffer
import os
import utils
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import openai
from tools import tools

file = os.path.join("data", "ai-description.txt")
context = utils.readfile(file)

memory = ChatMemoryBuffer.from_defaults(token_limit=1500)


def main():
    openai.api_key = os.environ.get("KEY")
    llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context, memory=memory)

    while (prompts := input("Enter a prompt (q to quit): ")) != "q":
        try:
            resultOfAgentReact = agent.query(prompts)
            print(resultOfAgentReact)
        except ValueError as e:

            resultOfAgentReact = llm.complete(prompts)
            print(resultOfAgentReact)
        finally:
            memory.put(ChatMessage(role="system", context=resultOfAgentReact))
            memory.put(ChatMessage(role="user", context=prompts))



if __name__ == '__main__':
    main()
