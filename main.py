from PyQt6.QtWidgets import QApplication
from chatbot_controller import ChatbotController
from chatbot_agent import YourOpenAIAgent
from llama_index.tools import FunctionTool
from dotenv import load_dotenv

def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)

def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)




def main():
    load_dotenv()
    import sys  # Add this import
    app = QApplication(sys.argv)

    # Initialize the FunctionTool instances
    multiply_tool = FunctionTool.from_defaults(fn=multiply)
    add_tool = FunctionTool.from_defaults(fn=add)

    chat_agent = YourOpenAIAgent(tools=[multiply_tool, add_tool])
    controller = ChatbotController(chat_agent)
    controller.show() 
    sys.exit(app.exec())  # Use sys.exit here

if __name__ == "__main__":
    main()
