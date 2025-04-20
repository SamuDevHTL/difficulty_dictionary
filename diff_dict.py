import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


class DictionarySearchApp(QWidget):
    def __init__(self):
        super().__init__()

        # Load dictionaries
        self.dict1 = self.load_json("men.json")
        self.dict2 = self.load_json("women.json")

        # Apply Dark Mode Theme
        self.apply_dark_mode()

        # Initialize UI
        self.init_ui()

    def load_json(self, filename):
        """Load dictionary data from a JSON file."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {filename} not found!")
            return {}

    def apply_dark_mode(self):
        """Apply dark mode styling to the app."""
        dark_palette = QPalette()

        # Background color
        dark_palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))

        # Text Input
        dark_palette.setColor(QPalette.ColorRole.Base, QColor(50, 50, 50))
        dark_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))

        # Highlighting
        dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 100, 150))
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))

        self.setPalette(dark_palette)

    def init_ui(self):
        """Initialize the UI components."""
        main_layout = QVBoxLayout()
        
        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Type a word to search...")
        self.search_bar.textChanged.connect(self.perform_search)
        self.search_bar.setFont(QFont("Arial", 30))
        self.search_bar.setFixedHeight(80)
        self.search_bar.setStyleSheet("""
            QLineEdit {
                background-color: #323232;
                color: white;
                border: 1px solid #555;
                padding: 8px;
                border-radius: 8px;
            }
        """)
        main_layout.addWidget(self.search_bar)

        # Dictionaries Layout
        dict_layout = QHBoxLayout()

        # Dictionary 1 UI
        self.dict1_label = QLabel("Men")
        self.dict1_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.dict1_label.setStyleSheet("color: white")  # Light Coral color
        self.dict1_text = QTextEdit()
        self.dict1_text.setReadOnly(True)
        self.dict1_text.setFont(QFont("Arial", 30))
        self.dict1_text.setStyleSheet("""
            QTextEdit {
                background-color: #424242;
                color: #ffffff;
                border: 1px solid #666;
                border-radius: 8px;
                padding: 8px;
            }
        """)

        # Dictionary 2 UI
        self.dict2_label = QLabel("Women")
        self.dict2_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.dict2_label.setStyleSheet("color: white")  # Light Sky Blue color
        self.dict2_text = QTextEdit()
        self.dict2_text.setReadOnly(True)
        self.dict2_text.setFont(QFont("Arial", 30))
        self.dict2_text.setStyleSheet("""
            QTextEdit {
                background-color: #424242;
                color: #ffffff;
                border: 1px solid #666;
                border-radius: 8px;
                padding: 8px;
            }
        """)

        # Adding widgets to layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.dict1_label)
        left_layout.addWidget(self.dict1_text)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.dict2_label)
        right_layout.addWidget(self.dict2_text)

        dict_layout.addLayout(left_layout)
        dict_layout.addSpacing(10)  # Space between columns
        dict_layout.addLayout(right_layout)

        main_layout.addLayout(dict_layout)

        # Make text areas resizable
        self.dict1_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.dict2_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.setLayout(main_layout)
        self.setWindowTitle("Difficulty Dictionary")
        self.setGeometry(200, 100, 900, 500)  # Larger, standard window size

    def perform_search(self):
        """Search for words that contain the entered text in both dictionaries."""
        query = self.search_bar.text().strip().lower()  # Convert the search query to lowercase

        if not query:
            self.dict1_text.clear()
            self.dict2_text.clear()
            return

        # Find matches in both dictionaries (convert keys to lowercase for comparison)
        matches1 = {k: v for k, v in self.dict1.items() if query in k.lower()}  # Use `in` for partial match
        matches2 = {k: v for k, v in self.dict2.items() if query in k.lower()}  # Use `in` for partial match

        # Format results
        result1 = "\n\n".join([f"{k}: {v}" for k, v in matches1.items()]) if matches1 else "Not found"
        result2 = "\n\n".join([f"{k}: {v}" for k, v in matches2.items()]) if matches2 else "Not found"

        # Display results
        self.dict1_text.setPlainText(result1)
        self.dict2_text.setPlainText(result2)




# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionarySearchApp()
    window.show()
    sys.exit(app.exec())
