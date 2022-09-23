from typing import Tuple
from manim import *
from pathlib import Path
import os
import json
import itertools as it

class TrianguloData(VGroup):
    def __init__(
        self, 
        vertices: Tuple[
            Tuple[float, float, float], 
            Tuple[float, float, float], 
            Tuple[float, float, float]
        ] = (
            (-2, -1, 0),
            (2, -1, 0),
            (0, 2, 0), 
        ),
        aresta_object = Line,
        length_labels = ['a', 'b', 'c'],
        show_braces = True,
        **kwargs
    ):
        super().__init__(**kwargs)

        arestas = VGroup(
            aresta_object(vertices[0], vertices[1], color=RED),
            aresta_object(vertices[1], vertices[2], color=GREEN),
            aresta_object(vertices[2], vertices[0], color=BLUE),
        )

        angulos_forma = VGroup(
            Angle(arestas[0], arestas[1], radius=0.5, quadrant=(-1, 1), other_angle=True, color=BLUE),
            Angle(arestas[1], arestas[2], radius=0.5, quadrant=(-1, 1), other_angle=True, color=RED),
            Angle(arestas[2], arestas[0], radius=0.5, quadrant=(-1, 1), other_angle=True, color=GREEN),            
        )

        angulo_labels = VGroup(
            MathTex("\\widehat{C}", color=BLUE).move_to(angulos_forma[0].get_center() + 0.35*LEFT+0.2*UP).scale(0.5),
            MathTex("\\widehat{A}", color=RED).move_to(angulos_forma[1].get_center() + 0.35*DOWN).scale(0.5),
            MathTex("\\widehat{B}", color=GREEN).move_to(angulos_forma[2].get_center() + 0.35*RIGHT+0.2*UP).scale(0.5),
        )

        angulos = VGroup(
            *[
                VGroup(angulos_forma[i], angulo_labels[i]) 
                for i in range(len(angulos_forma))
            ]
        )

        braces = [
            BraceBetweenPoints(arestas[0].points[0], arestas[0].points[-1], color=RED),
            BraceBetweenPoints(arestas[1].points[0], arestas[1].points[-1], color=GREEN),
            BraceBetweenPoints(arestas[2].points[0], arestas[2].points[-1], color=BLUE),
        ]

        braces_labels = [
            MathTex(length_labels[0]).move_to(braces[0].get_center() + 0.35*DOWN).scale(0.8).set_color(RED),
            MathTex(length_labels[1]).move_to(braces[1].get_center() + 0.5*RIGHT+0.3*UP).scale(0.8).set_color(GREEN),
            MathTex(length_labels[2]).move_to(braces[2].get_center() + 0.5*LEFT+0.3*UP).scale(0.8).set_color(BLUE),
        ]

        if show_braces:
            lengths = VGroup(
                *[
                    VGroup(braces[i], braces_labels[i])
                    for i in range(len(braces))
                ]
            )
        else:
            braces_labels = [
                MathTex(length_labels[0]).move_to(braces[0].get_center() + 0.35*DOWN).scale(0.8).set_color(RED),
                MathTex(length_labels[1]).move_to(braces[1].get_center() + 0.15*RIGHT).scale(0.8).set_color(GREEN),
                MathTex(length_labels[2]).move_to(braces[2].get_center() + 0.1*LEFT).scale(0.8).set_color(BLUE),
            ]
            lengths = VGroup(
                *[
                    VGroup(braces_labels[i])
                    for i in range(len(braces))
                ]
            )

        circulo = Circle(radius=2.15, color=YELLOW).move_to(0.15*DOWN)

        self.add(arestas, lengths, angulos, circulo)

    @property
    def arestas(self):
        return self[0]

    @property
    def lengths(self):
        return self[1]

    @property
    def angulos(self):
        return self[2]

    @property
    def circulo(self):
        return self[3]

class Seta(Line):
    def __init__(self, start=(0, 0, 0), end=(1, 1, 0), **kwargs):
        super().__init__(start, end, **kwargs)
        triangulo = Triangle()
        triangulo.scale(0.15).rotate(-90*DEGREES)\
            .set_fill(kwargs['color'], opacity=1).set_stroke(width=0)
        try:
            triangulo.rotate(np.arctan((end[1] - start[1])/(end[0] - start[0])))
            if end[0] - start[0] < 0 or end[1] - start[1] < 0:
                triangulo.rotate(180*DEGREES)
        except ZeroDivisionError:
            if end[1] - start[1] < 0:
                triangulo.rotate(270*DEGREES)
            else:
                triangulo = Triangle().scale(0.15)
        triangulo.move_to(self.point_from_proportion(0.95))
        self.add(triangulo)

class DerivandoLeiSenos(Scene):
    def construct(self):
        
        self.abertura()
        self.mostrar_lei_senos()
        self.revisao_algebra_linear()
        self.lei_senos()
        self.fechamento()

    def mostrar_lei_senos(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        titulo = Tex('Lei dos Senos').scale(2).set_color(ORANGE)
        lei_senos = MathTex('\\frac{a}{sen(\\widehat{A})} = \\frac{b}{sen(\\widehat{B})} = \\frac{c}{sen(\\widehat{C})} = 2R').scale(0.8).move_to(2*RIGHT)
        triangulo = TrianguloData()

        play(Write(titulo))
        play(titulo.animate.scale(0.5).move_to(3*UP))
        play(Write(triangulo.arestas), t=2)
        play(Write(triangulo.angulos), t=2)
        play(Write(triangulo.lengths), t=2)
        play(Write(triangulo.circulo), t=2)
        play(triangulo.animate.move_to(3.5*LEFT).scale(0.8))
        play(Write(lei_senos), t=2)
        play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)

    def revisao_algebra_linear(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        # Definição de dependência linear
        # titulo = Tex('Revisão de Algebra Linear').scale(2)
        # topicos = BulletedList(
        #     '($\\vec{u}$, $\\vec{v}$) é LD (Linearmente dependente) se $\\vec{u}$ e $\\vec{v}$ são paralelos',
        #     '($\\vec{u}$, $\\vec{v}$, $\\vec{w}$) é LD (Linearmente dependente) se $\\vec{u}$, $\\vec{v}$ e $\\vec{w}$ são paralelos \\\\ a um mesmo plano',
        # ).scale(0.5).move_to(2*UP + 2*LEFT)

        # v1 = Vector(4*RIGHT, color=RED).scale(0.5, scale_tips=True)
        # v2 = Vector(4*RIGHT, color=GREEN).scale(0.5, scale_tips=True)
        # v1.next_to(topicos[0], DOWN, buff=0.6)
        # v2.next_to(v1, DOWN, buff=0.4)
        # v1_label = MathTex('\\vec{u}', color=RED).scale(0.8).move_to(v1.point_from_proportion(1)+0.2*UP + 0.3*RIGHT)
        # v2_label = MathTex('\\vec{v}', color=GREEN).scale(0.8).move_to(v2.point_from_proportion(1)+0.2*UP + 0.3*RIGHT)
        # topicos[1].shift(1.6*DOWN)
        # vetores = VGroup(VGroup(v1, v2), VGroup(v1_label, v2_label))

        # plano = VGroup(
        #     Polygon(
        #         (0, 0, 0),
        #         (5, 0, 0),
        #         (6, 1, 0),
        #         (1, 1, 0),
        #         fill_color=BLUE,
        #         stroke_width=0,
        #         z_index=3,
        #     ),
        #     Polygon(
        #         (6, 1, 0),
        #         (7, 2, 0),
        #         (2, 2, 0),
        #         (1, 1, 0),
        #         fill_color=BLUE,
        #         stroke_width=0,
        #         z_index=1
        #     ),
        # ).scale(0.5).move_to(2*DOWN + 3*LEFT).set_color(BLUE).set_fill(BLUE, 0.5)

        # v3 = Vector([0, 6, 0], color=RED, z_index=2).scale(0.4, scale_tips=True).move_to(plano)
        # v4 = Vector([0, 6, 0], color=GREEN, z_index=2).scale(0.4, scale_tips=True).move_to(plano)
        # v5 = Vector([0, 6, 0], color=YELLOW, z_index=2).scale(0.4, scale_tips=True).move_to(plano)
        # v3.shift(0.5*LEFT)
        # v5.shift(0.5*RIGHT)
        # v3_label = MathTex('\\vec{u}', color=RED).scale(0.8).move_to(v3.point_from_proportion(1)+0.2*UP + 0.3*RIGHT)
        # v4_label = MathTex('\\vec{v}', color=GREEN).scale(0.8).move_to(v4.point_from_proportion(1)+0.2*UP + 0.3*RIGHT)
        # v5_label = MathTex('\\vec{w}', color=YELLOW).scale(0.8).move_to(v5.point_from_proportion(1)+0.2*UP + 0.3*RIGHT)
        # vetores3d = VGroup(VGroup(v3, v3_label), VGroup(v4, v4_label), VGroup(v5, v5_label))

        # play(Write(titulo), t=2)
        # play(titulo.animate.move_to(3.5*UP).scale(0.4))
        # play(Write(topicos[0]))
        # play(Write(vetores[0]))
        # play(Write(vetores[1]))
        # play(Write(topicos[1]))
        # play(FadeIn(plano), t=2)
        # play(Write(vetores3d[0]))
        # play(Write(vetores3d[1]))
        # play(Write(vetores3d[2]))
        # play(FadeOut(topicos, vetores, vetores3d, plano))

        # Produto vetorial
        titulo = Tex('Produto Vetorial').scale(2)
        produto_vetorial = Tex('$\\vec{u} \\wedge \\vec{v}$: produto vetorial').scale(0.5)
        topicos = Tex(
            '\\raggedright $\\bullet \\quad$ Se $(\\vec{u}, \\vec{v})$ é LD, então $\\vec{u} \\wedge \\vec{v} = \\vec{0}$ \\\\',
            '\\raggedright $\\bullet \\quad$ Se $(\\vec{u}, \\vec{v}, \\vec{w})$ é LI, então: \\\\',
            '\\raggedright $\\bullet \\quad ||\\vec{u} \\wedge \\vec{v}|| = ||\\vec{u}|| \\cdot ||\\vec{v}|| \\cdot sen(\\theta)$ \\\\',
            '\\raggedright $\\bullet \\quad \\vec{u} \\wedge \\vec{v}$ é ortogonal a $\\vec{u}$ e $\\vec{v}$ \\\\',
            '\\raggedright $\\bullet \\quad (\\vec{u}, \\vec{v}, \\vec{u} \\wedge \\vec{v})$ é uma base positiva \\\\',
        ).scale(0.5).move_to(0.8*UP + 3.2*LEFT)
        topicos[2].shift(0.5*RIGHT)
        topicos[3].shift(0.5*RIGHT)
        topicos[4].shift(0.5*RIGHT)

        v1 = Vector(8*RIGHT, color=RED).scale(0.5, scale_tips=True)
        v2 = Vector(8*RIGHT, color=GREEN).scale(0.5, scale_tips=True)
        v1.next_to(topicos[0], RIGHT, buff=1.5).scale(0.5)
        v1_label = MathTex('\\vec{u}', color=RED).move_to(v1.point_from_proportion(1)+0.2*UP + 0.3*RIGHT).scale(0.8)
        v2.next_to(v1, DOWN, buff=0.4).scale(0.5)
        v2_label = MathTex('\\vec{v}', color=GREEN).move_to(v2.point_from_proportion(1)+0.2*UP + 0.3*RIGHT).scale(0.8)
        vetores = VGroup(VGroup(v1, v1_label), VGroup(v2, v2_label))

        v3 = Vector([0, 3, 0], color=RED)
        v3_label = MathTex('\\vec{u}', color=RED).scale(1.6).move_to(v3.point_from_proportion(1)+0.8*UP + RIGHT)
        v4 = Vector([3, 0, 0], color=GREEN)
        v4_label = MathTex('\\vec{v}', color=GREEN).scale(1.6).move_to(v4.point_from_proportion(1)+0.8*UP + RIGHT)
        v5 = Vector([-1.8, -1.8, 0], color=YELLOW)
        v5_label = MathTex('\\vec{w}', color=YELLOW).scale(1.6).move_to(v5.point_from_proportion(1)+0.8*DOWN + LEFT)
        vetores3d = VGroup(VGroup(v3, v3_label), VGroup(v4, v4_label), VGroup(v5, v5_label)).scale(0.5).move_to(1.5*DOWN+RIGHT)

        play(Write(titulo), t=2)
        play(titulo.animate.move_to(3.5*UP).scale(0.4), t=2)
        play(Write(produto_vetorial), t=2)
        play(produto_vetorial.animate.move_to(2*UP+4*LEFT), t=2)
        play(Write(topicos[0]), t=2)
        self.wait(2)
        play(Write(vetores[0]), t=2)
        self.wait(2)
        play(Write(vetores[1]), t=2)
        self.wait(2)
        play(Write(topicos[1]), t=2)
        self.wait(2)
        play(Write(vetores3d[0]), t=2)
        play(Write(vetores3d[1]), t=2)
        play(Write(vetores3d[2]), t=2)
        play(Write(topicos[2]), t=2)
        self.wait(2)
        play(Write(topicos[3]), t=2)
        self.wait(2)
        play(Write(topicos[4]), t=2)
        self.wait(2)
        play(FadeOut(titulo, produto_vetorial, topicos, vetores, vetores3d))

        # Intepretação do produto vetorial
        titulo_interpretacao = Tex('Interpretação do Produto Vetorial').scale(1.5)
        introducao = Tex('Se $(\\vec{u}, \\vec{v})$ é LI:').scale(0.5).move_to(2*UP + 5*LEFT)
        interpretacao = Tex(
            '$\\bullet || \\vec{u} \\wedge \\vec{v} ||$ pode ser entendido como a área de um paralelograma'\
        ).scale(0.5).move_to(introducao.get_center() + 0.5*DOWN + 4*RIGHT)
        
        
        v1 = Vector((5, 0, 0), color=RED)
        v2 = Vector((2, 3, 0), color=GREEN)
        v3 = Vector((5, 0, 0), color=RED).shift(3*UP + 2*RIGHT)
        v4 = Vector((2, 3, 0), color=GREEN).shift(5*RIGHT)
        v1_label = MathTex('\\vec{u}', color=RED).move_to(v1.get_center() + 0.5*DOWN)
        v2_label = MathTex('\\vec{v}', color=GREEN).move_to(v2.get_center() + 0.5*LEFT)
        v3_label = MathTex('\\vec{u}', color=RED).move_to(v3.get_center() + 0.5*UP)
        v4_label = MathTex('\\vec{v}', color=GREEN).move_to(v4.get_center() + 0.5*RIGHT)
        h = DashedLine((2, 0, 0), (2, 3, 0), color=BLUE)
        h_label = MathTex('h', color=BLUE).scale(1.5).scale(0.5).move_to(h.get_center() + 0.5*RIGHT)
        angulo = Angle(v1, v2, radius=0.6, color=YELLOW)
        angulo_label = MathTex('\\theta', color=YELLOW).scale(0.8).move_to(angulo.get_center() + 0.2*UP + 0.3*RIGHT)

        paralelograma = VGroup(
            v1, v2, v3, v4, 
            v1_label, v2_label, v3_label, v4_label, 
            h, h_label, angulo, angulo_label
        ).scale(0.6).move_to(DOWN+3*LEFT)

        explicacao_area = [
            Tex('Podemos provar isso calculando a área do paralelograma:').scale(0.5).move_to(interpretacao.get_center() + 0.5*DOWN + 0.6*LEFT),
            Tex('Usamos a fórmula $ base \cdot altura $ para calcular sau área.').move_to(interpretacao.get_center() + 0.5*LEFT + 0.5*DOWN).scale(0.5),
            Tex('Calculando a altura pelo seno, temos:').move_to(interpretacao.get_center() + 1.5*LEFT + 0.5*DOWN).scale(0.5),
            Tex('Assim, temos que a área será dada por:').move_to(interpretacao.get_center() + 1.5*LEFT + 0.5*DOWN).scale(0.5),
        ]

        triangulo_forma = Polygon(
            (0, 0, 0), (2, 0, 0), (2, 3, 0), color=PURPLE
        ).scale(0.6).move_to(paralelograma.get_center() + 1.5*LEFT)
        t_h_label = h_label.copy()
        t_v2_label = v2_label.copy()
        t_angulo = angulo.copy()
        t_angulo_label = angulo_label.copy()

        triangulo = VGroup(
            triangulo_forma, t_h_label, t_v2_label, t_angulo, t_angulo_label
        )

        formula_seno = [
            MathTex('sen(\\theta)', '=', '{h', '\\over', '||\\vec{v}||}').scale(0.5).move_to(3*RIGHT),
            MathTex('h = ||\\vec{v}|| \\cdot sen(\\theta)').scale(0.5).move_to(3*RIGHT),
        ]

        formula_area = [
            MathTex('base', '\\cdot', 'altura').scale(0.5).move_to(3*RIGHT + DOWN),
            MathTex('||\\vec{u}||', '\\cdot', 'h').scale(0.5).move_to(3*RIGHT + DOWN),
            MathTex('||\\vec{u}||', '\\cdot', '||\\vec{v}|| \\cdot sen(\\theta)').scale(0.5).move_to(3*RIGHT + DOWN),
            MathTex('||\\vec{u} \\wedge \\vec{v}||').scale(0.5).move_to(3*RIGHT + DOWN),
        ]


        definicao_raio = Tex(
            'Para a lei dos senos, precisamos de mais uma definação:'
        ).to_corner(UP).scale(0.7)
        formula_raio = MathTex('R = {abc \\over 4 \\cdot A_{\\text{\\textit{triângulo}}}').scale(0.7).shift(2*RIGHT)
        definicao_r = Tex(
            'onde R é o raio da circunferência circunscrita ao triângulo'
        ).scale(0.7).shift(2.5*DOWN)
        triangulo_circunscrito = VGroup(
            Circle(radius=2.15, color=YELLOW).move_to(0.15*DOWN),
            Line(start=(-2, -1, 0), end=(2, -1, 0), color=RED),
            Line(start=(2, -1, 0), end=(0, 2, 0), color=GREEN),
            Line(start=(0, 2, 0), end=(-2, -1, 0), color=BLUE),
            MathTex('a').shift(1.25*UP + 1.25*LEFT).set_color(BLUE),
            MathTex('b').shift(1.25*UP + 1.25*RIGHT).set_color(GREEN),
            MathTex('c').shift(1.5*DOWN).set_color(RED),
        ).shift(3*LEFT).scale(0.5)

        play(Write(titulo_interpretacao), t=2)
        self.wait(2)
        play(titulo_interpretacao.animate.next_to(titulo, DOWN, buff=0.2).scale(0.4), t=2)
        self.wait(2)
        play(Write(introducao), t=2)
        self.wait(2)
        play(Write(interpretacao), t=2)
        self.wait(2)
        play(Write(paralelograma), t=2)
        self.wait(2)
        play(Write(explicacao_area[0]), t=2)
        self.wait(2)
        play(FadeOut(explicacao_area[0]))
        self.wait(2)
        play(Write(explicacao_area[1]), t=2)
        self.wait(2)
        play(FadeOut(explicacao_area[1]))
        self.wait(2)
        play(Write(explicacao_area[2]), t=2)
        self.wait(2)
        play(Write(triangulo), t=2)
        self.wait(2)
        play(triangulo.animate.shift(5*RIGHT))
        self.wait(2)
        play(ReplacementTransform(triangulo[1].copy(), formula_seno[0][2]), t=2)
        self.wait(2)
        play(ReplacementTransform(triangulo[2].copy(), formula_seno[0][4]), t=2)
        self.wait(2)
        play(ReplacementTransform(triangulo[4].copy(), formula_seno[0][0]), t=2)
        self.wait(2)
        play(FadeIn(formula_seno[0][1], formula_seno[0][3]), t=2)
        self.wait(2)
        play(TransformMatchingShapes(formula_seno[0], formula_seno[1]), t=2)
        self.wait()
        play(FadeOut(triangulo), t=2)
        self.wait(2)
        play(FadeOut(explicacao_area[2]), t=2)
        self.wait(2)
        play(Write(explicacao_area[3]), t=2)
        self.wait(2)
        play(Write(formula_area[0]), t=2)
        self.wait(2)
        play(
            ReplacementTransform(formula_area[0][0], formula_area[1][0]), 
            ReplacementTransform(formula_area[0][1], formula_area[1][1]),
            ReplacementTransform(formula_area[0][2], formula_area[1][2]),
        t=2)
        self.wait(2)
        play(
            ReplacementTransform(formula_area[1][0], formula_area[2][0]), 
            ReplacementTransform(formula_area[1][1], formula_area[2][1]),
            ReplacementTransform(formula_area[1][2], formula_area[2][2]),
        t=2)
        self.wait(2)
        play(
            ReplacementTransform(formula_area[2], formula_area[3]), 
        t=2)
        self.wait(2)
        play(Write(SurroundingRectangle(formula_area[3])), t=2)
        self.wait(2)

        play(FadeOut(*[mob for mob in self.mobjects if mob != titulo]))
        play(Write(definicao_raio), t=2)
        self.wait()
        play(Write(formula_raio), t=2)
        self.wait(3)
        play(Write(definicao_r), t=2)
        self.wait(3)
        play(Write(triangulo_circunscrito), t=2)
        self.wait(3)

        play(FadeOut(*[mob for mob in self.mobjects]))

    def lei_senos(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        triangulo = TrianguloData(
            aresta_object=Seta, 
            length_labels = [
                '\\vec{b}', 
                '\\vec{a}', 
                '\\vec{c}'
            ],
            show_braces=False
        )

        titulo = Tex('Derivando a Lei dos Senos').scale(2)
        textos = [
            Tex('Considerandpo um triângulos que é a soma dos vetores $\\vec{a}$, $\\vec{b}$ e $\\vec{c}$.').scale(0.5).move_to(3*UP),
            Tex('$||\\vec{a} \\wedge \\vec{b}||$ representa a área de um paralelograma').scale(0.5).move_to(3*UP),
            Tex('$||\\vec{a} \\wedge \\vec{b}||$ representa a área do triângulo').scale(0.5).move_to(3*UP),
            Tex('Usando $||\\vec{u} \\wedge \\vec{v}|| = ||\\vec{u}|| \\cdot ||\\vec{v}|| \\cdot sen \\theta$, temos:').scale(0.5).move_to(3*UP),
            Tex('Se considerarmos $||\\vec{a}|| = a$, $||\\vec{b}|| = b$, $||\\vec{c}|| = c$, temos:').scale(0.5).move_to(3*UP),
        ]

        formulas = [
            MathTex('\\frac{||\\vec{a} \\wedge \\vec{b}||}{2} = \\frac{||\\vec{a} \\wedge \\vec{b}||}{2} = \\frac{||\\vec{a} \\wedge \\vec{b}||}{2} = A_{\\text{\\textit{triângulo}}}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('||\\vec{a} \\wedge \\vec{b}|| = ||\\vec{a} \\wedge \\vec{b}|| = ||\\vec{a} \\wedge \\vec{b}|| = 2A_{\\text{\\textit{triângulo}}}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('||\\vec{a}|| \\cdot ||\\vec{b}|| \\cdot sen(\\widehat{C}) = ||\\vec{a}|| \\cdot ||\\vec{c}|| \\cdot sen(\\widehat{B}) = ||\\vec{b}|| \\cdot ||\\vec{c}|| \\cdot sen(\\widehat{A}) = 2A_{\\text{\\textit{triângulo}}}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('a \\cdot b \\cdot sen(\widehat{C}) = a \\cdot c \\cdot sen(\widehat{B}) = b \\cdot c \\cdot sen(\widehat{A}) = 2A_{\\text{\\textit{triângulo}}}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('\\frac{ab \\cdot sen(\widehat{C})}{abc} = \\frac{ac \\cdot sen(\widehat{B})}{abc} = \\frac{bc \\cdot sen(\widehat{A})}{abc} = \\frac{2A_{\\text{\\textit{triângulo}}}}{abc}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('\\frac{sen(\\widehat{C})}{c} = \\frac{sen(\\widehat{B})}{b} = \\frac{sen(\\widehat{A})}{a} = \\frac{2A_{\\text{\\textit{triângulo}}}}{abc}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('R = \\frac{abc}{4 \\cdot A_{\\text{\\textit{triângulo}}}} \\rightarrow 4 \\cdot A_{\\text{\\textit{triângulo}}} = \\frac{abc}{R}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('2 \\cdot A_{\\text{\\textit{triângulo}}} = \\frac{abc}{2R} \\rightarrow \\frac{2 \\cdot A_{\\text{\\textit{triângulo}}}}{abc} = \\frac{1}{2R}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('\\frac{sen \\widehat{C}}{c} = \\frac{sen \\widehat{B}}{b} = \\frac{sen \\widehat{A}}{a} = \\frac{1}{2R}').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
            MathTex('\\frac{c}{sen(\\widehat{C})} = \\frac{b}{sen(\\widehat{B})} = \\frac{a}{sen(\\widehat{A})} = 2R').scale(0.5).move_to(2.5*RIGHT + 2.5*UP),
        ]

        formulas_pos = it.cycle([0.7*DOWN, 1.4*DOWN, 2.1*DOWN, 2.8*DOWN, 3.5*DOWN, 4.2*DOWN, 4.9*DOWN])

        formulas = [mob.shift(pos) for mob, pos in zip(formulas, formulas_pos)]

        play(Write(titulo), t=2)
        play(titulo.animate.scale(0.25).move_to(3.5*UP))

        play(Write(textos[0]), t=2)

        play(Write(triangulo.arestas), t=2)
        self.wait(2)
        play(Write(triangulo.angulos), t=2)
        self.wait(2)
        play(Write(triangulo.lengths), t=2)
        self.wait(2)
        play(Write(triangulo.circulo), t=2)
        self.wait(2)
        play(triangulo.animate.scale(0.75).move_to(4.5*LEFT))
        self.wait(2)
        
        play(FadeOut(textos[0]))
        self.wait(2)
        play(Write(textos[1]), t=2)
        self.wait(2)
        play(FadeOut(textos[1]))
        self.wait(2)
        play(Write(textos[2]), t=2)
        self.wait(2)
        play(FadeOut(textos[2]))
        self.wait(2)
        play(Write(textos[3]), t=2)
        self.wait(2)

        play(Write(formulas[0]), t=2)
        self.wait(2)
        play(ReplacementTransform(formulas[0].copy(), formulas[1]), t=2)
        self.wait(2)

        play(FadeOut(textos[3]), t=2)
        self.wait(2)
        play(Write(textos[4]), t=2)
        self.wait(2)

        for i, formula in enumerate(formulas[2:]):
            if i == 5:
                try:
                    play(FadeOut(*formulas[i-5:i+2]), TransformMatchingShapes(formulas[i+1].copy(), formula), t=2)
                except:
                    pass
            else:
                play(TransformMatchingShapes(formulas[i+1].copy(), formula), t=2)
            self.wait(2)

        play(FadeOut(*formulas[len(formulas) - 3: len(formulas)-1]))

        play(Write(SurroundingRectangle(formulas[-1])), t=2)

        play(FadeOut(*[mob for mob in self.mobjects]))

    def abertura(self):
        titulo = Tex('Lei dos Senos').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)

        self.play(FadeIn(titulo))
        self.wait(1.5)
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
CENA = DerivandoLeiSenos.__name__
ARGS = '-pqh'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')