from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import openai
import os
import utils
from tools import tools
from dotenv import load_dotenv

load_dotenv()


class Roberto:
    def __init__(self):
        self.conversation_history = None
        self.file = os.path.join("data", "ai-description.txt")
        self.context = utils.readfile(self.file)
        self.memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

        openai.api_key = "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"
        self.llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)
        self.agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, context=self.context, memory=self.memory)

    def startNewConversation(self):
        self.memory.reset()

    def ConversationPerMessage(self, prompts):
        try:
            self.conversation_history = self.memory.get_all()
            # Combine all messages into a single string
            conversation_text = ""
            for message in self.conversation_history:
                conversation_text += message.content + "\n"

            # Call the agent and store the response
            resultOfAgentReact = self.agent.query(conversation_text + "\n" + prompts)

            return resultOfAgentReact
        except Exception as e:
            print(f"An error occurred: {e}")
            return "We got a problem please reset your chat"

        finally:
            self.memory.put(ChatMessage(role="system", context=resultOfAgentReact))
            self.memory.put(ChatMessage(role="user", context=prompts))
