from manim import *
from pathlib import Path
import os

class Progressoes(Scene):
    def construct(self):
        # self.abertura()
        self.intro()
        # self.fechamento()

    def intro(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)
        
        introducao = Tex(r'\raggedright Na vida real, existem diversos padrões que são identificados pelo ser humano. As progressões são um desses padrões.'
            ).scale(0.7).to_corner(UP)
        exemplo_text = Tex(r'\raggedright Na imagem a seguir, podemos perceber um padrão se repetindo. O tamanho dos lados dos quadrados está aumentando'
            ).scale(0.7).to_corner(UP)
        quadrados = VGroup(*[
            VGroup(
                Square(0.2*i).next_to(DOWN, UP, buff=0).shift(6*LEFT + 1.24**i*RIGHT + i*0.05*RIGHT),
                MathTex(f'{i}').scale(0.7).next_to(DOWN, DOWN, buff=0.3).shift(6*LEFT + 1.24**i*RIGHT + i*0.05*RIGHT),
            )
            for i in range(1, 8, 2)
        ]).add(Tex('...').next_to(DOWN, UP, buff=0)).shift(4.5*LEFT + 1.24**8*RIGHT + 8*0.05*RIGHT)
        definicao = Tex(r'\raggedright Podemos perceber que o lado dos quadrados está aumentando de 2 em 2. Essa é uma Progressão Aritmética (P.A.).'
            ).scale(0.7).to_corner(UP)
        explicacao = Tex(r'\raggedright Se listarmos os valores da progressão acima, temos:'
            ).scale(0.7).to_corner(UP)
        funcoes_exemplo = MathTex(r'f(1)=1\\f(2)=3\\f(3)=4\\f(4)=7').scale(0.7).shift(2*RIGHT)
        funcao = MathTex('f(n) = 1 + 2n')


        play(Write(introducao))
        play(FadeOut(introducao))
        play(Write(exemplo_text))
        play(Write(quadrados))
        play(FadeOut(exemplo_text))
        play(Write(definicao))
        play(FadeOut(definicao))
        play(Write(explicacao))
        play(quadrados.animate.shift(2*LEFT))
        play(Write(funcoes_exemplo))
        play()


        


    def abertura(self):
        titulo = Tex('Progressões').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)
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
CENA = Progressoes.__name__
ARGS = '-s'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')