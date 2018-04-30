from __main__ import vtk, qt, ctk, slicer
import numpy as np
#
# HelloPython
#

class T1:
  def __init__(self, parent):
    parent.title = "T1_Module"
    parent.categories = ["CJun"]
    parent.dependencies = []
    parent.contributors = ["Changhan Jun (Northwestern, Neurosurgery)",
                           "Jean-Paul Wolinsky (Northwestern, Neurosurgery)"]

    parent.helpText = """
    Application for Spine Screw Placement 
    """
    parent.acknowledgementText = """
    This file was originally developed by Changhan Jun, Northwestern University""" # replace with organization, grant and thanks.
    self.parent = parent

#
# qHelloPythonWidget
#

class T1Widget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    # Instantiate and connect widgets ...

    # Collapsible button
    self.sampleCollapsibleButton = ctk.ctkCollapsibleButton()
    self.sampleCollapsibleButton.text = "A collapsible button"
    self.layout.addWidget(self.sampleCollapsibleButton)

    # Layout within the sample collapsible button
    self.sampleFormLayout = qt.QFormLayout(self.sampleCollapsibleButton)

    # the volume selectors
    self.inputFrame = qt.QFrame(self.sampleCollapsibleButton)
    self.inputFrame.setLayout(qt.QHBoxLayout())
    self.sampleFormLayout.addWidget(self.inputFrame)
    # self.inputSelector = qt.QLabel("Input Volume: ", self.inputFrame) # for testing
    self.inputSelector = qt.QLabel("Load STL Models: ", self.inputFrame)
    self.inputFrame.layout().addWidget(self.inputSelector)
    self.inputSelector = slicer.qMRMLNodeComboBox(self.inputFrame)
    #    self.inputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode"), "")
    self.inputSelector.nodeTypes = (("vtkMRMLModelNode"), "")
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    self.inputFrame.layout().addWidget(self.inputSelector)



    ########################
    # Add tutorial code here Section A
    # Hello world Button
    helloWorldButton = qt.QPushButton("Transform")
    helloWorldButton.toolTip ="Print'XX' in standard output"

    helloWorldButton.connect('clicked(bool)', self.onHelloWorldButtonClicked)
    ########################
    
    # Add vertical spacer
    self.layout.addStretch(1)

    # Set local var as instance attribute
    self.helloWorldButton = helloWorldButton

  def onHelloWorldButtonClicked(self):
    print "Hello World !"

    ########################
    # Add tutorial code here Section B
    qt.QMessageBox.information(
      slicer.util.mainWindow(),
      'Slicer Python','HelloWorld!')
    ########################

