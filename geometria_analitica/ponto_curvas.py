''' 
TODO
1) Substituir
“para desenhar pontos, curvas utilizamos o plano cartesiano” 
por
“para representar pontos e curvas utilizamos o plano cartesiano” 
OK

2) Substituir
“Podemos desenhar um ponto no plano através de suas coordenadas” 
por
“Representamos um ponto usando suas coordenadas” 
OK

3) Substituir
“Podemos representar um conjunto de pontos” 
por
“Podemos representar também um conjunto de pontos” 
OK

4) No momento que vc indica o coeficiente linear (fazendo o -1 se mover para o lugar de b), seria possível antes aumentar o tamanho do onde cruza o eixo y para destacar o ponto  ?
OK

5) quando vc coloca a expressão dist(P,F1), etc, seria possível escrever D1 e F2 como F_1 e F_2 (com os números no sub-índice) ?
OK

6) Engraçado, mas tive a impressão que o segmento de reta entre o ponto P e r na parabola não está igual ao segmento entre P e F quando vc faz a animação variando a posição do ponto P ?
Não sei resolver

7) Acho que ao invés de usar “objeto” para falar da parábola, elipse e hipérbole, seria melhor usar “curva” mesmo. 
OK

8) acho que vc poderia indicar também P, F1, F2 nos pontos correspondentes da hipérbole como vc fez na elipse e parábola.
OK

9) No final, teria como remover o gráfico e ficar apenas com tela preta. Nela vc poderia colocar info sobre a produção como o seu nome como autor, referencia ao projeto do PIBIC (número) e meu nome como orientador, se der também colocar o símbolo da Unicamp e FT (como fizemos no vídeo o Explora).
OK

Outra coisa: seria possível alterar as flechas que representam os eixos do plano cartesiano para algo como -> e não como um triângulo todos preenchido ?

'''

from typing import Callable
from manim import *
from pathlib import Path
import os


class CenaPontoCurvas(Scene):
    plano: Axes = Axes(
        x_range=[-6.9, 6.9, 1], 
        y_range=[-3.25, 3.25, 1],
        x_axis_config={
            # 'include_numbers': True,
            'font_size': 24,
            'color': BLUE_B,
            'include_tip': False
        },
        y_axis_config={
            # 'include_numbers': True,
            'font_size': 24,
            'color': GREEN_B,
            'include_tip': False
        }
    ).shift(0.5*DOWN)

    def construct(self):
        self.config_textos()
        self.abertura()
        self.explicar_plano_ponto()
        self.explicar_reta()
        self.explicar_elipse()
        self.explicar_parabola()
        self.explicar_hiperbole()
        self.fechamento()
        
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
        wait = lambda x=1: self.wait(x)
        coords = (x, y)
        eixo_x: NumberLine = self.plano.x_axis
        eixo_y: NumberLine = self.plano.y_axis
        valor_coord_x, valor_coord_y = coords[0], coords[1] 
        ponto = self.plano.c2p(*coords)
        seta_x = MathTex('\\rightarrow').next_to(self.plano, RIGHT, -0.2).set_color(BLUE_B)
        seta_y = MathTex('\\rightarrow').rotate(90*DEGREES).next_to(self.plano, UP, -0.2).set_color(GREEN_B)
        
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
        play(Write(textos[0]), run_time=2)
        play(textos[0].animate.to_corner(UP))
        play(FadeIn(self.plano), FadeIn(seta_x), FadeIn(seta_y), FadeIn(label_x), FadeIn(label_y), run_time=3)
        play(FadeOut(textos[0]))
        wait()

        # Animação do ponto e sua explicação
        play(Write(textos[1]), run_time=2)
        wait()
        play(FadeIn(m_coord))
        wait()
        play(ReplacementTransform(m_coord[1].copy(), num_eixo_x), run_time=2)
        wait()
        play(ReplacementTransform(m_coord[3].copy(), num_eixo_y), run_time=2)
        wait()
        play(Write(linha_horizontal), Write(linha_vertical), run_time=2)
        play(FadeIn(m_ponto), run_time=3)
        wait()
        play(FadeOut(*[mob for mob in self.mobjects if mob != self.plano]))
   
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
        wait = lambda x=1: self.wait(x)
        seta_x = MathTex('\\rightarrow').next_to(self.plano, RIGHT, -0.2).set_color(BLUE_B)
        seta_y = MathTex('\\rightarrow').rotate(90*DEGREES).next_to(self.plano, UP, -0.2).set_color(GREEN_B)

        # ---------------------- Mobjects ----------------------
        coords_text = get_texto_coords('A', coords)
        pontos: list[Dot] = get_pontos_de_coords(coords, self.plano)
        tex_eq_reta = MathTex('y=', 'a', 'x+', 'b').move_to(textos[5].get_center() + DOWN + 4*LEFT).scale(0.8)
        pontos_reta = VGroup(*[Dot().scale(0.5).set_color(RED_E).move_to(self.plano.c2p(i, y(i))) for i in np.arange(-4, 6, 0.5)])
        reta = Line(self.plano.c2p(-4, f(-4)), self.plano.c2p(6, f(6))).set_color(RED_D)
        angulo = Angle(self.plano.x_axis, reta, 1).set_color(YELLOW)
        tex_angulo = MathTex(r'\theta').move_to(angulo.get_center() + 0.4*RIGHT + 0.1*UP).set_color(YELLOW)
        linha_vertical = self.plano.get_vertical_line(self.plano.c2p(5, y(5)), line_func=Line).set_color(GREEN).set_stroke(width=7)
        linha_horizontal = Line(self.plano.c2p(2, 0), self.plano.c2p(5, 0)).set_color(PURPLE).set_stroke(width=7)
        delta_y_brace = Brace(linha_vertical, RIGHT)
        delta_x_brace = Brace(linha_horizontal, DOWN)
        delta_y_tex = MathTex('\Delta y').next_to(delta_y_brace, RIGHT).scale(0.7).set_color(GREEN)
        delta_x_tex = MathTex('\Delta x').next_to(delta_x_brace, DOWN).scale(0.7).set_color(PURPLE)
        delta_y_x = MathTex(r'tg \theta =', '{\Delta y', '\over', '\Delta x}', '=', 'a').move_to(3*RIGHT + 2.5*DOWN).scale(0.8)
        coef_linear_eixo = self.plano.y_axis.get_number_mobject(-1)
        coef_angular = VGroup(MathTex(r'\rightarrow').rotate(270*DEGREES).next_to(tex_eq_reta[1], DOWN, buff=0.2), Text('coeficiente angular').move_to(tex_eq_reta[1].get_center() + LEFT + DOWN).scale(0.4).set_color(YELLOW))
        coef_linear = VGroup(MathTex(r'\rightarrow').rotate(270*DEGREES).next_to(tex_eq_reta[3], DOWN, buff=0.2), Text('coeficiente linear').move_to(tex_eq_reta[3].get_center() + 0.9*RIGHT + DOWN).scale(0.4).set_color(ORANGE))
        
        # ---------------------- Animações ----------------------
        self.add(self.plano, seta_x, seta_y)
        self.add(label_x, label_y)
        play(Write(textos[2]), run_time=2)
        wait()
        play(Write(coords_text), run_time=3)
        play(ReplacementTransform(coords_text[3 :10].copy(), pontos[0]), run_time=2)
        wait()
        play(ReplacementTransform(coords_text[11:17].copy(), pontos[1]), run_time=2)
        wait()
        play(ReplacementTransform(coords_text[18:23].copy(), pontos[2]), run_time=2)
        wait()
        play(ReplacementTransform(coords_text[24:29].copy(), pontos[3]), run_time=2)
        wait()
        play(ReplacementTransform(coords_text[30:36].copy(), pontos[4]), run_time=2)
        wait()
        play(ReplacementTransform(coords_text[37:43].copy(), pontos[5]), run_time=2)
        wait()
        play(FadeOut(textos[2]))
        play(Write(textos[3]), run_time=2)
        wait()
        play(coords_text[3 :10].animate.set_color(RED_E), pontos[0].animate.set_color(RED_E), run_time=2)
        wait()
        play(coords_text[11:17].animate.set_color(RED_E), pontos[1].animate.set_color(RED_E), run_time=2)
        wait()
        play(coords_text[18:23].animate.set_color(RED_E), pontos[2].animate.set_color(RED_E), run_time=2)
        wait()
        play(Write(pontos_reta), run_time=3)
        wait()
        play(ReplacementTransform(pontos_reta, reta), run_time=3)
        wait()
        play(FadeOut(textos[3]))
        play(Write(textos[4]), run_time=2)
        wait(3)
        play(FadeOut(textos[4]))
        play(Write(textos[5]))
        wait(3)
        play(Write(tex_eq_reta), run_time=3)
        wait()
        play(FadeIn(coef_angular), run_time=2)
        wait(2)
        play(FadeIn(coef_linear), run_time=2)
        wait(2)
        play(tex_eq_reta[1].animate.set_color(YELLOW))
        play(tex_eq_reta[3].animate.set_color(ORANGE))
        wait()
        play(Write(angulo), Write(tex_angulo))
        wait()
        play(FadeIn(linha_vertical))
        wait()
        play(FadeIn(linha_horizontal))
        wait()
        play(Write(delta_y_brace), Write(delta_y_tex))
        wait()
        play(Write(delta_x_brace), Write(delta_x_tex))
        play(Write(delta_y_x[0]))
        play(ReplacementTransform(delta_y_tex.copy(), delta_y_x[1]), run_time=2)
        play(ReplacementTransform(delta_x_tex.copy(), delta_y_x[3]), run_time=2)
        wait()
        play(FadeIn(delta_y_x[2]))
        play(FadeIn(delta_y_x[4]))
        play(FadeIn(delta_y_x[5]))
        play(ReplacementTransform(delta_y_x[5].copy(), tex_eq_reta[1]), run_time=3)
        wait()
        play(FadeIn(coef_linear_eixo))
        wait()
        play(coef_linear_eixo.animate.scale(2).set_color(ORANGE))
        play(coef_linear_eixo.animate.scale(0.5))
        wait()
        play(ReplacementTransform(coef_linear_eixo.copy(), tex_eq_reta[3]), run_time=3)
        wait()
        play(*[FadeOut(mobject) for mobject in self.mobjects if mobject != self.plano])

    def explicar_elipse(self):
        # ---------------------- Dados ----------------------
        textos = self.m_textos
        play: Callable = self.play
        c2p = self.plano.c2p
        a, b = 4, 3
        c = np.sqrt(a**2 - b**2) if a >= b else np.sqrt(b**2 - a**2)
        focos = [c2p(-c, 0), c2p(c, 0)] if a >= b else [c2p(0, c), c2p(0, -c)]
        wait = lambda x=1: self.wait(x)

        # ---------------------- Mobjects ----------------------
        seta_x = MathTex('\\rightarrow').next_to(self.plano, RIGHT, -0.2).set_color(BLUE_B)
        seta_y = MathTex('\\rightarrow').rotate(90*DEGREES).next_to(self.plano, UP, -0.2).set_color(GREEN_B)
        
        
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
            'F_1',     # 3
            ')',      # 4
            '+',      # 5
            'dist(',  # 6
            'P',      # 7
            ',',      # 8  
            'F_2',     # 9  
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

        relacao_elipse2 = MathTex(
            'D_1',
            '+',      
            'D_2',     
            '=',      
            '2',      
            'a'       
        ).scale(0.6).move_to(2.5*UP + 4*RIGHT)
        relacao_elipse2[5].set_color(DARK_BLUE)
        
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
        self.add(plano, label_x, label_y, seta_x, seta_y)
        play(Write(textos[6]), run_time=2)
        wait()
        play(Write(m_elipse), run_time=2)
        wait()
        play(FadeOut(textos[6]))
        play(Write(textos[7]), run_time=2)
        wait()
        play(Write(focos_text))
        wait()
        play(ReplacementTransform(focos_text, VGroup(m_focos, f1_label, f2_label)), run_time=3)
        play(FadeIn(comprimento_c), run_time=2)
        wait()
        play(Write(eixo_maior_text))
        wait()
        play(ReplacementTransform(eixo_maior_text, comprimento_a), run_time=2)
        wait()
        play(comprimento_a.animate.shift((c2p(0, b)[1] - c2p(0, 0)[1])*DOWN), run_time=2)
        wait()
        play(Write(eixo_menor_text))
        wait()
        play(ReplacementTransform(eixo_menor_text, comprimento_b), run_time=2)
        wait()
        play(comprimento_b.animate.shift((c2p(a, 0)[0] - c2p(0, 0))*RIGHT), run_time=2)
        wait()
        play(FadeOut(comprimento_a[2:4]), FadeOut(comprimento_b[2:4]), FadeOut(comprimento_c[2:4]))
        play(comprimento_b[0:2].animate.shift((c2p(a, 0)[0] - c2p(0, 0))*LEFT), run_time=1.5)
        wait()
        play(Transform(comprimento_a[0:2], VGroup(Line(c2p(-c, 0), c2p(0, b)), Tex('a').move_to(0.9*UP+1.7*LEFT)).set_color(DARK_BLUE)), run_time=2)
        wait()
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
        play(Write(textos[8]), run_time=2)
        play(Write(eq_elipse), run_time=2)
        play(ReplacementTransform(comprimento_a[1].copy(), eq_elipse[2]), run_time=2)
        play(ReplacementTransform(comprimento_b[1].copy(), eq_elipse[6]), run_time=2)
        play(FadeOut(textos[8]))
        play(Write(textos[9]), run_time=2)
        wait()
        play(Write(relacao_elipse), run_time=2)
        wait()
        
        play(FadeOut(comprimento_a[0:2], comprimento_b[0:2], comprimento_c[0:2]))
        play(FadeIn(ponto_exemplo, ponto_exemplo_label), run_time=2)
        wait()
        play(ReplacementTransform(relacao_elipse[1].copy(), ponto_exemplo), run_time=2)
        wait()
        play(ReplacementTransform(relacao_elipse[3].copy(), m_focos[0]), run_time=2)
        wait()
        play(ReplacementTransform(relacao_elipse[7].copy(), ponto_exemplo), run_time=2)
        wait()
        play(ReplacementTransform(relacao_elipse[9].copy(), m_focos[1]), run_time=2)
        wait()
        play(TransformMatchingTex(relacao_elipse, relacao_elipse2))
        wait()
        play(ReplacementTransform(relacao_elipse2[0].copy(), linha_f1))
        play(ReplacementTransform(relacao_elipse2[0].copy(), linha_f2))
        wait()
        
        # ---------------------- Animação do ponto com as retas seguindo  ----------------------
        
        play(FadeOut(ponto_exemplo, ponto_exemplo_label, linha_f1, linha_f2))
        play(FadeIn(ponto))
        play(Write(linha1))
        play(Write(linha2))
        play(Write(ponto_label))
        
        def ponto_updater(mob: Mobject, dt: float):
            if self.offset < 1:
                self.offset = (self.offset + 0.125*dt) % 1
                mob.move_to(m_elipse.point_from_proportion(self.offset))

        def linha1_updater(mob: Mobject, dt: float):
            mob.become(Line(f1.get_center(), ponto.get_center()))
        
        def linha2_updater(mob: Mobject, dt: float):
            mob.become(Line(f2.get_center(), ponto.get_center()))
        
        def ponto_label_updater(mob: Mobject, dt:float):
            mob.move_to(ponto.get_center() + 0.3*UP + 0.3*RIGHT)

        ponto.add_updater(ponto_updater)
        linha1.add_updater(linha1_updater)
        linha2.add_updater(linha2_updater)
        ponto_label.add_updater(ponto_label_updater)
        
        self.wait(8)
        
        self.remove(linha1,linha2, ponto, ponto_label)
        
        play(*[FadeOut(mob) for mob in self.mobjects if mob != plano], 
            FadeOut(Line(f1.get_center(), m_elipse.point_from_proportion(1))), 
            FadeOut(Line(f2.get_center(), m_elipse.point_from_proportion(1)))
            )

    def explicar_parabola(self):
        # ---------------------- Dados ----------------------
        play = self.play
        plano = self.plano
        c2p = plano.c2p
        textos = self.m_textos
        p = 1
        x_limits = 4/p**(1/2)
        func = lambda x: (x**2)/4*p
        cor_parabola = RED
        cor_reta = DARK_BLUE
        cor_foco = YELLOW
        cor_p = ORANGE
        cor_ponto = PURPLE
        cor_linhas = PINK
        wait = lambda x=1: self.wait(x)

        # ---------------------- Mobjects ----------------------
        seta_x = MathTex('\\rightarrow').next_to(self.plano, RIGHT, -0.2).set_color(BLUE_B)
        seta_y = MathTex('\\rightarrow').rotate(90*DEGREES).next_to(self.plano, UP, -0.2).set_color(GREEN_B)
        label_x, label_y = self.plano.get_axis_labels(x_label='x', y_label='y')
        label_x.scale(0.7).shift(0.4*LEFT + 0.1*UP).set_color(BLUE_B)
        label_y.scale(0.7).shift(0.4*DOWN + 0.1*RIGHT).set_color(GREEN_B)
        parabola = plano.get_graph(func, x_range=[-x_limits, x_limits, 1]).set_color(cor_parabola)
        reta_diretriz = Line(c2p(-7, 0), c2p(7, 0)).move_to(c2p(0, -p)).set_color(cor_reta)
        reta_diretriz_texto = Tex('Reta Diretriz').scale(0.7).move_to(5*LEFT+2*UP)
        reta_diretriz_label = Tex('r').scale(0.7).set_color(cor_reta).move_to(reta_diretriz.get_center() + 0.3*UP + 6*RIGHT)
        foco = Dot(c2p(0, p)).set_color(cor_foco)
        foco_texto = Tex('Foco').scale(0.7).move_to(5*LEFT+2*UP)
        foco_label = Tex('F').scale(0.7).set_color(cor_foco).move_to(foco.get_center() + 0.3*LEFT + 0.3*UP)
        aux_top, aux_down = Line(c2p(0, 0), c2p(0, p)), Line(c2p(0, 0), c2p(0, -p))
        p_top = VGroup(Brace(aux_top, RIGHT), Tex('p').scale(0.7).move_to(aux_top.get_center() + 0.7*RIGHT)).set_color(cor_p)
        p_down = VGroup(Brace(aux_down, RIGHT), Tex('p').scale(0.7).move_to(aux_down.get_center() + 0.7*RIGHT)).set_color(cor_p)
        eq_parabola = MathTex(
            'y',        # 0
            '=',        # 1
            '{1',       # 2
            '\\over',   # 3
            '4',        # 4
            'p}',       # 5
            'x^2'       # 6
        ).scale(0.7).move_to(5*LEFT+2*UP)
        eq_parabola[0].set_color(GREEN_B)
        eq_parabola[5].set_color(cor_p)
        eq_parabola[6].set_color(BLUE_B)

        relacao_parabola = MathTex(
            'dist(',        # 0
            'P',            # 1
            ',',            # 2
            'r',            # 3
            ')',            # 4
            '=',            # 5
            'dist(',        # 6
            'P',            # 7
            ',',            # 8
            'F',            # 9
            ')'             # 10
        ).scale(0.7).move_to(5*RIGHT+2*UP)
        relacao_parabola[1].set_color(cor_ponto)
        relacao_parabola[3].set_color(cor_reta)
        relacao_parabola[7].set_color(cor_ponto)
        relacao_parabola[9].set_color(cor_foco)

        relacao_parabola2 = MathTex(
            'D_1',           
            '=',  
            'D_2'            
        ).scale(0.7).move_to(5*RIGHT+2*UP)
        
        pos_ponto_exemplo = parabola.point_from_proportion(0.3)
        ponto_exemplo = Dot(pos_ponto_exemplo).set_color(cor_ponto)
        linha_reta_exemplo = Line(pos_ponto_exemplo, [pos_ponto_exemplo[0], c2p(0, -p)[1], 0]).set_color(cor_linhas)
        linha_foco_exemplo = Line(pos_ponto_exemplo, foco.get_center()).set_color(cor_linhas)
        ponto_label_exemplo = Tex('P').set_color(cor_ponto).move_to(ponto_exemplo.get_center() + 0.5*UP).scale(0.7)
        
        pos_ponto_inicio = parabola.point_from_proportion(0) 
        ponto = Dot(pos_ponto_inicio).set_color(cor_ponto)
        linha_horizontal = Line(pos_ponto_inicio, foco.get_center()).set_color(cor_linhas)
        linha_vertical = Line(pos_ponto_inicio, [pos_ponto_inicio[0], c2p(0, -p)[1], 0]).set_color(cor_linhas)
        ponto_label = Tex('P').move_to(ponto.get_center() + 0.5*UP).scale(0.6).set_color(cor_ponto)
        
        # ---------------------- Animações ----------------------
        self.add(plano, label_x, label_y, seta_x, seta_y)
        play(Write(textos[10]))
        wait()
        play(Write(parabola))
        wait()
        play(FadeOut(textos[10]))
        play(Write(textos[11]))
        wait()
        play(Write(foco_texto))
        wait()
        play(ReplacementTransform(foco_texto, foco), run_time=2)
        wait()
        play(Write(foco_label))
        play(Write(reta_diretriz_texto))
        wait()
        play(ReplacementTransform(reta_diretriz_texto, reta_diretriz), run_time=3)
        wait()
        play(Write(reta_diretriz_label))
        play(Write(p_top), run_time=2)
        play(Write(p_down), run_time=2)
        play(FadeOut(textos[11]))
        play(Write(textos[12]))
        wait()
        play(Write(eq_parabola), run_time=2)
        wait()
        play(FadeOut(textos[12]))
        play(Write(textos[13]))
        wait()
        play(Write(relacao_parabola))
        wait()
        play(Write(linha_reta_exemplo))
        play(Write(linha_foco_exemplo))
        play(Write(ponto_exemplo))
        play(Write(ponto_label_exemplo))
        play(ReplacementTransform(VGroup(relacao_parabola[1].copy(), relacao_parabola[7].copy()), ponto_exemplo), run_time=2)
        wait()
        play(ReplacementTransform(relacao_parabola[3].copy(), reta_diretriz), run_time=2)
        wait()
        play(ReplacementTransform(relacao_parabola[9].copy(), foco), run_time=2)
        wait()
        play(TransformMatchingTex(relacao_parabola, relacao_parabola2))
        wait()        
        play(ReplacementTransform(relacao_parabola2[0].copy(), linha_reta_exemplo), run_time=2)
        wait()
        play(ReplacementTransform(relacao_parabola2[2].copy(), linha_foco_exemplo), run_time=2)
        wait()
        play(FadeOut(linha_reta_exemplo, linha_foco_exemplo, ponto_exemplo, ponto_label_exemplo), run_time=2)
        wait()
        play(FadeIn(ponto))
        play(Write(linha_horizontal))
        play(Write(linha_vertical))
        play(Write(ponto_label))
        wait()
        
        self.offset = 0
        
        def ponto_updater(mob: Mobject, dt: float):
            if self.offset < 1-0.25*dt:
                self.offset = (self.offset + 0.25*dt) % 1
                mob.move_to(parabola.point_from_proportion(self.offset))
                
        def linha_vertical_updater(mob: Mobject, dt: float):
            mob.become(Line(ponto.get_center(), [ponto.get_center()[0], c2p(0, -p)[1], 0])).set_color(cor_linhas)
            
        def linha_horizontal_updater(mob: Mobject, dt: float):
            mob.become(Line(ponto.get_center(), foco.get_center())).set_color(cor_linhas)
            
        def ponto_label_updater(mob: Mobject, dt: float):
            mob.move_to(ponto.get_center() + 0.5*UP)
            
        ponto.add_updater(ponto_updater)
        linha_vertical.add_updater(linha_vertical_updater)
        linha_horizontal.add_updater(linha_horizontal_updater)
        ponto_label.add_updater(ponto_label_updater)
        
        self.wait(7)
        
        ponto.clear_updaters()
        linha_vertical.clear_updaters()
        linha_horizontal.clear_updaters()
        ponto_label.clear_updaters()

        wait()
        
        play(FadeOut(*[mobject for mobject in self.mobjects if mobject != plano], linha_horizontal, linha_vertical))
    
    def explicar_hiperbole(self):
        # ---------------------- Dados ----------------------
        play = self.play
        plano = self.plano
        textos = self.m_textos
        c2p = plano.c2p
        cor_hiperbole = PURPLE
        cor_foco = ORANGE
        cor_c = YELLOW
        cor_a = DARK_BLUE
        cor_ponto = GREEN
        
        a, b = 3, 2
        c = np.sqrt(a**2 + b**2)
        func = lambda x: np.sqrt((((x**(2))/(a**(2)))-1)*b**(2)) if x**2/a**2 >= 1 else 0

        wait = lambda x=1: self.wait(x)
        
        velocidade = 5
        # ---------------------- Mobjects ----------------------
        seta_x = MathTex('\\rightarrow').next_to(self.plano, RIGHT, -0.2).set_color(BLUE_B)
        seta_y = MathTex('\\rightarrow').rotate(90*DEGREES).next_to(self.plano, UP, -0.2).set_color(GREEN_B)
        hiperbole = VGroup(
            VGroup(
                *[Line(c2p(x, func(x)), c2p(x+0.01, func(x+0.01))) for x in np.arange(plano.x_range[0]+1, -a-0.01, 0.01)],
                *[Line(c2p(x, -func(x)), c2p(x+0.01, -func(x+0.01))) for x in np.arange(-a-0.01, plano.x_range[0]+1, -0.01)]
            ),
            VGroup(
                *[Line(c2p(x, func(x)), c2p(x+0.01, func(x+0.01))) for x in np.arange(plano.x_range[1]-1, a-0.01, -0.01)],
                *[Line(c2p(x, -func(x)), c2p(x+0.01, -func(x+0.01))) for x in np.arange(a, plano.x_range[1]-1, 0.01)]
            )
        ).set_color(cor_hiperbole)
                
        # ---------------------- c ----------------------
        comprimento_c = VGroup(
            Line(c2p(0, 0), c2p(-c, 0)), 
            Tex('c').move_to(Line(c2p(0, 0), c2p(-c, 0)).get_center() + 0.3*UP),
            Line(c2p(0, 0), c2p(c, 0)),
            Tex('c').move_to(Line(c2p(0, 0), c2p(c, 0)).get_center() + 0.3*UP),
        ).set_color(cor_c)
        
        linha_vertical_c = [
            DashedLine(start=c2p(-c, 2), end=c2p(-c, 0)).set_color(cor_c),
            DashedLine(start=c2p(c, 2), end=c2p(c, 0)).set_color(cor_c)
        ]
        
        # ---------------------- a ----------------------
        
        comprimento_a = VGroup(
            Line(c2p(0, 0), c2p(-a, 0)), 
            Tex('a').move_to(Line(c2p(0, 0), c2p(-a, 0)).get_center() + 0.3*DOWN),
            Line(c2p(0, 0), c2p(a, 0)),
            Tex('a').move_to(Line(c2p(0, 0), c2p(a, 0)).get_center() + 0.3*DOWN),
        ).set_color(cor_a)
        
        linha_vertical_a = [
            DashedLine(start=c2p(-a, -2), end=c2p(-a, 0)).set_color(cor_a),
            DashedLine(start=c2p(a, -2), end=c2p(a, 0)).set_color(cor_a)
        ]
        
        # ---------------------- focos ----------------------
        
        focos = VGroup(Dot(c2p(-c, 0)), Dot(c2p(c, 0))).set_color(cor_foco)
        
        # ---------------------- ponto_1 ----------------------
        
        ponto_1 = Dot(hiperbole[0][0].get_center())
        linha_p_f1_1 = Line(focos[0].get_center(), ponto_1.get_center())
        linha_p_f2_1 = Line(focos[1].get_center(), ponto_1.get_center())
        
        # ---------------------- Ponto 2 ----------------------
        
        ponto_2 = Dot(hiperbole[1][0].get_center())
        linha_p_f1_2 = Line(focos[0].get_center(), ponto_2.get_center())
        linha_p_f2_2 = Line(focos[1].get_center(), ponto_2.get_center())
        
        # ---------------------- Equação da hipérbole ----------------------
        
        eq_hiperbole = MathTex(
            '{x^2', 
            '\\over', 
            'a^2}', 
            '-', 
            '{y^2', 
            '\\over', 
            'b^2}', 
            '=', 
            '1'
        ).scale(0.7).move_to(4*RIGHT+2.5*UP)
        
        eq_hiperbole[0].set_color(BLUE_B)
        eq_hiperbole[2].set_color(cor_a)
        eq_hiperbole[4].set_color(GREEN_B)
        
        # ---------------------- Relação da hipérbole ----------------------
        
        relacao_hiperbole = MathTex(
            '|',     # 0
            'dist(', # 1
            'P',     # 2
            ',',     # 3
            'F_1',   # 4
            ')',     # 5
            '-',     # 6
            'dist(', # 7
            'P',     # 8
            ',',     # 9
            'F_2',   # 10
            ')',     # 11
            '|',     # 12
            '=',     # 13
            '2a'     # 14
        ).scale(0.7).move_to(4*LEFT+2.5*UP)
        
        relacao_hiperbole[2].set_color(cor_ponto)
        relacao_hiperbole[4].set_color(cor_foco)
        relacao_hiperbole[8].set_color(cor_ponto)
        relacao_hiperbole[10].set_color(cor_foco)
        relacao_hiperbole[14].set_color(cor_a)

        relacao_hiperbole2 = MathTex(
            '|',     
            'D_1'    
            '-',     
            'D_2'
            '|',     
            '=',     
            '2a'
        ).scale(0.7).move_to(4*LEFT+2.5*UP)
        relacao_hiperbole2[-1].set_color(cor_a)
        
        # ---------------------- Updaters ----------------------
        
        def ponto_2_updater(mob: Mobject, dt):
            if self.offset < len(hiperbole[1]) - velocidade:
                self.offset += velocidade
                mob.move_to(hiperbole[1][self.offset].get_center())
                
        def linha_p_f1_2_updater(mob: Mobject, dt):
            mob.become(Line(focos[0].get_center(), ponto_2.get_center()))  
            
        def linha_p_f2_2_updater(mob: Mobject, dt):
            mob.become(Line(focos[1].get_center(), ponto_2.get_center()))  
            
        def ponto_1_updater(mob: Mobject, dt):
            if self.offset < len(hiperbole[0]) - velocidade:
                self.offset += velocidade
                mob.move_to(hiperbole[0][self.offset].get_center())
                
        def linha_p_f1_1_updater(mob: Mobject, dt):
            mob.become(Line(focos[0].get_center(), ponto_1.get_center()))  
            
        def linha_p_f2_1_updater(mob: Mobject, dt):
            mob.become(Line(focos[1].get_center(), ponto_1.get_center())) 
        
        # ---------------------- Animações ----------------------
        self.add(plano, seta_x, seta_y)
        play(Write(textos[14]))
        wait()
        play(Write(hiperbole[0]))
        play(Write(hiperbole[1]))
        wait()
        
        play(FadeOut(textos[14]))
        play(Write(textos[15]))
        play(FadeIn(focos))
        
        play(Write(comprimento_c))
        play(comprimento_c.animate.shift(c2p(0, 2) - c2p(0, 0)))
        play(FadeIn(linha_vertical_c[0]), FadeIn(linha_vertical_c[1]))     
        wait()   
        
        play(Write(comprimento_a))
        play(comprimento_a.animate.shift(c2p(0, -2) - c2p(0, 0)))
        play(FadeIn(linha_vertical_a[0]), FadeIn(linha_vertical_a[1]))
        wait()

        play(FadeOut(textos[15]))
        play(Write(textos[16]), run_time=2)
        wait()
        
        play(Write(eq_hiperbole), run_time=2)
        wait()
        play(FadeOut(textos[16]))
        play(Write(textos[17]))
        wait()
        
        play(Write(relacao_hiperbole))
        wait()

        self.offset = 0
        
        play(ReplacementTransform(VGroup(relacao_hiperbole[2], relacao_hiperbole[8]).copy(), ponto_1))
        wait()
        play(ReplacementTransform(relacao_hiperbole[4].copy(), linha_p_f1_1))
        wait()
        play(ReplacementTransform(relacao_hiperbole[10].copy(), linha_p_f2_1))
        wait()
        play(ReplacementTransform(relacao_hiperbole[14].copy(), comprimento_a))
        wait()

        play(TransformMatchingTex(relacao_hiperbole, relacao_hiperbole2))
        wait()
                
        ponto_1.add_updater(ponto_1_updater)
        linha_p_f1_1.add_updater(linha_p_f1_1_updater)
        linha_p_f2_1.add_updater(linha_p_f2_1_updater)
        self.wait(4)
        ponto_1.clear_updaters()
        linha_p_f1_1.clear_updaters()
        linha_p_f2_1.clear_updaters()
        self.remove(ponto_1, linha_p_f1_1, linha_p_f2_1)
        
        ponto_final_1 = Dot(hiperbole[0][-1].get_center())
        play(FadeOut(
            ponto_final_1,
            Line(focos[0].get_center(), ponto_final_1.get_center()),
            Line(focos[1].get_center(), ponto_final_1.get_center())
        ))        
        
        self.offset = 0

        play(Write(ponto_2))
        play(Write(linha_p_f1_2))
        play(Write(linha_p_f2_2))
        wait()
        
        velocidade = 5
        
        ponto_2.add_updater(ponto_2_updater)
        linha_p_f1_2.add_updater(linha_p_f1_2_updater)
        linha_p_f2_2.add_updater(linha_p_f2_2_updater)
        self.wait(4)
        ponto_2.clear_updaters()
        linha_p_f1_2.clear_updaters()
        linha_p_f2_2.clear_updaters()
        self.remove(ponto_2, linha_p_f1_2, linha_p_f2_2)
        ponto_final_2 = Dot(hiperbole[1][-1].get_center())
        play(FadeOut(
            ponto_final_2, 
            Line(focos[0].get_center(), ponto_final_2), 
            Line(focos[1].get_center(), ponto_final_2))
        )   
        wait()  
        
        play(FadeOut(*[mob for mob in self.mobjects]))
        wait()

    def abertura(self):
        titulo = Tex('Geometria Analítica').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)
        subtitulo = Tex('Ponto e Curvas').scale(1.5).set_color('#43bfca').move_to(titulo.get_center() + 1.2*DOWN)

        self.play(FadeIn(titulo, subtitulo))
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(subtitulo))
        self.wait()

    def fechamento(self):
        pibit = MathTex("\\text{PIBIT: 0220036212472856}").scale(2).move_to(2*UP).set_color(DARK_BLUE)
        autor = MathTex("\\text{Autor: Eric Satoshi Suzuki Kishimoto}").set_color("#dc6a40").move_to(ORIGIN)
        orientador = MathTex("\\text{Orientador: Prof. Vitor Rafael Coluci}").set_color("#dc6a40").move_to(DOWN)
        ft = ImageMobject("./logo-FT.jpeg").scale(0.4).shift(1.5*DOWN+3*RIGHT)
        unicamp = ImageMobject("./logo-unicamp.jpeg").scale(0.3).shift(1.5*DOWN+3*LEFT)

        self.play(FadeIn(pibit))
        self.wait(1)
        self.play(FadeIn(unicamp), FadeIn(ft))
        self.wait(1)
        self.play(FadeOut(unicamp), FadeOut(ft))
        self.wait(0.8)
        self.play(FadeIn(autor), FadeIn(orientador))
        self.wait(2)
        self.play(FadeOut(*[mob for mob in self.mobjects]))


def main():
    ARQ_NOME = Path(__file__).resolve()
    CENA = CenaPontoCurvas.__name__
    ARGS = '-pqh'

    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')


if __name__ == '__main__':
    main()
