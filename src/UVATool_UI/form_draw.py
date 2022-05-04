# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_draw.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from distutils.command.clean import clean
from PyQt5 import QtCore, QtGui, QtWidgets

from form_results import Ui_ResultForm
from uvat import Apoio, Canvas, Defaults, Element, Node, Grid


class Ui_DrawForm(object):
    def setupUi(self, DrawForm: QtWidgets.QDialog):
        DrawForm.setObjectName("DrawForm")
        DrawForm.resize(470, 420)
        DrawForm.setMinimumSize(QtCore.QSize(470, 420))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/draw.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DrawForm.setWindowIcon(icon)
        self.gridLayout_5 = QtWidgets.QGridLayout(DrawForm)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(DrawForm)
        self.tabWidget.setObjectName("tabWidget")
        self.structure = QtWidgets.QWidget()
        self.structure.setObjectName("structure")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.structure)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listViewNodeStructure = QtWidgets.QListWidget(self.structure)
        self.listViewNodeStructure.setObjectName("listViewNodeStructure")
        self.verticalLayout_2.addWidget(self.listViewNodeStructure)
        self.listViewElementStructure = QtWidgets.QListWidget(self.structure)
        self.listViewElementStructure.setObjectName("listViewElementStructure")
        self.verticalLayout_2.addWidget(self.listViewElementStructure)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.structure)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonFirstClass.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButtonFirstClass.setChecked(True)
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.verticalLayout_4.addWidget(self.radioButtonFirstClass)
        self.radioButtonSecondClass = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonSecondClass.setObjectName("radioButtonSecondClass")
        self.verticalLayout_4.addWidget(self.radioButtonSecondClass)
        self.radioButtonTirdClass = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonTirdClass.setObjectName("radioButtonTirdClass")
        self.verticalLayout_4.addWidget(self.radioButtonTirdClass)
        self.radioButtonSemiRigidClass = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonSemiRigidClass.setObjectName(
            "radioButtonSemiRigidClass")
        self.verticalLayout_4.addWidget(self.radioButtonSemiRigidClass)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEditNodeX = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNodeX.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditNodeX.setAutoFillBackground(False)
        self.lineEditNodeX.setObjectName("lineEditNodeX")
        self.verticalLayout_5.addWidget(self.lineEditNodeX)
        self.lineEditNodeY = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNodeY.setObjectName("lineEditNodeY")
        self.verticalLayout_5.addWidget(self.lineEditNodeY)
        self.lineEditNodeRotation = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNodeRotation.setObjectName("lineEditNodeRotation")
        self.verticalLayout_5.addWidget(self.lineEditNodeRotation)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonNodeDraw = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonNodeDraw.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButtonNodeDraw.setMaximumSize(QtCore.QSize(75, 23))
        self.pushButtonNodeDraw.setObjectName("pushButtonNodeDraw")
        self.horizontalLayout_3.addWidget(self.pushButtonNodeDraw)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.structure)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.lineEditSecondNodeY = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSecondNodeY.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditSecondNodeY.setObjectName("lineEditSecondNodeY")
        self.gridLayout.addWidget(self.lineEditSecondNodeY, 3, 0, 1, 1)
        self.lineEditFistNodeX = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditFistNodeX.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditFistNodeX.setObjectName("lineEditFistNodeX")
        self.gridLayout.addWidget(self.lineEditFistNodeX, 0, 0, 1, 1)
        self.lineEditFistNodeY = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditFistNodeY.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditFistNodeY.setObjectName("lineEditFistNodeY")
        self.gridLayout.addWidget(self.lineEditFistNodeY, 1, 0, 1, 1)
        self.lineEditSecondNodeX = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSecondNodeX.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditSecondNodeX.setObjectName("lineEditSecondNodeX")
        self.gridLayout.addWidget(self.lineEditSecondNodeX, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.structure, "")
        self.loadings = QtWidgets.QWidget()
        self.loadings.setObjectName("loadings")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.loadings)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.listWidgetNodeLoadings = QtWidgets.QListWidget(self.loadings)
        self.listWidgetNodeLoadings.setObjectName("listWidgetNodeLoadings")
        self.gridLayout_10.addWidget(self.listWidgetNodeLoadings, 0, 0, 2, 1)
        self.groupBoxLoadingType = QtWidgets.QGroupBox(self.loadings)
        self.groupBoxLoadingType.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBoxLoadingType.setObjectName("groupBoxLoadingType")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxLoadingType)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBoxLoadingType)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 0, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBoxLoadingType)
        self.radioButton_7.setEnabled(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_3.addWidget(self.radioButton_7, 1, 0, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBoxLoadingType)
        self.radioButton_8.setEnabled(False)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout_3.addWidget(self.radioButton_8, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBoxLoadingType, 0, 1, 1, 1)
        self.groupBoxGenerateNode = QtWidgets.QGroupBox(self.loadings)
        self.groupBoxGenerateNode.setObjectName("groupBoxGenerateNode")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBoxGenerateNode)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBoxGenerateNode)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEditForceX = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditForceX.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditForceX.setObjectName("lineEditForceX")
        self.gridLayout_6.addWidget(self.lineEditForceX, 0, 0, 1, 1)
        self.lineEditForceY = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditForceY.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditForceY.setObjectName("lineEditForceY")
        self.gridLayout_6.addWidget(self.lineEditForceY, 1, 0, 1, 1)
        self.lineEditMoment = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditMoment.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditMoment.setObjectName("lineEditMoment")
        self.gridLayout_6.addWidget(self.lineEditMoment, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBoxGenerateNode)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEditNodeX_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditNodeX_2.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEditNodeX_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditNodeX_2.setObjectName("lineEditNodeX_2")
        self.gridLayout_7.addWidget(self.lineEditNodeX_2, 0, 0, 1, 1)
        self.lineEditNodeY_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditNodeY_2.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEditNodeY_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditNodeY_2.setObjectName("lineEditNodeY_2")
        self.gridLayout_7.addWidget(self.lineEditNodeY_2, 0, 1, 1, 1)
        self.lineEditNodeRotation_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditNodeRotation_2.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNodeRotation_2.setObjectName("lineEditNodeRotation_2")
        self.gridLayout_7.addWidget(self.lineEditNodeRotation_2, 1, 0, 1, 2)
        self.gridLayout_8.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonNodeDraw_2 = QtWidgets.QPushButton(
            self.groupBoxGenerateNode)
        self.pushButtonNodeDraw_2.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButtonNodeDraw_2.setMaximumSize(QtCore.QSize(75, 23))
        self.pushButtonNodeDraw_2.setObjectName("pushButtonNodeDraw_2")
        self.horizontalLayout.addWidget(self.pushButtonNodeDraw_2)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout_8.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBoxGenerateNode, 1, 1, 1, 1)
        self.tabWidget.addTab(self.loadings, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(DrawForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DrawForm)
        DrawForm.setTabOrder(self.lineEditNodeX, self.lineEditNodeY)
        DrawForm.setTabOrder(self.lineEditNodeY, self.lineEditNodeRotation)
        DrawForm.setTabOrder(self.lineEditNodeRotation, self.lineEditFistNodeX)
        DrawForm.setTabOrder(self.lineEditFistNodeX, self.lineEditFistNodeY)
        DrawForm.setTabOrder(self.lineEditFistNodeY, self.lineEditSecondNodeX)
        DrawForm.setTabOrder(self.lineEditSecondNodeX,
                             self.lineEditSecondNodeY)
        DrawForm.setTabOrder(self.lineEditSecondNodeY, self.pushButtonNodeDraw)
        DrawForm.setTabOrder(self.pushButtonNodeDraw, self.pushButton_2)
        DrawForm.setTabOrder(self.pushButton_2, self.radioButtonFirstClass)
        DrawForm.setTabOrder(self.radioButtonFirstClass,
                             self.radioButtonSecondClass)
        DrawForm.setTabOrder(self.radioButtonSecondClass,
                             self.radioButtonTirdClass)
        DrawForm.setTabOrder(self.radioButtonTirdClass,
                             self.radioButtonSemiRigidClass)

###############################################################################################################
        self.canvas = Canvas()
        self.graphicsScene = QtWidgets.QGraphicsScene()
        self.lineEditNodeRotation.setEnabled(False)
        self.lineEditNodeRotation_2.setEnabled(False)
        self.listViewNodeStructure.clicked.connect(
            self.listViewNodeStructureClicked)
        self.listViewNodeStructure.doubleClicked.connect(
            self.listViewNodeStructureDoubleClicked)
        self.listViewElementStructure.clicked.connect(
            self.listViewElementStructureClicked)
        self.pushButtonNodeDraw.clicked.connect(self.pushButtonNodeDrawClicked)
        self.pushButton_2.clicked.connect(self.pushButtonElementDrawClicked)

    def fillNodeListStructure(self):
        if self.canvas is not None:
            # print("Entrei no fill nodes")
            for node in self.canvas.nodes:
                item = "{0}, {1}".format(
                    str(node).split(",")[0], str(node).split(",")[1])
                self.listViewNodeStructure.addItem(item)
        else:
            print('nodes:CANVAS NÃO INSERIDO CORRETAMENTE PELO UVATOOL')

    def fillElementListStructure(self):
        if self.canvas is not None:
            # print("Entrei no fill elements")
            for element in self.canvas.elements:
                item = "{0}; {1}".format(
                    str(element).split(";")[0], str(element).split(";")[1])
                self.listViewElementStructure.addItem(item)
        else:
            print('elements:CANVAS NÃO INSERIDO CORRETAMENTE PELO UVATOOL')

    def setCanvas(self, canvas: Canvas):
        self.canvas = canvas

    def setGraphicsScene(self, scene: QtWidgets.QGraphicsScene):
        self.graphicsScene = scene

    def listViewNodeStructureClicked(self):
        node = self.listViewNodeStructure.currentItem()
        nodeText = node.text().replace(" ", "")
        xCoord = nodeText.split(",")[0]
        yCoord = nodeText.split(",")[1]
        listPos = self.listViewNodeStructure.indexFromItem(node).row()
        apoio = self.canvas.nodes[listPos].apoio
        self.lineEditNodeX.setText(xCoord)
        self.lineEditNodeY.setText(yCoord)
        if apoio == Apoio.primeiroGenero:
            self.radioButtonFirstClass.setChecked(True)
        elif apoio == Apoio.segundoGenero:
            self.radioButtonSecondClass.setChecked(True)
        elif apoio == Apoio.terceiroGenero:
            self.radioButtonTirdClass.setChecked(True)
        elif apoio == Apoio.semiRigido:
            self.radioButtonSemiRigidClass.setChecked(True)
        self.pushButtonNodeDraw.setText("Edit")
        # Teste de implementação para trocar cor dos icones quando estão selecionados
        # nodeTest = Node(float(xCoord)-self.correcaoClickImage()
        #                 [0], float(yCoord)-self.correcaoClickImage()[1])
        # for node in self.canvas.drawnElements:
        #     if node == nodeTest:
        #         self.graphicsScene.removeItem(node)
        #         mask = node.createMaskFromColor(
        #             QtGui.QColor('black'), QtCore.Qt.MaskOutColor)
        #         node.fill((QtGui.QColor('red')))
        #         node.setMask(mask)
        #         self.graphicsScene.addPixmap(node)

    def listViewNodeStructureDoubleClicked(self):
        node = self.listViewNodeStructure.currentItem()
        nodeText = node.text().replace(" ", "")
        xCoord = nodeText.split(",")[0]
        yCoord = nodeText.split(",")[1]
        # Acho q não precisa disso.. Verificar as possibilidades
        # listPos = self.listViewNodeStructure.indexFromItem(node).row()
        # apoio = self.canvas.nodes[listPos].apoio
        # node = Node(xCoord, yCoord)
        # node.apoio = apoio
        # print(node)
        # self.verifyElementTexts()

        fistX = self.lineEditFistNodeX.text()
        fistY = self.lineEditFistNodeY.text()
        secondX = self.lineEditSecondNodeX.text()
        secondY = self.lineEditSecondNodeY.text()

        if fistX == "" and fistY == "":
            self.lineEditFistNodeX.setText(xCoord)
            self.lineEditFistNodeY.setText(yCoord)
        elif secondX == "" and secondY == "":
            self.lineEditSecondNodeX.setText(xCoord)
            self.lineEditSecondNodeY.setText(yCoord)

    def listViewElementStructureClicked(self):
        structure = self.listViewElementStructure.currentItem()
        structureText = structure.text().replace(
            "Node1=", "").replace("Node2=", "").replace(" ", "")
        node1X = float(structureText.split(";")[0].split(",")[0])
        node1Y = float(structureText.split(";")[0].split(",")[1])
        node2X = float(structureText.split(";")[1].split(",")[0])
        node2Y = float(structureText.split(";")[1].split(",")[1])
        self.lineEditFistNodeX.setText(str(node1X))
        self.lineEditFistNodeY.setText(str(node1Y))
        self.lineEditSecondNodeX.setText(str(node2X))
        self.lineEditSecondNodeY.setText(str(node2Y))
        node1 = Node(node1X, node1Y)
        node2 = Node(node2X, node2Y)
        element = Element(node1, node2)
        self.pushButton_2.setText("Edit")

    def verifyNodeTexts(self):
        try:
            float(self.lineEditNodeX.text())
            float(self.lineEditNodeY.text())
            # Descomentar quando for implementar rotação
            # float(self.lineEditNodeRotation.text())
        except:
            raise RuntimeError(
                "Os textos dos nodes foram escritos de forma errada!")

    def verifyElementTexts(self):
        try:
            t1 = self.lineEditFistNodeX.text()
            if t1 != "":
                float(t1)
            t2 = self.lineEditFistNodeY.text()
            if t2 != "":
                float(t2)
            t3 = self.lineEditSecondNodeX.text()
            if t3 != "":
                float(t3)
            t4 = self.lineEditSecondNodeY.text()
            if t4 != "":
                float(t4)
        except:
            raise RuntimeError(
                "Os textos do elemento foram escritos de forma errada!")

    def verifySuportChecked(self) -> Apoio:
        apoio = None
        if self.radioButtonFirstClass.isChecked():
            apoio = Apoio.primeiroGenero
        elif self.radioButtonSecondClass.isChecked():
            apoio = Apoio.segundoGenero
        elif self.radioButtonTirdClass.isChecked():
            apoio = Apoio.terceiroGenero
        elif self.radioButtonSemiRigidClass.isChecked():
            apoio = Apoio.semiRigido
        return apoio

    def imageReturn(self) -> str:
        apoio = self.verifySuportChecked()
        imagem = None
        if apoio == Apoio.primeiroGenero:
            imagem = "icons/apoio_primeiro_genero.png"
        elif apoio == Apoio.segundoGenero:
            imagem = "icons/apoio_segundo_genero.png"
        elif apoio == Apoio.terceiroGenero:
            imagem = "icons/apoio_terceiro_genero.png"
        elif apoio == Apoio.semiRigido:
            imagem = "icons/apoio_semi_rigido.png"
        return imagem

    def correcaoClickImage(self):
        apoio = self.verifySuportChecked()
        correcaoClickImagem = []
        if apoio == Apoio.primeiroGenero:
            correcaoClickImagem = [16, 5]
        elif apoio == Apoio.segundoGenero:
            correcaoClickImagem = [17, 7]
        elif apoio == Apoio.terceiroGenero:
            correcaoClickImagem = [17, 14]
        elif apoio == Apoio.semiRigido:
            correcaoClickImagem = [15, 12]
        return correcaoClickImagem

    def pushButtonNodeDrawClicked(self):
        self.verifyNodeTexts()
        x = float(self.lineEditNodeX.text())
        y = float(self.lineEditNodeY.text())
        self.pushButtonNodeDraw.setText("Draw")
        self.lineEditNodeX.setText("")
        self.lineEditNodeY.setText("")
        self.lineEditNodeRotation.setText("")
        node = Node(x, y)
        node.apoio = self.verifySuportChecked()
        self.drawSupport(node)
        item = "{0}, {1}".format(
            str(node).split(",")[0], str(node).split(",")[1])
        self.listViewNodeStructure.addItem(item)

    def pushButtonElementDrawClicked(self):
        self.verifyElementTexts()
        fistX = float(self.lineEditFistNodeX.text())
        fistY = float(self.lineEditFistNodeY.text())
        secondX = float(self.lineEditSecondNodeX.text())
        secondY = float(self.lineEditSecondNodeY.text())
        self.lineEditFistNodeX.setText("")
        self.lineEditFistNodeY.setText("")
        self.lineEditSecondNodeX.setText("")
        self.lineEditSecondNodeY.setText("")
        node1 = Node(fistX, fistY)
        node2 = Node(secondX, secondY)
        element = Element(node1, node2)
        self.drawElement(node1, node2)
        item = "{0}; {1}".format(
            str(element).split(";")[0], str(element).split(";")[1])
        self.listViewElementStructure.addItem(item)

    def drawSupport(self, node: Node):
        if node.apoio == None:
            raise RuntimeError("node não possui apoio para desenhar")
        imagem = self.imageReturn()
        if imagem == None or imagem == "":
            raise RuntimeError("node não possui imagem para desenhar")
        pixMap = QtGui.QPixmap(imagem)
        imagem = self.graphicsScene.addPixmap(pixMap)
        point = None
        point = QtCore.QPointF(
            node.x - self.correcaoClickImage()[0], node.y - self.correcaoClickImage()[1])
        imagem.setPos(point)
        self.canvas.nodes.append(node)
        self.canvas.drawnNodes.append(imagem)

    def drawElement(self, node1: Node, node2: Node) -> None:
        test1 = False
        test2 = False
        for node in self.canvas.nodes:
            if node == node1:
                test1 = True
            if node == node2:
                test2 = True
        if test1 and test2:
            element = Element(node1, node2)
            line = self.graphicsScene.addLine(
                node1.x, node1.y, node2.x, node2.y, QtGui.QPen(QtCore.Qt.GlobalColor.black, 2))
            self.canvas.elements.append(element)
            self.canvas.drawnElements.append(line)
        else:
            raise RuntimeError(
                'Os nodes selecionados para desenhar não foram inseridos no canvas corretamente!')


###############################################################################################################

    def retranslateUi(self, DrawForm):
        _translate = QtCore.QCoreApplication.translate
        DrawForm.setWindowTitle(_translate("DrawForm", "Draw Tool"))
        self.groupBox.setTitle(_translate("DrawForm", "Node"))
        self.radioButtonFirstClass.setText(_translate("DrawForm", "1º Class"))
        self.radioButtonSecondClass.setText(_translate("DrawForm", "2º class"))
        self.radioButtonTirdClass.setText(_translate("DrawForm", "3º class"))
        self.radioButtonSemiRigidClass.setText(
            _translate("DrawForm", "Semi Rigid"))
        self.lineEditNodeX.setPlaceholderText(
            _translate("DrawForm", "X value"))
        self.lineEditNodeY.setPlaceholderText(
            _translate("DrawForm", "Y value"))
        self.lineEditNodeRotation.setPlaceholderText(
            _translate("DrawForm", "Rotation (º)"))
        self.pushButtonNodeDraw.setText(_translate("DrawForm", "Draw"))
        self.groupBox_2.setTitle(_translate("DrawForm", "Element"))
        self.pushButton_2.setText(_translate("DrawForm", "Draw"))
        self.lineEditSecondNodeY.setPlaceholderText(
            _translate("DrawForm", "2nd Node Y value"))
        self.lineEditFistNodeX.setPlaceholderText(
            _translate("DrawForm", "1st Node X value"))
        self.lineEditFistNodeY.setPlaceholderText(
            _translate("DrawForm", "1st Node Y value"))
        self.lineEditSecondNodeX.setPlaceholderText(
            _translate("DrawForm", "2nd Node X value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.structure), _translate("DrawForm", "Structure"))
        self.groupBoxLoadingType.setTitle(
            _translate("DrawForm", "Loading Type"))
        self.radioButton_5.setText(_translate("DrawForm", "Nodal Forces"))
        self.radioButton_7.setText(_translate("DrawForm", "Uniform"))
        self.radioButton_8.setText(_translate("DrawForm", "Linear"))
        self.groupBoxGenerateNode.setTitle(
            _translate("DrawForm", "Generate Node"))
        self.groupBox_3.setTitle(_translate("DrawForm", "Loadings"))
        self.lineEditForceX.setPlaceholderText(
            _translate("DrawForm", "Loading in X (Fx)"))
        self.lineEditForceY.setPlaceholderText(
            _translate("DrawForm", "Loading in Y (Fy)"))
        self.lineEditMoment.setPlaceholderText(
            _translate("DrawForm", "Moment (M)"))
        self.groupBox_4.setTitle(_translate("DrawForm", "Position"))
        self.lineEditNodeX_2.setPlaceholderText(
            _translate("DrawForm", "X value"))
        self.lineEditNodeY_2.setPlaceholderText(
            _translate("DrawForm", "Y value"))
        self.lineEditNodeRotation_2.setPlaceholderText(
            _translate("DrawForm", "Rotation (º)"))
        self.pushButtonNodeDraw_2.setText(_translate("DrawForm", "Draw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.loadings), _translate("DrawForm", "Loadings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DrawForm = QtWidgets.QDialog()
    ui = Ui_DrawForm()
    ui.setupUi(DrawForm)
    DrawForm.show()
    sys.exit(app.exec_())
