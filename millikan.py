# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:50:02 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*

interactive(True)
close('all')



class OilDrop(object):
    
    temperature = 25        # Celsius
    pressure = 1            # Atm
    density = 871           # kg/m**3
    fall_d = 0.5            # mm
    rise_d = 0.5            # mm
    
    def __init__(self, fall_time, rise_time, tension):
        

        self.fall_t = fall_time             # second
        self.rise_t = rise_time             # second
        self.tension = tension              # Volt
        self.fall_v, self.rise_v = speed()  # mm/s
        
    def speed(self):
        
        fall_speed = fall_d / self.fall_t
        rise_speed = rise_d / self.rise_t
        return fall_speed, rise_speed