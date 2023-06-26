import json
import pickle
from typing import Sequence
from langchain.chat_models import ChatOpenAI
from llama_index.tools import BaseTool, FunctionTool
from langchain.schema import FunctionMessage
from langchain.memory import ChatMessageHistory
from typing import Dict


class YourOpenAIAgent:
    def __init__(
        self,
        tools: Sequence[BaseTool] = [],
        llm: ChatOpenAI = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0613"),
    ) -> None:
        self._llm = llm
        self._tools = {tool.metadata.name: tool for tool in tools}
        self._chat_history = ChatMessageHistory()


    def reset(self) -> None:
        self._chat_history.clear()

    def chat(self, message: str) -> str:
        chat_history = self._chat_history
        chat_history.add_user_message(message)
        functions = [tool.metadata.to_openai_function() for _, tool in self._tools.items()]

        ai_message = self._llm.predict_messages(chat_history.messages, functions=functions)
        chat_history.add_message(ai_message)

        function_call = ai_message.additional_kwargs.get("function_call", None)
        if function_call is not None:
            function_message = self._call_function(function_call)
            chat_history.add_message(function_message)
            ai_message = self._llm.predict_messages(chat_history.messages)
            chat_history.add_message(ai_message)

        return ai_message.content

    def _call_function(self, function_call: dict) -> FunctionMessage:
        tool = self._tools[function_call["name"]]
        output = tool(**json.loads(function_call["arguments"]))
        return FunctionMessage(
            name=function_call["name"],
            content=str(output), 
        )


    def save_chat_history(self, file_path: str):
        with open(file_path, "wb") as file:
            pickle.dump(self._chat_history, file)

    def load_chat_history(self, file_path: str):
        with open(file_path, "rb") as file:
            self._chat_history = pickle.load(file)