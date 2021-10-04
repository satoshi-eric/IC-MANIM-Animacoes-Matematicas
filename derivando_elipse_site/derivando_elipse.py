from manim import *
from pathlib import Path
import os

class DerivandoElipse(Scene):
    def construct(self):
        self.config_textos()
        self.propriedades_elipse()

    def config_textos(self):
        dir_str = os.path.dirname(__file__).__str__()
        caminho = dir_str + '\\textos.txt'
        with open(caminho, 'r', encoding='utf8') as f:
            self.textos = f.readlines()
        self.m_textos = [
            self.format_text(texto)
            for texto in self.textos
        ]

    def propriedades_elipse(self):
        # ---------------------- Funções auxiliares ----------------------
        def play(anim: Animation, time: float=1):
            self.play(anim)
            self.wait(time)
        
        # ---------------------- Dados ----------------------
        a, b = 3, 1
        c: float
        focos: list
        if a >= b: 
            c = float(np.sqrt(a**2 - b**2))
            focos = [(-c, 0), (c, 0)]
        else:
            c = float(np.sqrt(b**2 - a**2))
            focos = [(0, -c), (0, c)]
        
        # ---------------------- Mobjects ----------------------     
        m_eixos = Axes()
        m_focos = Dot(m_eixos.c2p(*focos[0])), Dot(m_eixos.c2p(*focos[1]))
        

        # ---------------------- Animações ----------------------



ARQ_NOME = Path(__file__).resolve()
CENA = DerivandoElipse.__name__
ARGS = '-pql'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')