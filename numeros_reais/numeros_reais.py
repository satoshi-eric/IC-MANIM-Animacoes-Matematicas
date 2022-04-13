from manim import *
from pathlib import Path
import os

class Grade(VMobject):
    def __init__(self):
        super().__init__()
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

class NumerosReais(Scene):
    def construct(self):
        self.add(Grade())
        self.definicao()
        self.definicao_2()

    def definicao(self):
        def play(*anim, anim_time=2, wait_time=2):
            self.play(*anim, run_time=anim_time)
            self.wait(wait_time)

        introducao = Tex('\\raggedright Podemos definir os números \
             reais como o conjunto no qual qualquer \
             número inteiro ou decimal pertence a esse grupo.'
        ).scale(0.7).to_edge(UP)

        conjunto = VDict({
            'diagraama': Ellipse(2, 4),
            'numeros': VGroup(
                MathTex('1').scale(0.8),
                MathTex('2').scale(0.8),
                MathTex('2,71').scale(0.8),
                MathTex('3').scale(0.8),
                MathTex('3,14').scale(0.8),
            ).arrange(RIGHT, buff=0.5).shift(4*RIGHT),
        }, show_keys=False).shift(4*LEFT)

        play(Write(introducao))
        play(Write(conjunto['diagraama']))
        play(Write(conjunto['numeros']))
        for i in range(len(conjunto['numeros'])):
            play(
                MoveAlongPath(
                    conjunto['numeros'][i], 
                    ArcBetweenPoints(conjunto['numeros'][i].get_center(), 4*LEFT + 1.5*UP + 0.75*DOWN*i)
                ),
            )

        self.clear_scene()

    def definicao_2(self):
        def play(*anim, anim_time=2, wait_time=2):
            self.play(*anim, run_time=anim_time)
            self.wait(wait_time)

        introducao = Tex(
            '\\raggedright O conjunto do reais pode ser definido de outra forma, a união entre os conjuntos dos racionais e irracionais'
        ).scale(0.7).to_edge(UP)

        conjunto_racionais = Tex(
            '\\raggedright O conjunto dos racionais se refere ao conjunto dos números que podem ser representados por uma fração'
        ).scale(0.7).to_edge(UP)
        racionais_exemplo = MathTex(
            r'\frac{12}{10} = 1,2 = 1 + 0,2'
        ).scale(0.7).next_to(conjunto_racionais, DOWN)

        conjunto_irracionais = Tex(
            '\\raggedright O conjunto dos irracionais se refere ao conjunto dos números com casas decimais, mas não podem ser representados como fração.'
        ).scale(0.7).to_edge(UP)
        irracionais_exemplo = MathTex(
            r'\pi = 3,141592653589793... \\ e = 2,718281828459045...'
        ).scale(0.7).next_to(conjunto_irracionais, DOWN)

        diagrama_texto = Tex(
            'Dessa forma, temos o seguinte diagrama de Venn'
        ).scale(0.7).to_edge(UP)
        diagrama_venn = VDict({
            'reais': VDict({
                'diagrama': Ellipse(4, 5),
                'simbolo': MathTex(r'\mathbb{R}'),
            }),
            'racionais': VDict({
                'diagrama': Ellipse(2, 3).shift(2*RIGHT),
                'simbolo': MathTex(r'\mathbb{Q}')
            }),
            'irracionais': VDict({
                'diagrama': Ellipse(2, 2).shift(2*LEFT),
                'simbolo': MathTex(r'\mathbb{Z}')
            }),
        })

        play(Write(introducao))
        play(FadeOut(introducao))
        play(Write(conjunto_racionais))
        play(FadeOut(conjunto_racionais))
        play(Write(racionais_exemplo))
        play(FadeOut(racionais_exemplo))
        play(Write(conjunto_irracionais))
        play(FadeOut(conjunto_irracionais))
        play(Write(irracionais_exemplo))
        play(FadeOut(irracionais_exemplo))
        play(Write(diagrama_texto))
        play(Write(diagrama_venn['racionais']))
        play(Write(diagrama_venn['irracionais']))
        play(Write(diagrama_venn['reais']))
        # play(FadeOut(diagrama_texto))
        # play(FadeOut(diagrama_venn))

    def clear_scene(self):
        self.play(FadeOut(*[mob for mob in self.mobjects if type(mob) != Grade]))

ARQ_NOME = Path(__file__).resolve()
CENA = NumerosReais.__name__
ARGS = '-s'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')