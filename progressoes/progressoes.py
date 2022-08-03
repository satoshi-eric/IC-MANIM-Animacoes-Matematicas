from manim import *
from pathlib import Path
import os

class Progressoes(Scene):
    def construct(self):
        self.abertura()
        self.intro()
        self.definicao_intuitiva()
        self.somatorio()
        self.progressao_geometrica()
        self.fechamento()

    def limpar_cena(self):
        self.play(FadeOut(*[mob for mob in self.mobjects]))

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
        explicacao_formula = Tex(r'\raggedright Com isso, podemos escrever uma função que calcule o tamanho do lado do n-ésimo quadrado dessa progressão. '
            ).scale(0.7).to_corner(UP)
        funcoes_exemplo = MathTex(r'f(1)=1\\f(2)=3\\f(3)=4\\f(4)=7').scale(0.7).shift(1.5*RIGHT)
        funcao = MathTex('f(n) = 1 + 2n').scale(0.7).shift(4*RIGHT)


        play(Write(introducao))
        play(FadeOut(introducao))
        play(Write(exemplo_text))
        play(Write(quadrados))
        play(FadeOut(exemplo_text))
        play(Write(definicao))
        play(FadeOut(definicao))
        play(Write(explicacao))
        play(quadrados.animate.shift(2*LEFT))
        play(FadeOut(explicacao))
        play(Write(funcoes_exemplo))
        play(Write(explicacao_formula))
        play(Write(funcao))
        self.limpar_cena()

    def definicao_intuitiva(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)

        duvida = Tex(r'\raggedright Mas como chegamos a essa função. Podemos visualizar melhor da seguinte forma.'
            ).scale(0.7).to_corner(UP)
        numeros = [
            Tex(f'{i}').scale(0.9).shift(2*LEFT + i*0.5*RIGHT)
            for i in range(1, 8, 2)
        ]
        steps = [
            ArcBetweenPoints(start=start.get_center() + 0.05*RIGHT, end=end.get_center() + 0.1*LEFT, color=YELLOW).shift(0.5*DOWN)
            for start, end in zip(numeros[:-1], numeros[1:])
        ]
        steps_number = [
            Tex(f'+2', color=YELLOW).scale(0.8).next_to(steps[i], DOWN, buff=0.3).shift(0.05*LEFT)
            for i in range(len(steps))
        ]
        visualizar = VGroup(*numeros, *steps, *steps_number)
        explicacao = Tex(r'\raggedright A progressão começa em 1 e aumenta de 2 em 2, logo, temos a fórmula:'
            ).scale(0.7).to_corner(UP)
        formula = MathTex(r'f(n) = 1 + 2n').scale(0.7).shift(0.5*UP)
        explicacao_formula = Tex(
            r'\raggedright Para escrever essa fórmula, precisamos do primeiro termo da progressão, no caso 1, e da diferença entre 2 termos, no caso 2. Com isso, escrevemos a seguinte fórmula.',
            'Usamos n-1 pois a progressão começa a partir da posição 0 em vez da 1.'
        ).scale(0.7).to_corner(UP)
        formula_geral = MathTex(r'a_{n} = a_{1} + (n - 1) \cdot r').scale(0.7).shift(0.5*RIGHT)
        termos = Tex(
            r'''
            \raggedright
            $f(n)$: n-ésimo termo da progressão \\
            $f(1)$: primeiro termo da progressão \\
            $n$: posição do termo na progressão \\
            $r$: razão
            '''
        ).scale(0.6).shift(RIGHT + 2*DOWN)
        
        play(Write(duvida))
        play(Write(visualizar))
        play(FadeOut(duvida))
        play(
            Write(explicacao),
            visualizar.animate.shift(4*LEFT)
        )
        play(Write(formula))
        play(FadeOut(explicacao))
        play(Write(explicacao_formula))
        play(Write(formula_geral))
        play(Write(termos))
        self.limpar_cena()

    def somatorio(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)

        introducao = Tex(
            r'\raggedright Além de calcular um dos termos, podemos o somatório de todos os elementos de uma P.A.',
            r'Considerando a P.A. 2 + (n - 1)*1, podemos representá-la da seguinte forma.',
            r'Podemos observar a formação de um trapézio. Ou seja, podemos calcular o somatório através de sua área.',
            r'Dessa forma, temos a seguinte fórmula:'
        ).scale(0.7).to_corner(UP)
        pontos = VGroup(*[
            VGroup(*[
                Dot().shift(0.5*j*RIGHT) for j in range(i)
            ]).shift(0.5*i* DOWN) for i in range(2, 6)
        ]).shift(UP + LEFT)
        pontos_labels = VGroup(*[
            Tex(f'{i}').scale(0.7).shift(0.5*i*DOWN)
            for i in range(2, 6)
        ]).next_to(pontos, LEFT, buff=0.5)
        conta = MathTex(r'\frac{(2+5)}{2} \cdot 4 = 14').scale(0.7)
        formula = MathTex(r'\frac{a_1 + a_n}{2} \cdot n').scale(0.7)

        play(Write(introducao[0]))
        play(Write(introducao[1]))
        play(Write(pontos), Write(pontos_labels))
        play(Write(introducao[2]))
        play(pontos.animate.shift(3.5*LEFT), pontos_labels.animate.shift(3.5*LEFT))
        play(Write(conta))
        play(Write(introducao[3]))
        play(ReplacementTransform(conta, formula))
        self.limpar_cena()


    def progressao_geometrica(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)

        introducao = Tex(r'\raggedright Além da progressão aritmética, temos a progressão geométrica. A ideia é usar multiplicação em vez de adição. Para calcular um elemento da progressão, usamos a seguinte fórmula.'
            ).scale(0.7).to_corner(UP)
        formula = MathTex(r'a_{n} = a_{1} \cdot r^{n-1}').scale(0.7)
        somatorio_label = Tex(r'Para calcular a soma dos números da PG, utilizamos a seguinte fórmula'
            ).scale(0.7).to_corner(UP)
        somatorio = MathTex(r'\frac{a_{1} \cdot r^{n-1}}{1-r}').scale(0.7)

        play(Write(introducao))
        play(Write(formula))
        self.limpar_cena()
        play(Write(somatorio_label))
        play(Write(somatorio))
        self.limpar_cena()



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