from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class TexturingView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Texturing Tab"))
        self.setLayout(layout)
