import gtk.gdk, time, os
import sys
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
		print("Failed taking screenshot")
		exit()
	
	img_arr = screencap.get_pixels_array()
	#img_arr = np.fromstring(pixbuf, np.uint8).reshape(img_height, img_width, ncolors)
	image = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
	return image

if __name__ == '__main__':
	cascPath = sys.argv[1]
	villagerCascade = cv2.CascadeClassifier(cascPath)
	while(True):
		image = screencap()
		villagers = villagerCascade.detectMultiScale(
			image,
			scaleFactor=1.1,
			minNeighbors=25,
			minSize=(50,80),
			)
		if len(villagers) > 0:
		#	for (x, y, w, h) in villagers:
		#		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		#	cv2.imshow("Villagers", image)
		#	cv2.waitKey(0)
			pyautogui.keyDown('b')
			time.sleep(0.1)

			pyautogui.keyUp('b')
		time.sleep(0.02)
