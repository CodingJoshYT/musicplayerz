import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from subprocess import run

class InstallerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Music Player Installer')
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel('Click "Install" to install the Music Player', self)
        self.install_button = QPushButton('Install', self)
        self.install_button.clicked.connect(self.install_music_player)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.install_button)

        self.setLayout(vbox)

    def install_music_player(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Python Scripts (*.py)")
        file_dialog.setDefaultSuffix("py")

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                script_path = selected_files[0]
                self.label.setText(f"Installing Music Player...\n")
                run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
                run(['pyinstaller', '--onefile', script_path])
                self.label.setText(f"Installation complete!\nExecutable is in the 'dist' folder.")
            else:
                self.label.setText('Installation canceled.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    installer_gui = InstallerGUI()
    installer_gui.show()
    sys.exit(app.exec_())
