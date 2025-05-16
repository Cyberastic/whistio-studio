import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from gui.views.modeling_view import ModelingView
from gui.views.sculpting_view import SculptingView
from gui.views.shading_view import ShadingView
from gui.views.animation_view import AnimationView
from gui.views.whisperguide_view import WhisperGuideView

class WhitioStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Whitió Studio")
        self.setGeometry(100, 100, 1280, 720)
        self.initUI()

    def initUI(self):
        # Set custom window icon
        self.setWindowIcon(QIcon('assets/icons/window_icon.png'))

        # Set custom font (optional: match Blender’s style)
        font = QFont("Roboto", 10)
        self.setFont(font)

        self.tabs = QTabWidget(self)

        # Create placeholder tab widgets
        layout_tab = QWidget()
        modeling_tab = ModelingView()
        sculpting_tab = SculptingView()
        shading_tab = ShadingView()
        animation_tab = AnimationView()
        whisperguide_tab = WhisperGuideView()

        # Add tabs
        self.tabs.addTab(layout_tab, "Layout")
        self.tabs.addTab(modeling_tab, "Modeling")
        self.tabs.addTab(sculpting_tab, "Sculpting")
        self.tabs.addTab(shading_tab, "Shading")
        self.tabs.addTab(animation_tab, "Animation")
        self.tabs.addTab(whisperguide_tab, "WhisperGuide")

        # Add tab icons
        self.tabs.setTabIcon(0, QIcon('assets/icons/layout_icon.png'))
        self.tabs.setTabIcon(1, QIcon('assets/icons/modeling_icon.png'))
        self.tabs.setTabIcon(2, QIcon('assets/icons/sculpting_icon.png'))
        self.tabs.setTabIcon(3, QIcon('assets/icons/shading_icon.png'))
        self.tabs.setTabIcon(4, QIcon('assets/icons/animation_icon.png'))
        self.tabs.setTabIcon(5, QIcon('assets/icons/whisperguide_icon.png'))

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WhitioStudio()
    window.show()
    sys.exit(app.exec_())
