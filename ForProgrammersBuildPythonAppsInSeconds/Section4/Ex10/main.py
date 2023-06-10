import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDateEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime

class TemperatureGraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Graph App")
        self.setGeometry(100, 100, 800, 600)

        self.date_label_start = QLabel("Start Date:")
        self.date_edit_start = QDateEdit()
        self.date_edit_start.setCalendarPopup(True)

        self.date_label_end = QLabel("End Date:")
        self.date_edit_end = QDateEdit()
        self.date_edit_end.setCalendarPopup(True)

        self.graph_button = QPushButton("Generate Graph")
        self.graph_button.clicked.connect(self.generate_graph)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.date_label_start)
        layout.addWidget(self.date_edit_start)
        layout.addWidget(self.date_label_end)
        layout.addWidget(self.date_edit_end)
        layout.addWidget(self.graph_button)
        layout.addWidget(self.canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def generate_graph(self):
        start_date = self.date_edit_start.date().toPyDate()
        end_date = self.date_edit_end.date().toPyDate()

        dates, temperatures = self.read_data_from_csv("temperature_data.csv")
        filtered_dates, filtered_temperatures = self.filter_data_by_date(dates, temperatures, start_date, end_date)

        self.figure.clear()
        ax = self.figure.add_subplot()
        ax.plot(filtered_dates, filtered_temperatures)
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature")
        ax.set_title("Temperature Graph")

        self.canvas.draw()

    @staticmethod
    def read_data_from_csv(file_path):
        dates = []
        temperatures = []
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                date_str = row["Date"]
                temperature = float(row["Temperature"])
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                dates.append(date)
                temperatures.append(temperature)
        return dates, temperatures


    @staticmethod
    def filter_data_by_date(dates, temperatures, start_date, end_date):
        filtered_dates = []
        filtered_temperatures = []
        for date, temperature in zip(dates, temperatures):
            if start_date <= date <= end_date:
                filtered_dates.append(date)
                filtered_temperatures.append(temperature)
        return filtered_dates, filtered_temperatures


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureGraphApp()
    window.show()
    sys.exit(app.exec())