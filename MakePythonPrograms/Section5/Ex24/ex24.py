import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton


class ExcelViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excel Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_file)

        self.view_button = QPushButton("View")
        self.view_button.clicked.connect(self.view_excel)
        self.view_button.setEnabled(False)

        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.open_button)
        self.button_layout.addWidget(self.view_button)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.button_layout)

        self.table_widget = QTableWidget()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.button_widget)
        main_layout.addWidget(self.table_widget)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.file_path = file_path
            self.view_button.setEnabled(True)

    def view_excel(self):
        data = pd.read_excel(self.file_path)
        self.table_widget.setRowCount(data.shape[0])
        self.table_widget.setColumnCount(data.shape[1])

        headers = data.columns
        self.table_widget.setHorizontalHeaderLabels(headers)

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                cell_value = str(data.values[i, j])
                self.table_widget.setItem(i, j, QTableWidgetItem(cell_value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    excel_viewer = ExcelViewer()
    excel_viewer.show()
    sys.exit(app.exec())