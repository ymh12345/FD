import numpy as np
import glob
from FD1D import FD1D
from gif import create_gif
import os


def f(t):
    return np.power(np.sin(np.pi * t / 5), 2)
    #   if t == 1:
    #         return 1
    #   else:
    #        return 0

velocity_list = [4 for i in range(100)]
velocity_list[25:30] = [5 for i in range(5)]
velocity_list[70:75] = [3 for i in range(5)]


FD = FD1D(dx = 1,\
      dt = 0.1,\
      length = 100,\
      time_length = 30,\
      plot = True,\
      plot_interval = 1,\
      homogeneous = False,\
      velocity = velocity_list,\
      source_position = 50,\
      left_bc = "stress_free",\
      right_bc = "fixed",\
      source_func = f,
      source_duration = 5)

img_list = ["%s.jpg"%(int(t*0.1)) for t in range(10 ,300 ,10)]
create_gif(img_list, "1.gif")
# tmp = glob.glob(r"*.jpg")
# for i in tmp:
#       os.remove(i)