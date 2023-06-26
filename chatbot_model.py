import json
from typing import Dict
from langchain.memory import ChatMessageHistory

class ChatbotModel:
    def __init__(self):
        self.chat_history = ChatMessageHistory()

    def save_chat_history(self, file_path: str):
        with open(file_path, "w") as file:
            json.dump(self.chat_history.messages, file)

    def load_chat_history(self, file_path: str):
        with open(file_path, "r") as file:
            self.chat_history.messages = json.load(file)

    def add_message(self, message: Dict[str, str]):
        for key, value in message.items():
            if key == 'User':
                self.chat_history.add_user_message(value)
            elif key == 'Bot':
                self.chat_history.add_ai_message(value)
