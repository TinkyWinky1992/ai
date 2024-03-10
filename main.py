from dotenv import load_dotenv
<<<<<<< HEAD
from llama_index.core import SimpleDirectoryReader
from llama_index.core import ChatPromptTemplate
from llama_index.core.memory import ChatMemoryBuffer
=======
from llama_index.core.base.llms.types import ChatMessage

load_dotenv()
from llama_index.core.memory import ChatMemoryBuffer
import os
import utils
>>>>>>> 01b866f3b7d24b65019a89a232268b32e3f79403
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
            resultOfAgentReact = agent.query(prompts)
            print(resultOfAgentReact)
        except Exception as e:
            print(f"An error occurred: {e}")

<<<<<<< HEAD
        finally:
            memory.ф
            memory.add_message(ChatMessage(role="user", context=resultOfAgentReact))
=======
            resultOfAgentReact = llm.complete(prompts)
            print(resultOfAgentReact)
        finally:
            memory.put(ChatMessage(role="system", context=resultOfAgentReact))
            memory.put(ChatMessage(role="user", context=prompts))
>>>>>>> 01b866f3b7d24b65019a89a232268b32e3f79403




if __name__ == "__main__":
    main()
