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
        ).scale(0.5).to_edge(UP)

        conjunto = VDict({
            'diagraama': Ellipse(2, 4),
            'numeros': VGroup(
                MathTex('1'),
                MathTex('2'),
                MathTex('2,71'),
                MathTex('3'),
                MathTex('3,14')
            ).arrange(RIGHT, buff=0.5).shift(4*RIGHT),
        }, show_keys=False).shift(4*LEFT)

        play(Write(introducao))
        play(Write(conjunto['diagraama']))
        play(Write(conjunto['numeros']))
        for i in range(len(conjunto['numeros'])):
            play(
                MoveAlongPath(
                    conjunto['numeros'][i], 
                    ArcBetweenPoints(conjunto['numeros'][i].get_center(), 4*LEFT + 1.5*UP + 0.5*DOWN*i)
                ),
            )

    def definicao_2(self):
        introducao = Tex('\\raggedright O conjunto do reais pode ser definido de outra forma, a união entre os conjuntos dos racionais e irracionais')

        conjunto_racionais = Tex('O conjunto dos racionais se refere ao conjunto dos números que podem ser representados por uma fração')
        racionais_exemplo = MathTex(r'\frac{12}{10} = 1,2 = 1 + 0,2')

        conjunto_irracionais = Tex('O conjunto dos irracionais se refere ao conjunto dos números com casas decimais, mas não podem ser representados como fração.')
        irracionais_exemplo = MathTex(r'\pi = 3,141592653589793 \\ e = 2,718281828459045')

        diagrama_texto = Tex('Dessa forma, temos o seguinte diagrama de Venn')
        diagrama_venn = VDict({
            'reais': VDict({
                'diagrama': Ellipse(2, 4),
                'simbolo': Tex(r'\mathbb{R}'),
            }),
            'racionais': VDict({
                'diagrama': Ellipse(2, 3),
                'simbolo': Tex(r'\mathbb{Q}')
            }),
            'irracionais': VDict({
                'diagrama': Ellipse(2, 2),
                'simbolo': Tex(r'\mathbb{Z}')
            }),
            'inteiros': VDict({
                'diagrama': Ellipse(2, 2),
                'simbolo': Tex(r'\mathbb{Z}')
            }),
            'naturais': VDict({
                'diagrama': Ellipse(2, 1),
                'simbolo': Tex(r'\mathbb{N}')
            })
        })

ARQ_NOME = Path(__file__).resolve()
CENA = NumerosReais.__name__
ARGS = '-pql'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')