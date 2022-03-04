

__version__ = "1.0.0"


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
from kivy.uix.carousel import Carousel
from kivymd.uix.expansionpanel import *
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
screen_manager = ScreenManager()
if platform != "android":
	Window.size =(360,640)
	
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


dialo = ["yes"]
	
def show_message(Ok):
	if dialo[-1] is "yes":
		print(dialo)
		dialog=Snackbar(text="No Internet!",
		snackbar_x="10dp",

		radius=[30,30,30,30],
		snackbar_y="10dp",
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
	

class SRAPS_APP(MDApp):
	screen_manager = screen_manager
	NI="assets/no-internet.png"
	News="No Internet"
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

SRAPS_APP().run()
