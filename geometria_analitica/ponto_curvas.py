from typing import Callable
from manim import *
from pathlib import Path
import os


class CenaPontoCurvas(Scene):
    plano: Axes = Axes(
        x_range=[-6.9, 7, 1], 
        y_range=[-3.9, 4, 1],
        x_axis_config={
            # 'include_numbers': True,
            'font_size': 24,
            'color': BLUE_B
        },
        y_axis_config={
            # 'include_numbers': True,
            'font_size': 24,
            'color': GREEN_B
        }
    ).shift(0.5*DOWN)

    ###################### Ponto de Entrada #########################
    def construct(self):
        self.config_textos()
        # self.explicar_plano_ponto()
        # self.explicar_reta()
        # self.explicar_elipse()
        self.explicar_parabola()
    #################################################################    
        

    def config_textos(self):
        dir_str = os.path.dirname(__file__).__str__()
        caminho = dir_str + '\\textos.txt'
        with open(caminho, 'r', encoding='utf8') as f:
            self.textos = f.readlines()
        self.m_textos = [
            self.format_text(texto)
            for texto in self.textos
        ]
            
    def format_text(self, string: str) -> Text:
        tamanho_string = 80
        pos = 0
        if len(string) > tamanho_string:
            for i in range(tamanho_string, len(string), 1):
                if string[i] == ' ':
                    pos = i
                    break
            text1 = string[0:pos]
            text2 = string[pos+1:]
            text = text1 + '\n' + text2
        else:
            text = string
        return Text(text).scale(0.5).to_corner(UP)

    def explicar_plano_ponto(self, x: float = 3, y: float = 2):
        # ---------------------- Dados ----------------------
        play: Callable = self.play
        coords = (x, y)
        eixo_x: NumberLine = self.plano.x_axis
        eixo_y: NumberLine = self.plano.y_axis
        valor_coord_x, valor_coord_y = coords[0], coords[1] 
        ponto = self.plano.c2p(*coords)
        
        # ---------------------- Mobjects ----------------------
        num_eixo_x = eixo_x.get_number_mobject(valor_coord_x)
        num_eixo_y = eixo_y.get_number_mobject(valor_coord_y)
        textos = self.m_textos
        m_coord: Text = Text(coords.__str__(), t2c={'[1:2]': BLUE_B, '[3:4]': GREEN_B}).move_to(2*UP + 4*RIGHT).scale(0.7)
        linha_vertical = self.plano.get_vertical_line(ponto)
        linha_horizontal = self.plano.get_horizontal_line(ponto)
        m_ponto = Dot().move_to(self.plano.c2p(*coords))
        label_x, label_y = self.plano.get_axis_labels(x_label='x', y_label='y')
        label_x.scale(0.7).shift(0.4*LEFT + 0.1*UP).set_color(BLUE_B)
        label_y.scale(0.7).shift(0.4*DOWN + 0.1*RIGHT).set_color(GREEN_B)

        # ---------------------- Animações ----------------------

        # Animação do plano cartesiano e sua explicação
        play(Write(textos[0]))
        play(textos[0].animate.to_corner(UP))
        play(Write(self.plano), Write(label_x), Write(label_y), run_time=3)
        play(FadeOut(textos[0]))

        # Animação do ponto e sua explicação
        play(Write(textos[1]))
        play(FadeIn(m_coord))
        play(ReplacementTransform(m_coord[1].copy(), num_eixo_x))
        play(ReplacementTransform(m_coord[3].copy(), num_eixo_y))
        play(Write(linha_horizontal), Write(linha_vertical))
        play(FadeIn(m_ponto))
        play(
            FadeOut(textos[1]),
            FadeOut(m_coord),
            FadeOut(m_ponto),
            FadeOut(linha_horizontal),
            FadeOut(linha_vertical),
        )
   
    
        
        

def main():
    ARQ_NOME = Path(__file__).resolve()
    CENA = CenaPontoCurvas.__name__
    ARGS = '-pql'

    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')


if __name__ == '__main__':
    main()