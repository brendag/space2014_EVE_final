# Assignment1Widget.py
# (C)2014
# Brenda Griggs

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget, QtGui

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment1Widget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S
    global startFrame
    global endFrame
#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment1Widget, self).__init__(parent, **kwargs)
        self.stationButton.clicked.connect(self._handleSpaceStationButton)
        self.camera1Button.clicked.connect(self._handleCamera1)
        self.camera2Button.clicked.connect(self._handleCamera2)
        self.camera3Button.clicked.connect(self._handleCamera3)
        self.camera4Button.clicked.connect(self._handleCamera4)

        self.monolithButton.clicked.connect(self._handleMonolithButton)

        self.twirlButton.clicked.connect(self._handleTwirlButton)
        self.flyButton.clicked.connect(self._handleFlyButton)
        self.robotButton.clicked.connect(self._handleRobotButton)

        self.homeBtn.clicked.connect(self._handleReturnHome)


#===================================================================================================
#
#                                                                      H A N D L E R S

#_________________________________________________________________________________________________ _handleCameraButtons

    def _handleCamera1(self):
        cmds.lookThru( 'camera1' )

    def _handleCamera2(self):
        cmds.lookThru( 'camera2' )

    def _handleCamera3(self):
        cmds.lookThru( 'camera3' )

    def _handleCamera4(self):
        cmds.lookThru( 'camera4' )
#_________________________________________________________________________________________________ _handleRobotButton

    def _handleRobotButton(self):
        global startFrame
        startFrame = int(self.startFrameField.text())
        global endFrame
        endFrame = int(self.endFrameField.text())
        angleArmLeft = 0;
        angleArmRight = 0;
        moveHeady = 2.965
        headHeight = self.headHeightBox.value()
        i = startFrame
        if(startFrame < endFrame):
            while i <= endFrame:
                #cmds.select('EVE')
                cmds.setKeyframe('head_base', attribute='translateY', value=moveHeady, t=i)
                cmds.setKeyframe('arm_left', attribute='rotateX', value=angleArmLeft, t=i)
                cmds.setKeyframe('arm_right', attribute='rotateX', value=angleArmRight, t=i)
                if(i <= (startFrame + ((endFrame-startFrame)/2))):
                    angleArmRight += ((float(endFrame-startFrame)/2.0)/50.0)
                    angleArmLeft -= ((float(endFrame-startFrame)/2.0)/50.0)
                    moveHeady += ((headHeight)/(float(endFrame-startFrame)/2.0))

                if(i > (startFrame + ((endFrame-startFrame)/2.0))):
                    angleArmRight -= (((endFrame-startFrame)/2.0)/50.0)
                    angleArmLeft += (((endFrame-startFrame)/2.0)/50.0)
                    moveHeady -= ((headHeight)/(float(endFrame-startFrame)/2.0))
                i+=1
            print('EVE robot gesture created.')
        elif (startFrame == endFrame):
            QtGui.QMessageBox.information(self, 'Alert', 'Start and end frames are equal.')
        else:
            QtGui.QMessageBox.warning(self, 'Alert', 'Start frame is greater than end frame. Please re-adjust values so start frame < end frame.')
#_________________________________________________________________________________________________ _handleFlyButton

    def _handleFlyButton(self):
        global startFrame
        startFrame = int(self.startFrameField.text())
        global endFrame
        endFrame = int(self.endFrameField.text())
        height = self.heightBox.value()
        currentHeight = 0
        if(startFrame < endFrame):

            i = startFrame
            while i <= endFrame:
                #cmds.select('EVE')
                cmds.setKeyframe('EVE', attribute='translateY', value=currentHeight, t=i)
                currentHeight += (height/(float(endFrame-startFrame)))
                print("Current height: " + str(currentHeight))
                i+=1
            print('EVE - flying created.')
        elif (startFrame == endFrame):
            QtGui.QMessageBox.information(self, 'Alert', 'Start and end frames are equal.')
        else:
            QtGui.QMessageBox.warning(self, 'Alert', 'Start frame is greater than end frame. Please re-adjust values so start frame < end frame.')

#_________________________________________________________________________________________________ _handleTwirlButton

    def _handleTwirlButton(self):
        global startFrame
        startFrame = int(self.startFrameField.text())
        global endFrame
        endFrame = int(self.endFrameField.text())
        twirls = self.twirlBox.value()
        currentAngle = 0
        if(startFrame < endFrame):
            i = startFrame

            while i <= endFrame:
                cmds.setKeyframe('EVE', attribute='rotateY', value=currentAngle, t=i)
                currentAngle += ((360.0 * twirls)/float(endFrame - startFrame))
                #print ("Current angle: " + str(currentAngle)+ " at i: " + str(i))
                i+= 1
            print('EVE twirl created.')
        elif (startFrame == endFrame):
            QtGui.QMessageBox.information(self, 'Alert', 'Start and end frames are equal.')
        else:
            QtGui.QMessageBox.warning(self, 'Alert', 'Start frame is greater than end frame. Please re-adjust values so start frame < end frame.')


#_______________________________________________________________________________________________ _handleSpaceStationHome
    def _handleSpaceStationButton(self):
        #Rotate Y angles
        angleWheel = 0;
        angleSolarPanels = 0
        angleDoor = 0
        angleEVE = 180.0
        angleArmLeft = -15;
        angleArmRight = 15;
        angleHead = 90

        #Translate Z values
        moveEVEz = .197

        #Translate Y values
        moveHeady = 2.965
        moveEVEy = 2.34

        cmds.camera()
        cmds.select('camera1')
        cmds.move(-1.186, 2.441, 2.849, relative=True)
        cmds.rotate(1.8, -27.2, 0)
        cmds.camera()
        cmds.select('camera2')
        cmds.move(0.25, 4.5, 15, relative=True)
        cmds.rotate(-10, -2, 0)

        cmds.camera()
        cmds.select('camera3')
        cmds.move(0.083, 8.809, 4.579, relative=True)
        cmds.rotate(-49.2, -10, 0)

        cmds.camera()
        cmds.select('camera4')
        cmds.move(-18.709, 15.459, -20.347, relative=True)
        cmds.rotate(-24, -151.6, 0)

        cmds.move(.186,2.34,.197,'EVE')
        for i in range (360):
            #rotate station
            cmds.setKeyframe('station1:Wheel', attribute='rotateY', value=angleWheel, t=i)
            angleWheel+=.5
            #rotate solar panels
            cmds.setKeyframe('station1:SolarPanels', attribute='rotateY', value=angleSolarPanels, t=i)
            angleSolarPanels+=.5
            #open station door
            if (i <= 72):
                cmds.setKeyframe('station1:spaceDoor', attribute='rotateY', value=angleDoor, t=i)
                angleDoor -= (120/70)
            #turn/rotate EVE
            if(i <= 72):
                cmds.setKeyframe('EVE', attribute='rotateY', value=angleEVE, t=i)
                angleEVE += (180.0/72.0)
            #EVE robot gesture
            if(i > 72 and i < (72 + 48)):
                cmds.setKeyframe('head_base', attribute='translateY', value=moveHeady, t=i)
                cmds.setKeyframe('arm_left', attribute='rotateX', value=angleArmLeft, t=i)
                cmds.setKeyframe('arm_right', attribute='rotateX', value=angleArmRight, t=i)
                moveEVEz += (.757-.197)/(48.0)
                if(i <= (72 + 24)):
                    angleArmRight += (24/15)
                    angleArmLeft -= (24/15)
                    cmds.setKeyframe('EVE', attribute='translateZ', value=moveEVEz, t=i)
                    moveHeady += ((3.194-2.965)/24)

                if(i > (72 + 24)):
                    angleArmRight -= (24/15)
                    angleArmLeft += (24/15)
                    cmds.setKeyframe('EVE', attribute='translateZ', value=moveEVEz, t=i)
                    moveHeady -= ((3.194-2.965)/24)

            if(i > (120) and i < (120+48)):
                #EVE head turn right
                if(i <= (120 + 24)):
                    angleHead -= (90-15)/24
                    cmds.setKeyframe('head_base', attribute='rotateY', value=angleHead, t=i)
                #EVE head turn left
                if( i > 144):
                    angleHead += (90+30)/(24)
                    cmds.setKeyframe('head_base', attribute='rotateY', value=angleHead, t=i)
                    #EVE move outside of station
                    if(i > (168-12)):
                        moveEVEz += ((1.709-.745)/2)/48
                        cmds.setKeyframe('EVE', attribute='translateZ', value=moveEVEz, t=i)

            if(i > 168 and i < (168+48)):
                if(i < 168 + 24):
                    #EVE return head to normal position
                    angleHead -= (30/24)
                    cmds.setKeyframe('head_base', attribute='rotateY', value=angleHead, t=i)
                    cmds.setKeyframe('EVE', attribute='rotateY', value=angleEVE, t=i)

                #close station door
                if(i <= 206):
                    cmds.setKeyframe('station1:spaceDoor', attribute='rotateY', value=angleDoor, t=i)
                    angleDoor += (120/48)
                moveEVEz += ((1.709-.745)/2)/48.0
                cmds.setKeyframe('EVE', attribute='translateZ', value=moveEVEz, t=i)
                angleEVE += (720.0/48.0)
                moveEVEy += (3.094-2.965)/48.0
                #move up
                cmds.setKeyframe('EVE', attribute='translateY', value=moveEVEy, t=i)

            if(i > 216):
                if(i < 270):
                     cmds.setKeyframe('EVE', attribute='translateY', value=angleHead, t=i)
                     angleHead += (700/48)
                #fly up
                cmds.setKeyframe('EVE', attribute='translateY', value = moveEVEy, t=i )
                # twirl
                cmds.setKeyframe('EVE', attribute='rotateY', value = angleEVE, t=i )
                moveEVEy += (11.0-2.466)/(360-216) + .01
        print('EVE - Space Station scene created.')

#_________________________________________________________________________________________________ _handleMonolithButton
    def _handleMonolithButton(self):
        #print("Total animation keyframes:   PROCESSING")
        height = 12.00
        stepSize = 0.40
        originalStepSize = stepSize
        cmds.select('EVE')
        currentHeight = -20.0
        rotateAngle = 0.0
        count = 0;
        cmds.setAttr('EVE.rotateY', 0.0)
        armliftAngleR = 0.0
        armliftAngleL = 0.0

        cmds.camera()
        cmds.select('camera1')
        cmds.move(12.0, 10.0, 10.0, relative=True)
        cmds.aimConstraint('EVE', 'camera1', offset=(0, -90, 0))
        cmds.lookThru('camera1')


        while(currentHeight <= height):
            if(currentHeight >= 1*(height/2)):
                stepSize = (originalStepSize * 3.0)/4.0
                rotateAngle = rotateAngle + 5
                if(armliftAngleL >= -50.0 and armliftAngleR <= 50):
                    armliftAngleL -= 1
                    armliftAngleR += 1

            cmds.setKeyframe('arm_left', attribute='rotateX', value=armliftAngleL, t=count)
            cmds.setKeyframe('arm_right', attribute='rotateX', value=armliftAngleR, t=count)
            cmds.setKeyframe('EVE', attribute='translateY', value = currentHeight, t=count )
            cmds.setKeyframe('EVE', attribute='rotateY', value = rotateAngle, t=count )
            if(currentHeight < 1*(height/2)):
                rotateAngle = rotateAngle + 1

            currentHeight += stepSize
            count += 1
            # print("Step size: " + str(stepSize))
            # print("Current height: " + str(currentHeight))
        for i in range (360/4):
            rotateAngle = rotateAngle + 3
            cmds.setKeyframe('EVE', attribute='rotateY', value = rotateAngle, t=count )
            count += 1
        stepSize = ((originalStepSize * 3.0)/4.0)/2
        while(currentHeight >= 0):
            cmds.setKeyframe('arm_left', attribute='rotateX', value=armliftAngleL, t=count)
            cmds.setKeyframe('arm_right', attribute='rotateX', value=armliftAngleR, t=count)
            cmds.setKeyframe('EVE', attribute='translateY', value = currentHeight, t=count )
            cmds.setKeyframe('EVE', attribute='rotateY', value = rotateAngle, t=count )
            rotateAngle = rotateAngle + 1

            currentHeight -= stepSize
            count += 1
            #print("Step size: " + str(stepSize))
            #print("Current height: " + str(currentHeight))

        print('EVE - Monolith scene created.')

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
