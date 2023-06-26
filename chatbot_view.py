from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class ChatbotView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.layout = QVBoxLayout()

        self.conversation_window = QTextEdit()
        self.conversation_window.setReadOnly(True)
        self.layout.addWidget(self.conversation_window)

        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.controller.send_message)
        self.layout.addWidget(self.send_button)

        self.layout.setStretchFactor(self.conversation_window, 8)  # 80% of height
        self.layout.setStretchFactor(self.input_field, 2)  # 20% of height
        self.layout.setStretchFactor(self.send_button, 0)  # Fixed height

        self.setLayout(self.layout)

    def update_conversation(self, message: str):
        self.conversation_window.append(message)
        self.input_field.clear()