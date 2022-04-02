# TODO
"""
conjuntos:

1) aumentar um pouco o tamanho das coisas (inclusive as fontes dos textos).

2) operações entre conjuntos: colocar os símbolos de -, interseção e união depois que apresentar a operação 
e não abaixo da representação dos conjuntos,

"""


from manim import *
from pathlib import Path
from typing import List

from matplotlib import scale
from scipy.fftpack import shift

class Utils:
    escala_tamanho_texto = 0.7
    cor_conjunto_elipse = ORANGE
    escala_tamanho_elemento_conjunto = 1.2
    cor_elemento_conjunto = YELLOW

    
class Conjuntos(Scene):
    def debug(self):
        grade = VGroup(*[
            VGroup(
                Line(6*UP, 7*DOWN).set_opacity(0.3).shift(i*RIGHT),
                MathTex(f'{i}').shift(i*RIGHT + 3.8*DOWN).scale(0.8)
            ) for i in range(-7, 8)
        ],
        *[
            VGroup(
                Line(8*LEFT, 8*RIGHT).set_opacity(0.3).shift(i*DOWN),
                MathTex(f'{-i}').shift(i*DOWN + 6.8*LEFT).scale(0.8)
            ) for i in range(-5, 6)
        ])
        self.add(grade)

    def construct(self):
        self.debug()
        self.abertura()
        self.introducao()
        self.explicacao_simbolos()
        self.conjuntos_epeciais()
        self.relacoes()
        self.operacoes()
        self.fechamento()

    def clear_scene(self):
        self.play(FadeOut(*self.mobjects))

    def introducao(self):
        play = lambda *anim, t=2: self.play(*anim, run_time=t)

        
        texto_introducao = Tex(
            r'\raggedright Podemos definir um conjunto como uma coleção de elementos. ',
            r'Podemos representá-los como diagramas:'
        ).scale(Utils.escala_tamanho_texto).to_corner(UP)

        conjunto = Ellipse(width=3, height=4).set_color(Utils.cor_conjunto_elipse).move_to(3*LEFT)
        numeros_conjunto = VGroup(*[
            MathTex(2*i + 1).set_color(Utils.cor_elemento_conjunto).scale(1.2).move_to(RIGHT + i*RIGHT) for i in range(0, 3)
        ]).move_to(2*RIGHT).add(MathTex('...').move_to(4*RIGHT))
        elementos_conjunto = conjunto.copy().set_fill(opacity=0.5)

        play(Write(texto_introducao[0]))
        self.wait(2)

        play(Write(texto_introducao[1]))
        self.wait(2)

        play(Write(conjunto))
        self.wait(2)
        play(Write(numeros_conjunto))
        self.wait(2)
        play(
            MoveAlongPath(numeros_conjunto[0], ArcBetweenPoints(numeros_conjunto[0].get_center(), conjunto.get_center() + UP)),
            numeros_conjunto[1].animate.shift(0.5*LEFT),
            numeros_conjunto[2].animate.shift(0.5*LEFT),
            numeros_conjunto[3].animate.shift(0.5*LEFT),
        )
        self.wait(2)
        play(
            MoveAlongPath(numeros_conjunto[1], ArcBetweenPoints(numeros_conjunto[1].get_center(), conjunto.get_center())),
            numeros_conjunto[2].animate.shift(0.5*LEFT),
            numeros_conjunto[3].animate.shift(0.5*LEFT)
        )
        self.wait(2)
        play(
            MoveAlongPath(numeros_conjunto[2], ArcBetweenPoints(numeros_conjunto[2].get_center(), conjunto.get_center() + DOWN)),
            numeros_conjunto[3].animate.shift(0.5*LEFT)
        )
        self.wait(2)
        play(ReplacementTransform(numeros_conjunto[-1], elementos_conjunto))
        self.wait(2)

        self.clear_scene()

    def explicacao_simbolos(self):
        play =  lambda *anim, t=2: self.play(*anim, run_time=t)

        texto = Tex(
            r'\raggedright $\bullet$ Para simplificar, podemos usar símbolos para representar os conjuntos.\\',
            r'\raggedright \quad $A = \{1, 3, 5, ...\}$\\',
            r'\raggedright $\bullet$ Ou através de uma regra que todos os elementos respeitem.\\',
            r'\raggedright \quad $A = \{x | \text{x é ímpar e maior que 0}\}$\\',
        ).scale(Utils.escala_tamanho_texto)

        explicacao_1 = texto[0].shift(UP)
        conjunto_numerado = texto[1].shift(0.5*UP)
        explicacao_2 = texto[2].shift(0.5*DOWN)
        conjunto_regra = texto[3].shift(DOWN)

        play(Write(explicacao_1))
        self.wait(2)
        play(Write(conjunto_numerado))
        self.wait(2)
        play(Write(explicacao_2))
        self.wait(2)
        play(Write(conjunto_regra))
        self.wait(2)

        self.clear_scene()

    def conjuntos_epeciais(self):

        play = lambda *anim, t=2: self.play(*anim, run_time=t)

        texto = Tex(
            r'\raggedright Também temos conjuntos especiais:\\', 
            r'\raggedright \quad $\bullet$ Conjunto vazio: não possui elementos\\',
            r'\raggedright Representado por $\emptyset$\\',
            r'\raggedright \quad $\bullet$ Conjunto unitário: possui apenas um elemento\\',
        ).scale(Utils.escala_tamanho_texto).shift(0.2*DOWN)

        introducao = texto[0].shift(3*UP + 2*LEFT)
        texto_conjunto_vazio = texto[1].shift(2.5*UP + 2*LEFT)
        representacao = texto[2].shift(1.5*UP + 1.5*RIGHT)
        texto_conjunto_unitario = texto[3].shift(2*LEFT)

        conjunto_vazio = Ellipse(width=1, height=1.5).shift(3.5*LEFT + 1.2*UP)
        conjunto_unitario = VGroup(
            Ellipse(width=1, height=1.5),
            MathTex('1').scale(0.7)
        ).shift(3.5*LEFT + 2*DOWN)


        play(Write(introducao))
        self.wait(2)
        play(Write(texto_conjunto_vazio))
        self.wait(2)
        play(Write(conjunto_vazio))
        self.wait(2)
        play(Write(representacao))
        self.wait(2)
        play(Write(texto_conjunto_unitario))
        self.wait(2)
        play(Write(conjunto_unitario))
        self.wait(2)

        self.clear_scene()

    def relacoes(self):
        play = lambda *anim, t=2: self.play(*anim, run_time=t)

        introducao = Tex('Agora, veremos as relações entre: \\')\
            .scale(Utils.escala_tamanho_texto)\
            .move_to(3.25*UP + 4*LEFT)

        ####################### Relação Conjunto Conjunto ############################

        texto_conjunto_conjunto = Tex(r'''
            \raggedright Conjunto e Conjunto: \\
            \raggedright \quad $\bullet \subset$: contido \\
            \raggedright \quad $\bullet \supset$: contém \\
            \raggedright \quad $\bullet \not \subset$: não está contido \\
            \raggedright \quad $\bullet \not \supset$: não contém \\
        ''')\
            .scale(Utils.escala_tamanho_texto)\
            .move_to(1.75*UP + 4*LEFT)

        ######################## Contido ###########################

        conjunto_contido = VGroup(
            Ellipse(height=1.8, width=1).shift(5*LEFT).set_color(Utils.cor_conjunto_elipse),
            VGroup(
                *[MathTex(f'{2*i + 1}').shift(UP + 0.5*i*DOWN).scale(0.7) for i in range(2)]
            ).shift(5*LEFT + 0.5*DOWN)
        ).shift(DOWN)
        
        conjunto_total_1 = VGroup(
            Ellipse(height=1.8, width=1).shift(3*LEFT).set_color(Utils.cor_conjunto_elipse),
            VGroup(
                *[MathTex(f'{2*i + 1}').shift(UP + 0.5*i*DOWN).scale(0.7) for i in range(3)]
            ).shift(3*LEFT + 0.5*DOWN)
        ).shift(DOWN)

        contido = MathTex(r'\subset').shift(4*LEFT + DOWN)

        simbolo_conjunto_contido = MathTex(r'\{ 1, 3 \}')\
            .scale(0.7)\
            .move_to(conjunto_contido)
        simbolo_conjunto_total = MathTex(r'\{ 1, 3, 5 \}')\
            .scale(0.7)\
            .move_to(conjunto_total_1)

        ###################################################

        ####################### Não contido ############################

        conjunto_nao_contido = VGroup(
            Ellipse(height=1.8, width=1).shift(5*LEFT).set_color(Utils.cor_conjunto_elipse),
            VGroup(
                *[MathTex(f'{i+1}').shift(UP + 0.5*i*DOWN).scale(0.7) for i in range(2)]
            ).shift(5*LEFT + 0.5*DOWN)
        ).shift(DOWN)
        
        conjunto_total_2 = VGroup(
            Ellipse(height=1.8, width=1).shift(3*LEFT).set_color(Utils.cor_conjunto_elipse),
            VGroup(
                *[MathTex(f'{2*i + 1}').shift(UP + 0.5*i*DOWN).scale(0.7) for i in range(3)]
            ).shift(3*LEFT + 0.5*DOWN)
        ).shift(DOWN)

        nao_contido = MathTex(r'\not \subset').shift(4*LEFT + DOWN)

        simbolo_conjunto_nao_contido = MathTex(r'\{ 1, 2 \}')\
            .scale(0.7)\
            .move_to(conjunto_nao_contido)
        simbolo_conjunto_total_2 = MathTex(r'\{ 1, 3, 5 \}')\
            .scale(0.7)\
            .move_to(conjunto_total_2)
        ###################################################

        ######################## Relação elemento conjunto ###########################

        texto_conjunto_elemento = Tex(r'''
            \raggedright Conjunto e Elemento: \\
            \raggedright \quad $\bullet \in$: pertence \\
            \raggedright \quad $\bullet \not \in$: não pertence \\
        ''')\
            .scale(Utils.escala_tamanho_texto)\
            .move_to(2*UP + 2*RIGHT)

        ###################################################

        ########################### Pertence ########################

        elemento = MathTex('1').scale(0.7).shift(1.5*RIGHT + DOWN)
        pertence = MathTex(r'\in').shift(2*RIGHT + DOWN)

        conjunto_pertence = VGroup(
            Ellipse(width=1, height=1.8).set_color(Utils.cor_conjunto_elipse),
            VGroup(
                *[MathTex(f'{2*i + 1}').shift(0.5*UP + 0.5*i*DOWN).scale(0.7) for i in range(3)]
            )
        ).shift(3*RIGHT + DOWN)

        simbolo_elemento = MathTex(r'1')\
            .scale(0.7)\
            .move_to(elemento)\
            .shift(DOWN)
        simbolo_conjunto_pertence = MathTex(r'\{ 1, 3, 5 \}')\
            .scale(0.7)\
            .move_to(conjunto_pertence)

        ###################################################

        ######################### Não Pertence ##########################
        
        elemento_nao_pertence = MathTex('2').scale(0.7).shift(1.5*RIGHT + DOWN)
        nao_pertence = MathTex(r'\not \in').shift(2*RIGHT + DOWN)

        conjunto_nao_pertence = VGroup(
            Ellipse(width=1, height=1.8).set_color(Utils.cor_conjunto_elipse),
            VGroup(
                *[MathTex(f'{2*i + 1}').shift(0.5*UP + 0.5*i*DOWN).scale(0.7) for i in range(3)]
            )
        ).shift(3*RIGHT + DOWN)

        simbolo_conjunto_nao_pertence = MathTex(r'\{ 1, 3, 5 \}')\
            .scale(0.7)\
            .move_to(conjunto_nao_pertence)

        ###################################################

        play(Write(introducao))
        self.wait(2)
        play(Write(texto_conjunto_conjunto))
        self.wait(2)
        play(Write(conjunto_contido))
        self.wait(2)
        play(Write(conjunto_total_1))
        self.wait(2)
        play(
            conjunto_contido[1][0].animate.scale(3/2).set_color(GREEN),
            conjunto_total_1[1][0].animate.scale(3/2).set_color(GREEN),
            t=1
        )
        self.wait()
        play(
            conjunto_contido[1][0].animate.scale(2/3).set_color(WHITE),
            conjunto_total_1[1][0].animate.scale(2/3).set_color(WHITE),
            t=1
        )
        self.wait()
        play(
            conjunto_contido[1][1].animate.scale(3/2).set_color(RED),
            conjunto_total_1[1][0].animate.scale(3/2).set_color(RED),
            t=1
        )
        self.wait()
        play(
            conjunto_contido[1][1].animate.scale(2/3).set_color(WHITE),
            conjunto_total_1[1][0].animate.scale(2/3).set_color(WHITE),
            t=1
        )
        self.wait()
        play(
            conjunto_contido[1][1].animate.scale(3/2).set_color(GREEN),
            conjunto_total_1[1][1].animate.scale(3/2).set_color(GREEN),
            t=1
        )
        self.wait()
        play(
            conjunto_contido[1][1].animate.scale(2/3).set_color(WHITE),
            conjunto_total_1[1][1].animate.scale(2/3).set_color(WHITE),
            t=1
        )
        self.wait(2)
        play(FadeIn(contido))
        self.wait(2)
        play(ReplacementTransform(conjunto_contido, simbolo_conjunto_contido))
        self.wait(2)
        play(ReplacementTransform(conjunto_total_1, simbolo_conjunto_total))
        self.wait(2)
        play(FadeOut(simbolo_conjunto_contido, simbolo_conjunto_total, contido))
        self.wait(2)
        
        play(Write(conjunto_nao_contido))
        self.wait(2)
        play(Write(conjunto_total_2))
        self.wait(2)
        
        play(
            conjunto_nao_contido[1][0].animate.scale(3/2).set_color(GREEN), 
            conjunto_total_2[1][0].animate.scale(3/2).set_color(GREEN), t=1
        )
        self.wait()
        play(
            conjunto_nao_contido[1][0].animate.scale(2/3).set_color(WHITE),
            conjunto_total_2[1][0].animate.scale(2/3).set_color(WHITE), t=1
        )
        self.wait()
        
        play(
            conjunto_nao_contido[1][1].animate.scale(3/2).set_color(RED),
            conjunto_total_2[1][0].animate.scale(3/2).set_color(RED), t=1
        )
        self.wait()
        play(
            conjunto_nao_contido[1][1].animate.scale(2/3).set_color(WHITE),
            conjunto_total_2[1][0].animate.scale(2/3).set_color(WHITE), t=1
        )
        self.wait()
        play(
            conjunto_nao_contido[1][1].animate.scale(3/2).set_color(RED),
            conjunto_total_2[1][1].animate.scale(3/2).set_color(RED), t=1
        )
        self.wait()
        play(
            conjunto_nao_contido[1][1].animate.scale(2/3).set_color(WHITE),
            conjunto_total_2[1][1].animate.scale(2/3).set_color(WHITE), t=1
        )
        self.wait()
        play(
            conjunto_nao_contido[1][1].animate.scale(3/2).set_color(RED),
            conjunto_total_2[1][2].animate.scale(3/2).set_color(RED), t=1
        )
        self.wait()
        play(
            conjunto_nao_contido[1][1].animate.scale(2/3).set_color(WHITE),
            conjunto_total_2[1][2].animate.scale(2/3).set_color(WHITE), t=1
        )
        self.wait()

        play(FadeIn(nao_contido))
        self.wait(2)
        play(ReplacementTransform(conjunto_nao_contido, simbolo_conjunto_nao_contido))
        self.wait(2)
        play(ReplacementTransform(conjunto_total_2, simbolo_conjunto_total_2))
        self.wait(2)
        # play(FadeIn(simbolo_conjunto_contido, simbolo_conjunto_total, contido))
        play(
            simbolo_conjunto_contido.animate.shift(DOWN),
            simbolo_conjunto_total.animate.shift(DOWN),
            contido.animate.shift(DOWN),
        )
        self.wait(2)

        play(Write(texto_conjunto_elemento))
        self.wait(2)
        play(Write(elemento))
        self.wait(2)
        play(Write(conjunto_pertence))
        self.wait(2)
        play(
            elemento.animate.scale(3/2).set_color(GREEN),
            conjunto_pertence[1][0].animate.scale(3/2).set_color(GREEN),
        )
        self.wait()
        play(
            elemento.animate.scale(2/3).set_color(WHITE),
            conjunto_pertence[1][0].animate.scale(2/3).set_color(WHITE),
        )
        self.wait()
        play(FadeIn(pertence))
        self.wait(2)
        play(ReplacementTransform(conjunto_pertence, simbolo_conjunto_pertence))
        self.wait(2)
        play(FadeOut(elemento, simbolo_conjunto_pertence, pertence))
        self.wait(2)
        play(Write(elemento_nao_pertence))
        self.wait(2)
        play(Write(conjunto_nao_pertence))
        self.wait(2)
        play(
            elemento_nao_pertence.animate.scale(3/2).set_color(RED),
            conjunto_nao_pertence[1][0].animate.scale(3/2).set_color(RED),
        )
        self.wait()
        play(
            elemento_nao_pertence.animate.scale(2/3).set_color(WHITE),
            conjunto_nao_pertence[1][0].animate.scale(2/3).set_color(WHITE),
        )
        self.wait()
        play(
            elemento_nao_pertence.animate.scale(3/2).set_color(RED),
            conjunto_nao_pertence[1][1].animate.scale(3/2).set_color(RED),
        )
        self.wait()
        play(
            elemento_nao_pertence.animate.scale(2/3).set_color(WHITE),
            conjunto_nao_pertence[1][1].animate.scale(2/3).set_color(WHITE),
        )
        self.wait()
        play(
            elemento_nao_pertence.animate.scale(3/2).set_color(RED),
            conjunto_nao_pertence[1][2].animate.scale(3/2).set_color(RED),
        )
        self.wait()

        play(
            elemento_nao_pertence.animate.scale(2/3).set_color(WHITE),
            conjunto_nao_pertence[1][2].animate.scale(2/3).set_color(WHITE),
        )
        self.wait()
        play(FadeIn(nao_pertence))
        self.wait(2)
        play(ReplacementTransform(conjunto_nao_pertence, simbolo_conjunto_nao_pertence))
        self.wait(2)
        play(
            FadeIn(simbolo_conjunto_pertence, elemento, pertence),
            elemento_nao_pertence.animate.shift(DOWN),
            conjunto_nao_pertence.animate.shift(DOWN),
            nao_pertence.animate.shift(DOWN),
        )
        self.wait(2)

        self.clear_scene()
        
    def operacoes(self):

        play = lambda *anim, t=2: self.play(*anim, run_time=t)

        introducao = Tex('Também podemos realizar operações entre conjuntos.').scale(Utils.escala_tamanho_texto).shift(3.25*UP + 2.5*LEFT)
        texto_operacoes = [
            Tex(r'\raggedright $\bullet$ Diferença').scale(Utils.escala_tamanho_texto).shift(2.5*UP + 5*LEFT),
            Tex(r'\raggedright $\bullet$ Interseção').scale(Utils.escala_tamanho_texto).shift(2.5*UP + 5*LEFT),
            Tex(r'\raggedright $\bullet$ União').scale(Utils.escala_tamanho_texto).shift(2.5*UP + 5*LEFT),
        ]

        play(Write(introducao))
        self.wait(2)
        play(Write(texto_operacoes[0]))
        self.wait(2)
        
        ################### Diferença ###################

        conjunto_ellipse_a = Ellipse(width=2.5, height=3.5, color=GREEN, fill_opacity=0.25).shift(2*LEFT + 0.25*UP)
        conjunto_ellipse_b = Ellipse(width=2.5, height=3.5, color=RED, fill_opacity=0.25).shift(0.5*LEFT + 0.25*UP)

        exclusivo_a = Difference(conjunto_ellipse_a, conjunto_ellipse_b, fill_opacity=0.5, color=GREEN)
        exclusivo_b = Difference(conjunto_ellipse_b, conjunto_ellipse_a, fill_opacity=0.5, color=RED)
        label_conjunto_a = MathTex('A').next_to(conjunto_ellipse_a, UL, buff=0).set_color(GREEN)
        label_conjunto_b = MathTex('B').next_to(conjunto_ellipse_b, UR, buff=0).set_color(RED)

        elementos_a = VGroup(
            MathTex('1').shift(0.75*UP),
            MathTex('2').shift(0.75*DOWN),
        ).move_to(exclusivo_a)

        elementos_b = VGroup(
            MathTex('4').shift(0.75*UP),
            MathTex('5').shift(0.75*DOWN),
        ).move_to(exclusivo_b)

        elementos_intersecao = MathTex('3')\
            .move_to(Intersection(conjunto_ellipse_a, conjunto_ellipse_b))

        diferenca_a_b = MathTex(r'A - B = \{ 1, 2 \}', color=GREEN).scale(0.8).move_to(exclusivo_a)#.next_to(exclusivo_a, DOWN, buff=0.25).shift(LEFT)
        diferenca_b_a = MathTex(r'B - A = \{ 4, 5 \}', color=RED).scale(0.8).next_to(exclusivo_b, DOWN, buff=0.25).shift(RIGHT)

        play(Write(conjunto_ellipse_a), Write(label_conjunto_a), Write(elementos_a))
        self.wait(2)
        play(Write(conjunto_ellipse_b), Write(label_conjunto_b), Write(elementos_b))
        self.wait(2)
        play(Write(elementos_intersecao))
        self.wait(2)
        play(FadeIn(exclusivo_a))
        self.wait(2)
        play(FadeOut(
            label_conjunto_a, 
            label_conjunto_b, 
            conjunto_ellipse_a,
            conjunto_ellipse_b, 
            elementos_a, 
            elementos_b, 
            elementos_intersecao, 
            exclusivo_a))
        # play(Write(diferenca_a_b))
        # self.wait(2)
        # play(FadeIn(exclusivo_b))
        # self.wait(2)
        play(Write(diferenca_a_b))
        self.wait(2)
        # play(FadeOut(
        #     conjunto_ellipse_a,
        #     label_conjunto_a,
        #     elementos_a,
        #     conjunto_ellipse_b,
        #     label_conjunto_b,
        #     elementos_b,
        #     elementos_intersecao,
        #     exclusivo_a,
        #     diferenca_a_b,
        #     exclusivo_b,
        #     diferenca_b_a,
        # ))
        self.wait(2)
        play(FadeOut(texto_operacoes[0], diferenca_a_b))
        self.wait(2)

        ######################################

        ################### Interseção ###################

        
        conjunto_ellipse_a = Ellipse(width=2.5, height=3.5, color=GREEN, fill_opacity=0.25).shift(2*LEFT + 0.25*UP)
        conjunto_ellipse_b = Ellipse(width=2.5, height=3.5, color=RED, fill_opacity=0.25).shift(0.5*LEFT + 0.25*UP)

        label_conjunto_a = MathTex('A').next_to(conjunto_ellipse_a, UL, buff=0).set_color(GREEN)
        label_conjunto_b = MathTex('B').next_to(conjunto_ellipse_b, UR, buff=0).set_color(RED)

        interseccao_a_b = Intersection(conjunto_ellipse_a, conjunto_ellipse_b, color=BLUE, fill_opacity=0.5)

        elementos_a = VGroup(
            MathTex('1').shift(0.75*UP),
            MathTex('2').shift(0.75*DOWN),
        ).move_to(exclusivo_a)

        elementos_b = VGroup(
            MathTex('4').shift(0.75*UP),
            MathTex('5').shift(0.75*DOWN),
        ).move_to(exclusivo_b)

        elementos_intersecao = MathTex('3')\
            .move_to(Intersection(conjunto_ellipse_a, conjunto_ellipse_b))

        tex_interseccao_a_b = MathTex(r'A \cap B = \{ 3 \}', color=BLUE).move_to(interseccao_a_b)#.scale(0.8).next_to(interseccao_a_b, DOWN, buff=1)

        play(Write(texto_operacoes[1]))
        self.wait(2)
        play(Write(conjunto_ellipse_a), Write(label_conjunto_a), Write(elementos_a))
        self.wait(2)
        play(Write(conjunto_ellipse_b), Write(label_conjunto_b), Write(elementos_b))
        self.wait(2)
        play(Write(elementos_intersecao))
        self.wait(2)
        play(FadeIn(interseccao_a_b))
        self.wait(2)
        play(FadeOut(
            conjunto_ellipse_a,
            label_conjunto_a,
            elementos_a,
            conjunto_ellipse_b,
            label_conjunto_b,
            elementos_b,
            elementos_intersecao,
            interseccao_a_b,
        ))
        self.wait(2)
        play(Write(tex_interseccao_a_b))
        self.wait(2)
        play(FadeOut(texto_operacoes[1], tex_interseccao_a_b))
        self.wait(2)

        ######################################

        ################## União ####################

        conjunto_ellipse_a = Ellipse(width=2.5, height=3.5, color=GREEN, fill_opacity=0.25).shift(2*LEFT + 0.25*UP)
        conjunto_ellipse_b = Ellipse(width=2.5, height=3.5, color=RED, fill_opacity=0.25).shift(0.5*LEFT + 0.25*UP)

        label_conjunto_a = MathTex('A').next_to(conjunto_ellipse_a, UL, buff=0).set_color(GREEN)
        label_conjunto_b = MathTex('B').next_to(conjunto_ellipse_b, UR, buff=0).set_color(RED)

        uniao = Union(conjunto_ellipse_a, conjunto_ellipse_b, color=BLUE, fill_opacity=0.5)

        elementos_a = VGroup(
            MathTex('1').shift(0.75*UP),
            MathTex('2').shift(0.75*DOWN),
        ).move_to(exclusivo_a)

        elementos_b = VGroup(
            MathTex('4').shift(0.75*UP),
            MathTex('5').shift(0.75*DOWN),
        ).move_to(exclusivo_b)

        elementos_intersecao = MathTex('3')\
            .move_to(Intersection(conjunto_ellipse_a, conjunto_ellipse_b))

        tex_uniao_a_b = MathTex(r'A \cup B = \{ 1, 2, 3, 4, 5 \}', color=BLUE).move_to(interseccao_a_b)#.scale(0.8).next_to(interseccao_a_b, DOWN, buff=1)

        play(Write(texto_operacoes[2]))
        self.wait(2)
        play(Write(conjunto_ellipse_a), Write(label_conjunto_a), Write(elementos_a))
        self.wait(2)
        play(Write(conjunto_ellipse_b), Write(label_conjunto_b), Write(elementos_b))
        self.wait(2)
        play(Write(elementos_intersecao))
        self.wait(2)
        play(FadeIn(uniao))
        self.wait(2)
        play(FadeOut(
            conjunto_ellipse_a,
            label_conjunto_a,
            elementos_a,
            conjunto_ellipse_b,
            label_conjunto_b,
            elementos_b,
            elementos_intersecao,
            uniao
        ))
        self.wait(2)
        play(Write(tex_uniao_a_b))
        self.wait(2)
        play(FadeOut(texto_operacoes[2], tex_uniao_a_b))
        self.wait(2)
        
        ######################################

        self.clear_scene()

    def abertura(self):
        titulo = Tex('Conjuntos').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)
        # subtitulo = Tex('Pontos, reta e as cônicas').scale(1.5).set_color('#43bfca').move_to(titulo.get_center() + 1.2*DOWN)

        # self.play(FadeIn(titulo, subtitulo))
        self.play(FadeIn(titulo))
        self.wait(1.5)
        # self.play(FadeOut(titulo), FadeOut(subtitulo))
        self.play(FadeOut(titulo))
        self.wait()

    def fechamento(self):
        pibit = MathTex("\\text{PIBIT/CNPQ: 0220036212472856}").scale(1.5).move_to(2*UP).set_color(DARK_BLUE)
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
        

ARQ_NOME = Path(__file__).resolve()
CENA = Conjuntos.__name__
ARGS = '-pqh'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')

