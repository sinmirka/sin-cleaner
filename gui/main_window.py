from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from core.rename import rename_file
from core.meta.image import get_image_metadata, clean_image_metadata


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_file: Path | None = None

        self._load_ui()
        self._connect_signals()

        self.setFixedSize(self.size())
    
    def _load_ui(self):
        loader = QUiLoader()

        ui_path = Path(__file__).parent / "sincleaner.ui"
        ui_file = QFile(str(ui_path))
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file)
        ui_file.close()

        self.setCentralWidget(self.ui.centralWidget())
        self.setWindowTitle(self.ui.windowTitle())


    def _connect_signals(self):
        # File tab
        self.ui.btnSelectFile.clicked.connect(self.choose_file)
        self.ui.btnRenameFile.clicked.connect(self.rename_file)

        # Metadata tab
        self.ui.btnClearMetadata.clicked.connect(self.choose_file)
        

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose file",
            "",
            "All files (*.*)",
        )

        if not file_path:
            return
        
        self.current_file = Path(file_path)
        self.ui.labelCurrentFile.setText(self.current_file.name)

    def rename_file(self):
        if not self.current_file:
            QMessageBox.warning(self, "Error", "No file selected")
            return
        
        try:
            report = rename_file(self.current_file)
        except Exception as e:
            QMessageBox.critical(self, "Rename failed", str(e))
            return
        
        self.ui.textInfo.setPlainText("\n".join(report))