"""
numeros naturais e inteiros:
1) na ilustração de operação menor-> colocar os carros do mesmo tamanho como no caso  da operação maior. OK

2) numeros inteiros: acho melhor não usar o desenho do carro quando falar dos inteiros. 
Quando vc mostra a reta dos interios usar uma flecha apontando para baixo no ligar do carro que 
fica deslocando da direita para a esquerda. OK

3) quando vc mostra que os naturais pertence no conjunto dos inteiros, não seria está contido ? 
Aqui seria legal colocar os números formando os dois conjuntos para indicar que o N está contido em Z. 
Ou ainda usar a reta dos inteiros para mostrar que o lado direito corresponde aos naturais. OK

4) seria bom indicar que o conjuntos do naturais se chama N e o dos inteiro Z em vez de apenas 
apresentar essas letras na ultima cena, a dos conjuntos um dentro do outro. OK

5) aumentar também um pouco as fontes e o tamanho dos objetos OK
"""
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


class Carro(VGroup):
    def __init__(self, cor=BLUE, **kwargs):
        super().__init__(**kwargs)
        corpo = Union(
            Difference(
                Difference(
                    Rectangle(width=4.5, height=1), 
                    Circle(radius=0.5).shift(0.5*DOWN + 1.25*RIGHT), 
                ),
                Circle(radius=0.5).shift(0.5*DOWN + 1.25*LEFT)
            ).set_fill(color=cor, opacity=0.5),
            Difference(
                Difference(
                    ArcBetweenPoints(0.5*UP + 1.3*LEFT, 0.5*UP + 1.3*RIGHT, angle=-135*DEGREES),
                    Difference(
                        ArcBetweenPoints(0.5*UP + LEFT, 0.5*UP + RIGHT, angle=-145*DEGREES),
                        Square().shift(0.9*RIGHT + 0.3*UP)
                    ),  
                ),
                Difference(
                    ArcBetweenPoints(0.5*UP + LEFT, 0.5*UP + RIGHT, angle=-145*DEGREES),
                    Square().shift(0.9*LEFT + 0.3*UP)
                ),
            )
        ).set_color(color=cor).set_fill(color=cor, opacity=0.9)

        rodas = VGroup(
            Difference(
                Circle(radius=0.4).shift(0.55*DOWN + 1.25*RIGHT),
                Circle(radius=0.25).shift(0.55*DOWN + 1.25*RIGHT)
            ).set_fill(color=GRAY, opacity=1).set_color(color=GRAY),
            Difference(
                Circle(radius=0.4).shift(0.55*DOWN + 1.25*LEFT),
                Circle(radius=0.25).shift(0.55*DOWN + 1.25*LEFT)
            ).set_fill(color=GRAY, opacity=1).set_color(color=GRAY),
        )

        self.add(
            corpo,
            rodas
        )


class Lapis(VGroup):
    def __init__(self, cor=YELLOW, **kwargs):
        super().__init__(**kwargs)
        corpo = Rectangle(width=0.5, height=4).set_fill(color=cor, opacity=0.9).set_stroke(color=WHITE, width=3)
        linhas = VGroup(
            *[    
                Line(start=1.99*UP + 0.125*LEFT + 0.125*i*RIGHT, end=1.99*DOWN + 0.125*LEFT + 0.125*i*RIGHT)
                    .set_color(WHITE).set_stroke(width=4)
                for i in range(3)
            ]
        )
        ponta = VGroup(
            Polygon(
                (-0.25, -2, 0),
                (0.25, -2, 0),
                (0.05, -2.5, 0),
                (-0.05, -2.5, 0),
            ).set_fill(color=LIGHT_PINK, opacity=1).set_color(color=LIGHT_PINK),
            Polygon(
                (0.05, -2.5, 0),
                (0, -2.65, 0),
                (-0.05, -2.5, 0),
            ).set_fill(color=cor, opacity=1).set_color(color=cor)
        )


        self.add(
            corpo,
            linhas, 
            ponta
        )

    def scale(self, scale_factor):
        super().scale(scale_factor)
        for linha in self[1]:
            linha.set_stroke(width=4*scale_factor)
        for poligono in self[2]:
            poligono.set_stroke(width=6*scale_factor)
        return self


class NumerosNaturaisEInteiros(Scene):
    def construct(self):
        # self.add(Grade())
        self.abertura()
        self.introducao()
        self.conjunto_naturais()
        self.operacoes()
        self.relacoes()
        self.numeros_inteiros()
        self.reta_inteiros()
        self.conjuntos_pertence()
        self.fechamento()

    def limpar_cena(self):
        self.play(FadeOut(*self.mobjects))

    def introducao(self):
        def play(*anim, t=2, wait_time=2):
            self.play(*anim, run_time=t)
            self.wait(wait_time)

        texto_introducao = Tex(
            'Números naturais são utilizados para contar quantidades.'
        ).scale(0.7).shift(3*UP + 2.5*LEFT)

        carros = VGroup(
            Carro(color=BLUE).shift(5*LEFT + UP).scale(0.35),
            Carro(color=RED).shift(5*LEFT).scale(0.35),
            Carro(color=GREEN).shift(5*LEFT + DOWN).scale(0.35),
        )
        destaque_1 = SurroundingRectangle(carros, buff=0.2)
        qtd_1 = MathTex('3').shift(3.5*LEFT)

        conjunto_lapis = VGroup(
            *[
                Lapis(color=YELLOW).shift(0.5*UP + LEFT + 0.5*i*RIGHT).scale(0.5)
                for i in range(5)
            ]
        )
        destaque_2 = SurroundingRectangle(conjunto_lapis, buff=0.2)
        qtd_2 = MathTex('4').shift(2*RIGHT)

        play(Write(texto_introducao))

        for carro in carros:
            play(FadeIn(carro), wait_time=1)
        
        play(Write(qtd_1))
        play(
            Write(destaque_1),
            qtd_1.animate.scale(3/2).set_color(YELLOW)
        )
        play(qtd_1.animate.scale(2/3).set_color(WHITE))
        
        for lapis in conjunto_lapis:
            play(FadeIn(lapis), wait_time=1)

        play(Write(qtd_2))
        play(
            Write(destaque_2),
            qtd_2.animate.scale(3/2).set_color(YELLOW)
        )
        play(qtd_2.animate.scale(2/3).set_color(WHITE))

        self.limpar_cena()

    def conjunto_naturais(self):
        def play(*anim, t=2, wait_time=2):
            self.play(*anim, run_time=t)
            self.wait(wait_time)

        texto_introducao = Tex(r'\raggedright Os números naturais pertencem a um conjunto, \\o conjunto dos números naturais chamado $\mathbb{N}$ ')\
            .scale(0.7).shift(3*UP + 3*LEFT)
        conjunto_elipse = Ellipse(width=1, height=3)\
            .set_stroke(color=ORANGE).shift(5*LEFT + 0.5*UP)
        conjunto_numeros = VGroup(
            *[
                MathTex(str(i)).scale(0.5).shift(LEFT + 0.5*i*RIGHT)
                for i in range(5)
            ]
        ).add(MathTex('...').shift(LEFT + 0.5*5*RIGHT)).shift(3*LEFT + 0.5*UP)

        texo_representacao = Tex(r'\raggedright Representamos ele da seguinte forma:')\
            .scale(0.7).shift(2*DOWN + 3.5*LEFT)

        representacao_conjunto = MathTex(r'\mathbb{N} = \{ 0, 1, 2, 3, 4, ... \}')\
            .scale(0.5).shift(2.5*DOWN + 4.4*LEFT)

        play(Write(texto_introducao))
        play(Write(conjunto_elipse))
        play(Write(conjunto_numeros))

        for i, numero in enumerate(conjunto_numeros):
            if i == len(conjunto_numeros) - 1:
                play(ReplacementTransform(conjunto_numeros[i], conjunto_elipse.set_fill(color=ORANGE, opacity=0.25)))
            else:
                play(
                    MoveAlongPath(
                        numero,
                        path=ArcBetweenPoints(
                            numero.get_center(),
                            5*LEFT + 1.5*UP + 0.5*i*DOWN
                        )
                    ),
                    conjunto_numeros[i+1:].animate.shift(0.5*LEFT)
                )

        play(Write(texo_representacao))
        play(Write(representacao_conjunto))

        self.limpar_cena()

    def operacoes(self):
        def play(*anim, t=2, wait_time=2):
            self.play(*anim, run_time=t)
            self.wait(wait_time)

        ###################################################
        introducao = Tex('Podemos realizar operações entre os números.')\
            .scale(0.7).shift(3*UP + 3*LEFT)

        ###################################################

        ######################## Adição ###########################
        texto_adicao = Tex(r'$\bullet$ Adição')\
            .scale(0.7).shift(2.5*UP + 4.7*LEFT)
        lapis_adicao = VGroup(
            Lapis(cor=YELLOW).shift(5*LEFT + 1.5*UP).scale(0.2),
            MathTex('+').shift(4.5*LEFT + 1.25*UP),
            Lapis(cor=YELLOW).shift(4*LEFT + 1.5*UP).scale(0.2),
            MathTex('=').shift(3.5*LEFT + 1.25*UP),
            Lapis(cor=YELLOW).shift(3*LEFT + 1.5*UP).scale(0.2),
            Lapis(cor=YELLOW).shift(2.5*LEFT + 1.5*UP).scale(0.2),
        )
        num1_adicao = MathTex('1').shift(5*LEFT + 0.25*UP)
        num2_adicao = MathTex('1').shift(4*LEFT + 0.25*UP)
        resultado_adicao = MathTex('2').shift(2.75*LEFT + 0.25*UP)

        ###################################################

        ######################## Subtração ###########################
        texto_subtracao = Tex(r'$\bullet$ Subtração')\
            .scale(0.7).shift(2.5*UP + 2*RIGHT)
        lapis_subtracao = VGroup(
            Lapis(cor=RED).shift(2*RIGHT + 1.5*UP).scale(0.2),
            Lapis(cor=RED).shift(2.5*RIGHT + 1.5*UP).scale(0.2),
            MathTex('-').shift(3*RIGHT + 1.25*UP),
            Lapis(cor=RED).shift(3.5*RIGHT + 1.5*UP).scale(0.2),
            MathTex('=').shift(4*RIGHT + 1.25*UP),
            Lapis(cor=RED).shift(4.5*RIGHT + 1.5*UP).scale(0.2),
        )
        num1_subtracao = MathTex('2').shift(2.25*RIGHT + 0.25*UP)
        num2_subtracao = MathTex('1').shift(3.5*RIGHT + 0.25*UP)
        resultado_subtracao = MathTex('1').shift(4.5*RIGHT + 0.25*UP)

        ###################################################

        ######################## Multiplicação ###########################
        texto_multiplicacao = Tex(r'$\bullet$ Multiplicação')\
            .scale(0.7).shift(0.5*DOWN + 4.7*LEFT)
        lapis_multiplicacao = VGroup(
            Lapis(cor=BLUE).shift(5*LEFT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(4.5*LEFT + 1.5*DOWN).scale(0.2),
            MathTex('\cdot').shift(4*LEFT + 1.75*DOWN),
            MathTex('3').shift(3.5*LEFT + 1.75*DOWN),
            MathTex('=').shift(3*LEFT + 1.75*DOWN),
            Lapis(cor=BLUE).shift(2.5*LEFT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(2.2*LEFT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(1.9*LEFT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(1.6*LEFT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(1.3*LEFT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(1*LEFT + 1.5*DOWN).scale(0.2),
        )
        num_multiplicacao = MathTex('2').shift(4.75*LEFT + 2.7*DOWN)
        resultado_multiplicacao = MathTex('6').shift(1.75*LEFT + 2.7*DOWN)

        ###################################################

        ######################## Divisão ###########################
        texto_divisao = Tex(r'$\bullet$ Divisão')\
            .scale(0.7).shift(0.5*DOWN + 1.9*RIGHT)
        lapis_divisao = VGroup(
            Lapis(cor=BLUE).shift(2*RIGHT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(2.3*RIGHT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(2.6*RIGHT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(2.9*RIGHT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(3.2*RIGHT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(3.5*RIGHT + 1.5*DOWN).scale(0.2),
            VGroup(
                Line().scale(0.3), Dot().shift(0.3*UP), Dot().shift(0.3*DOWN)
            ).scale(0.5).shift(4*RIGHT + 1.75*DOWN),
            MathTex('3').shift(4.5*RIGHT + 1.75*DOWN),
            MathTex('=').shift(5*RIGHT + 1.75*DOWN),
            Lapis(cor=BLUE).shift(5.5*RIGHT + 1.5*DOWN).scale(0.2),
            Lapis(cor=BLUE).shift(6*RIGHT + 1.5*DOWN).scale(0.2),
        )
        num_divisao = MathTex('6').shift(2.7*RIGHT + 2.7*DOWN)
        resultado_divisao = MathTex('2').shift(5.75*RIGHT + 2.7*DOWN)
        

        ###################################################

    
        play(Write(introducao))
        play(Write(texto_adicao))
        play(Write(lapis_adicao))
        play(
            Write(num1_adicao), 
            Write(num2_adicao), 
            Write(resultado_adicao)
        )
        play(Write(texto_subtracao))
        play(Write(lapis_subtracao))
        play(
            Write(num1_subtracao),
            Write(num2_subtracao),
            Write(resultado_subtracao)
        )
        play(Write(texto_multiplicacao))
        play(Write(lapis_multiplicacao))
        play(
            Write(num_multiplicacao),
            Write(resultado_multiplicacao)
        )
        play(Write(texto_divisao))
        play(Write(lapis_divisao))
        play(
            Write(num_divisao),
            Write(resultado_divisao)
        )

        self.limpar_cena()
        

    def relacoes(self):
        def play(*anim, t=2, wait_time=2):
            self.play(*anim, run_time=t)
            self.wait(wait_time)

        introducao = Tex('Também podemos realizar \
            operações de relações entre eles.') \
                .scale(0.7).move_to(3*UP + 3*LEFT)
        
        texto_maior = Tex(r'$\bullet$ Operador maior:') \
            .scale(0.7).move_to(2*UP + 4.5*LEFT)
        relacao_maior = VGroup(
            VGroup(
                Carro(),
                Carro().shift(3*DOWN)
            ).scale(0.3).move_to(1.2*LEFT),
            MathTex('>'),
            VGroup(
                Carro()
            ).scale(0.3).move_to(1.2*RIGHT)
        ).move_to(0.7*UP + 3.5*LEFT)
        numeros_maior = VGroup(
            MathTex('2').scale(0.7),
            MathTex('1').scale(0.7).shift(2.4*RIGHT)
        ).move_to(0.5*DOWN + 3.5*LEFT)

        texto_menor = Tex(r'$\bullet$ Operador menor') \
            .scale(0.5).move_to(2*UP + RIGHT)
        relacao_menor = VGroup(
            VGroup(
                Carro()
            ).scale(0.3).move_to(1.2*LEFT),
            MathTex('<'),
            VGroup(
                Carro().scale(0.7),
                Carro().scale(0.7).shift(3*DOWN)
            ).scale(0.3).move_to(1.2*RIGHT)
        ).move_to(0.7*UP + 2*RIGHT)
        numeros_menor = VGroup(
            MathTex('1').scale(0.7),
            MathTex('2').scale(0.7).shift(2.4*RIGHT)
        ).move_to(0.5*DOWN + 2.2*RIGHT)


        texto_igual = Tex(r'$\bullet$ Operador igual') \
            .scale(0.7).move_to(4.5*LEFT + 1.3*DOWN)
        relacao_igual = VGroup(
            Carro().scale(0.3).move_to(1.2*LEFT),
            MathTex('='),
            Carro().scale(0.3).move_to(1.2*RIGHT)
        ).move_to(3.5*LEFT + 2.2*DOWN)
        numeros_igual = VGroup(
            MathTex('1').scale(0.7),
            MathTex('1').scale(0.7).shift(2.4*RIGHT)
        ).move_to(3*DOWN + 3.5*LEFT)

        play(Write(introducao))
        play(Write(texto_maior))
        play(Write(relacao_maior))
        play(FadeIn(numeros_maior))
        play(Write(texto_menor))
        play(Write(relacao_menor))
        play(FadeIn(numeros_menor))
        play(Write(texto_igual))
        play(Write(relacao_igual))
        play(FadeIn(numeros_igual))

        self.limpar_cena()

    def numeros_inteiros(self):
        play = lambda *anim, t=2, wait_time=2: self.play(*anim, run_time=t)

        introducao = Tex(
            '\\raggedright Número inteiros são números positivos \
            ou negativos sem casa decimal e pertencem ao conjunto dos \
            inteiros chamado $\\mathbb{Z}$. Podemos \
            asssociar números positivos ao ganho e \
            números negativos à perda.'
        ).scale(0.7).move_to(3*UP)
        positivo = MathTex('+3')
        negativo = MathTex('-2')
        carros = VGroup(
            Carro().scale(0.3).shift(UP),
            Carro().scale(0.3),
            Carro().scale(0.3).shift(DOWN),
        ).shift(3*LEFT)

        play(Write(introducao), t=4)
        play(FadeIn(positivo))
        play(FadeIn(carros))
        play(FadeOut(positivo))
        play(FadeIn(negativo))
        play(FadeOut(carros[-1], carros[-2]))
        play(FadeOut(negativo))

        self.limpar_cena()

    def reta_inteiros(self):
        play = lambda *anim, t=2, wait_time=2: self.play(*anim, run_time=t)
        introducao = Tex(
            f'\\raggedright Podemos representar os números naturais com a reta dos naturais.', 
            f' Com a parte negativa, temos a reta dos inteiros.',
            f' Com ela, podemos representar o deslocamento de um objeto como um carro.'
        ).scale(0.7).shift(3*UP)
        reta_naturais = NumberLine(x_range=(0, 4, 1), include_numbers=True).shift(2*RIGHT)
        reta_inteiros_negativo = NumberLine(x_range=(-4, 0, 1), include_numbers=True).shift(2*LEFT)
        carro = Carro().scale(0.25).shift(0.5*UP)
        seta = Arrow(DOWN, ORIGIN).shift(0.7*DOWN)
        movimentos = (
            +3,
            -2,
            +1,
            -3,
        )

        def criar_movimento(movimento):
            if movimento <= 0:
                return MathTex(str(movimento)).scale(0.7).shift(5*RIGHT + 2*UP)
            else:
                return MathTex('+' + str(movimento)).scale(0.7).shift(5*RIGHT + 2*UP)

        m_movimentos = list(map(criar_movimento, movimentos))
        
        obs = Tex('Obs: Perceba que não é possível parar entre os números. Isso porque eles são números inteiros')\
            .scale(0.7).move_to(2*DOWN)

        play(Write(introducao[0]))
        play(FadeIn(reta_naturais))
        play(Write(introducao[1]))
        play(FadeIn(reta_inteiros_negativo))
        play(Write(introducao[2]))
        play(Write(carro), Write(seta))
        
        for movimento, m_movimento in zip(movimentos, m_movimentos):
            play(FadeIn(m_movimento))
            play(
                carro.animate.shift(movimento*RIGHT),
                seta.animate.shift(movimento*RIGHT)
            )
            play(FadeOut(m_movimento))

        play(Write(obs))

        self.limpar_cena()

    def conjuntos_pertence(self):
        play = lambda *anim, t=2, wait_time=2: self.play(*anim, run_time=t)

        introducao = Tex('\\raggedright O conjunto dos números naturais está contido \\\\ no conjunto dos inteiros.')\
            .scale(0.7).shift(3*UP)
        conjuntos_aninhados = VGroup(
            VGroup(
                Ellipse(2.5, 3),
                MathTex('\\mathbb{Z}').shift(0.8*RIGHT)
            ),
            VGroup(
                Ellipse(1.5, 2).shift(0.25*LEFT),
                MathTex('\\mathbb{N}').shift(0.25*LEFT)
            )
        )

        play(Write(introducao))
        play(FadeIn(conjuntos_aninhados))

        self.limpar_cena()

    def abertura(self):
        titulo = Tex('Números naturais e inteiros').scale(2).set_color("#dc6a40").move_to(0.5*UP)
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
        self.wait(2)




ARQ_NOME = Path(__file__).resolve()
CENA = NumerosNaturaisEInteiros.__name__
ARGS = '-pqh'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')