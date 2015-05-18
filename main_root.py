import main
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.properties import StringProperty
from kivy.clock import Clock

Builder.load_file('months.kv')
Builder.load_file('dates.kv')
Builder.load_file('select.kv')
Builder.load_file('status.kv')
Builder.load_file('days.kv')
Builder.load_file('calendar.kv')

class main_root(BoxLayout):
    def __init__(self,**kwargs):
        super(main_root,self).__init__(**kwargs)
# ------------------------------------------------------------------------------------------------#

# class for status.kv file
class Status(BoxLayout):
    
    def __init__(self,**kwargs):
        super(Status,self).__init__(**kwargs)
        
        
class Root(BoxLayout):
    def __init__(self,**kwargs):
        super(Root,self).__init__(**kwargs)

class main_rootApp(App):
    
    time = StringProperty()
    def update(self,*args):
        self.time = str(time.asctime())
        
    def build(self):
        self.title = "Multipurpose Application"
        Clock.schedule_interval(self.update,1)
        return main_root()
    
if __name__ == '__main__':
    app = main_rootApp()
    app.run()
    