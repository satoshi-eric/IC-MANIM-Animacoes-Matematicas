from manim import *
from pathlib import Path
import os
from typing import *


class DerivandoElipse(Scene):
    def construct(self):
        self.init_dados()
        self.init_objetos()
        self.mostrar_definicoes_em_objetos()
        self.manipulacao_algebrica()

    def init_dados(self):
        a = 3
        b = 2
        c = np.sqrt(a**2 - b**2 if a >= b else b**2 - a**2)
        f1, f2 = ((-c, 0, 0), (c, 0, 0)) if a >= b else ((0, -c, 0), (0, c, 0))
        self.a = a
        self.b = b
        self.c = c
        self.f1 = f1
        self.f2 = f2
        
    
    def init_objetos(self):
        escala_objetos = 0.6
        posicao_objetos = 4*LEFT
        cor_elipse = RED
        cor_focos = GREEN
        cor_ponto = PURPLE
        cor_c = BLUE
        cor_b = ORANGE
        cor_a = YELLOW
        posicao_definicoes = 4*RIGHT
        escala_definicoes = 0.6
        cor_segmento_focal = MAROON
        posicao_def_elipse = 2*RIGHT

        # -------- Elementos da Elipse --------

        # -------- Eixos --------
        eixos = Axes(x_length=2*(self.a+1), x_axis_config={"include_ticks": False}, y_axis_config={"include_ticks": False})
        
        # -------- Elipse --------
        elipse = Ellipse(width=2*self.a, height=2*self.b).set_color(cor_elipse)
        elipse_label = MathTex("E").move_to(elipse.point_from_proportion(0.4) + UP).set_color(cor_elipse)
        
        # -------- Focos --------
        f1 = Dot(self.f1).set_color(cor_focos)
        f2 = Dot(self.f2).set_color(cor_focos)
        f1_label = MathTex("F_1").next_to(f1, UP*0.5).set_color(cor_focos)
        f2_label = MathTex("F_2").next_to(f2, UP*0.5).set_color(cor_focos)

        # -------- Função para pegar y do ponto --------
        f = lambda x: np.sqrt(self.b**2 * (1 - (x**2/self.a**2))) if (x**2/self.a**2) <= 1 and self.a != 0 else None
        x = 2
        y = f(x)

        # -------- Ponto pertencente a Elipse --------
        p = Dot((x, y, 0)).set_color(cor_ponto)
        p_label = MathTex("P_1").next_to(p, UP*0.5).set_color(cor_ponto)

        # -------- Distância focal (c) --------
        dist_c_1 = Line(self.f1, ORIGIN).shift(DOWN).set_color(cor_c)
        dist_c_2 = Line(ORIGIN, self.f2).shift(DOWN).set_color(cor_c)
        dist_c_1_label = MathTex("c").next_to(dist_c_1, UP*0.5).set_color(cor_c)
        dist_c_2_label = MathTex("c").next_to(dist_c_2, UP*0.5).set_color(cor_c)

        # -------- Semi-eixo maior (a) --------
        dist_a_1 = Line(elipse.point_from_proportion(0), ORIGIN).shift(self.b * DOWN).set_color(cor_a)
        dist_a_2 = Line(ORIGIN, elipse.point_from_proportion(0.5)).shift(self.b * DOWN).set_color(cor_a)
        dist_a_1_label = MathTex("a").next_to(dist_a_1, DOWN, 0.5).set_color(cor_a)
        dist_a_2_label = MathTex("a").next_to(dist_a_2, DOWN, 0.5).set_color(cor_a)

        # -------- Semi-eixo menor (b) --------

        dist_b_1 = Line(elipse.point_from_proportion(0.25), ORIGIN).shift(self.a * LEFT).set_color(cor_b)
        dist_b_2 = Line(ORIGIN, elipse.point_from_proportion(0.75)).shift(self.a * LEFT).set_color(cor_b)
        dist_b_1_label = MathTex("b").next_to(dist_b_1, LEFT, 0.5).set_color(cor_b)
        dist_b_2_label = MathTex("b").next_to(dist_b_2, LEFT, 0.5).set_color(cor_b)


        # -------- Segmento focal --------
        segmento_focal = Line(self.f1, self.f2).set_color(cor_segmento_focal)

        # -------- Agrupando objetos para manipulá-los juntos --------
        objetos = VGroup(
            eixos, elipse, elipse_label, f1, f2, f1_label, f2_label, 
            p, p_label, dist_c_1, 
            dist_c_2, dist_c_1_label, dist_c_2_label, 
            dist_a_1, dist_a_2, dist_a_1_label, dist_a_2_label,
            segmento_focal, dist_b_1, dist_b_2, dist_b_1_label, dist_b_2_label)\
            .scale(escala_objetos).move_to(posicao_objetos)

        # -------- Agrupando objetos para manipulá-los separados --------
        self.eixos = objetos[0]
        self.elipse = objetos[1]
        self.elipse_label = objetos[2]
        self.f1 = objetos[3]
        self.f2 = objetos[4]
        self.f1_label = objetos[5]
        self.f2_label = objetos[6]
        self.p = objetos[7]
        self.p_label = objetos[8]
        self.dist_c_1 = objetos[9]
        self.dist_c_2 = objetos[10]
        self.dist_c_1_label = objetos[11]
        self.dist_c_2_label = objetos[12]
        self.dist_a_1 = objetos[13]
        self.dist_a_2 = objetos[14]
        self.dist_a_1_label = objetos[15]
        self.dist_a_2_label = objetos[16]
        self.segmento_focal = objetos[17]
        self.dist_b_1 = objetos[18]
        self.dist_b_2 = objetos[19]
        self.dist_b_1_label = objetos[20]
        self.dist_b_2_label = objetos[21]

        self.focos = VGroup(self.f1_label, self.f2_label, self.f1, self.f2)
        self.distancia_focal = VGroup(self.dist_c_1, self.dist_c_2, self.dist_c_1_label, self.dist_c_2_label)
        self.eixo_maior = VGroup(self.dist_a_1, self.dist_a_2, self.dist_a_1_label, self.dist_a_2_label)
        self.eixo_menor = VGroup(self.dist_b_1, self.dist_b_2, self.dist_b_1_label, self.dist_b_2_label)

        # -------- Criando as definições --------
        definicoes = Tex(
            '$E$', ': elipse\n\n',
            '$P_1$', ': ponto\n\n',
            '$F_1, F_2$', ': focos\n\n',
            '$\\overline{F_1F_2}$', ': segmento focal\n\n',
            '$2c$', ': distância focal\n\n',
            '$2a$', ': eixo maior\n\n',
            '$2b$', ': eixo menor\n\n',
            tex_environment="flushleft"
        ).scale(escala_definicoes).move_to(posicao_definicoes)
        
        self.def_elipse = definicoes[0:2]
        self.def_ponto = definicoes[2:4]
        self.def_focos = definicoes[4:6]
        self.def_segmento_focal = definicoes[6:8]
        self.def_distancia_focal = definicoes[8:10]
        self.def_eixo_maior = definicoes[10:12]
        self.def_eixo_menor = definicoes[12:14]

        self.eq_elipse = MathTex('E = \{(x, y)\ /\ d(P_1, F_1) + d(P_1, F_2) = 2a\}').move_to(posicao_def_elipse).scale(escala_definicoes)
        self.eq_f1 = MathTex('F_1 = (-c, 0)').scale(escala_definicoes)
        self.eq_f2 = MathTex('F_2 = (c, 0)').scale(escala_definicoes)
        self.eq_ponto = MathTex(
            'P_1 = (x, y) \\in E \\rightarrow', 
            'd(P_1, F_1)', 
            '+', 
            'd(P_2, F_2)', 
            '= 2a'
        ).scale(escala_definicoes).move_to(1.5*RIGHT)

        self.def_dist_1 = MathTex('d(P_1, F_1) = \\sqrt{(x - (-c))^2 + (y - 0)^2}').scale(escala_definicoes).move_to(RIGHT)
        self.def_dist_2 = MathTex('d(P_1, F_2) = \\sqrt{(x - (c))^2 + (y - 0)^2}').scale(escala_definicoes).move_to(RIGHT)

        eqs = list(map(lambda eq: eq.scale(0.6).move_to(RIGHT + DOWN),
            [
                MathTex('\\sqrt{(x + c)^2 + (y - 0)^2} = 2a'),
                MathTex('\\sqrt{(x + c)^2 = 2a + (y - 0)^2}'),
                MathTex('(x + c)^2 + y^2 = 4a^2 - 4a\\sqrt{(x - c)^2 + y^2} + (x - c)^2 + y^2'),
                MathTex('(x + c)^2 = 4a^2 - 4a\\sqrt{(x - c)^2 + y^2} + (x - c)^2'),
                MathTex('x^2 + 2cx + c^2 = 4a^2 - 4a \\sqrt{(x - c)^2+ y^2} + x^2 - 2cx + c^2'),
                MathTex('2cx = 4a^2 - 4a \\sqrt{(x - c)^2+ y^2} - 2cx'),
                MathTex
            ]
        ))

    def mostrar_definicoes_em_objetos(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.eixos))

        play(Write(self.def_elipse))
        play(Transform(self.def_elipse[0].copy(), self.elipse_label))
        play(FadeIn(self.elipse))

        play(FadeIn(self.def_ponto))
        play(Transform(self.def_ponto[0].copy(), self.p_label))
        play(FadeIn(self.p))

        play(FadeIn(self.def_focos))
        play(Transform(self.def_focos[0].copy(), self.focos))
        
        play(FadeIn(self.def_segmento_focal))
        play(Transform(self.def_segmento_focal[0].copy(), self.segmento_focal))

        play(FadeIn(self.def_distancia_focal))
        play(Transform(self.def_distancia_focal[0].copy(), self.distancia_focal))

        play(FadeIn(self.def_eixo_maior))
        play(Transform(self.def_eixo_maior[0].copy(), self.eixo_maior))

        play(FadeIn(self.def_eixo_menor))
        play(Transform(self.def_eixo_menor[0].copy(), self.eixo_menor))

        play(
            self.def_elipse.animate.shift(2*UP+1.5*RIGHT),
            self.def_ponto.animate.shift(2*UP+1.5*RIGHT),
            self.def_focos.animate.shift(2*UP+1.5*RIGHT),
            self.def_segmento_focal.animate.shift(2*UP+1.5*RIGHT),
            self.def_distancia_focal.animate.shift(2*UP+1.5*RIGHT),
            self.def_eixo_maior.animate.shift(2*UP+1.5*RIGHT),
            self.def_eixo_menor.animate.shift(2*UP+1.5*RIGHT),
        )

        self.wait(1)

    def manipulacao_algebrica(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        play(Write(self.eq_elipse))
        play(self.eq_elipse.animate.shift(3*UP + LEFT))
        play(Write(self.eq_f1))
        play(self.eq_f1.animate.shift(2.5*UP + 0.8*LEFT))
        play(Write(self.eq_f2))
        play(self.eq_f2.animate.shift(2.5*UP + 1.5*RIGHT))
        play(Write(self.eq_ponto))
        play(self.eq_ponto.animate.shift(2*UP + LEFT)) 
        play(Write(self.def_dist_1))
        play(self.def_dist_1.animate.shift(1.5*UP + 0.5*RIGHT))
        play(TransformMatchingShapes(self.def_dist_1, MathTex('d(P_1, F_1) = \\sqrt{(x + c)^2 + y^2}').scale(0.6).move_to(self.def_dist_1.get_center())))
        play(Write(self.def_dist_2))
        play(self.def_dist_2.animate.shift(1*UP + 0.5*RIGHT))
        play(TransformMatchingShapes(self.def_dist_2, MathTex('d(P_1, F_2) = \\sqrt{(x - c)^2 + y^2}').scale(0.6).move_to(self.def_dist_2.get_center())))
        play(self.eq_ponto[1:5].copy().animate.move_to(RIGHT + DOWN))

        # 'P_1 = (x, y) \\in E \\rightarrow', 
        #     'd(P_1, F_1)', 
        #     '+', 
        #     'd(P_2, F_2)', 
        #     '= 2a'
        
    

ARQ_NOME = Path(__file__).resolve()
CENA = DerivandoElipse.__name__
ARGS = '-s'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')