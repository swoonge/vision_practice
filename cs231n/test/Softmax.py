import numpy as np
import math

class Softmax:
    def __init__(self) -> None:
        self.p = 0
        self.loss = 0
        pass

    def calLoss(self, scores, y):
        self.p = math.exp(scores[y])/np.sum(np.exp(np.array(scores)))
        self.loss = -math.log10(self.p)
        return self.loss

    def reset(self):
        self.__init__()

# def main():
#     pass

# if __name__ == '__main__':
#     print("\n[start]\nnumpy version = " + np.__version__ + "\n")
#     main()