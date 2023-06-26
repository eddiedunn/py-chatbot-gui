from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMenuBar
from PyQt6.QtGui import QAction
from chatbot_view import ChatbotView
from chatbot_agent import YourOpenAIAgent
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

class ChatbotController(QMainWindow):
    def __init__(self, chat_agent: YourOpenAIAgent):
        super().__init__()
        self.view = ChatbotView(self)
        self.chat_agent = chat_agent
        self.setCentralWidget(self.view)  # Set view as central widget
        self.create_menu()  # Create the menu during initialization
        load_dotenv()
        self.ai_name=os.getenv("AI_NAME")

    def create_menu(self):
        self.menu = self.menuBar()  # This method returns the QMenuBar for the window

        # Create a File menu
        self.file_menu = self.menu.addMenu('File')

        # Create a Save action
        self.save_action = QAction('Save', self)
        self.save_action.triggered.connect(self.save_chat_history)
        self.file_menu.addAction(self.save_action)

        # Create a Load action
        self.load_action = QAction('Load', self)
        self.load_action.triggered.connect(self.load_chat_history)
        self.file_menu.addAction(self.load_action)
        
    def send_message(self):
        user_input = self.view.input_field.toPlainText()
        if user_input:
            self.view.update_conversation(f"User: {user_input}")
            bot_message = self.chat_agent.chat(user_input)
            self.view.update_conversation(f"{self.ai_name}: {bot_message}")
            
    def save_chat_history(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Chat History", "", "Pickle Files (*.pkl)")
        if file_path:
            if not file_path.endswith(".pkl"):
                file_path += ".pkl"
            self.chat_agent.save_chat_history(file_path)

    def load_chat_history(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Chat History", "", "Pickle Files (*.pkl)")
        if file_path:
            self.chat_agent.load_chat_history(file_path)
            self.view.conversation_window.clear()
            for message in self.chat_agent._chat_history.messages:
                if isinstance(message, HumanMessage):
                    self.view.update_conversation(f"User: {message.content.strip()}")
                elif isinstance(message, AIMessage):
                    self.view.update_conversation(f"{self.ai_name}: {message.content.strip()}")
