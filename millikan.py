# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:50:02 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*
#from numpy import genfromtxt

interactive(True)
close('all')



class OilDrop(object):
    
    temperature = 25                # Celsius
    pressure = 760                  # Torr
    density = 871                   # kg/m**3
    air_viscosity = 1.861598E-5     # kg/ms
    fall_d = 0.5/1000               # mm/1000 = m
    rise_d = 0.5/1000               # mm/1000 = m
    plate_separation = 6/1000       # mm/1000 = m
    
    def __init__(self, drop_parameters):
        
        drop_number = int(drop_parameters[0])
        fall_time = drop_parameters[1]
        rise_time = drop_parameters[2]
        tension = drop_parameters[3]
        
        self.number = drop_number
        self.fall_t = fall_time             # second
        self.rise_t = rise_time             # second
        self.tension = tension              # Volt
        self.fall_v, self.rise_v = self.speed()  # mm/s                        
        self.field = self.electric_field()
    def speed(self):
        
        fall_speed = self.fall_d / self.fall_t
        rise_speed = self.rise_d / self.rise_t

        return fall_speed, rise_speed
    
    def electric_field(self):
        
        E=self.tension / self.plate_separation
        
        return E

    def __add__(self, other):
        if self.tension == other.tension:
            return OilDrop(self.fall_t+other.fall_t, self.rise_t+other.rise_t, self.tension)
        else:
            print 'Not same tension'

#class OilDropAvg(OilDrop):
    
    #def __init__():

     
#def avarage_drop():
#    
#    return

data_table = genfromtxt('millikan_data.csv', delimiter=',')
previous = [0,0,0,0]
counter = 1
drop_avg = []
added = [0,0,0,0]
for row in data_table:
    if row[0] == previous[0] and row[3] == previous[3]:
        added = [row[0],row[1] + previous[1], row[2] + previous[2], row[3]]
#        print added
        counter += 1
        previous = added
    elif counter>1:
        added[1] /= counter 
        added[2] /= counter
#        print '\n'+str(counter)
#        print '\n'+str(added)+'\n'
        drop_avg.append(added)
        previous = row
        counter = 1
    else:
        drop_avg.append(list(row))
#        print 'i am here'
        previous=row

drop_list = []
for drop in drop_avg:
#    print drop
    drop_list.append(OilDrop(drop))