import gtk.gdk, time, os
from PIL import Image
import pyautogui
import cv2
import numpy as np

def screencap():
	try:
		img_width = gtk.gdk.screen_width()
		img_height = gtk.gdk.screen_height()

		screencap = gtk.gdk.Pixbuf(
			gtk.gdk.COLORSPACE_RGB,
			False,
			8,
			img_width,
			img_height
	)

		screencap.get_from_drawable(
			gtk.gdk.get_default_root_window(),
			gtk.gdk.colormap_get_system(),
			0, 0, 0, 0,
			img_width,
			img_height
	)

	except:
		print "Failed taking screenshot"
		exit()
	
	pixbuf = screencap.get_pixels()
#	nparr = np.fromstring(screencap.get_pixels(), np.uint8).reshape(img_height, 
#																	img_width,
#																	screencap.get_rowstride())
	nparr = np.fromstring(pixbuf, np.uint8)
	img_cv2 = cv2.imdecode(nparr, 1)

	final_screencap = Image.frombuffer(
		"RGB",
		(img_width, img_height),
		screencap.get_pixels(),
		"raw",
		"RGB",
		screencap.get_rowstride(),
		1
	)
	return final_screencap

i=0
s = screencap()
while (True):
	time.sleep(0.9)
	s = screencap()
	newfile = False
	while (newfile == False):
		path = '/home/nick/487/autocraft/neg/' + str(i) + '.png'
		if os.path.isfile(path):
			print(str(i))
			i += 1
			continue
		else:
			newfile = True
			s.save(path, 'png')

