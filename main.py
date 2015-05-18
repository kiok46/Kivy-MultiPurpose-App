# Project made by: Kuldeep Singh
# Student at LNMIIT,Jaipur,India

# import Statements
import calendar
import time
import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.event import EventDispatcher
from kivy.uix.textinput import TextInput

# Builder used to load all the kivy files to be loaded in the main.py file
''' 
this is commented because i will make is a subclass
Builder.load_file('months.kv')
Builder.load_file('dates.kv')
Builder.load_file('select.kv')
Builder.load_file('days.kv')
'''
# class for calendar.kv file
class Calendar(BoxLayout):
    def __init__(self,**kwargs):
        super(Calendar,self).__init__(**kwargs)
        
# ------------------------------------------------------------------------------------------------#


# class for Reminder in Dates
class Reminder(BoxLayout):
    tell_me = BooleanProperty(False)
    def __init__(self,**kwargs):
        super(Reminder,self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.add_widget(TextInput())
        self.b = BoxLayout(orientation = 'horizontal' , size_hint = (1,.15))
        self.add_widget(self.b)
        self.b.add_widget(Button(on_release = self.on_release,text = "OK!"))
        
    def on_release(self,event):
        print "OK clicked!"
        print event.parent.parent.parent.parent.parent
        self.tell_me = True
        return self.tell_me
        

# ------------------------------------------------------------------------------------------------#
'''
class get_months(GridLayout):
    def __init__(self,c,**kwargs):
        super(get_months,self).__init__(**kwargs)
        self.cols = 7
        self.c  = calendar.monthcalendar(2015,5)
        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(Button(on_release = self.on_release,text = '{j}'.format(j='')))
                else:
                    self.add_widget(Button(on_release = self.on_release, text = '{j}'.format(j=j)))
    
    def on_release(self,args):
        pass
        
        
'''
# class for dates.kv file
class Dates(GridLayout):
    now = datetime.datetime.now()
    c  = calendar.monthcalendar(2015,5)
    btn_1 = ObjectProperty(None)
    btn_2 = ObjectProperty(None)
    btn_3 = ObjectProperty(None)
    btn_4 = ObjectProperty(None)
    btn_5 = ObjectProperty(None)
    btn_6 = ObjectProperty(None)
    btn_7 = ObjectProperty(None)
    btn_8 = ObjectProperty(None)
    btn_9 = ObjectProperty(None)
    btn_10 = ObjectProperty(None)
    btn_11 = ObjectProperty(None)
    btn_12 = ObjectProperty(None)
    btn_13 = ObjectProperty(None)
    btn_14 = ObjectProperty(None)
    btn_15 = ObjectProperty(None)
    btn_16 = ObjectProperty(None)
    btn_17 = ObjectProperty(None)
    btn_18 = ObjectProperty(None)
    btn_19 = ObjectProperty(None)
    btn_20 = ObjectProperty(None)
    btn_21 = ObjectProperty(None)
    btn_22 = ObjectProperty(None)
    btn_23 = ObjectProperty(None)
    btn_24 = ObjectProperty(None)
    btn_25 = ObjectProperty(None)
    btn_26 = ObjectProperty(None)
    btn_27 = ObjectProperty(None)
    btn_28 = ObjectProperty(None)
    btn_29 = ObjectProperty(None)
    btn_30 = ObjectProperty(None)
    btn_31 = ObjectProperty(None)
    btn_32 = ObjectProperty(None)
    btn_33 = ObjectProperty(None)
    btn_34 = ObjectProperty(None)
    btn_35 = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(Dates,self).__init__(**kwargs)
        self.cols = 7
    
    def on_dismiss(self, arg):
        # Do something on close of popup
        pass
    
    def on_release(self,event):
        #print event
        #print event.background_color
        #print "date clicked :" + event.text
        #event.background_color = 1,0,0,1
        if event.text == '':
            pass
        else:
            self.popup = Popup(title= "Set Reminder :",
            content = Reminder(),
            size_hint=(None, None), size=(self.width*3/4, self.height))
            self.popup.bind(on_dismiss = self.on_dismiss)
            self.popup.open() 
        
    def on_blast(self):
        self.popup = Popup(title= "Set Reminder :",
        content = Reminder(),
        size_hint=(None, None), size=(self.width*3/4, self.height))
        self.popup.bind(on_dismiss = self.on_dismiss)
        self.popup.open() 


# ------------------------------------------------------------------------------------------------#

# class for select.kv file
class Select(BoxLayout):
    
    month = ObjectProperty()
    y1 = ListProperty()
    y2 = ListProperty()
    year_1 = ObjectProperty(None)
    year_2 = ObjectProperty(None)
    lbl_ = ObjectProperty(None)
    btn = ObjectProperty(None)
    c  = calendar.monthcalendar(2015,5)
    global count
    
    def __init__(self,**kwargs):
        super(Select,self).__init__(**kwargs)
        self.count = 0 
        self.month = 1
        
    def get_years(self):
        if self.count == 0:
            for i in range(0,100):
                if i<10:
                    self.y1.append('0'+str(i))
                    if i == 0:
                        pass
                    else:
                        self.y2.append('0'+str(i))
                else:
                    self.y1.append(str(i))
                    self.y2.append(str(i))
        self.count = 1
        self.year_1.values = self.y1
        self.year_2.values = self.y2
        
    def on_release(self):
        self.parent.parent.ids.dates.btn_1.text = "change"
        self.a = int(self.year_1.text)
        self.b = int(self.year_2.text)
        
        #print "a-> %02d" % (self.a,)
        #print "b-> %02d" % (self.b,)
        self.final = int(str("%02d" % (self.a,))+str("%02d" % (self.b,)))
        #print int("%04d"%(self.final,))
        self.survive = []
        #print "month is ", self.parent.parent.ids.months.decide
        self.c = calendar.monthcalendar(self.final,self.parent.parent.ids.months.decide)
        for i in self.c:
            for j in i:
                if j == 0:
                    self.survive.append(' ')
                else:
                    self.survive.append(j)

        #print self.survive
        
        self.parent.parent.ids.dates.btn_1.text = str(self.survive[0])
        self.parent.parent.ids.dates.btn_2.text = str(self.survive[1])
        self.parent.parent.ids.dates.btn_3.text = str(self.survive[2])
        self.parent.parent.ids.dates.btn_4.text = str(self.survive[3])
        self.parent.parent.ids.dates.btn_5.text = str(self.survive[4])
        self.parent.parent.ids.dates.btn_6.text = str(self.survive[5])
        self.parent.parent.ids.dates.btn_7.text = str(self.survive[6])
        self.parent.parent.ids.dates.btn_8.text = str(self.survive[7])
        self.parent.parent.ids.dates.btn_9.text = str(self.survive[8])
        self.parent.parent.ids.dates.btn_10.text = str(self.survive[9])
        self.parent.parent.ids.dates.btn_11.text = str(self.survive[10])
        self.parent.parent.ids.dates.btn_12.text = str(self.survive[11])
        self.parent.parent.ids.dates.btn_13.text = str(self.survive[12])
        self.parent.parent.ids.dates.btn_14.text = str(self.survive[13])
        self.parent.parent.ids.dates.btn_15.text = str(self.survive[14])
        self.parent.parent.ids.dates.btn_16.text = str(self.survive[15])
        self.parent.parent.ids.dates.btn_17.text = str(self.survive[16])
        self.parent.parent.ids.dates.btn_18.text = str(self.survive[17])
        self.parent.parent.ids.dates.btn_19.text = str(self.survive[18])
        self.parent.parent.ids.dates.btn_20.text = str(self.survive[19])
        self.parent.parent.ids.dates.btn_21.text = str(self.survive[20])
        self.parent.parent.ids.dates.btn_22.text = str(self.survive[21])
        self.parent.parent.ids.dates.btn_23.text = str(self.survive[22])
        self.parent.parent.ids.dates.btn_24.text = str(self.survive[23])
        self.parent.parent.ids.dates.btn_25.text = str(self.survive[24])
        self.parent.parent.ids.dates.btn_26.text = str(self.survive[25])
        self.parent.parent.ids.dates.btn_27.text = str(self.survive[26])
        self.parent.parent.ids.dates.btn_28.text = str(self.survive[27])
        self.parent.parent.ids.dates.btn_29.text = str(self.survive[28])
        self.parent.parent.ids.dates.btn_30.text = str(self.survive[29])
        self.parent.parent.ids.dates.btn_31.text = str(self.survive[30])
        self.parent.parent.ids.dates.btn_32.text = str(self.survive[31])
        self.parent.parent.ids.dates.btn_33.text = str(self.survive[32])
        self.parent.parent.ids.dates.btn_34.text = str(self.survive[33])
        self.parent.parent.ids.dates.btn_35.text = str(self.survive[34])
        

# ------------------------------------------------------------------------------------------------#

# class for months.kv file
class Months(BoxLayout):
    decide = ObjectProperty(None)
    btn_jan = ObjectProperty(None)
    btn_feb = ObjectProperty(None)
    btn_mar = ObjectProperty(None)
    btn_april = ObjectProperty(None)
    btn_may = ObjectProperty(None)
    btn_june = ObjectProperty(None)
    btn_july = ObjectProperty(None)
    btn_aug = ObjectProperty(None)
    btn_sept = ObjectProperty(None)
    btn_oct = ObjectProperty(None)
    btn_nov = ObjectProperty(None)
    btn_dec = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(Months,self).__init__(**kwargs)
        self.decide = 1
        
    def on_release(self,event):
        self.previous = event.name
        if event.text == 'Jan':
            self.decide = 1
            self.parent.parent.ids.select.month = 1
        elif event.text == 'Feb':
            self.decide = 2
            self.parent.parent.ids.select.month = 2
        elif event.text == 'Mar':
            self.decide = 3
            self.parent.parent.ids.select.month = 3
        elif event.text == 'April':
            self.decide = 4
            self.parent.parent.ids.select.month = 4
        elif event.text == 'May':
            self.decide = 5
            self.parent.parent.ids.select.month = 5
        elif event.text == 'June':
            self.decide = 6
            self.parent.parent.ids.select.month = 6
        elif event.text == 'July':
            self.decide = 7
            self.parent.parent.ids.select.month = 7
        elif event.text == 'Aug':
            self.decide = 8
            self.parent.parent.ids.select.month = 8
        elif event.text == 'Sept':
            self.decide = 9
            self.parent.parent.ids.select.month = 9
        elif event.text == 'Oct':
            self.decide = 10
            self.parent.parent.ids.select.month = 10
        elif event.text == 'Nov':
            self.decide = 11
            self.parent.parent.ids.select.month = 11
        elif event.text == 'Dec':
            self.decide = 12
            self.parent.parent.ids.select.month = 12
        #event.background_color = 1,0,0,1
        
        

# ------------------------------------------------------------------------------------------------#

'''
# mainApp class
class mainApp(App):
    time = StringProperty()
    
    def update(self,*args):
        self.time = str(time.asctime())
    
    def build(self):
        self.title = "Kivy-Calendar"
        self.load_kv('calender.kv')
        Clock.schedule_interval(self.update,1)
        return Calender()

# BoilerPlate
if __name__ =='__main__':
    app = mainApp()
    app.run()'''