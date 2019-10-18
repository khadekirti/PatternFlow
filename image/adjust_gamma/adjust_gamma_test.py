#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 02:02:27 2019

@author: khadekirti
"""


#import os 
#os.chdir('/Users/khadekirti/Desktop/PRP2/PatternFlow/exposure/adjust_gamma')

from  adjust_gamma import adjust_gamma
from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt 

# First - Test a normal 
image = img_as_float(data.moon()) 
im = adjust_gamma(image, 2) 


# Second - if negative 
image = img_as_float(data.moon()) 
image[0] = -1
try: 
    im = adjust_gamma(image, 2) 
except ValueError: 
    print("Passed")   
    
# Second - if image is negative  
image = img_as_float(data.moon()) 
image[0] = -1
try: 
    im = adjust_gamma(image, 2) 
except ValueError: 
    print("Passed")       
    
    
# Third - if gamma is negative  
image = img_as_float(data.moon()) 
try: 
    im = adjust_gamma(image, -2) 
except ValueError: 
    print("Passed")            