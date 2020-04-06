import cv2
import numpy
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.popup import Popup
from capture import *

class IdentifierPopup(Popup):
    pass

class MainApp(App):
    kv_directory = 'templates'
   
    def getIdUser(self):
        popup = IdentifierPopup()
        popup.open()

    def setIdUser(self, id, popup):
        capturePic = Capture()
        capturePic.startCapture(str(id))
        popup.dismiss()


if __name__ == '__main__':
    MainApp().run()