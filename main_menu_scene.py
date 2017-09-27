# Created by: Julie Nguyen
# Created on: Sep 2017
# Created for: ICS3U
# This program is the first file in a multi-scene game template
#    This template is meant to be used with the Xcode template,
#    to make apps for the App Store.
#
# Originally from: Ole Zorn, from the Xcode template
# for use with https://github.com/omz/PythonistaAppTemplate
# Also from the Pythonista community forum.
#
# This file creates the UIView that will be used by Xcode,
#  then creates the scene inside it. once everything is ready
#  to go, the scene transitions immediately to the first scene.
# It is assumed you bring along all your assets, 
#   and not use any of the mornal ones built into Pythonista.
#
# To exit the app in Pythonista, pull down with 2 fingers.

from scene import *
import ui

class MainMenuScene(Scene):

                                       
    def setup(self):
        # this method is called, when user moves to this scene
        pass
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.background = SpriteNode(position = self.size/2,
                                     color = (0.11, 0.99, 0.11),
                                     parent = self,
                                     size = self.size)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
