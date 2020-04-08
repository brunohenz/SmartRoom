import cv2
import numpy
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.popup import Popup
from capture import *
from recognizer import *
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

class IdentifierPopup(Popup):
    pass

class MainScreen(Screen):
    pass

class ConfirmCustomerScreen(Screen):
    pass

presentation = Builder.load_file("templates/main.kv")

class MainApp(App):
    def build(self):
        return presentation
   
    def getIdUser(self):
        popup = IdentifierPopup()
        popup.open()

    def captureFace(self, id, popup):
        capturePic = CaptureFace()
        capturePic.startCapture(str(id))
        popup.dismiss()

    def recognizerFace(self):
        recognizer = RecognizerFace()
        recognizer.startRecognizer()
        
if __name__ == '__main__':
    MainApp().run()