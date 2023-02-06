import numpy as np
import math

class SVM:
    def __init__(self) -> None:
        self.losses_stack = []
        self.loss = 0

    def addSVMLoss(self, scores, y):
        s_y = scores[y]
        self.losses_stack.append(np.sum(np.array([max(0, s - s_y +1) for s in scores if s != s_y])))

    def getMultiSVMLoss(self):
        self.loss = np.mean(self.losses_stack)
        return self.loss

    def reset(self):
        self.__init__()