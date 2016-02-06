# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manuskript/ui/views/propertiesView_ui.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_propertiesView(object):
    def setupUi(self, propertiesView):
        propertiesView.setObjectName("propertiesView")
        propertiesView.resize(192, 159)
        self.verticalLayout = QtWidgets.QVBoxLayout(propertiesView)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtTitle = lineEditView(propertiesView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txtTitle.setFont(font)
        self.txtTitle.setStyleSheet("background:transparent;")
        self.txtTitle.setFrame(False)
        self.txtTitle.setObjectName("txtTitle")
        self.verticalLayout.addWidget(self.txtTitle)
        self.stack = QtWidgets.QStackedWidget(propertiesView)
        self.stack.setObjectName("stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblPOV = QtWidgets.QLabel(self.page)
        self.lblPOV.setObjectName("lblPOV")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblPOV)
        self.cmbPOV = cmbOutlinePersoChoser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPOV.sizePolicy().hasHeightForWidth())
        self.cmbPOV.setSizePolicy(sizePolicy)
        self.cmbPOV.setFrame(False)
        self.cmbPOV.setObjectName("cmbPOV")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbPOV)
        self.lblStatus = QtWidgets.QLabel(self.page)
        self.lblStatus.setObjectName("lblStatus")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblStatus)
        self.cmbStatus = cmbOutlineStatusChoser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbStatus.sizePolicy().hasHeightForWidth())
        self.cmbStatus.setSizePolicy(sizePolicy)
        self.cmbStatus.setFrame(False)
        self.cmbStatus.setObjectName("cmbStatus")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbStatus)
        self.lblLabel = QtWidgets.QLabel(self.page)
        self.lblLabel.setObjectName("lblLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblLabel)
        self.cmbLabel = cmbOutlineLabelChoser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLabel.sizePolicy().hasHeightForWidth())
        self.cmbLabel.setSizePolicy(sizePolicy)
        self.cmbLabel.setFrame(False)
        self.cmbLabel.setObjectName("cmbLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbLabel)
        self.lblCompile = QtWidgets.QLabel(self.page)
        self.lblCompile.setObjectName("lblCompile")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblCompile)
        self.chkCompile = chkOutlineCompile(self.page)
        self.chkCompile.setText("")
        self.chkCompile.setObjectName("chkCompile")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.chkCompile)
        self.lblGoal = QtWidgets.QLabel(self.page)
        self.lblGoal.setObjectName("lblGoal")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblGoal)
        self.txtGoal = lineEditView(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtGoal.sizePolicy().hasHeightForWidth())
        self.txtGoal.setSizePolicy(sizePolicy)
        self.txtGoal.setAutoFillBackground(False)
        self.txtGoal.setStyleSheet("border-radius: 6px;")
        self.txtGoal.setFrame(False)
        self.txtGoal.setObjectName("txtGoal")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtGoal)
        self.lblLabel_2 = QtWidgets.QLabel(self.page)
        self.lblLabel_2.setObjectName("lblLabel_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblLabel_2)
        self.cmbType = cmbOutlineTypeChoser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbType.sizePolicy().hasHeightForWidth())
        self.cmbType.setSizePolicy(sizePolicy)
        self.cmbType.setFrame(False)
        self.cmbType.setObjectName("cmbType")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cmbType)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblPOV_2 = QtWidgets.QLabel(self.page_2)
        self.lblPOV_2.setObjectName("lblPOV_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblPOV_2)
        self.cmbPOVMulti = cmbOutlinePersoChoser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPOVMulti.sizePolicy().hasHeightForWidth())
        self.cmbPOVMulti.setSizePolicy(sizePolicy)
        self.cmbPOVMulti.setFrame(False)
        self.cmbPOVMulti.setObjectName("cmbPOVMulti")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbPOVMulti)
        self.label_31 = QtWidgets.QLabel(self.page_2)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.cmbStatusMulti = cmbOutlineStatusChoser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbStatusMulti.sizePolicy().hasHeightForWidth())
        self.cmbStatusMulti.setSizePolicy(sizePolicy)
        self.cmbStatusMulti.setFrame(False)
        self.cmbStatusMulti.setObjectName("cmbStatusMulti")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbStatusMulti)
        self.label_34 = QtWidgets.QLabel(self.page_2)
        self.label_34.setObjectName("label_34")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.cmbLabelMulti = cmbOutlineLabelChoser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLabelMulti.sizePolicy().hasHeightForWidth())
        self.cmbLabelMulti.setSizePolicy(sizePolicy)
        self.cmbLabelMulti.setFrame(False)
        self.cmbLabelMulti.setObjectName("cmbLabelMulti")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbLabelMulti)
        self.label_35 = QtWidgets.QLabel(self.page_2)
        self.label_35.setObjectName("label_35")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.chkCompileMulti = chkOutlineCompile(self.page_2)
        self.chkCompileMulti.setText("")
        self.chkCompileMulti.setObjectName("chkCompileMulti")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chkCompileMulti)
        self.label_36 = QtWidgets.QLabel(self.page_2)
        self.label_36.setObjectName("label_36")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.txtGoalMulti = lineEditView(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtGoalMulti.sizePolicy().hasHeightForWidth())
        self.txtGoalMulti.setSizePolicy(sizePolicy)
        self.txtGoalMulti.setAutoFillBackground(False)
        self.txtGoalMulti.setStyleSheet("border-radius: 6px;")
        self.txtGoalMulti.setFrame(False)
        self.txtGoalMulti.setObjectName("txtGoalMulti")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtGoalMulti)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.stack.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stack)

        self.retranslateUi(propertiesView)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(propertiesView)

    def retranslateUi(self, propertiesView):
        _translate = QtCore.QCoreApplication.translate
        propertiesView.setWindowTitle(_translate("propertiesView", "Form"))
        self.lblPOV.setText(_translate("propertiesView", "POV"))
        self.lblStatus.setText(_translate("propertiesView", "Status"))
        self.lblLabel.setText(_translate("propertiesView", "Label"))
        self.lblCompile.setText(_translate("propertiesView", "Compile"))
        self.lblGoal.setText(_translate("propertiesView", "Goal"))
        self.txtGoal.setPlaceholderText(_translate("propertiesView", "Word count"))
        self.lblLabel_2.setText(_translate("propertiesView", "Text type:"))
        self.lblPOV_2.setText(_translate("propertiesView", "POV"))
        self.label_31.setText(_translate("propertiesView", "Status"))
        self.label_34.setText(_translate("propertiesView", "Label"))
        self.label_35.setText(_translate("propertiesView", "Compile"))
        self.label_36.setText(_translate("propertiesView", "Goal"))
        self.txtGoalMulti.setPlaceholderText(_translate("propertiesView", "Word count"))

from manuskript.ui.views.chkOutlineCompile import chkOutlineCompile
from manuskript.ui.views.cmbOutlineLabelChoser import cmbOutlineLabelChoser
from manuskript.ui.views.cmbOutlinePersoChoser import cmbOutlinePersoChoser
from manuskript.ui.views.cmbOutlineStatusChoser import cmbOutlineStatusChoser
from manuskript.ui.views.cmbOutlineTypeChoser import cmbOutlineTypeChoser
from manuskript.ui.views.lineEditView import lineEditView
