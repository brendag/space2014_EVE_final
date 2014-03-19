# Assignment2Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment2Widget
class Assignment2Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment2Widget."""
        super(Assignment2Widget, self).__init__(parent, **kwargs)
        self.SpaceShipEnterButton.clicked.connect(self._handleSpaceShipEnterButton)
        self.SpaceShipAndAsteroid.clicked.connect(self._handleSpaceShipAndAsteroid)
        self.Camera1a.clicked.connect(self._handleCamera1a)
        self.Camera2a.clicked.connect(self._handleCamera2a)
        self.Camera1b.clicked.connect(self._handleCamera1b)
        self.Camera2b.clicked.connect(self._handleCamera2b)
        self.Camera3b.clicked.connect(self._handleCamera3b)
        self.homeBtn.clicked.connect(self._handleReturnHome)


#===================================================================================================
#
#                                                                         H A N D L E R S
#  Cameras

    def _handleCamera1a(self):
        cmds.lookThru( 'camera1' )

    def _handleCamera2a(self):
        cmds.lookThru( 'camera2' )

    def _handleCamera1b(self):
        cmds.lookThru( 'camera1' )

    def _handleCamera2b(self):
        cmds.lookThru( 'camera2' )

    def _handleCamera3b(self):
        cmds.lookThru( 'camera3' )



    def _handleSpaceShipEnterButton(self):
        cmds.file('$HOME/PycharmProjects/space2014/graphics/SpaceShip/scenes/SpaceShipEnter.ma',i=True)
        scale = 0
        scaleC = 0
        scaleX = 0

        moveX = 1300
        moveY = 290.702
        moveZ = 76

        xRot = 0
        yRot = 0
        doorRot = 0
        centerR = 0

        time = 1
        cmds.camera()
        cmds.select('camera1')
        cmds.move(600.0, 300.0, 100.0, relative = True)
        cmds.aimConstraint( 'SpaceShip2', 'camera1', offset = (0,-90,0)  )
        cmds.camera()
        cmds.select('camera2')
        cmds.move(160, 392.383, -60.0, relative = True)
        cmds.aimConstraint( 'SpaceShip2', 'camera2', offset = (0,-90,0)  )
        for k in range( 30 ):
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleZ', value = scale , t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleY', value = scaleC , t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleX', value = scaleX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateY', value = moveY, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateZ', value = moveZ, t=time )
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5


            scaleX = scaleX + .01
            scale = scale + .01
            scaleC = scaleC + .01
            moveX = moveX - 10.00
            time = time + 1

        for j in range (20):
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleZ', value = scale , t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleY', value = scaleC , t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleX', value = scaleX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateY', value = moveY, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateZ', value = moveZ, t=time )
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5


            scaleX = scaleX + .01
            scale = scale + .01
            scaleC = scaleC + .01
            moveX = moveX - 7.00
            time = time + 1

        for m in range (100):
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleZ', value = scale , t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleY', value = scaleC , t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='scaleX', value = scaleX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateY', value = moveY, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateZ', value = moveZ, t=time )
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5


            moveX = moveX - 4.00
            time = time + 1

        for p in range (60):
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateY', value = moveY, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateZ', value = moveZ, t=time )
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5



            moveX = moveX - 2.6
            time = time + 1

        for i in range (30):
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateY', value = moveY, t=time )
            cmds.setKeyframe( 'SpaceShip2', attribute='translateZ', value = moveZ, t=time )
            cmds.setKeyframe ('SpaceShip2', attribute='rotateX', value = xRot, t=time)
            cmds.setKeyframe ('SpaceShip2', attribute='rotateY', value= yRot, t=time)
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5

            xRot = xRot - .80
            yRot = yRot - .50


            moveX = moveX - 2.6
            moveY = moveY + 2.6
            moveZ = moveZ - 2.6
            time = time + 1

        for a in range (30):
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe ('SpaceShip2', attribute='rotateX', value = xRot, t=time)
            cmds.setKeyframe ('SpaceShip2', attribute='rotateY', value= yRot, t=time)
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5


            xRot = xRot + .80
            yRot = yRot + .50
            time = time + 1

            moveX = moveX - 2.6

        for b in range (35):
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5

            moveX = moveX - 2.0
            time = time + 1

        for c in range (47):
            cmds.setKeyframe('spaceDoor', attribute='rotateY', value = doorRot, t=time)
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5


            time = time + 1
            doorRot = doorRot - 1.5

        for o in range(62):
            cmds.setKeyframe( 'SpaceShip2', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5

            moveX = moveX - 1.0
            time = time + 1

        for q in range (47):
            cmds.setKeyframe('spaceDoor', attribute='rotateY', value = doorRot, t=time)
            cmds.setKeyframe( 'group5', attribute='rotateY', value = centerR, t=time )
            centerR = centerR + .5

            time = time + 1
            doorRot = doorRot + 1.5

    def _handleSpaceShipAndAsteroid(self):
        cmds.file('$HOME/PycharmProjects/space2014/graphics/SpaceShip/scenes/Asteroid.ma',i=True)
        rotY = 0
        rotX = 0
        rotZ = 0
        moveX = 0
        centerR = 0

        aX = -1000
        aY = 352.834
        sX = 0
        doorRot = 0


        time = 0
        time2 = 175


        cmds.camera()
        cmds.move(-90, 370.0, 40.0, relative = True)
        cmds.aimConstraint( 'pCylinder11', 'camera1', offset = (0,-85,0)  )
        cmds.camera()
        cmds.move(-1000, 360.0, 40.0, relative = True)
        cmds.aimConstraint( 'asteroid', 'camera2', offset = (0,-90,0) )
        cmds.camera()
        cmds.move(-1158.453, 371.553, -.461, relative = True)
        cmds.aimConstraint( 'asteroid', 'camera3', offset = (0,-90,0) )




        for o in range(327):
            cmds.setKeyframe('Beam', attribute = 'visibility', value = 0, t=time)
            cmds.setKeyframe( 'asteroid', attribute='translateX', value = aX, t=time )
            cmds.setKeyframe( 'asteroid', attribute='translateY', value = aY, t=time )
            cmds.setKeyframe( 'asteroid', attribute='rotateY', value = rotY, t=time )
            cmds.setKeyframe( 'asteroid', attribute='rotateX', value = rotX, t=time )
            cmds.setKeyframe( 'asteroid', attribute='rotateZ', value = rotZ, t=time )
            cmds.setKeyframe( 'group', attribute='rotateY', value = centerR, t=time )

            rotY = rotY + .25
            rotX = rotX + .25
            rotZ = rotZ + .25
            aX = aX + 2.6
            centerR = centerR + .5

            time = time + 1


        for c in range (47):
            cmds.setKeyframe('spaceDoor', attribute='rotateY', value = doorRot, t=time2)
            time2 = time2 + 1
            doorRot = doorRot - 1.5

        for k in range(105):
            cmds.setKeyframe( 'SpaceShip1', attribute='translateX', value = moveX, t=time2 )
            moveX = moveX - 1.92
            time2 = time2 + 1

        for j in range (47):
            cmds.setKeyframe('spaceDoor', attribute='rotateY', value = doorRot, t=time2)
            time2 = time2 + 1
            doorRot = doorRot + 1.5

        for i in range (500):
            cmds.setKeyframe('Beam', attribute = 'visibility', value = 1, t=time)
            cmds.setKeyframe( 'SpaceShip1', attribute='translateX', value = moveX, t=time )
            cmds.setKeyframe( 'asteroid', attribute='translateX', value = aX, t=time )
            cmds.setKeyframe( 'group', attribute='rotateY', value = centerR, t=time )


            centerR = centerR + .5
            aX = aX - 1.92
            moveX = moveX - 1.92

            time = time + 1

        for i in range (350):
            cmds.setKeyframe('Beam', attribute = 'visibility', value = 0, t=time)
            cmds.setKeyframe( 'asteroid', attribute='translateX', value = aX, t=time )
            cmds.setKeyframe( 'group', attribute='rotateY', value = centerR, t=time )
            cmds.setKeyframe( 'asteroid', attribute='rotateY', value = rotY, t=time )
            cmds.setKeyframe( 'asteroid', attribute='rotateX', value = rotX, t=time )
            cmds.setKeyframe( 'asteroid', attribute='rotateZ', value = rotZ, t=time )

            centerR = centerR + .5
            aX = aX - 1.92

            time = time + 1


#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
