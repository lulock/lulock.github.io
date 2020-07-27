# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:27:05 2020

@author: Lulock
"""


from PIL import Image
import glob, os

size = 1024, 1024

# os.makedirs('../thumbs/')    
# new_dir = '../thumbs/'

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    # im.save(new_dir + file + "-thumbnail.png", "PNG")
    im.save(file + "-thumbnail.png", "PNG")