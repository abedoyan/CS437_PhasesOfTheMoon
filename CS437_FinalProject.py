# Arda Bedoyan
# Final Project
# CS437 Internet of Things

# Code based off of and influenced by code from Henner Zeller 
# https://github.com/hzeller/rpi-rgb-led-matrix.git

#!/usr/bin/env python
import time
import sys
import requests

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
from bs4 import BeautifulSoup


# Web scraping to get the current phase of the moon

# Making a GET request
get_site = requests.get('https://www.moongiant.com/phase/today/')
 
# Parsing the HTML
soup = BeautifulSoup(get_site.content, 'html.parser')

# Finding the part of the website where the moon's phase is listed
today_phase = soup.find('td', id='today_')
phase_text = today_phase.text

# Extracting the phase from the website text
# and setting the image and text based off of the results
if 'New Moon' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/NewMoon.jpeg"
    moon_phase = 'New Moon'
elif 'Waxing Crescent' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/WaxingCrescent.jpeg"
    moon_phase = 'Waxing Crescent'
elif 'First Quarter' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/FirstQuarter.jpeg"
    moon_phase = 'First Quarter'
elif 'Waxing Gibbous' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/WaxingGibbous.jpeg"
    moon_phase = 'Waxing Gibbous'
elif 'Full Moon' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/FullMoon.jpeg"
    moon_phase = 'Full Moon'
elif 'Waning Gibbous' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/WaningGibbous.jpeg"
    moon_phase = 'Waning Gibbous'
elif 'Last Quarter' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/Last Quarter.jpeg"
    moon_phase = 'Last Quarter'
elif 'Waning Crescent' in phase_text:
    image_file = "/home/arda/Pictures/MoonPhases/WaningCrescent.jpeg"
    moon_phase = 'Waning Crescent'
else:
    image_file = "/home/arda/Pictures/Earth"
    moon_phase = "Hi Arda!"

# Convert to an image file that will be compatible with the LED matrix
image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.gpio_slowdown = 4
options.chain_length = 1
options.parallel = 1
options.brightness = 100
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit the matrix
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

# Initialize variables needed to print text on the matrix
canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor1 = graphics.Color(0, 255, 0)
textColor2 = graphics.Color(128, 0, 128)
textColor3 = graphics.Color(0, 0, 255)
pos = canvas.width
time_text = "   " + time.strftime("%I:%M")
date_text = time.strftime("%m/%d/%Y")


# Running the code
try:
    print("Press CTRL-C to stop.")
    
    while True:
        counter = 0
        
        # Image of the phase of the moon
        while (counter < 100):
            time.sleep(0.075)
            matrix.SetImage(image.convert('RGB'))
            counter += 1
        
        # Scrolling text of the phase of the moon
        while (counter < 360):
            canvas.Clear()
            len = graphics.DrawText(canvas, font, pos, 20, textColor3, moon_phase)
            pos -= 1
            
            if (pos + len < 0):
                pos = canvas.width
                
            time.sleep(0.075)
            canvas = matrix.SwapOnVSync(canvas)
            counter += 1
        
        # Scrolling text of the date and time
        while (counter < 565):
            canvas.Clear()
            len1 = graphics.DrawText(canvas, font, pos, 13, textColor1, date_text)
            len2 = graphics.DrawText(canvas, font, pos, 28, textColor2, time_text)
            pos -= 1
            
            if (pos + len1 < 0):
                pos = canvas.width
                
            time.sleep(0.075)
            canvas = matrix.SwapOnVSync(canvas)
            counter += 1
        
        # Image of the globe for fun
        while (counter < 620):
            time.sleep(0.075)
            image2 = Image.open("/home/arda/Pictures/Earth")
            image2.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
            matrix.SetImage(image2.convert('RGB'))
            counter += 1


except KeyboardInterrupt:
    sys.exit(0)

