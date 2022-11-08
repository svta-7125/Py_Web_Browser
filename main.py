import sys
from PyQt5.QtCore import *                                     #Unable to find seperate functions. *Work needed*
from PyQt5.QtWidgets import *                                  #QAction and QApplication few of the functions. *Work needed*
from PyQt5.QtWebEngineWidgets import QWebEngineView 


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # NavigationBar
        NavigationBar = QToolBar()
        self.addToolBar(NavigationBar)

        back_button = QAction('<---', self)
        back_button.triggered.connect(self.browser.back)
        NavigationBar.addAction(back_button)

        forward_button = QAction('--->', self)
        forward_button.triggered.connect(self.browser.forward)
        NavigationBar.addAction(forward_button)

        reload_button = QAction('Q', self)
        reload_button.triggered.connect(self.browser.reload)
        NavigationBar.addAction(reload_button)

        home_button = QAction('~_~', self)
        home_button.triggered.connect(self.navigate_home)
        NavigationBar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        NavigationBar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('SVTA\'S BEST BROWSER!!!!!')
window = MainWindow()
app.exec_()
