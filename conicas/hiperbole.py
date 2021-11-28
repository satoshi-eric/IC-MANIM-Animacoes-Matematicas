from manim import *
from matplotlib import pyplot as plt
import numpy as np
from typing import Callable, Tuple

class Hiperbole(VGroup):
    def __init__(
        self, 
        a: float = 2, 
        b: float = 1, 
        x_linspace: Tuple[int, int] = (-5, 5), 
        y_linspace: Tuple[int, int] = (-3, 3), 
        num_points: int = 50,
        **kwargs
    ):
        super().__init__(**kwargs)
        def m_point(coord: np.ndarray) -> np.ndarray:
            return np.append(coord, 0)

        x = np.linspace(*x_linspace, num_points)
        y = np.linspace(*y_linspace, num_points)
        x, y = np.meshgrid(x, y)

        self.__a = a
        self.__b = b
        
        hiperbole_plot = plt.contour(x, y, x**2/a**2 - y**2/b**2, [1])
        h_esq_plot = np.array(list(map(m_point, hiperbole_plot.allsegs[0][0])))
        h_dir_plot = np.array(list(map(m_point, hiperbole_plot.allsegs[0][1])))
        self.__h_esq, self.__h_dir = VGroup(), VGroup()
        
        for p_ini, p_fim in zip(h_esq_plot[0:-2], h_esq_plot[1:-1]):
            self.__h_esq.add(Line(p_ini, p_fim))

        for p_ini, p_fim in zip(h_dir_plot[0:-2], h_dir_plot[1:-1]):
            self.__h_dir.add(Line(p_ini, p_fim))

        self.add(self.__h_esq, self.__h_dir)

        self.__c = np.sqrt(a**2 + b**2)
        self.__f1 = np.array([self.__c, 0, 0])
        self.__f2 = np.array([-self.__c, 0, 0])


    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def f1(self):
        return self.__f1

    @property
    def f2(self):
        return self.__f2

    @property
    def hiperbola_esq(self):
        return self.__h_esq

    @property
    def hiperbola_dir(self):
        return self.__h_dir


from manim import *
from pathlib import Path
import os

class HiperboleCena(Scene):
    def construct(self):
        hiperbole = Hiperbole(a=2, b=1)
        self.add(hiperbole)

ARQ_NOME = Path(__file__).resolve()
CENA = HiperboleCena.__name__
ARGS = '-s'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')