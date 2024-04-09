import json

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


def generateResponse(resultOfAgentReact) -> str:
    try:
        # Attempt JSON parsing first
        result = json.loads(resultOfAgentReact.response)
        print("not on problem ", result.action_input)
        return result["action_input"]
    except json.JSONDecodeError:
        # Fallback parsing if JSON parsing fails
        if "action" in resultOfAgentReact.response and "action_input" in resultOfAgentReact.response:
            action, action_input = resultOfAgentReact.response.split('"', 2)[1::2]
            result = {"action": action, "action_input": action_input}
        else:
            # Handle completely invalid output (optional)
            result = {"action": "Final Answer", "action_input": resultOfAgentReact.response}
        return result["action_input"]


class Roberto:
    def __init__(self):
        self.conversation_history = None
        self.file = os.path.join("data", "ai-description.txt")
        self.context = utils.readfile(self.file)
        self.memory = ChatMemoryBuffer.from_defaults(token_limit=500)

        openai.api_key = "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"

        self.llm = OpenAI(model="gpt-4-0125-preview", openai_api_key=openai.api_key)
        self.agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, context=self.context, memory=self.memory)

    def startNewConversation(self):
        self.memory.reset()

    def ConversationPerMessage(self, prompts) -> str:
        resultOfAgentReact = ""
        self.conversation_history = self.memory.get_all()
        # Combine all messages into a single string
        conversation_text = ""
        for message in self.conversation_history:
            conversation_text += message.content + "\n"

        # Call the agent and store the response
        resultOfAgentReact = self.agent.query(conversation_text + "\n" + prompts)
        self.memory.put(ChatMessage(role="system", context=resultOfAgentReact.response))
        self.memory.put(ChatMessage(role="user", context=prompts))
        return generateResponse(resultOfAgentReact)
