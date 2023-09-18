# Form implementation generated from reading ui file 'torf_gui/about.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog:
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        AboutDialog.resize(605, 253)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            AboutDialog.sizePolicy().hasHeightForWidth()
        )
        AboutDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.programNameLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.programNameLabel.sizePolicy().hasHeightForWidth()
        )
        self.programNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.programNameLabel.setFont(font)
        self.programNameLabel.setObjectName("programNameLabel")
        self.verticalLayout.addWidget(self.programNameLabel)
        self.programVersionLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.programVersionLabel.sizePolicy().hasHeightForWidth()
        )
        self.programVersionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.programVersionLabel.setFont(font)
        self.programVersionLabel.setObjectName("programVersionLabel")
        self.verticalLayout.addWidget(self.programVersionLabel)
        self.dtVersionLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dtVersionLabel.sizePolicy().hasHeightForWidth()
        )
        self.dtVersionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dtVersionLabel.setFont(font)
        self.dtVersionLabel.setObjectName("dtVersionLabel")
        self.verticalLayout.addWidget(self.dtVersionLabel)
        self.infoLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.infoLabel.sizePolicy().hasHeightForWidth()
        )
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setOpenExternalLinks(True)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(AboutDialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.programNameLabel.setText(_translate("AboutDialog", "torf-gui"))
        self.programVersionLabel.setText(
            _translate("AboutDialog", "PROGRAM_VERSION")
        )
        self.dtVersionLabel.setText(_translate("AboutDialog", "TORF_VERSION"))
        self.infoLabel.setText(
            _translate(
                "AboutDialog",
                '<html><head/><body><p><span style=" font-size:10pt;">© 2023 Oliver Sayers</span></p><p><span style=" font-size:10pt;">torf-gui is made available under the terms of the </span><a href="http://choosealicense.com/licenses/gpl-3.0/"><span style=" font-size:10pt; text-decoration: underline; color:#0000ff;">GNU General Public License, version 3</span></a><span style=" font-size:10pt;">.</span></p><p><a href="https://github.com/SavageCore/dottorrent-gui"><span style=" font-size:10pt; text-decoration: underline; color:#0000ff;">https://github.com/SavageCore/dottorrent-gui</span></a></p></body></html>',
            )
        )