Python Chatbot with GUI

This is a simple Python project demonstrating an OpenAI agent using function calls implemented in a chatbot with a GUI using PyQt6. New  functions can be added in addition to the add and multiply (check out the ones defined in `main.py`)

https://gpt-index.readthedocs.io/en/v0.6.28/examples/agent/openai_agent.html


Project Files

The project consists of four main files:

    chatbot_agent.py: This file contains the main Chatbot Agent class which handles chatting with the user, managing the chat history and performing functions based on the user's input.
    chatbot_controller.py: This file contains the controller for the GUI. It connects actions in the GUI (such as sending a message or loading/saving the chat history) to the Chatbot Agent.
    chatbot_view.py: This file contains the view for the GUI. It defines the layout of the chat window, input field, and send button.
    main.py: This is the entry point for the application. It creates instances of the Chatbot Agent and Controller, and starts the GUI.

Getting Started
Prerequisites

Before you begin, ensure you have met the following requirements:

    You have installed Python 3.7+.
    You have a valid OpenAI API key 

Installing and Running the Chatbot

To install and run the chatbot, follow these steps:

    Clone the repository: git clone <repo_url>.
    Navigate into the directory: cd <repo_directory>.
    Install the necessary Python packages: pip install -r requirements.txt.
    copy `env-example` to `.env` and fill in your OpenAI API key.
    Run the main script: python main.py.

The chatbot GUI will open. You can type your messages into the input field at the bottom and click "Send" to chat with the AI.
Built-in Functions

The chatbot includes a few built-in functions that can be called by the user via conversation. These are:

    Multiply two integers: multiply(a, b).
    Add two integers: add(a, b).

More functions can be added in `main.py`. Please remember to add to `tool_list`

Chat History

The chat history can be saved and loaded via the "File" menu at the top of the GUI. The history is saved as a .pkl file.
Contributing

If you want to contribute to this project, please fork the repository and make a pull request. We're always happy to review and accept changes!