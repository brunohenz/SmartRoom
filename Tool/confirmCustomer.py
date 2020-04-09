from kivy.app import App
from kivy.properties import StringProperty
from os.path import join, dirname
from kivy.lang import Builder
from kivy.uix.popup import Popup
import json

Builder.load_file(join(dirname(__file__), 'templates/confirmCustomer.kv'))

class ConfirmPopup(Popup):
    customer = StringProperty("")
    
    def __init__(self, customer):
        super(ConfirmPopup, self).__init__()        
        
        _customer = json.loads(customer)        
        print(_customer["Nome"])

    def error(self):
        self.dismiss()

