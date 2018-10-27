# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:41:59 2018

@author: mhyang
"""

import imageio
import os

def create_gif(image_list, gif_name):  
  
    frames = []  
    for image_name in image_list:  
        frames.append(imageio.imread(image_name))  
    # Save them as frames into a gif   
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.3)  
  
    return  
  
    
    