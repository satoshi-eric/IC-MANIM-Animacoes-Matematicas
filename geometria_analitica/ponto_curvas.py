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
   
    def explicar_reta(self):
        def get_texto_coords(nome_conj: str, conj_coords: list) -> Text:
            coords_str = nome_conj + '={'
            index_final = len(conj_coords) - 1
            count = 0
            for i in range(index_final):
                if count >= 2:
                    coords_str += '\n' + conj_coords[i].__str__() + ','
                    count = 0
                else:
                    coords_str += conj_coords[i].__str__() + ','
                    count += 1
            if count >= 2:
                coords_str += '\n' + conj_coords[index_final].__str__() + '}'
            else:
                coords_str += conj_coords[index_final].__str__() + '}'
            text_coords = Text(coords_str).scale(0.5).move_to(2*UP + 4*RIGHT)
            return text_coords
        
        def get_pontos_de_coords(coords: list, eixos: Axes) -> list:
            pontos = [Dot(point=eixos.c2p(*coord)) for coord in coords]
            return pontos
        
        # ---------------------- Dados ----------------------
        play: Callable = self.play
        f = lambda x: int(0.5*x - 1)
        y = lambda x: 0.5*x - 1
        coords = [(-2, f(-2)), (0, f(0)), (2, f(2)), (1, 2), (1, -3), (-2, 1)]
        textos = self.m_textos
        label_x, label_y = self.plano.get_axis_labels(x_label='x', y_label='y')
        label_x.scale(0.7).shift(0.4*LEFT + 0.1*UP).set_color(BLUE_B)
        label_y.scale(0.7).shift(0.4*DOWN + 0.1*RIGHT).set_color(GREEN_B)
        
        # ---------------------- Mobjects ----------------------
        coords_text = get_texto_coords('A', coords)
        pontos: list[Dot] = get_pontos_de_coords(coords, self.plano)
        tex_eq_reta = MathTex('y=', 'a', 'x+', 'b').move_to(textos[5].get_center() + DOWN + 4*LEFT).scale(0.8)
        pontos_reta = VGroup(*[Dot().scale(0.5).set_color(RED_E).move_to(self.plano.c2p(i, y(i))) for i in np.arange(-4, 6, 0.5)])
        reta = Line(self.plano.c2p(-4, f(-4)), self.plano.c2p(6, f(6))).set_color(RED_D)
        angulo = Angle(self.plano.x_axis, reta, 1).set_color(YELLOW)
        tex_angulo = MathTex(r'\theta').move_to(angulo.get_center() + 0.4*RIGHT + 0.1*UP).set_color(YELLOW)
        linha_vertical = self.plano.get_vertical_line(self.plano.c2p(5, y(5)), line_func=Line).set_color(GREEN)
        linha_horizontal = Line(self.plano.c2p(2, 0), self.plano.c2p(5, 0)).set_color(PURPLE)
        delta_y_brace = Brace(linha_vertical, RIGHT)
        delta_x_brace = Brace(linha_horizontal, DOWN)
        delta_y_tex = MathTex('\Delta y').next_to(delta_y_brace, RIGHT).scale(0.7).set_color(GREEN)
        delta_x_tex = MathTex('\Delta x').next_to(delta_x_brace, DOWN).scale(0.7).set_color(PURPLE)
        delta_y_x = MathTex(r'tg \theta =', '{\Delta y', '\over', '\Delta x}', '=', 'a').move_to(3*RIGHT + 2.5*DOWN).scale(0.8)
        coef_linear_eixo = self.plano.y_axis.get_number_mobject(-1)
        coef_angular = VGroup(MathTex(r'\rightarrow').rotate(270*DEGREES).next_to(tex_eq_reta[1], DOWN, buff=0.2), Text('coeficiente angular').move_to(tex_eq_reta[1].get_center() + LEFT + DOWN).scale(0.4).set_color(YELLOW))
        coef_linear = VGroup(MathTex(r'\rightarrow').rotate(270*DEGREES).next_to(tex_eq_reta[3], DOWN, buff=0.2), Text('coeficiente linear').move_to(tex_eq_reta[3].get_center() + 0.9*RIGHT + DOWN).scale(0.4).set_color(ORANGE))
        
        # ---------------------- Animações ----------------------
        self.add(self.plano)
        self.add(label_x, label_y)
        play(Write(textos[2]))
        play(Write(coords_text))
        play(ReplacementTransform(coords_text[3 :10].copy(), pontos[0]))
        play(ReplacementTransform(coords_text[11:17].copy(), pontos[1]))
        play(ReplacementTransform(coords_text[18:23].copy(), pontos[2]))
        play(ReplacementTransform(coords_text[24:29].copy(), pontos[3]))
        play(ReplacementTransform(coords_text[30:36].copy(), pontos[4]))
        play(ReplacementTransform(coords_text[37:43].copy(), pontos[5]))
        play(FadeOut(textos[2]))
        play(Write(textos[3]))
        play(coords_text[3 :10].animate.set_color(RED_E), pontos[0].animate.set_color(RED_E))
        play(coords_text[11:17].animate.set_color(RED_E), pontos[1].animate.set_color(RED_E))
        play(coords_text[18:23].animate.set_color(RED_E), pontos[2].animate.set_color(RED_E))
        play(Write(pontos_reta))
        play(ReplacementTransform(pontos_reta, reta))
        play(FadeOut(textos[3]))
        play(Write(textos[4]))
        play(FadeOut(textos[4]))
        play(Write(textos[5]))
        play(Write(tex_eq_reta))
        play(FadeIn(coef_angular))
        play(FadeIn(coef_linear))
        play(tex_eq_reta[1].animate.set_color(YELLOW))
        play(tex_eq_reta[3].animate.set_color(ORANGE))
        play(Write(angulo))
        play(Write(tex_angulo))
        play(Write(linha_vertical))
        play(Write(linha_horizontal))
        play(Write(delta_y_brace), Write(delta_y_tex))
        play(Write(delta_x_brace), Write(delta_x_tex))
        play(Write(delta_y_x[0]))
        play(ReplacementTransform(delta_y_tex.copy(), delta_y_x[1]))
        play(ReplacementTransform(delta_x_tex.copy(), delta_y_x[3]))
        play(FadeIn(delta_y_x[2]))
        play(FadeIn(delta_y_x[4]))
        play(FadeIn(delta_y_x[5]))
        play(ReplacementTransform(delta_y_x[5].copy(), tex_eq_reta[1]))
        play(ReplacementTransform(coef_linear_eixo.copy(), tex_eq_reta[3]))
        play(*[FadeOut(mobject) for mobject in self.mobjects if mobject != self.plano])


    def explicar_elipse(self):
        # ---------------------- Dados ----------------------
        textos = self.m_textos
        play: Callable = self.play
        c2p = self.plano.c2p
        a, b = 4, 3
        c = np.sqrt(a**2 - b**2) if a >= b else np.sqrt(b**2 - a**2)
        focos = [c2p(-c, 0), c2p(c, 0)] if a >= b else [c2p(0, c), c2p(0, -c)]
        
        # ---------------------- Mobjects ----------------------
        
        # ---------------------- plano ----------------------
        plano = self.plano
        label_x, label_y = self.plano.get_axis_labels(x_label='x', y_label='y')
        label_x.scale(0.7).shift(0.4*LEFT + 0.1*UP).set_color(BLUE_B)
        label_y.scale(0.7).shift(0.4*DOWN + 0.1*RIGHT).set_color(GREEN_B)
        # ---------------------- Elipse ----------------------
        m_elipse = Ellipse(
            (c2p(a, 0)[0] - c2p(0, 0)[0])*2,
            (c2p(0, b)[1] - c2p(0, 0)[1])*2
        ).move_to(c2p(0, 0))
        # ---------------------- focos ----------------------
        focos_text = Tex('Focos').scale(0.7).move_to(5*LEFT+2*UP)
        m_focos = VGroup(Dot(focos[0]), Dot(focos[1]))
        f1, f2 = m_focos
        f1_label = Tex('F1').move_to(f1.get_center() + 0.3*UP + 0.3*LEFT ).scale(0.6).set_color(ORANGE)
        f2_label = Tex('F2').move_to(f2.get_center() + 0.3*UP + 0.3*RIGHT).scale(0.6).set_color(MAROON)
        f1.set_color(ORANGE)
        f2.set_color(MAROON)
        # ---------------------- eixo maior ----------------------
        eixo_maior_text = Tex('Eixo maior').scale(0.7).move_to(5*LEFT+2*UP)
        comprimento_a = VGroup(
            Line(c2p(0, 0), c2p(-a, 0)), 
            Tex('a').next_to(Line(c2p(0, 0), c2p(-a, 0)), DOWN, 0.5).scale(0.8),
            Line(c2p(0, 0), c2p(a, 0)),
            Tex('a').next_to(Line(c2p(0, 0), c2p( a, 0)), DOWN, 0.5).scale(0.8),
        ).set_color(DARK_BLUE)
        # ---------------------- eixo menor ----------------------
        eixo_menor_text = Tex('Eixo menor').scale(0.7).move_to(5*LEFT+2*UP)
        comprimento_b = VGroup(
            Line(c2p(0, 0), c2p(0,  b)), 
            Tex('b').next_to(Line(c2p(0, 0), c2p(0,  b)), RIGHT, 0.5).scale(0.8),
            Line(c2p(0, 0), c2p(0, -b)),
            Tex('b').next_to(Line(c2p(0, 0), c2p(0, -b)), RIGHT, 0.5).scale(0.8),
        ).set_color(PURPLE)
        
        # ---------------------- c ----------------------
        comprimento_c = VGroup(
            Line(c2p(0, 0), focos[0]), 
            Tex('c').next_to(Line(c2p(0, 0), focos[0]), DOWN, 0.5).scale(0.8), 
            Line(c2p(0, 0), focos[1]),
            Tex('c').next_to(Line(c2p(0, 0), focos[1]), DOWN, 0.5).scale(0.8)
        ).set_color(YELLOW)

        # ---------------------- Equação c ----------------------
        eq_c1 = MathTex('a^2', '=', 'b^2', '+', 'c^2').scale(0.7).move_to(5*LEFT+2*UP)
        eq_c1[0].set_color(DARK_BLUE) # a^2
        eq_c1[2].set_color(PURPLE) # b^2
        eq_c1[4].set_color(YELLOW) # c^2
        
        eq_c2 = MathTex('-c^2', '=', 'b^2', '-a^2').scale(0.7).move_to(5*LEFT+1.5*UP)
        eq_c2[0].set_color(YELLOW) # -c^2
        eq_c2[2].set_color(PURPLE) # b^2
        eq_c2[3].set_color(DARK_BLUE) # -a^2
        
        eq_c3 = MathTex('c^2', '=', '-b^2', '+', 'a^2').scale(0.7).move_to(5*LEFT+1*UP)
        eq_c3[0].set_color(YELLOW) # c^2
        eq_c3[2].set_color(PURPLE) # -b^2
        eq_c3[4].set_color(DARK_BLUE) # a^2
        
        eq_c4 = MathTex('c^2', '=', 'a^2', '-b^2').scale(0.7).move_to(5*LEFT+0.5*UP)
        eq_c4[0].set_color(YELLOW) # c^2
        eq_c4[2].set_color(DARK_BLUE) # -b^2
        eq_c4[3].set_color(PURPLE) # a^2
        
        eq_c5 = MathTex('c', '=', '\sqrt{', 'a^2', '-b^2', '}').scale(0.7).move_to(5*LEFT+0*UP)
        eq_c5[0].set_color(YELLOW) # c^2
        eq_c5[3].set_color(DARK_BLUE) # -b^2
        eq_c5[4].set_color(PURPLE) # a^2
        
        # ---------------------- Equação da elipse ----------------------
        eq_elipse = MathTex('{x^2', '\over', 'a^2}', '+', '{y^2', '\over', 'b^2}', '=', '1').scale(0.7).move_to(5*LEFT+2*UP)
        eq_elipse[0].set_color(BLUE_B)
        eq_elipse[2].set_color(DARK_BLUE)
        eq_elipse[4].set_color(GREEN_B)
        eq_elipse[6].set_color(PURPLE)
        
        # ---------------------- Relação da elipse ----------------------
        relacao_elipse = MathTex(
            'dist(',  # 0
            'P',      # 1
            ',',      # 2
            'F1',     # 3
            ')',      # 4
            '+',      # 5
            'dist(',  # 6
            'P',      # 7
            ',',      # 8  
            'F2',     # 9  
            ')',      # 10
            '=',      # 11
            '2',      # 12
            'a'       # 13
        ).scale(0.6).move_to(2.5*UP + 4*RIGHT)
        relacao_elipse[1].set_color(GOLD)
        relacao_elipse[3].set_color(ORANGE)
        relacao_elipse[7].set_color(GOLD)
        relacao_elipse[9].set_color(MAROON)
        relacao_elipse[13].set_color(DARK_BLUE)
        
        # relacao_elipse_algebrica = MathTex(
        #     '\\sqrt{(', # 0     
        #     'x',        # 1
        #     '+',        # 2
        #     'c',        # 3   
        #     ')^2 - (',  # 4  
        #     'y',        # 5 
        #     '- 0)^2}',  # 6
        #     '+',        # 7
        #     '\\sqrt{('  # 8
        #     'x',        # 9
        #     '-',        # 10
        #     'c',        # 11
        #     ')^2 - (',  # 12    
        #     'y',        # 13
        #     '- 0)^2}',  # 14  
        #     '= 2',      # 15
        #     'a'         # 16
        # ).scale(0.6).move_to(2*UP + 4*RIGHT)
        # relacao_elipse_algebrica[1].set_color(BLUE_B)
        # relacao_elipse_algebrica[9].set_color(BLUE_B)
        # relacao_elipse_algebrica[3].set_color(YELLOW)
        # relacao_elipse_algebrica[11].set_color(YELLOW)
        # relacao_elipse_algebrica[5].set_color(GREEN_B)
        # relacao_elipse_algebrica[13].set_color(GREEN_B)
        # relacao_elipse_algebrica[15].set_color(DARK_BLUE)
        
        # ---------------------- ponto ----------------------
        ponto_exemplo = Dot(m_elipse.point_from_proportion(0.35)).set_color(GOLD)
        ponto_exemplo_label = Tex('P').scale(0.6).move_to(ponto_exemplo.get_center() + 0.3*LEFT + 0.3*UP).set_color(GOLD)
        linha_f1 = Line(f1.get_center(), ponto_exemplo.get_center())
        linha_f2 = Line(f2.get_center(), ponto_exemplo.get_center())
        
        # ---------------------- Aimação do ponto seguindo a elipse ----------------------
        self.offset = 0
        ponto = Dot(m_elipse.point_from_proportion(self.offset)).set_color(GOLD)
        linha1 = Line(f1, ponto)
        linha2 = Line(f2, ponto)
        ponto_label = MathTex('P').scale(0.6).move_to(ponto.get_center() + 0.3*UP + 0.3*RIGHT)
                       
        # ---------------------- Animações ----------------------        
        self.add(plano, label_x, label_y)
        play(Write(textos[6]))
        play(Write(m_elipse))
        play(FadeOut(textos[6]))
        play(Write(textos[7]))
        play(Write(focos_text))
        play(ReplacementTransform(focos_text, VGroup(m_focos, f1_label, f2_label)))
        play(Write(comprimento_c))
        play(Write(eixo_maior_text))
        play(ReplacementTransform(eixo_maior_text, comprimento_a))
        play(comprimento_a.animate.shift((c2p(0, b)[1] - c2p(0, 0))*DOWN))
        play(Write(eixo_menor_text))
        play(ReplacementTransform(eixo_menor_text, comprimento_b))
        play(comprimento_b.animate.shift((c2p(a, 0)[0] - c2p(0, 0))*RIGHT))
        play(FadeOut(comprimento_a[2:4]), FadeOut(comprimento_b[2:4]), FadeOut(comprimento_c[2:4]))
        play(comprimento_b[0:2].animate.shift((c2p(a, 0)[0] - c2p(0, 0))*LEFT),)
        play(Transform(comprimento_a[0:2], VGroup(Line(c2p(-c, 0), c2p(0, b)), Tex('a').move_to(0.9*UP+1.7*LEFT)).set_color(DARK_BLUE)))
        
        play(ReplacementTransform(comprimento_a[1].copy(), eq_c1[0]))
        play(ReplacementTransform(comprimento_b[1].copy(), eq_c1[2]))
        play(ReplacementTransform(comprimento_c[1].copy(), eq_c1[4]))
        play(FadeIn(eq_c1[1]), FadeIn(eq_c1[3]))    
      
        # # # eq_c1 -> eq_c2
        play(FadeIn(eq_c2[1]))
        play(ReplacementTransform(eq_c1[0].copy(), eq_c2[3]))
        play(ReplacementTransform(eq_c1[2].copy(), eq_c2[2]))
        play(ReplacementTransform(eq_c1[4].copy(), eq_c2[0]))
        
        # # # eq_c2 -> eq_c3
        play(FadeIn(eq_c3[1], eq_c3[3]))
        play(ReplacementTransform(eq_c2[0].copy(), eq_c3[0]))
        play(ReplacementTransform(eq_c2[2].copy(), eq_c3[2]))
        play(ReplacementTransform(eq_c2[3].copy(), eq_c3[4]))
    
        # # # eq_c3 -> eq_c4
        play(FadeIn(eq_c4[1]))
        play(ReplacementTransform(eq_c3[0].copy(), eq_c4[0]))
        play(ReplacementTransform(eq_c3[2].copy(), eq_c4[3]))
        play(ReplacementTransform(eq_c3[4].copy(), eq_c4[2]))
        
        # # # eq_c4 -> eq_c5
        play(FadeIn(eq_c5[1], eq_c5[2], eq_c5[5]))
        play(ReplacementTransform(eq_c4[0].copy(), eq_c5[0]))
        play(ReplacementTransform(eq_c4[2:5].copy(), eq_c5[3:5]))
        play(FadeOut(eq_c1, eq_c2, eq_c3, eq_c4), eq_c5.animate.shift(1*UP))
        
        play(FadeOut(textos[7]))
        play(Write(textos[8]))
        play(Write(eq_elipse))
        play(ReplacementTransform(comprimento_a[1].copy(), eq_elipse[2]))
        play(ReplacementTransform(comprimento_b[1].copy(), eq_elipse[6]))
        play(FadeOut(textos[8]))
        play(Write(textos[9]))
        play(Write(relacao_elipse))
        
        play(FadeOut(comprimento_a[0:2], comprimento_b[0:2], comprimento_c[0:2]))
        play(FadeIn(ponto_exemplo, ponto_exemplo_label))
        play(ReplacementTransform(relacao_elipse[1].copy(), ponto_exemplo))
        play(ReplacementTransform(relacao_elipse[3].copy(), m_focos[0]))
        play(ReplacementTransform(relacao_elipse[7].copy(), ponto_exemplo))
        play(ReplacementTransform(relacao_elipse[9].copy(), m_focos[1]))
        play(Write(linha_f1))
        play(Write(linha_f2))
        
        # ---------------------- Animação do ponto com as retas seguindo  ----------------------
        
        play(FadeOut(ponto_exemplo, ponto_exemplo_label, linha_f1, linha_f2))
        play(FadeIn(ponto))
        play(Write(linha1))
        play(Write(linha2))
        play(Write(ponto_label))
        
        def ponto_updater(mob: Mobject, dt: float):
            if self.offset < 1:
                self.offset = round(self.offset + 0.01, 2)
                mob.move_to(m_elipse.point_from_proportion(self.offset % 1))

        def linha1_updater(mob: Mobject, dt: float):
            mob.become(Line(f1.get_center(), ponto))
        
        def linha2_updater(mob: Mobject, dt: float):
            mob.become(Line(f2.get_center(), ponto))
        
        def ponto_label_updater(mob: Mobject, dt:float):
            mob.move_to(ponto.get_center() + 0.3*UP + 0.3*RIGHT)

        ponto.add_updater(ponto_updater)
        linha1.add_updater(linha1_updater)
        linha2.add_updater(linha2_updater)
        ponto_label.add_updater(ponto_label_updater)
        
        self.wait(8)
        
        # print([mob for mob in self.mobjects if mob != self.plano])
        play(*[FadeOut(mob) for mob in self.mobjects if mob != plano])
    
        



def main():
    ARQ_NOME = Path(__file__).resolve()
    CENA = CenaPontoCurvas.__name__
    ARGS = '-pql'

    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')


if __name__ == '__main__':
    main()