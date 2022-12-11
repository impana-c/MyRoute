import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.properties import StringProperty,ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.utils import platform
from kivy.base import runTouchApp
from plyer import notification
import webbrowser
import sys
import os
import android
reload(sys)
sys.setdefaultencoding('utf-8')

os.system('start /b server-socket.py')
os.system('start /b droidgpspush.py')

Builder.load_string("""
#...............................LOGIN..........................................
<Login>:
    canvas.before:
        Color:
            rgba: -1000, 0.47, 900, 1900
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        id: login_layout
        orientation: 'vertical'
        padding: [10,10,10,10]
        spacing: 5

        Label:
            font_name: 'Dream Orphans'
            text: 'MyRoute'
            halign: 'center'
            font_size: 180
            bold: True

        BoxLayout:
            orientation: 'vertical'

            Button:
                text: "Add a New Route"
                font_name: 'BreeSerif-Regular'
                font_size: 60
                on_press: root.manager.current = 'newroute2'

        BoxLayout:
            orientation: 'vertical'

            Button:
                text: "Log In"
                font_name: 'BreeSerif-Regular'
                font_size: 60
                on_press: root.do_login()


        BoxLayout:
            orientation: 'vertical'

            Button:
                text: "Sign Up with Google"
                font_name: 'BreeSerif-Regular'
                font_size: 60
                on_press: root.do_signupg()

        BoxLayout:
            orientation: 'vertical'

            Button:
                text: "Sign Up with Facebook"
                font_name: 'BreeSerif-Regular'
                font_size: 60
                on_press: root.do_signupf()


##################### ADD NEW ROUTE without logging in ######################
<NewRoute2>:
    label_wid: startroute

    canvas.before:
        Color:
            rgba: -1000, 0.47, 900, 1900
        Rectangle:
            pos: self.pos
            size: self.size


    BoxLayout
        id: newroute2_layout
        orientation: 'vertical'
        padding: [10,10,10,10]
        spacing: 5


        Label:
            text: 'Add a New Route'
            font_name: 'BreeSerif-Regular'
            text_size: root.width, None
            size: self.texture_size
            halign: 'center'
            font_size: 110
            bold: True


        Label:
            text: 'Enter the 3-letter IATA code, 4-letter ICAO code, or the name of the airport'
            text_size: root.width, None
            size: self.texture_size
            font_name: 'Raleway-Regular'
            halign: 'center'
            font_size: 70
            italic: True

        BoxLayout
            orientation: 'horizontal'

            Label:
                font_name: 'American Typewriter Regular'
                text: 'Start Destination:'
                halign: 'left'
                font_size: 60


            TextInput:
                id: start_dstn
                multiline:False
                font_size: 80
                size_hint_y: None
                height: '40dp'



        BoxLayout
            orientation:'horizontal'

            Label:
                text: 'End Destination:'
                font_name: 'American Typewriter Regular'
                halign: 'left'
                font_size: 60


            TextInput:
                id: end_dstn
                multiline:False
                font_size: 80
                size_hint_y: None
                height: '40dp'


        Button:
            id: startroute
            text: 'Start Route'
            background_color: (10,10,10,10)
            size_hint: .3 , .4
            pos: -300,200
            font_size: 50
            color: (0,0,0,1)
            on_press: root.save_new_route(start_dstn.text, end_dstn.text)
            

        Button:
            font_name: 'Dream Orphans'
            text: 'MyRoute'
            halign: 'center'
            size: (50, 30)
            font_size: 100
            bold: True
            size_hint_y: None
            height: '80dp'
            on_press: root.manager.current = 'login'


#..................................HOME......................................
<Home>:
    canvas.before:
        Color:
            rgba: -1000, 0.47, 900, 1900
        Rectangle:
            pos: self.pos
            size: self.size


    BoxLayout:
        orientation: 'vertical'

        Button:
            text: "Add a New Route"
            font_name: 'American Typewriter Regular'
            font_size: 50
        
        Button:
            text: "My Family and Friends"
            font_name: 'American Typewriter Regular'
            font_size: 20
            on_press: root.display_friends()
        
        Button:
            text: "Quit"
            font_name: 'American Typewriter Regular'
            font_size: 50
            on_press: root.disconnect()


        Label:
            text: 'MyRoute'
            font_name: 'American Typewriter Regular'            
            background_color: (-1000, 0.47, 900, 1900)
            font_size: 100
            bold: True

##################### ADD NEW ROUTE with logging in ######################
<NewRoute>:
    label_wid: startroute

    canvas.before:
        Color:
            rgba: -1000, 0.47, 900, 1900
        Rectangle:
            pos: self.pos
            size: self.size


    BoxLayout
        id: newroute_layout
        orientation: 'vertical'
        padding: [10,10,10,10]
        spacing: 5


        Label:
            text: 'Add a New Route'
            font_name: 'BreeSerif-Regular'
            text_size: root.width, None
            size: self.texture_size
            halign: 'center'
            font_size: 110
            bold: True


        Label:
            text: 'Enter the 3-letter IATA code, 4-letter ICAO code, or the name of the airport'
            text_size: root.width, None
            size: self.texture_size
            font_name: 'Raleway-Regular'
            halign: 'center'
            font_size: 70
            italic: True

        BoxLayout
            orientation: 'horizontal'

            Label:
                font_name: 'American Typewriter Regular'
                text: 'Start Destination:'
                halign: 'left'
                font_size: 60


            TextInput:
                id: start_dstn
                multiline:False
                font_size: 80
                size_hint_y: None
                height: '40dp'



        BoxLayout
            orientation:'horizontal'

            Label:
                text: 'End Destination:'
                font_name: 'American Typewriter Regular'
                halign: 'left'
                font_size: 60


            TextInput:
                id: end_dstn
                multiline:False
                font_size: 80
                size_hint_y: None
                height: '40dp'


        Button:
            id: startroute
            text: 'Start Route'
            background_color: (10,10,10,10)
            size_hint: .3 , .4
            pos: -300,200
            font_size: 50
            color: (0,0,0,1)
            on_press: root.save_new_route(start_dstn.text, end_dstn.text)
            

        Button:
            font_name: 'Dream Orphans'
            text: 'MyRoute'
            halign: 'center'
            size: (50, 30)
            font_size: 100
            bold: True
            size_hint_y: None
            height: '80dp'
            on_press: root.manager.current = 'home'


#................................START NEW ROUTE......................................
<StartNewRoute>:
    canvas.before:
        Color:
            rgba: -1000, 0.47, 900, 1900
        Rectangle:
            pos: self.pos
            size: self.size


    BoxLayout
        id: startnewroute_layout
        orientation: 'vertical'
        padding: [10,10,10,10]
        spacing: 5


        Label:
            id:alert
            font_name: 'BreeSerif-Regular'
            text: ''
            text_size: root.width, None
            size: self.texture_size
            halign: 'center'
            font_size: 200
            bold: True
            italic: True

    
        Button:
            id: button
            text: ''
            background_color: (-1000, 0.47, 900, 1900)
            halign: 'center'
            size_hint: (None, None)
            height: '100dp'
            width: '100dp'
            on_press: root.display_friends()
""")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
class Login(Screen):
    def do_login(self):
        webbrowser.open("https://www.pushbullet.com/signin?next=%2F")
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'home'
    
    def do_signupg(self):
        webbrowser.open("https://accounts.google.com/signin/oauth/oauthchooseaccount?client_id=336343571939-881tp5n559pij79kmb2irmnbg641qt7c.apps.googleusercontent.com&as=-20ff7343999749b0&destination=https%3A%2F%2Fwww.pushbullet.com&approval_state=!ChRMa3ZNUV9NVTY2UXY4Zm9GS184YRIfTXpzQU56U0xsbkFib1Bud0gtVkU1UUdtLVNBZUVCWQ%E2%88%99ACThZt4AAAAAWmACJ7txpLlf0tBNRL9ex3MR7ii9UE7M&xsrfsig=AHgIfE_ibst8b8Okzd3oJUg5wRs0UJPh7Q&flowName=GeneralOAuthFlow")
    
    def do_signupf(self):
        webbrowser.open("https://www.facebook.com/login.php?skip_api_login=1&api_key=1541617089384972&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.pushbullet.com%252F%26state%3D93fu5dnkb30lutes7vp2g%26scope%3Demail%26response_type%3Dtoken%26auth_type%3Drerequest%26client_id%3D1541617089384972%26ret%3Dlogin%26logger_id%3Da9ea4676-8cc8-d8bc-49ed-593420aa82a2&cancel_url=https%3A%2F%2Fwww.pushbullet.com%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D93fu5dnkb30lutes7vp2g%23_%3D_&display=page&locale=en_US&logger_id=a9ea4676-8cc8-d8bc-49ed-593420aa82a2")


###############################################################################
class Home(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('signup').resetForm()

    def display_friends(self):
       webbrowser.open("https://www.pushbullet.com/#people")

class StartNewRoute(Screen):


    def display_friends(self):
       webbrowser.open("https://www.pushbullet.com/#people")


################## IN CASE YOU CLICK ADD NEW ROUTE BEFORE LOGIN ##############
class NewRoute2(Screen):
    def save_new_route(self, start_dstnText, end_dstnText):
        title = Label(text=('[color=ff3333][/color]'), font_size=str(25) + 'sp', markup=True,pos=(0, 190))
        self.add_widget(title)
        
        quote = '"'
        s_d= quote + start_dstnText.lower() + quote
        e_d= quote + end_dstnText.lower() + quote
        
        with open('data.csv', 'r') as ab:

            for line in ab:
                if s_d=='""' or e_d=='""':
                   title.text = ('[color=ff3333]Add New Route Failed![/color]')
                   def my_callback(dt):
                       title.text= ''
                   Clock.schedule_interval(my_callback, 2)
                if s_d==e_d:
                   title.text = ('[color=ff3333]Add New Route Failed![/color]')
                   def my_callback(dt):
                       title.text= ''
                   Clock.schedule_interval(my_callback, 2)
                if len(start_dstnText)>4 or len(end_dstnText)>4:
                   title.text = ('[color=ff3333]Add New Route Failed![/color]')
                   def my_callback(dt):
                       title.text= ''
                   Clock.schedule_interval(my_callback, 2)


                if s_d in line:
                    start_line = line
                    list = start_line.split(',')
                    start_y=list[6]
                    start_x=list[7]
                if e_d in line:
                    end_line = line
                    list = end_line.split(',')
                    end_y=list[6]
                    end_x=list[7]


                if s_d and e_d in line and s_d != '""' and e_d != '""' and s_d != e_d:
                    with open('file', 'r') as f:
                        data = f.readlines()
                        for line in data:
                            values = line.split(', ')
                    lon = values[0]
                    lat = values[1].rstrip("\n\r")
                    lon_ = lon
                    lat_ = lat

                    if (start_x < end_x) and (start_y < end_y):
                        bbox_lx = start_x
                        bbox_dy = start_y
                        bbox_rx = end_x
                        bbox_uy = end_y
                    if (start_x < end_x) and (start_y > end_y):
                        bbox_lx = start_x
                        bbox_uy = start_y
                        bbox_rx = end_x
                        bbox_dy = end_y
                    if (start_x > end_x) and (start_y < end_y):
                        bbox_rx = start_x
                        bbox_dy = start_y
                        bbox_lx = end_x
                        bbox_uy = end_y

                        if (lat_ < bbox_rx) and (lat_ > bbox_lx) and (lon_ < bbox_uy) and (lon_ > bbox_dy):
                            screen2 = self.manager.get_screen('startnewroute')
                            screen2.ids.alert.text = "On Route!"
                            self.manager.transition = SlideTransition(direction="right")
                            self.manager.current = 'startnewroute'
                            def my_callback(dt):
                                self.manager.transition = SlideTransition(direction="left")
                                self.manager.current = 'newroute2'
                                self.label_wid.text = 'Recalculate'
                            Clock.schedule_interval(my_callback, 5)

                        if (lat_ > bbox_rx) or (lat_ < bbox_lx) or(lon_ > bbox_uy) or (lon_ < bbox_dy):    
                            android.vibrate(7)
                            notification.notify('ALERT', 'Plane is Off Route!!!')
                            screen2 = self.manager.get_screen('startnewroute')
                            screen2.ids.alert.text = "Off Route!"
                            title2 = Label(text=('[b][color=ff3333]<--- Alert Someone![/color][/b]'), font_size=str(29) + 'sp', markup=True,pos=(175, -850))
                            screen2.add_widget(title2)
                            self.manager.transition = SlideTransition(direction="right")
                            self.manager.current = 'startnewroute'
                            def my_callback(dt):
                                title2.text = ('[color=ff3333][/color]')
                                self.manager.transition = SlideTransition(direction="left")
                                self.manager.current = 'newroute2'
                                self.label_wid.text = 'Recalculate'
                            Clock.schedule_interval(my_callback, 7)
                    

                    if (start_x > end_x) and (start_y > end_y):
                        bbox_rx = start_x
                        bbox_uy = start_y
                        bbox_lx = end_x 
                        bbox_dy = end_y

                    if (lat_ < bbox_rx) and (lat_ > bbox_lx) and (lon_ < bbox_uy) and (lon_ > bbox_dy):
                        screen2 = self.manager.get_screen('startnewroute')
                        screen2.ids.alert.text = "On Route!"
                        self.manager.transition = SlideTransition(direction="right")
                        self.manager.current = 'startnewroute'
                        def my_callback(dt):
                            self.manager.transition = SlideTransition(direction="left")
                            self.manager.current = 'newroute2'
                            self.label_wid.text = 'Recalculate'
                        Clock.schedule_interval(my_callback, 5)


                    if (lat_ > bbox_rx) or (lat_ < bbox_lx) or(lon_ > bbox_uy) or (lon_ < bbox_dy):    
                        android.vibrate(7)
                        notification.notify('ALERT', 'Plane is Off Route!!!')
                        screen2 = self.manager.get_screen('startnewroute')
                        screen2.ids.alert.text = "Off Route!"
                        title2 = Label(text=('[b][color=ff3333]<--- Alert Someone![/color][/b]'), font_size=str(29) + 'sp', markup=True,pos=(175, -850))
                        screen2.add_widget(title2)
                        self.manager.transition = SlideTransition(direction="right")
                        self.manager.current = 'startnewroute'
                        def my_callback(dt):
                            title2.text = ('[color=ff3333][/color]')
                            self.manager.transition = SlideTransition(direction="left")
                            self.manager.current = 'newroute2'
                            self.label_wid.text = 'Recalculate'
                        Clock.schedule_interval(my_callback, 7)
                    
###############################################################################
# When you click Add New Route after you Login
class NewRoute(Screen):
    def save_new_route(self, start_dstnText, end_dstnText):
        title = Label(text=('[color=ff3333][/color]'), font_size=str(25) + 'sp', markup=True,pos=(0, 90))
        self.add_widget(title)      
        quote = '"'
        s_d= quote + start_dstnText.lower() + quote
        e_d= quote + end_dstnText.lower() + quote
        
        with open('data.csv', 'r') as ab:

            for line in ab:
                if s_d=='""' or e_d=='""':
                   title.text = ('[color=ff3333]Add New Route Failed![/color]')
                   def my_callback(dt):
                       title.text= ''
                   Clock.schedule_interval(my_callback, 2)
                if s_d==e_d:
                   title.text = ('[color=ff3333]Add New Route Failed![/color]')
                   def my_callback(dt):
                       title.text= ''
                   Clock.schedule_interval(my_callback, 2)
                if s_d or e_d not in line:
                    title.text = ('[color=ff3333]Add New Route Failed![/color]')
                    def my_callback(dt):
                       title.text= ''
                    Clock.schedule_interval(my_callback, 2)


                if s_d in line:
                    start_line = line
                    list = start_line.split(',')
                    start_y=list[6]
                    start_x=list[7]
                if e_d in line:
                    end_line = line
                    list = end_line.split(',')
                    end_y=list[6]
                    end_x=list[7]


                if s_d and e_d in line and s_d != '""' and e_d != '""' and s_d != e_d:
                    title.text='yep'
                    with open('file', 'r') as f:
                        data = f.readlines()
                        for line in data:
                            values = line.split(', ')
                    lon = values[0]
                    lat = values[1].rstrip("\n\r")
                    lon_ = lon
                    lat_ = lat

                    if (start_x < end_x) and (start_y < end_y):
                        bbox_lx = start_x
                        bbox_dy = start_y
                        bbox_rx = end_x
                        bbox_uy = end_y
                    if (start_x < end_x) and (start_y > end_y):
                        bbox_lx = start_x
                        bbox_uy = start_y
                        bbox_rx = end_x
                        bbox_dy = end_y
                    if (start_x > end_x) and (start_y < end_y):
                        bbox_rx = start_x
                        bbox_dy = start_y
                        bbox_lx = end_x
                        bbox_uy = end_y
                    if (start_x > end_x) and (start_y > end_y):
                        bbox_rx = start_x
                        bbox_uy = start_y
                        bbox_lx = end_x 
                        bbox_dy = end_y

                    if (lat_ < bbox_rx) and (lat_ > bbox_lx) and (lon_ < bbox_uy) and (lon_ > bbox_dy):
                        screen2 = self.manager.get_screen('startnewroute')
                        screen2.ids.alert.text = "On Route!"
                        self.manager.transition = SlideTransition(direction="right")
                        self.manager.current = 'startnewroute'
                        def my_callback(dt):
                            self.manager.transition = SlideTransition(direction="left")
                            self.manager.current = 'newroute'
                            self.label_wid.text = 'Recalculate'
                        Clock.schedule_interval(my_callback, 5)

                    if (lat_ > bbox_rx) or (lat_ < bbox_lx) or(lon_ > bbox_uy) or (lon_ < bbox_dy):    
                        android.vibrate(7)
                        notification.notify('ALERT', 'Plane is Off Route!!!')
                        screen2 = self.manager.get_screen('startnewroute')
                        screen2.ids.alert.text = "Off Route!"
                        title2 = Label(text=('[b][color=ff3333]<--- Alert Someone![/color][/b]'), font_size=str(29) + 'sp', markup=True,pos=(175, -850))
                        screen2.add_widget(title2)
                        self.manager.transition = SlideTransition(direction="right")
                        self.manager.current = 'startnewroute'
                        def my_callback(dt):
                            title2.text = ('[color=ff3333][/color]')
                            self.manager.transition = SlideTransition(direction="left")
                            self.manager.current = 'newroute'
                            self.label_wid.text = 'Recalculate'
                        Clock.schedule_interval(my_callback, 7)
                
######################################################################################################


#%%%%*****%%%%%%%%%%%**********%%%%%%%%%***********%%%%%%%%%%%***********%%%%%%%%%%%%%**********%%%
#%%%%*****%%%%%%%%%%%**********%%%%%%%%%***********%%%%%%%%%%%***********%%%%%%%%%%%%%**********%%%
                      

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Login(name='login'))
sm.add_widget(NewRoute2(name='newroute2'))
sm.add_widget(NewRoute(name='newroute'))
sm.add_widget(Home(name='home'))
sm.add_widget(StartNewRoute(name='startnewroute'))

class MyRouteApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyRouteApp().run()