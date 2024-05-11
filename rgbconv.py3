import math
from PIL import Image
import numpy as np


#name of file containing rgb values as a list
file = open(file-name,'r')
Lines = file.readlines()



tot = len(Lines[0])
op_c = 0
i = 0
pixels = []

#remove formatting and read in each rgb value 
while op_c < (tot-2):
	op_b = Lines[0].find("(",op_c,tot)
	op_c = Lines[0].find(")",op_b,tot)
	curr_rgb = Lines[0][(op_b+1):(op_c)]
	conv_rgb = curr_rgb.split(',')
	
	#comment out if already in 0-255 range
	r = math.ceil(float(conv_rgb[0]) * 255)
	g = math.ceil(float(conv_rgb[1]) * 255)
	b = math.ceil(float(conv_rgb[2]) * 255)
	
	pixels.append(r)
	pixels.append(g)
	pixels.append(b)

#convert to bytes
colors = bytes(pixels)
#convert to image with size W X H
img = Image.frombytes('RGB', (W, H), colors)
img.show()
img.save('hues.png')

