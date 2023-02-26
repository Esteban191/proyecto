
import numpy as np
import cv2

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Line,Rectangle



from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.utils.fitimage import FitImage
from kivy.properties import (
    StringProperty,
    BooleanProperty,
    ObjectProperty,
    NumericProperty,
    ListProperty,
    OptionProperty,
)



import kivy
import numpy as np
import cv2
kivy.require('2.0.0')
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
import cv2
from kivy.graphics import Line,Rectangle
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast


class Grafica(Screen):
    def negativo(self):
        I=cv2.imread(self.root.ids.pic.source)
        Ineg=255-I
        cv2.imwrite("nueva.jpg",Ineg)
        self.root.ids.pic.source=("nueva.jpg.jpg")
            
class Mycanvas(Widget):
    pass 

# class Grafica3(Screen):
#     def ero(self):
#         I2=cv2.imread("FRUTA.jpg")
#         I2=cv2.cvtColor(I2,cv2.COLOR_RGB2GRAY)
#         t,Ibina=cv2.threshold(I2,140,255,cv2.THRESH_BINARY)
#         EE=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#         Iero=cv2.erode(Ibina,EE)
#         cv2.imwrite("Iero.jpg",Iero)
#         with self.canvas.after:
#             Rectangle(source="Iero.jpg",pos=(300,70),size=(200,200))
#    
# class Mycanvas3(Widget):
#     pass

import os
from kivy.clock import Clock
    
class mykivyapp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Main()
    def Cerebro2Erode(self):
        I=cv2.imread(self.root.ids.pic.source)
        EE=cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
        erode=cv2.erode(I,EE)
        cv2.imwrite("C3.jpg",erode)
        self.root.ids.pic1.source=("C3.jpg")
    def chpic(self,new):
        if os.path.isfile(new)==True:
            self.root.ids.pic.source=new
            via=self.root.ids.pic.source
            print(new)
            print("The pictura was changed to:",via)    
    def negativo(self):
        I=cv2.imread(self.root.ids.pic.source)
        Ineg=255-I
        cv2.imwrite("nueva.jpg",Ineg)
        self.root.ids.pic.source=("nueva.jpg")
    
            
    def Cerebro3filtoaltos(self):
        I= cv2.imread(self.root.ids.pic.source)
        kernel=(1/9)*np.array([[-1,-1,-1],[-1,12,-1],[-1,-1,-1]])
        RxPasaAltos=cv2.filter2D(I,-1,kernel)
        cv2.imwrite("Cere32.jpg",RxPasaAltos)
        self.root.ids.pic.source=("Cere32.jpg")
    def Cerebro5HLS(self):
        I=cv2.imread(self.root.ids.pic.source)
        I=cv2.cvtColor(I,cv2.COLOR_RGB2HLS)
        cv2.imwrite("c9.jpg",I)
        self.root.ids.pic.source=("c9.jpg")
        
        
    def imgsecund(self,new):
        if os.path.isfile(new)==True:
            self.root.ids.pic1.source=new
            via1=self.root.ids.pic1.source
            print(new)
            print("The pictura was changed to:",via)     
               
    


    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        print(path)
        if os.path.isfile(path)==True:
            Clock.schedule_once(lambda x:self.chpic(path),1)
        toast(path)
        via1=path#here the location for the image file will be returned
        return path

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    pass

class Main(Screen):
    pass


if __name__ == '__main__':
    mykivyapp().run()