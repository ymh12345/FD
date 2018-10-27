# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
class source(object):
    def __init__(self, **source_para):
        if not source_para:
            self.__default_source()
        else:
            self.source_func = source_para.get("source_func")
            self.source_duration = source_para.get("source_duration")
            # plt.plot([t for t in np.arange(0, self.source_duration, 0.1)], [self.source_func(i) for i in np.arange(0, self.source_duration, 0.1)])
            # plt.savefig("source.jpg")
            # plt.clf
    def __default_source(self):
        self.source_func = self.__default_source_func
        self.source_duration = 1

    def __default_source_func(self, t):
        if t == 0:
            return 1
        else:
            return 0
        