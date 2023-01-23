from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, shutil, glob, sys
from hurry.filesize import size as convert_size

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

file_size_system = [
    (1024 ** 5, ' PB'),
    (1024 ** 4, ' TB'),
    (1024 ** 3, ' GB'),
    (1024 ** 2, ' MB'),
    (1024 ** 1, ' KB'),
    (1024 ** 0, ' bytes'),
]

home_path = 'C:' + os.environ['HOMEPATH']
downloads_path = 'Downloads'
working_dir = os.path.join(home_path, downloads_path)
os.chdir(working_dir)

global size_td_other
global items_td_other
size_td_other = 0
items_td_other = 0

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setFixedSize(450, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        main_window.setFont(font)
        if getattr(sys, 'frozen', False):
            self.script_dir = os.path.dirname(sys.executable)
        else:
            self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 431, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.welcome_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.vertical_layout.addWidget(self.welcome_label)
        self.choose_mode_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_mode_label.setFont(font)
        self.choose_mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_mode_label.setObjectName("choose_mode_label")
        self.vertical_layout.addWidget(self.choose_mode_label)
        self.default_m_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.default_m_check.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/default_mode_radio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.default_m_check.setIcon(icon1)
        self.default_m_check.setCheckable(True)
        self.default_m_check.setChecked(True)
        self.default_m_check.setObjectName("default_m_check")
        self.vertical_layout.addWidget(self.default_m_check)
        self.installers_m_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.installers_m_check.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/installers_radio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.installers_m_check.setIcon(icon2)
        self.installers_m_check.setCheckable(True)
        self.installers_m_check.setObjectName("installers_m_check")
        self.vertical_layout.addWidget(self.installers_m_check)
        self.images_m_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.images_m_check.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/images_radio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images_m_check.setIcon(icon3)
        self.images_m_check.setCheckable(True)
        self.images_m_check.setObjectName("images_m_check")
        self.vertical_layout.addWidget(self.images_m_check)
        self.doc_m_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doc_m_check.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/doc_check_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doc_m_check.setIcon(icon4)
        self.doc_m_check.setCheckable(True)
        self.doc_m_check.setObjectName("doc_m_check")
        self.vertical_layout.addWidget(self.doc_m_check)
        self.audio_m_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.audio_m_check.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/audios_check_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio_m_check.setIcon(icon5)
        self.audio_m_check.setCheckable(True)
        self.audio_m_check.setObjectName("audio_m_check")
        self.vertical_layout.addWidget(self.audio_m_check)
        self.videos_m_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.videos_m_check.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/videos_radio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.videos_m_check.setIcon(icon6)
        self.videos_m_check.setCheckable(True)
        self.videos_m_check.setObjectName("videos_m_check")
        self.vertical_layout.addWidget(self.videos_m_check)
        self.items_td_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_td_label.setFont(font)
        self.items_td_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_td_label.setObjectName("items_td_label")
        self.vertical_layout.addWidget(self.items_td_label)
        self.size_td_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.size_td_label.setFont(font)
        self.size_td_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_td_label.setObjectName("size_td_label")
        self.vertical_layout.addWidget(self.size_td_label)
        self.clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked=lambda: self.clear_downloads())
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setAutoFillBackground(False)
        self.clear_button.setStyleSheet("QPushButton#clear_button {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(4, 128, 92, 255), stop:0.25 rgba(20, 197, 152, 255), stop:0.5 rgba(13, 172, 160, 255), stop:0.75 rgba(10, 160, 164, 255), stop:1 rgba(10, 93, 94, 255));\n"
"border-radius: 9px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover#clear_button {\n"
"text-decoration: underline;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(self.script_dir + os.path.sep + "assets/button_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon7)
        self.clear_button.setFlat(False)
        self.clear_button.setObjectName("clear_button")
        self.vertical_layout.addWidget(self.clear_button)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.restrict_checkboxes_default()
        self.restrict_checkboxes_other()

        self.default_m_check.stateChanged.connect(lambda: self.restrict_checkboxes_default())
        self.installers_m_check.stateChanged.connect(lambda: self.restrict_checkboxes_other())
        self.images_m_check.stateChanged.connect(lambda: self.restrict_checkboxes_other())
        self.audio_m_check.stateChanged.connect(lambda: self.restrict_checkboxes_other())
        self.doc_m_check.stateChanged.connect(lambda: self.restrict_checkboxes_other())
        self.videos_m_check.stateChanged.connect(lambda: self.restrict_checkboxes_other())

        self.default_m_check.stateChanged.connect(lambda: self.show_size_and_items_default())
        self.installers_m_check.stateChanged.connect(lambda: self.show_size_and_items_installers())
        self.images_m_check.stateChanged.connect(lambda: self.show_size_and_items_images())
        self.audio_m_check.stateChanged.connect(lambda: self.show_size_and_items_audios())
        self.doc_m_check.stateChanged.connect(lambda: self.show_size_and_items_docs())
        self.videos_m_check.stateChanged.connect(lambda: self.show_size_and_items_videos())


    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Clear Downloads"))
        self.welcome_label.setText(_translate("main_window", "Welcome, let\'s clear your downloads folder."))
        self.choose_mode_label.setText(_translate("main_window", "Choose mode:"))
        self.default_m_check.setText(_translate("main_window", "Default: deletes all files"))
        self.installers_m_check.setText(_translate("main_window", "Installers: deletes all installer files (including .exe files)"))
        self.images_m_check.setText(_translate("main_window", "Images: deletes all image files"))
        self.doc_m_check.setText(_translate("main_window", "Documents: deletes all document files (e.g. .pdf files)"))
        self.audio_m_check.setText(_translate("main_window", "Audios: deletes all audio files"))
        self.videos_m_check.setText(_translate("main_window", "Videos: deletes all video files"))
        self.items_td_label.setText(_translate('main_window', 'Items: Loading...'))
        self.size_td_label.setText(_translate("main_window", 'Size: Loading...'))
        self.clear_button.setText(_translate("main_window", "Clear Downloads"))
    
    # My Functions

    def calculate_size_and_items_after_startup(self):
        _translate = QtCore.QCoreApplication.translate
        items_td = len(os.listdir())
        self.items_td_label.setText(_translate('main_window', f'Items: {items_td}'))

        total_size_td = 0
        for dirpath, dirnames, filenames in os.walk(working_dir):
            for file in filenames:
                filepath = os.path.join(dirpath, file)
                if not os.path.islink(filepath):
                    total_size_td += os.path.getsize(filepath)
        self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(total_size_td, system=file_size_system)}"))


    def show_startup_popup(self):
        def value_to_bool(value):
            if type(value) is str:
                return True if value == 'true' else False
            elif value is None:
                return False
            else:
                return value
        
        settings = QtCore.QSettings('Ansh Thaker', 'Clear Downloads')
        is_msg_hidden = value_to_bool(settings.value('is_ticked'))

        if not is_msg_hidden:
            msg = QMessageBox()
            msg.setWindowTitle('Welcome!')
            msg.setText('Welcome, please note that all files are deleted permanently and not stored in the Recycle Bin.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            check_box = QtWidgets.QCheckBox("Don't show this again.")
            msg.setCheckBox(check_box)
            show = msg.exec_()
            is_ticked = check_box.isChecked()
            settings.setValue('is_ticked', is_ticked)

    
    def restrict_checkboxes_other(self):
        other_checkboxes = [self.installers_m_check, self.images_m_check, self.audio_m_check, self.doc_m_check, self.videos_m_check]
        for checkbox in other_checkboxes:
            if checkbox.isChecked():
                self.default_m_check.setChecked(False)
    

    def restrict_checkboxes_default(self):
        other_checkboxes = [self.installers_m_check, self.images_m_check, self.audio_m_check, self.doc_m_check, self.videos_m_check]
        if self.default_m_check.isChecked():
            for checkbox in other_checkboxes:
                checkbox.setChecked(False)
            self.default_m_check.setChecked(True)
    

    def set_items_and_size_to_zero(self, _translate):
        self.size_td_label.setText(_translate("main_window", f"Size: 0 bytes"))
        self.items_td_label.setText(_translate("main_window", f"Items: 0"))


    def show_size_and_items_default(self):
        _translate = QtCore.QCoreApplication.translate

        self.size_td_label.setText(_translate("main_window", 'Size: Loading...'))
        self.items_td_label.setText(_translate('main_window', 'Items: Loading...'))

        if self.default_m_check.isChecked():

            total_size_td = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_td += os.path.getsize(filepath)
            self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(total_size_td, system=file_size_system)}"))

            items_td = len(os.listdir())
            self.items_td_label.setText(_translate('main_window', f'Items: {items_td}'))

        elif not self.default_m_check.isChecked() and not self.installers_m_check.isChecked() and not self.images_m_check.isChecked() and not self.audio_m_check.isChecked() and not self.doc_m_check.isChecked() and not self.videos_m_check.isChecked():
            self.size_td_label.setText(_translate("main_window", f"Size: 0 bytes"))
            self.items_td_label.setText(_translate('main_window', f'Items: 0'))
    

    def show_size_and_items_installers(self):
        _translate = QtCore.QCoreApplication.translate
        if self.installers_m_check.isChecked():

            types = ('*.msi', '*.exe', '*.msm', '*.msp', '*.mst', '*.idt', '*.cub', '*.pcp')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                global size_td_other
                global items_td_other
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other += os.path.getsize(file_path)
                        items_td_other += 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
            else:
                self.set_items_and_size_to_zero(_translate)

        elif not self.installers_m_check.isChecked():
            types = ('*.msi', '*.exe', '*.msm', '*.msp', '*.mst', '*.idt', '*.cub', '*.pcp')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other -= os.path.getsize(file_path)
                        items_td_other -= 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
    

    def show_size_and_items_images(self):
        _translate = QtCore.QCoreApplication.translate
        if self.images_m_check.isChecked():

            types = ('*.apng', '*.avif', '*.gif', '*.jpg', '*.jpeg', '*.png', '*.svg', '*.webp', '*.bmp', '*.ico', '*.tiff')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                global size_td_other
                global items_td_other
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other += os.path.getsize(file_path)
                        items_td_other += 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
            else:
                self.set_items_and_size_to_zero(_translate)

        elif not self.images_m_check.isChecked():
            types = ('*.apng', '*.avif', '*.gif', '*.jpg', '*.jpeg', '*.png', '*.svg', '*.webp', '*.bmp', '*.ico', '*.tiff')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other -= os.path.getsize(file_path)
                        items_td_other -= 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
            else:
                self.set_items_and_size_to_zero(_translate)
    

    def show_size_and_items_audios(self):
        _translate = QtCore.QCoreApplication.translate
        if self.audio_m_check.isChecked():

            types = ('*.aac', '*.ac3', '*.aif', '*.aifc', '*.aiff', '*.amr', '*.au', '*.caf', '*.flac', '*.m4a', '*.m4b', '*.mp3', '*.oga', '*.voc', '*.wav', '*.weba', '*.wma')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                global size_td_other
                global items_td_other
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other += os.path.getsize(file_path)
                        items_td_other += 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
            else:
                self.set_items_and_size_to_zero(_translate)

        elif not self.audio_m_check.isChecked():
            types = ('*.aac', '*.ac3', '*.aif', '*.aifc', '*.aiff', '*.amr', '*.au', '*.caf', '*.flac', '*.m4a', '*.m4b', '*.mp3', '*.oga', '*.voc', '*.wav', '*.weba', '*.wma')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other -= os.path.getsize(file_path)
                        items_td_other -= 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
    

    def show_size_and_items_docs(self):
        _translate = QtCore.QCoreApplication.translate
        if self.doc_m_check.isChecked():

            types = ('*.abw', '*.djvu', '*.doc', '*.docm', '*.docx', '*.dot', '*.dotx', '*.hwp', '*.lwp', '*.md', '*.odt', '*.pages', '*.pdf', '*.rst', '*.rtf', '*.tex', '*.txt', '*.wpd', '*.wps', '*.zabw')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                global size_td_other
                global items_td_other
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other += os.path.getsize(file_path)
                        items_td_other += 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
            else:
                self.set_items_and_size_to_zero(_translate)

        elif not self.doc_m_check.isChecked():
            types = ('*.abw', '*.djvu', '*.doc', '*.docm', '*.docx', '*.dot', '*.dotx', '*.hwp', '*.lwp', '*.md', '*.odt', '*.pages', '*.pdf', '*.rst', '*.rtf', '*.tex', '*.txt', '*.wpd', '*.wps', '*.zabw')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other -= os.path.getsize(file_path)
                        items_td_other -= 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
    

    def show_size_and_items_videos(self):
        _translate = QtCore.QCoreApplication.translate
        if self.videos_m_check.isChecked():

            types = ('*.mp4', '*.mov', '*.wmv', '*.avi', '*.avchd', '*.flv', '*.f4v', '*.swf', '*.mkv')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                global size_td_other
                global items_td_other
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other += os.path.getsize(file_path)
                        items_td_other += 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))
            else:
                self.set_items_and_size_to_zero(_translate)

        elif not self.videos_m_check.isChecked():
            types = ('*.mp4', '*.mov', '*.wmv', '*.avi', '*.avchd', '*.flv', '*.f4v', '*.swf', '*.mkv')    
            files_grabbed = []

            for files in types:
                files_grabbed.extend(glob.glob(files))
            if files_grabbed:
                self.size_td_label.setText(_translate("main_window", 'Loading...'))
                self.items_td_label.setText(_translate("main_window", 'Loading...'))
                for filename in files_grabbed:
                    file_path = os.path.join(working_dir, filename)
                    if not os.path.islink(file_path):
                        size_td_other -= os.path.getsize(file_path)
                        items_td_other -= 1
            
                self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(size_td_other, system=file_size_system)}"))
                self.items_td_label.setText(_translate("main_window", f"Items: {items_td_other}"))

    
    def clear_default(self):

        _translate = QtCore.QCoreApplication.translate

        items_deleted = 0
        size_deleted = 0

        if os.listdir():
            self.clear_button.setText(_translate("main_window", "Deleting..."))
            for filename in os.listdir():
                file_path = os.path.join(working_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        size = os.path.getsize(file_path)
                        os.unlink(file_path)
                        items_deleted += 1
                        size_deleted += size
                    elif os.path.isdir(file_path):
                        size = 0
                        for dirpath, dirnames, filenames in os.walk(file_path):
                            for file in filenames:
                                filepath = os.path.join(dirpath, file)
                                if not os.path.islink(filepath):
                                    size += os.path.getsize(filepath)
                        shutil.rmtree(file_path)
                        items_deleted += 1
                        size_deleted += size
                except Exception as error:
                    msg = QMessageBox()
                    msg.setWindowTitle('Failed to delete file')
                    msg.setText('Failed to delete %s.\nReason: %s' % (file_path, error))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(self.icon)
                    msg.setStandardButtons(msg.Ok)
                    show = msg.exec_()

            total_size_ad = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_ad += os.path.getsize(filepath)
            
            self.clear_button.setEnabled(False)
            self.size_td_label.setText(_translate("main_window", 'Loading...'))
            total_size_td = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_td += os.path.getsize(filepath)
            self.size_td_label.setText(_translate("main_window", f"Size: {convert_size(total_size_td, system=file_size_system)}"))

            self.items_td_label.setText(_translate('main_window', f'Loading...'))
            items_td = len(os.listdir())
            self.items_td_label.setText(_translate('main_window', f'Items: {items_td}'))

            self.clear_button.setEnabled(True)
            self.clear_button.setText(_translate("main_window", "Deleted!"))

            if items_deleted == 1:
                items_or_item = 'item'
                were_or_was = 'was'
            elif items_deleted > 1:
                items_or_item = 'items'
                were_or_was = 'were'

            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Default Mode')
            msg.setText(f'{items_deleted} {items_or_item} with a total size of {convert_size(size_deleted, system=file_size_system)} {were_or_was} deleted sucessfully.\nDownloads Size after deleting: {convert_size(total_size_ad, system=file_size_system)}')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('No items found')
            msg.setText(f'No files or folders found to delete in the Downloads folder.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
    

    def clear_installers(self):

        _translate = QtCore.QCoreApplication.translate

        items_deleted = 0
        size_deleted = 0

        types = ('*.msi', '*.exe', '*.msm', '*.msp', '*.mst', '*.idt', '*.cub', '*.pcp')    
        files_grabbed = []

        for files in types:
            files_grabbed.extend(glob.glob(files))
        if files_grabbed:
            self.clear_button.setText(_translate("main_window", "Deleting..."))
            for filename in files_grabbed:
                file_path = os.path.join(working_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        size = os.path.getsize(file_path)
                        os.unlink(file_path)
                        items_deleted += 1
                        size_deleted += size
                except Exception as error:
                    msg = QMessageBox()
                    msg.setWindowTitle('Failed to delete file')
                    msg.setText('Failed to delete %s.\nReason: %s' % (file_path, error))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(self.icon)
                    msg.setStandardButtons(msg.Ok)
                    show = msg.exec_()
            
            total_size_ad = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_ad += os.path.getsize(filepath)
            
            self.clear_button.setText(_translate("main_window", "Deleted!"))
            global size_td_other
            global items_td_other
            size_td_other -= size_deleted
            items_td_other -= items_deleted
            self.show_size_and_items_installers()
            
            if items_deleted == 1:
                installers_or_installer = 'installer'
                were_or_was = 'was'
            elif items_deleted > 1:
                installers_or_installer = 'installers'
                were_or_was = 'were'

            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Installers Mode')
            msg.setText(f'{items_deleted} {installers_or_installer} with a total size of {convert_size(size_deleted, system=file_size_system)} {were_or_was} deleted sucessfully.\nDownloads Size after deleting: {convert_size(total_size_ad, system=file_size_system)}')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('No installers found')
            msg.setText(f'No installer files found to delete in the Downloads folder.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()
            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
    

    def clear_images(self):

        _translate = QtCore.QCoreApplication.translate

        items_deleted = 0
        size_deleted = 0

        types = ('*.apng', '*.avif', '*.gif', '*.jpg', '*.jpeg', '*.png', '*.svg', '*.webp', '*.bmp', '*.ico', '*.tiff')    
        files_grabbed = []

        for files in types:
            files_grabbed.extend(glob.glob(files))
        if files_grabbed:
            self.clear_button.setText(_translate("main_window", "Deleting..."))
            for filename in files_grabbed:
                file_path = os.path.join(working_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        size = os.path.getsize(file_path)
                        os.unlink(file_path)
                        items_deleted += 1
                        size_deleted += size
                except Exception as error:
                    msg = QMessageBox()
                    msg.setWindowTitle('Failed to delete file')
                    msg.setText('Failed to delete %s.\nReason: %s' % (file_path, error))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(self.icon)
                    msg.setStandardButtons(msg.Ok)
                    show = msg.exec_()
            
            total_size_ad = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_ad += os.path.getsize(filepath)
            
            self.clear_button.setText(_translate("main_window", "Deleted!"))
            global size_td_other
            global items_td_other
            size_td_other -= size_deleted
            items_td_other -= items_deleted
            self.show_size_and_items_images()
            
            if items_deleted == 1:
                images_or_image = 'image'
                were_or_was = 'was'
            elif items_deleted > 1:
                images_or_image = 'images'
                were_or_was = 'were'

            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Images Mode')
            msg.setText(f'{items_deleted} {images_or_image} with a total size of {convert_size(size_deleted, system=file_size_system)} {were_or_was} deleted sucessfully.\nDownloads Size after deleting: {convert_size(total_size_ad, system=file_size_system)}')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('No images found')
            msg.setText(f'No image files found to delete in the Downloads folder.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))

    
    def clear_audios(self):

        _translate = QtCore.QCoreApplication.translate
        
        items_deleted = 0
        size_deleted = 0

        types = ('*.aac', '*.ac3', '*.aif', '*.aifc', '*.aiff', '*.amr', '*.au', '*.caf', '*.flac', '*.m4a', '*.m4b', '*.mp3', '*.oga', '*.voc', '*.wav', '*.weba', '*.wma')    
        files_grabbed = []

        for files in types:
            files_grabbed.extend(glob.glob(files))
        if files_grabbed:
            self.clear_button.setText(_translate("main_window", "Deleting..."))
            for filename in files_grabbed:
                file_path = os.path.join(working_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        size = os.path.getsize(file_path)
                        os.unlink(file_path)
                        items_deleted += 1
                        size_deleted += size
                except Exception as error:
                    msg = QMessageBox()
                    msg.setWindowTitle('Failed to delete file')
                    msg.setText('Failed to delete %s.\nReason: %s' % (file_path, error))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(self.icon)
                    msg.setStandardButtons(msg.Ok)
                    show = msg.exec_()
            
            total_size_ad = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_ad += os.path.getsize(filepath)
            
            self.clear_button.setText(_translate("main_window", "Deleted!"))
            global size_td_other
            global items_td_other
            size_td_other -= size_deleted
            items_td_other -= items_deleted
            self.show_size_and_items_audios()
            
            if items_deleted == 1:
                audio_or_audios = 'audio'
                were_or_was = 'was'
            elif items_deleted > 1:
                audio_or_audios = 'audios'
                were_or_was = 'were'

            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Audios Mode')
            msg.setText(f'{items_deleted} {audio_or_audios} with a total size of {convert_size(size_deleted, system=file_size_system)} {were_or_was} deleted sucessfully.\nDownloads Size after deleting: {convert_size(total_size_ad, system=file_size_system)}')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('No audios found')
            msg.setText(f'No audio files found to delete in the Downloads folder.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
    

    def clear_docs(self):

        _translate = QtCore.QCoreApplication.translate
                
        items_deleted = 0
        size_deleted = 0

        types = ('*.abw', '*.djvu', '*.doc', '*.docm', '*.docx', '*.dot', '*.dotx', '*.hwp', '*.lwp', '*.md', '*.odt', '*.pages', '*.pdf', '*.rst', '*.rtf', '*.tex', '*.txt', '*.wpd', '*.wps', '*.zabw')    
        files_grabbed = []

        for files in types:
            files_grabbed.extend(glob.glob(files))
        if files_grabbed:
            self.clear_button.setText(_translate("main_window", "Deleting..."))
            for filename in files_grabbed:
                file_path = os.path.join(working_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        size = os.path.getsize(file_path)
                        os.unlink(file_path)
                        items_deleted += 1
                        size_deleted += size
                except Exception as error:
                    msg = QMessageBox()
                    msg.setWindowTitle('Failed to delete file')
                    msg.setText('Failed to delete %s.\nReason: %s' % (file_path, error))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(self.icon)
                    msg.setStandardButtons(msg.Ok)
                    show = msg.exec_()
            
            total_size_ad = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_ad += os.path.getsize(filepath)
            
            self.clear_button.setText(_translate("main_window", "Deleted!"))
            global size_td_other
            global items_td_other
            size_td_other -= size_deleted
            items_td_other -= items_deleted
            self.show_size_and_items_docs()
            
            if items_deleted == 1:
                documents_or_document = 'document'
                were_or_was = 'was'
            elif items_deleted > 1:
                documents_or_document = 'documents'
                were_or_was = 'were'

            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Documents Mode')
            msg.setText(f'{items_deleted} {documents_or_document} with a total size of {convert_size(size_deleted, system=file_size_system)} {were_or_was} deleted sucessfully.\nDownloads Size after deleting: {convert_size(total_size_ad, system=file_size_system)}')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('No documents found')
            msg.setText(f'No document files found to delete in the Downloads folder.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
    

    def clear_videos(self):

        _translate = QtCore.QCoreApplication.translate
                        
        items_deleted = 0
        size_deleted = 0

        types = ('*.mp4', '*.mov', '*.wmv', '*.avi', '*.avchd', '*.flv', '*.f4v', '*.swf', '*.mkv')    
        files_grabbed = []

        for files in types:
            files_grabbed.extend(glob.glob(files))
        if files_grabbed:
            self.clear_button.setText(_translate("main_window", "Deleting..."))
            for filename in files_grabbed:
                file_path = os.path.join(working_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        size = os.path.getsize(file_path)
                        os.unlink(file_path)
                        items_deleted += 1
                        size_deleted += size
                except Exception as error:
                    msg = QMessageBox()
                    msg.setWindowTitle('Failed to delete file')
                    msg.setText('Failed to delete %s.\nReason: %s' % (file_path, error))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(self.icon)
                    msg.setStandardButtons(msg.Ok)
                    show = msg.exec_()
            
            total_size_ad = 0
            for dirpath, dirnames, filenames in os.walk(working_dir):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    if not os.path.islink(filepath):
                        total_size_ad += os.path.getsize(filepath)
            
            self.clear_button.setText(_translate("main_window", "Deleted!"))
            global size_td_other
            global items_td_other
            size_td_other -= size_deleted
            items_td_other -= items_deleted
            self.show_size_and_items_videos()
            
            if items_deleted == 1:
                video_or_videos = 'video'
                were_or_was = 'was'
            elif items_deleted > 1:
                video_or_videos = 'videos'
                were_or_was = 'were'

            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Videos Mode')
            msg.setText(f'{items_deleted} {video_or_videos} with a total size of {convert_size(size_deleted, system=file_size_system)} {were_or_was} deleted sucessfully.\nDownloads Size after deleting: {convert_size(total_size_ad, system=file_size_system)}')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('No videos found')
            msg.setText(f'No video files found to delete in the Downloads folder.')
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Ok)
            show = msg.exec_()

            self.clear_button.setText(_translate("main_window", "Clear Downloads"))
    
    
    def clear_other(self):
        if self.installers_m_check.isChecked():
            self.clear_installers()
        if self.images_m_check.isChecked():
            self.clear_images()
        if self.audio_m_check.isChecked():
            self.clear_audios()
        if self.doc_m_check.isChecked():
            self.clear_docs()
        if self.videos_m_check.isChecked():
            self.clear_videos()


    def clear_downloads(self):
        def value_to_bool(value):
            if type(value) is str:
                return True if value == 'true' else False
            elif value is None:
                return False
            else:
                return value
        
        settings = QtCore.QSettings('Ansh Thaker', 'Clear Downloads')
        is_msg_hidden = value_to_bool(settings.value('is_ticked_2'))

        if not is_msg_hidden:
            msg = QMessageBox()
            msg.setWindowTitle('Clear Downloads Confirmation')
            msg.setText('Are you sure you want to clear your downloads folder using the selected mode(s)?')
            msg.setIcon(QMessageBox.Question)
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(msg.Yes | msg.No)
            check_box = QtWidgets.QCheckBox("Don't confirm again.")
            msg.setCheckBox(check_box)
            show = msg.exec_()
            is_ticked = check_box.isChecked()
            settings.setValue('is_ticked_2', is_ticked)
        
            if show == msg.Yes:
                if self.default_m_check.isChecked():
                    self.clear_default()
                else:
                    self.clear_other()
        
        else:
            if self.default_m_check.isChecked():
                self.clear_default()
            else:
                self.clear_other()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    ui.show_startup_popup()
    ui.calculate_size_and_items_after_startup()
    sys.exit(app.exec_())
