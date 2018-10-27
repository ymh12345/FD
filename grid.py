# -*- coding:utf-8 -*-
import numpy as np

class grid_1D(object):
    def __init__(self, dx, dt, homogeneous, length, time_length, velocity, source_position):
        self.homogeneous = homogeneous
        self.length = length
        self.time_length = time_length
        self.source_position = source_position / dx
        self.grid_1D = np.zeros((int(time_length / dt), int(length / dx)))
        self.velocity = np.zeros(int(length / dx))
        # build velocity matrix
        if self.homogeneous:
            self.velocity.fill(velocity) 
        else:
            self.velocity = np.array(velocity) 
     