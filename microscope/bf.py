# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm

import pytesseract

# importing OpenCV
import cv2
from PIL import ImageGrab
from PIL import Image
import pyautogui
import random
import time
import itertools
import os
from tqdm import tqdm
pyautogui.FAILSAFE = True

numbers = '0123456789'
y = ''
pins = []
for c in itertools.product(numbers, repeat=4):
    pin = y+''.join(c)
    pins.append(pin)
random.shuffle(pins)
def imToString(box):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    cap = ImageGrab.grab(bbox=box)

    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
        lang='eng')
    return tesstr

#screenshot box
box = (1700, 604, 2050, 630)
pin_input_loc = ()
flag_box = ()
for pin in tqdm(pins):

    pyautogui.click(1369, 533)
    pyautogui.typewrite("%s" % pin)
    time.sleep(.1)
    pyautogui.click(1888, 576)
    result = imToString(box)
    # print(result.strip().lower())
    if "flag" in result.lower():
        print("Trying %s" % pin)
        print("FOUND FLAG?")
        print(result.strip().lower())
    if "{" in result.lower() and "}" in result.lower():
        print("Trying %s" % pin)
        print("FOUND FLAG?")
        print(result.strip().lower())
    pyautogui.typewrite(['backspace','backspace','backspace','backspace'])







