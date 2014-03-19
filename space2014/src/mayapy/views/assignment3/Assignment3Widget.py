# Assignment2Widget.py
# (C)2013
# Scott Ernst

import os
import platform
import nimble
from nimble import cmds
from nimble import MayaCommandException
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment2Widget
class Assignment3Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment2Widget."""
        super(Assignment3Widget, self).__init__(parent, **kwargs)
        self.createBtn.clicked.connect(self._handleCreate)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

    def _handleCreate(self):

        # set initial rotations to zero
        rStat = 0

        # get degrees pre frame for station whell
        rotStation = int(self.ssr.text())

        # set number of frames to shoot at each camera location
        aimPt_1_frames = int(self.cam1f.text())
        aimPt_2_frames = int(self.cam2f.text()) + aimPt_1_frames
        aimPt_3_frames = int(self.cam3f.text()) + aimPt_2_frames
        endPtFrames = 50 + aimPt_3_frames

        # camera position 1
        aimPt_1_x = float(self.cam1x.text())
        aimPt_1_y = float(self.cam1y.text())
        aimPt_1_z = float(self.cam1z.text())

        # camera position 2
        aimPt_2_x = float(self.cam2x.text())
        aimPt_2_y = float(self.cam2y.text())
        aimPt_2_z = float(self.cam2z.text())

        # camera position 3
        aimPt_3_x = float(self.cam3x.text())
        aimPt_3_y = float(self.cam3y.text())
        aimPt_3_z = float(self.cam3z.text())

        # import sun
        cmds.file('$HOME/PycharmProjects/space2014/graphics/SpaceStation/scenes/sun.ma', i=True)
        # move sun away from station
        cmds.move(0, 0, 655, 'pSphere1')
        # import station
        cmds.file('$HOME/PycharmProjects/space2014/graphics/SpaceStation/scenes/station.ma', i=True)
        # import background
        cmds.file('$HOME/PycharmProjects/space2014/graphics/SpaceStation/scenes/stage.ma', i=True)

        # create a new camera
        cam = cmds.camera()

        # move camera to first position
        cmds.move(aimPt_1_x, aimPt_1_y, aimPt_1_z, cam)

        cmds.lookThru(cam)

        cmds.setKeyframe( cam, t=0 )

        i = 1

        while i < aimPt_1_frames:

            cmds.setKeyframe( 'Wheel', attribute='rotateY', value=rStat, t=i )
            rStat = rStat + rotStation
            i += 1

        cmds.setKeyframe( cam, t=i )

        while i < aimPt_2_frames:
            cmds.setKeyframe( 'Wheel', attribute='rotateY', value=rStat, t=i )
            rStat = rStat + rotStation
            i += 1

        cmds.move(aimPt_2_x, aimPt_2_y, aimPt_2_z, cam)
        cmds.setKeyframe( cam, t=i )
        cmds.setKeyframe( 'SolarPanels', attribute='rotateZ', value=0, t=i)

        while i < aimPt_3_frames:
            cmds.setKeyframe( 'Wheel', attribute='rotateY', value=rStat, t=i )
            rStat = rStat + rotStation
            i += 1

        cmds.move(aimPt_3_x, aimPt_3_y, aimPt_3_z, cam)
        cmds.aimConstraint('spaceStation', 'camera1', offset = (0, -90, 0))
        cmds.setKeyframe( cam, t=i )
        cmds.setKeyframe( 'SolarPanels', attribute='rotateZ', value=float(self.spe.text()), t=i)
        # cmds.setKeyframe( 'SolarPanels', attribute='rotateX', value=float(self.spa.text()), t=i)

        while i < endPtFrames:
            cmds.setKeyframe( 'Wheel', attribute='rotateY', value=rStat, t=i )
            rStat = rStat + rotStation
            i += 1

        print 'Total number of frames = ', endPtFrames
        print platform.system()