from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from core.rename import rename_file


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_file: Path | None = None

        self._load_ui()
        self._connect_signals()

        self.setFixedSize(self.size())
    
    def _load_ui(self):
        loader = QUiLoader()
        ui_file = QFile("gui/ui_main.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(self.ui)

    def _connect_signals(self):