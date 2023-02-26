import kivy
kivy.require('2.0.0')
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Rectangle
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

import cv2


class Principal(ScreenManager):
    pass

class Panta1(Screen):
    def negativo(self):
        I=cv2.imread("1.jpeg")
        Window.clearColor = (1,0,1,0)
        Ineg=255-I
        cv2.imwrite("nueva.jpg",Ineg)
        with self.canvas.after:
            Rectangle(source="nueva.jpg",pos=(300,50),size=(200,200))

class Panta2(Screen):
    def ero(self):
        Ec=cv2.imread("Ecografia.jpeg",0) 
        t,EcBin=cv2.threshold(Ecografia,100,255,cv2.THRESH_BINARY)    
        cv2.imwrite("EcBin.jpg",EcBin) 
        with self.canvas.after:
            Window.clearColor = (1,0,1,0)
            Rectangle(source="Iero.jpg",pos=(300,70),size=(200,200))
        
    pass
class MiCanvas(Widget):
    pass
class MiCanvas2(Widget):
    pass

class pantasApp(App):
    def build(self):
        
        return Principal()
    
if __name__ == '__main__':
     pantasApp().run()
    
