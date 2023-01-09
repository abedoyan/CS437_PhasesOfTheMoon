# LED Matrix that Displays the Phases of the Moon

The goal of this project was to create a device that would light up in a way to mimic the phase of the moon every night. I ultimately decided on using an Adafruit LED matrix that connected to a Raspberry Pi 4 Model B and had code written in Python.

To start, git clone this repository: https://github.com/hzeller/rpi-rgb-led-matrix.git

Then you can run the python file. Update the code if using something other than an Adafruit Bonnet to connect the Raspberry Pi and the LED Matrix.

# Video Link:

https://uofi.box.com/s/s8dnggog1drr0w6njnflqorwu4n3w48c

https://drive.google.com/file/d/18FaXHNdpikIwiY9UzZFiFeFhmNT71YvS/view?usp=sharing


# Motivation:

When the Covid-19 pandemic first pushed us into lockdown over two and a half years ago, I,
along with many other folks, started noticing the difficulties of being homebound. Now with a
grandparent who is not able to go outside, I understand how terrible it can be to not see and enjoy
the simple pleasures of the outdoors. I constantly find myself looking out my window to catch a
peak of the moon and check on what phase of the moon cycle it is in. It is a simple task, but one
that brings me joy when I do get to see the moon and marvel at the incredible vastness and
beauty of outer space. However, sometimes I find myself not catching a glimpse of the moon,
even when I do go out to look for it.

My project therefore, was to have some sort of replica of the moon, that would illuminate in a
way that would show the current phase of the moon every night. I decided to use an LED matrix
to display the image of the moon, along with text like the current phase, the date, and the time.
An LED matrix works better for the task of displaying text than many individual light bulbs, and
therefore, I decided that it was the best tool to accomplish this project.

By the end of this project, I had a device that illuminates and mimics the phases of the moon, and
could act as a night light, a tool to fuel astronomical curiosity, or even something simply meant
to connect us with nature when we can’t see it.

The main sources I used to complete this project are listed below.

● https://github.com/hzeller/rpi-rgb-led-matrix

● https://moon.nasa.gov/moon-in-motion/moon-phases/

● https://www.moongiant.com/phase/today/


# Technical Approach:

In order to tackle this project, I first did some research on the different ways of implementing my
goal. I was initially leaning towards using an Arduino microcontroller and connecting multiple
individual light bulbs to it via a breadboard. The idea was to arrange the LED lights in a circular
pattern to form a half sphere, which would light up to mimic the phases of the moon. However,
after some time, I realized that the number of lights I would need and the questions around
voltage issues that I had were reasons to look for a different solution.

Already having a Raspberry Pi 4, I found various LED matrixes that were compatible with
Raspberry Pi’s. I decided to use the Adafruit 32x32 RGB LED matrix, which connected to an
Adafruit RGB matrix bonnet that would sit on the Raspberry Pi like a hat module. Additionally, I
bought a 5V 4A power supply and a 2.1mm power adapter.

Once I had all of the supplies needed to get started, I assembled the LED matrix. This involved
placing the bonnet on top of the pins on the Raspberry Pi and then connecting the matrix to the
bonnet via a cable that came with the matrix. Then I connected the wires to supply power to the
matrix and added the 2.1mm jack to the end of it, which then connected to the 5V power supply.
Once the matrix was connected and plugged in, I also plugged in a power source to the
Raspberry Pi. Then I was ready to start coding my program.

The code for the project is written in Python and was based off of the code from a GitHub
repository from Henner Zeller (https://github.com/hzeller/rpi-rgb-led-matrix). After the
repository was git cloned onto my machine, I explored the different functionalities to understand
what would help me solve my problem. The main two sources from the repository that I referred
to for my project were the image-viewer.py and the runtext.py files. I will go more into detail on
how I used these sources in my code in the Implementation section.

Ultimately, once the matrix, bonnet, and Pi were connected, it was just a matter of cloning the
GitHub repo and having the data flow from the Raspberry Pi to the LED matrix.

# Implementation:

As a reminder, I based my code off of Python code found in this GitHub repository:
https://github.com/hzeller/rpi-rgb-led-matrix. In particular, what I decided on doing was to show
an image of the current phase of the moon on the matrix, then show text saying what phase it is,
then show text of the date and time, and finally reshow the image of the moon in a continuous
loop. Ultimately, I decided to have the text portion of the project scroll on the matrix, because the
text was cutting off and was too large to fit on the 32x32 matrix.

The first step was to collect images of the moon that I wanted to light up on the matrix. I brushed
up on my knowledge of the moon cycle through NASA’s website
(https://moon.nasa.gov/moon-in-motion/moon-phases/) and pulled the images for the phases of
the moon from there. The NASA images are actual pictures of the moon and not drawings, and
therefore, when they appear on the matrix they do not look like plain white circles. I preferred
the imperfection of showing the actual pictures on the matrix because nature itself is imperfect.
The next step was to learn how to display images and text on the LED matrix. I imported the
rgbmatrix library and the Image library to be able to operate the matrix. The image-viewer.py
sample file from GitHub helped me to understand how to display any image saved to my
computer on the matrix. I updated some of the options to include a GPIO slowdown and to be
compatible with the bonnet. I also set the image file to be a path to the saved image on my
computer that I needed. The scrolling text on the matrix was influenced by the runtext.py file. I
modified the code to be able to display two different lines of text and to scroll for the entire
length of the longer line of text. The texts I wanted to display were the moon phase, the date, and
the time.

Before I could put everything together, I needed some way to know what phase the moon was in
every night. This problem was solved by web scraping. Web scraping was new to me, as I had
never had to do anything similar in the past. I spent a while researching web scraping and image
scraping to understand how to use it for my task at hand. I learned that I could not perform web
scraping on the NASA website, so instead, I found another site that displays the daily phase of
the moon (https://www.moongiant.com/phase/today/). Uponing inspecting the site, I initially
attempted to use image scraping to get the picture of the moon in its current phase and display
that on the matrix. However, due to the way the site stored its images, I was only able to pull in
the names of the image files, and not the link to the images. After many different attempts, I
decided that it would be better to pull in the text of the moon’s phase and display the NASA
moon images that I had saved based off of the web scraped text. I used the requests library to
make a Get request to the website and then I used BeautifulSoup for the actual web scraping
portion. Upon inspecting the website, I found that the moon’s daily phase was under the block of
code for “today_”. Then I pulled in only the text that fell under that section of the site’s code.
The code I wrote for this may appear simple in my final program, but it does not show just how
much time I spent troubleshooting and trying to understand how to pull only the important
information I needed. As a web scraping novice, this project showed me all the possibilities of
web scraping.

Once all the individual parts were figured out, it was finally time to piece them all together. After
I got the moon’s phase by web scraping, I used if statements to figure out which of the eight
phases of the moon it was. This determined the text and image to be displayed on the matrix.
Afterwards, I initialized the matrix to be able to display the moon’s image. I also added in the
code to display the text, including font, text color, and the current date and time in text form. I
added a while loop with a counter to be able to loop through the moon’s image and the text. I
found that a counter was a simple, yet effective way to maintain a continuous loop. Upon a
keyboard interrupt, the program stops and the matrix will stop displaying any content.

Additional Sources:

https://www.geeksforgeeks.org/image-scraping-with-python/

https://www.geeksforgeeks.org/python-web-scraping-tutorial/


# Results:

Overall, I am very happy with how the project turned out. I was initially skeptical that I would be
able to make a project that lit up in the exact shape of the moon every night, but through a lot of
research, I realized that it was not only possible, but that there were multiple ways of doing it.

I successfully got the matrix to read in the moon’s phase and display the correct image and text
based off of that. I also added a date and time feature that I had not initially planned for, because
I believe that people who will find use in this project will also want to use it as a clock. The
images I used for the moon phases would flicker a bit when they were being displayed on the
screen, but as noted earlier, I thought that the flicker added a nice effect to the results. This
flicker was most likely happening because I chose pictures of the moon that were very detailed
and more difficult to be displayed clearly on a small 32x32 matrix. Overall, I liked how the
screen display would loop and so viewers can continuously see the results of the program.

One initial design plan that did not come to fruition was a light sensor. I had originally wanted to
have the matrix turn on when it sensed that the environment it was in was dark. However, after
spending time understanding how to get the rest of the program to function, I was not left with
enough time to add a light-detection feature. Ultimately, I believe that this was for the best,
because sometimes someone may be in a lit room and still want to see the display of the matrix. I
do not want to limit the time that the matrix is on, so the display can be viewed at all times, in all
environments.

The most difficult part was understanding how to have the image viewer and scrolling text
features work together and not interfere with each other. I am very proud of my results,
especially because I worked on this project on my own and was able to accomplish what I had
envisioned. I worked on the project over the course of several weeks to truly ingest the topics
and skills I was learning about. For instance, this project taught me about web scraping and
improved my Python programming skills. I did not have a strong programming background
before starting this masters program, and so each new project I complete equates to new lessons
and skills learned.
