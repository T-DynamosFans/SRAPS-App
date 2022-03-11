

__version__ = "1.0.0"


import kivy
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import *
from kivymd.uix.label import *
from kivy.uix.image import *
from kivy.uix.label import *
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivy.core.text import LabelBase 
from kivymd.uix.button import *
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivy.core.audio import *
from kivymd.uix.list import *
from kivymd.toast import toast as Toast
from kivy.uix.scrollview import *
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.uix.modalview import ModalView

from kivy.uix.carousel import Carousel
from kivymd.uix.expansionpanel import *
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
import requests
import webbrowser
import os
import subprocess
import sys
import threading
from pathlib import Path
from kivy.clock import Clock
from functools import partial
from kivymd.icon_definitions import md_icons
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
import time
import _thread
from kivymd.uix.dialog import MDDialog
from functools import partial
from dataDb import Teachers
screen_manager = ScreenManager()
if platform != "android":
	Window.size =(360,640)
print(Window.size)
def check_intr():
	import requests
	try:
		requests.get("https://google.com",timeout=1)
	except Exception as e:
		print(str(e))
		return False
	return True

	
def getDb():
	apiUrl = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/app.database"
	try:
		a = requests.get(apiUrl,timeout=2)
		open('dataDb.py', 'wb').write(a.content)
		import dataDb
		from dataDb import DataBase, Teachers
	except Exception as e:
		return exit(str(e))
	return DataBase, Teachers

def return_Sycn(url):
	import random
	try:
		path = f'assets/tmp-{random.random()}.{(url.split("."))[-1]}'
		r = requests.get(url, allow_redirects=True)
		open(path ,'wb').write(r.content)
		return path
	except Exception:
		return "assets/no-internet.png"
def update_data():
	o = screen_manager.get_screen("Mscreen").ids
	DataBase, Teachers = getDb()
	o.news.text = str(DataBase["News"])		
	o.nimg.source = DataBase["SliderImages"]

def show_message(Ok):
		dialog=Snackbar(text="No Internet!",
		snackbar_x="10dp",

		radius=[30,30,30,30],
		snackbar_y="55dp",
		size_hint_x=.95)
		a = lambda self : (Toast("Updating data"),_thread.start_new_thread(update_data,()),dialog.dismiss())
		b = lambda self : Toast("Internet not connected")
		c = lambda self : (dialog.dismiss(),Clock.schedule_once(show_message,5))
		d = lambda self : a(True) if check_intr() is True else b(True)
		dialog.buttons = [
		MDFlatButton(text="Retry",
			font_name="assets/Poppins-Regular.ttf",
			theme_text_color="Custom",
			text_color=[1,1,1,1],
			on_press = d), 
		MDFlatButton (text="Cancel",
			font_name="assets/Poppins-Regular.ttf",
			theme_text_color="Custom",
			text_color=[1,1,1,1],
			on_press=c)]
		dialog.auto_dismiss=False
		dialog.open()
def show_timings():

	a = """
MDCard:
	radius:[30]
	size:(0.85,0.85)
	elevation:50
	ScrollView:
		MDGridLayout:
			cols:1
			adaptive_height:True
			spacing:app.spacing*3
			orientation :"lr-tb"

			MDLabel:
				text:"Timings can be changed any time as the situation demands."
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"• Parents must ensure that their children reach at least 10 minutes before the gate is closed so that children are able to attend the morning assembly."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:"• First Bell will ring 5 minutes prior to the time mentioned above."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:"• In the morning no student will be allowed to enter the school after the second bell."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:"• The gate will remain closed during assembly. At the time of dispersal gates will open at the time of last bell."
				font_name:"assets/Poppins-Regular.ttf"	
			MDLabel:
				text:"• For Primary Wing the gate will open only 5 minutes before dispersal time."
				font_name:"assets/Poppins-Regular.ttf"
		"""
	modal = ModalView(

	size_hint=(0.83, 0.7),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(a))

	modal.open()	
def show_fees():
	card = MDCard(elevation=50,radius=[30,30,30,30],size=(0.83,0.7))
	a = MDDataTable(
	size=(0.8,0.8),
	use_pagination=True,
	column_data=[

	("Sr.No.", dp(20)),

	("Class", dp(20)),

	("Monthly Fees", dp(20))],
	row_data = (
		["1","Newly Admit Fees","₹ 15395"],
		["2","NUR - UKG ","₹ 3080"],
		["3","I - V","₹ 3100"],
		["4","VI - VIII","₹ 3235"],
		["5","IX - X","₹ 3360"],
		["6","XI - XII Science","₹ 3545"],
		["7","XI - XII Commerce/Arts","₹ 3380"],
		)
	)
	card.add_widget(a)
	modal = ModalView(

	size_hint=(0.83, 0.7),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(card)

	modal.open()	
def show_teachers(self):
	card = MDCard(elevation=50, radius=[30],size=(1,1))
	f = MDDataTable(
	size=(0.8,0.8),
	use_pagination=True,
	column_data=[

	("No.", dp(20)),

	("Name", dp(20)),

	("Designation", dp(20)),

	("Qualification", dp(20))],
	row_data = Teachers) 

	card.add_widget(f)
	modal = ModalView(

	size_hint=(0.95, 0.95),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(card)

	modal.open()
def get_part_of_day(h):
    return (
        "Morning"
        if 5 <= h <= 11
        else "Afternoon"
        if 12 <= h <= 17
        else "Evening"
        if 18 <= h <= 22
        else "Night"
    )
from datetime import datetime

class SRAPS_APP(MDApp):
	Teachers = Teachers
	spacing = Window.size[1]//20
	time = get_part_of_day(datetime.now().hour)
	screen_manager = screen_manager
	NI="assets/no-internet.png"
	News="No Internet"
	time = lambda self:show_timings()
	fees = lambda self:show_fees()
	def colorHex(self, color):
		return get_color_from_hex(color)

	def build(self):
		screen_manager.add_widget(Builder.load_file('main.kv'))
		screen_manager.current = "Mscreen"
		return screen_manager
	def on_start(self):
		if check_intr() == True:
			update_data()
		else:
			show_message("true")

		os.system("rm assets/tmp-* ")
	def table(self):
		show_teachers("hy")

SRAPS_APP().run()
