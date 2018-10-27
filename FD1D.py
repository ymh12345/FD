# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from grid import grid_1D
from source import source 


class FD1D(object):
    def __init__(self, dx, dt, length, time_length, plot, plot_interval, homogeneous, velocity, source_position, left_bc, right_bc, **source_para):
        self.grid = grid_1D(dx, dt, homogeneous, length, time_length, velocity, source_position)
        self.source = source(**source_para)
        self.source_position = source_position
        self.dt = dt
        self.dx = dx
        self.left_bc = left_bc
        self.right_bc = right_bc
        self.plot = plot
        self.plot_interval = plot_interval
        self.length = length
        
        for t in np.arange(1, int(time_length/dt)):
            print("Processing : %ss"%(round(t*dt, 1)))
            if t == 1:
                self.grid.grid_1D[t, int(self.source_position / self.dx)] = self.source.source_func(t*dt)
                continue  

            for x in np.arange(1, int(length/dx) - 1):
                beta = self.grid.velocity[x]
                u_ij = self.grid.grid_1D[t - 1, x]
                u_ip1 = self.grid.grid_1D[t - 1, x + 1]
                u_jm1 = self.grid.grid_1D[t - 2, x]
                u_im1 = self.grid.grid_1D[t - 1, x - 1]
                self.grid.grid_1D[t, x] = ((beta * self.dt / self.dx) ** 2  * (u_ip1 - 2 * u_ij + u_im1)) + 2 * u_ij - u_jm1 
            # left boundary condition  
            if self.left_bc == "fixed":
                self.grid.grid_1D[t, 0] = 0
            elif self.left_bc == "stress_free":
                self.grid.grid_1D[t, 0] = self.grid.grid_1D[t, 1]
            else:
                self.grid.grid_1D[t, 0] = self.left_bc[t]
            # right boundary condition
            if self.right_bc == "fixed":
                self.grid.grid_1D[t, -1] = 0
            elif self.right_bc == "stress_free":
                self.grid.grid_1D[t, -1] = self.grid.grid_1D[t, -2]
            else:
                self.grid.grid_1D[t, -1] = self.left_bc[t]
            
            if t <= self.source.source_duration / dt:
                self.grid.grid_1D[t, int(self.source_position / self.dx)] = self.source.source_func(t*dt)


            if self.plot and t%(self.plot_interval/dt)==0:
                plt.ylim(-2, 2)
                plt.title("%s"%(int(t*dt)))
                plt.plot([x for x in np.arange(0, self.length, self.dx)], self.grid.grid_1D[t, :])
                plt.savefig(r"./%s.jpg"%(int(t*dt)))
                plt.clf()

