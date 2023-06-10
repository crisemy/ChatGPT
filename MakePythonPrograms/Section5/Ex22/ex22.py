import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit


class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Temperature Converter')

        self.celsius_label = QLabel('Celsius:')
        self.fahrenheit_label = QLabel('Fahrenheit:')

        self.celsius_input = QLineEdit()
        self.celsius_input.textChanged.connect(self.celsius_to_fahrenheit)

        self.fahrenheit_input = QLineEdit()
        self.fahrenheit_input.textChanged.connect(self.fahrenheit_to_celsius)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.celsius_label)
        self.layout.addWidget(self.celsius_input)
        self.layout.addWidget(self.fahrenheit_label)
        self.layout.addWidget(self.fahrenheit_input)

        self.setLayout(self.layout)

    def celsius_to_fahrenheit(self, text):
        celsius = text
        if celsius:
            try:
                fahrenheit = (float(celsius) * 9 / 5) + 32
                self.fahrenheit_input.setText(str(fahrenheit))
            except ValueError:
                self.fahrenheit_input.setText('Invalid input')

    def fahrenheit_to_celsius(self, text):
        fahrenheit = text
        if fahrenheit:
            try:
                celsius = (float(fahrenheit) - 32) * 5 / 9
                self.celsius_input.setText(str(celsius))
            except ValueError:
                self.celsius_input.setText('Invalid input')


if __name__ == '__main__':
    app = QApplication([])
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec())