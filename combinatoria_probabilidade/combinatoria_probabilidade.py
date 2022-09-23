from manim import *
from pathlib import Path
import os


class Camiseta(Polygon):
    def __init__(self, color=BLUE, fill_color=BLUE, fill_opacity=1, **kwargs):
        vertices = [
            ORIGIN, 4*RIGHT, 6*RIGHT + 2*DOWN, 5*RIGHT + 3*DOWN, 4*RIGHT + 2*DOWN, 4*RIGHT + 7*DOWN,
            7*DOWN, 2*DOWN, 3*DOWN + LEFT, 2*DOWN + 2*LEFT, ORIGIN
        ]
        super().__init__(*vertices, color=color, fill_opacity=fill_opacity, **kwargs)
        self.scale(0.25).shift(2*LEFT + 4*UP).set_fill(fill_color)


class Calca(Polygon):
    def __init__(self, color=BLUE, fill_color=BLUE, fill_opacity=1, **kwargs):
        vertices = [
            ORIGIN, 6*RIGHT, 6*RIGHT + 9*DOWN, 4*RIGHT + 9*DOWN, 3*RIGHT+DOWN, 2*RIGHT + 9*DOWN, 9*DOWN, ORIGIN
        ]
        super().__init__(*vertices, color=color, fill_opacity=fill_opacity, **kwargs)
        self.scale(0.15).shift(2*LEFT + 4*UP).set_fill(fill_color)


class Dado(VGroup):
    def __init__(self, side_length=2, number=1,  *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        self.add(Square(side_length))
        if number == 1:
            self.add(Dot(self.get_center()))
        elif number == 2:
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*RIGHT))
        elif number == 3:
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*RIGHT))
            self.add(Dot())
        elif number == 4:
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*RIGHT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*RIGHT))
        elif number == 5:
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*RIGHT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*RIGHT))
            self.add(Dot())
        elif number == 6:
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*UP + 0.3*side_length*RIGHT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*DOWN + 0.3*side_length*RIGHT))
            self.add(Dot(0.3*side_length*LEFT))
            self.add(Dot(0.3*side_length*RIGHT))


class Sorvete2Sabores(VGroup):
    def __init__(self, color1=DARK_BROWN, color2=PINK, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        self.add(Arc(radius=0.2, start_angle=-45*DEGREES, angle=270*DEGREES, color=color1, fill_color=color1, fill_opacity=1).shift(0.1*UP))
        self.add(Arc(radius=0.2, start_angle=-45*DEGREES, angle=270*DEGREES, color=color2, fill_color=color2, fill_opacity=1).shift(0.4*UP))
        self.add(Polygon(0.2*LEFT, 0.2*RIGHT, DOWN, color='#e0a510', fill_color='#e0a510', fill_opacity=1))


class CombinatoriaProbabilidade(Scene):
    def construct(self):
        self.abertura()
        self.intro_combinatoria()
        self.permutacoes()
        self.combinacoes()
        self.intro_probabilidade()
        self.exemplo_probabilidade()
        self.fechamento()


    def limpar_cena(self):
        self.play(FadeOut(*[mob for mob in self.mobjects]))
        self.wait()

    def intro_combinatoria(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)
        introducao = Tex(
            r'\raggedright Problemas de contagem aparecem frequentemente no cotidiano. É isso que a Combinatória estuda.', 
            'Por exemplo, de quantas formas podemos combinar 2 calças e 3 camisetas. Podemos visualizar com o seguinte esquema.'
        ).scale(0.7).to_corner(UP)
        principio_fundamental_contagem = Tex(
            r'\raggedright É isso que o princípio fundamental da contagem fala. Se há $x$ modos de tomar uma decisão $D_1$ e $y$ modos de tomar a decisão $D_2$, então o número de tomar sucessivamente as decisões é $x \cdot y$'
        ).scale(0.7).to_corner(DOWN)

        esquema_roupas = VGroup(
            Calca().scale(0.7),
            Calca(color=RED, fill_color=RED).shift(4*RIGHT).scale(0.7),
            Camiseta().scale(0.5).shift(0.1*LEFT + 3*DOWN),
            Camiseta(RED, RED).scale(0.5).shift(RIGHT + 3*DOWN),
            Camiseta(YELLOW, YELLOW).scale(0.5).shift(2.1*RIGHT + 3*DOWN),
            Camiseta(BLUE, BLUE).scale(0.5).shift(3.9*RIGHT + 3*DOWN),
            Camiseta(RED, RED).scale(0.5).shift(5*RIGHT + 3*DOWN),
            Camiseta(YELLOW, YELLOW).scale(0.5).shift(6.1*RIGHT + 3*DOWN),
            Line(RIGHT+DOWN, 0.1*LEFT + 2*DOWN),
            Line(RIGHT+DOWN, RIGHT + 2*DOWN),
            Line(RIGHT+DOWN, 2.1*RIGHT + 2*DOWN),
            Line(RIGHT+DOWN, 0.1*LEFT + 2*DOWN).shift(4*RIGHT),
            Line(RIGHT+DOWN, RIGHT + 2*DOWN).shift(4*RIGHT),
            Line(RIGHT+DOWN, 2.1*RIGHT + 2*DOWN).shift(4*RIGHT),
        ).shift(3*LEFT + 1.5*UP)

        play(Write(introducao), run=3, wait=5)
        play(FadeIn(esquema_roupas))
        play(Write(principio_fundamental_contagem), run=3, wait=5)
        self.limpar_cena()

    def permutacoes(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)

        intro = Tex(
            r'\raggedright Ainda existem outros problemas de combinatória: Permutações e Combinações'
        ).scale(0.7).to_corner(UP)
        exemplo_intro = Tex(
            r'\raggedright Um problema clássico de permutação é o de anagramas. Por exemplo, quantos são os anagramas da palavra "calor"? '
        ).scale(0.7).to_corner(UP)

        explicacao = [
            Tex(r'\raggedright Para a primeira letra, podemos selecionar qualquer uma das 5. Então fixamos a primeira.').scale(0.7).to_corner(DOWN),
            Tex(r'\raggedright Para a segunda, como já usamos 1 letra, podemos escolher apenas entre 4. Então fixamos ela.').scale(0.7).to_corner(DOWN),
            Tex(r'\raggedright Para a terceira, já usamos 2 letras, podemos escolher apenas entre 3 e assim por diante.').scale(0.7).to_corner(DOWN),
        ]

        cada_letra = VGroup(
            VGroup(
                Tex('C').shift(2.5*LEFT),
                Tex('A').shift(2.5*LEFT + 0.7*DOWN),
                Tex('L').shift(2.5*LEFT + 1.4*DOWN),
                Tex('O').shift(2.5*LEFT + 2.1*DOWN),
                Tex('R').shift(2.5*LEFT + 2.8*DOWN)
            ),
            VGroup(
                Tex('A').shift(1.5*LEFT),
                Tex('L').shift(1.5*LEFT + 0.7*DOWN),
                Tex('O').shift(1.5*LEFT + 1.4*DOWN),
                Tex('R').shift(1.5*LEFT + 2.1*DOWN),
            ),
            VGroup(
                Tex('L').shift(0.5*LEFT),
                Tex('O').shift(0.5*LEFT + 0.7*DOWN),
                Tex('R').shift(0.5*LEFT + 1.4*DOWN),
            ),
            VGroup(
                Tex('O').shift(0.5*RIGHT),
                Tex('R').shift(0.5*RIGHT + 0.7*DOWN),
            ),
            VGroup(
                Tex('R').shift(1.5*RIGHT),
            ),
        ).shift(1.5*UP + 2*LEFT).set_color(RED)

        numeros_permutacoes = VGroup(
            MathTex('5').next_to(cada_letra[0], DOWN, buff=0.5),
            MathTex('4').next_to(cada_letra[0], DOWN, buff=0.5).shift(RIGHT),
            MathTex('3').next_to(cada_letra[0], DOWN, buff=0.5).shift(2*RIGHT),
            MathTex('2').next_to(cada_letra[0], DOWN, buff=0.5).shift(3*RIGHT),
            MathTex('1').next_to(cada_letra[0], DOWN, buff=0.5).shift(4*RIGHT),
        ).set_color(BLUE)

        resultado = VGroup(*[
            MathTex(r'\cdot').move_to(numeros_permutacoes[0].get_center() + 0.5*RIGHT + i*RIGHT)
            for i in range(4)
        ]).add(Tex(' $ = 5! = 120$ combinações')
            .move_to(numeros_permutacoes[-1].get_center() + 3*RIGHT)).set_color(BLUE)

        espacos_letras = VGroup(*[
            Line(ORIGIN, 0.8*RIGHT).shift(2.5*LEFT + i*RIGHT) for i in range(5)
        ]).shift(0.4*LEFT + 1.15*UP).shift(2*LEFT).set_color(YELLOW)

        obs = Tex(
            r'\raggedright O símbolo representa a operação fatorial que como mostrada acima multiplica o número por todos seus antecessores até $1$.'
        ).scale(0.7).to_corner(DOWN)


        play(Write(intro))
        play(FadeOut(intro))
        play(Write(exemplo_intro), run=3, wait=3)
        play(Write(espacos_letras))
        for i in range(5):
            if i == 0:
                play(Write(explicacao[0]), wait=3)
                play(FadeOut(explicacao[0]))
            if i == 1:
                play(Write(explicacao[1]), wait=3)
                play(FadeOut(explicacao[1]))
            if i == 2:
                play(Write(explicacao[2]), wait=3)
                play(FadeOut(explicacao[2]))
            play(Write(cada_letra[i]), wait=3)
            play(Write(numeros_permutacoes[i]), wait=3)
        play(Write(resultado))
        play(Write(obs), wait=4)
        self.limpar_cena()

    def combinacoes(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)

        intro = Tex(
            r'\raggedright Também existe o problema das combinações. Por exemplo, em uma sorveteria que vende 6 sabores de sorvetes, de quantas formas podemos montar uma casquinha de 2 sabores diferentes?',
            r' Teríamos as seguintes combinações:'
        ).scale(0.7).to_corner(UP)

        cores = [PINK, BLUE, GREEN, YELLOW, ORANGE, PURPLE]
        sabores = [
            {'sabor1': cores[i], 'sabor2': cores[j]}
            for i in range(len(cores))
            for j in range(i+1, len(cores))
        ]
        sorvetes = VGroup(*[
            Sorvete2Sabores(color1=sabor['sabor1'], color2=sabor['sabor2']).shift(UP + 5*LEFT + i*0.7*RIGHT)
            for i, sabor in enumerate(sabores)
        ])

        formula = Tex(
            r'\raggedright Mas como calculá-las. Usamos a fórmula $C^{p}_{n} = \begin{pmatrix} n \\ p \end{pmatrix} = \frac{n!}{p!(n - p)!}$ para isso. ',
            r'Podemos ler como de n sabores, escolhe p sabores. ', 
            r'e temos $C^{2}_{6} = \frac{6!}{2!(6 - 2)!} = 15$ sabores.'
        ).scale(0.7).next_to(sorvetes, DOWN, buff=0.5)
        

        play(Write(intro[0]), wait=4)
        play(Write(intro[1]))
        play(FadeIn(sorvetes), run=2, wait=3)
        play(Write(formula[0]), run=2, wait=3)
        play(Write(formula[1]), run=2, wait=3)
        play(Write(formula[2]), run=2, wait=3)
        self.limpar_cena()


    def intro_probabilidade(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)

        intro = Tex(
            r'\raggedright Uma área bem relacionada com a combinatória é a probabilidade, que estuda a chance de um determinado evento acontecer. No cotidiano, existem diversos eventos aleatórios como o lançamento de um dado ou de uma moeda. As chances de ganhar na megasena, etc.'
        ).scale(0.7).to_corner(UP)
        conceitos = Tex(
            r'''Antes de começarmos a ver as fórmulas, vamos definir alguns conceitos.
            
            \raggedright \quad $\bullet$ Experiência aleatória: experimento que gera um resultado imprevisível \\
            \raggedright \quad $\bullet$ Espaço amostral: conjunto de todos os resultados possíveis \\
            \raggedright \quad $\bullet$ Evento: subconjunto do espaço amostral \\
            
            '''
        ).scale(0.7).next_to(intro, DOWN, buff=1.2)
        
        definicao = Tex(r'\raggedright A probabilidade de ocorrer um evento A é dado por:').scale(0.7).to_corner(UP)
        formula = MathTex(r'P(A)', '=', r'{n(A)', r'\over', r'n(\Omega)}').next_to(definicao, DOWN, buff=1)
        formula[0].set_color(YELLOW)
        formula[2].set_color(BLUE)
        formula[4].set_color(RED)
        items = Tex(
            '\\raggedright $\\bullet$ $P(A)$: ', 'probabilidade do evento ocorrer \n\n ',
            '$\\bullet$ $n(A)$: ', 'número de resultados favoráveis. Quantidade de elementos no evento. \n\n ',
            '$\\bullet$ $n(\Omega)$: ', 'número de resultados possíveis. Quantidade de elementos do espaço amostral. \n\n ',
        ).scale(0.6).next_to(formula, DOWN, buff=1)
        items[0].set_color(YELLOW)
        items[2].set_color(BLUE)
        items[4].set_color(RED)
        obs = Tex(
            r'\raggedright Obs: quando não sabemos o espaço amostral ou evento, usamos a combinatória para calculá-los.'
        ).scale(0.7).to_corner(DOWN)

        play(Write(intro),run=4, wait=10)
        play(Write(conceitos), run=4, wait=10)
        self.limpar_cena()
        play(Write(definicao))
        play(Write(formula))
        play(Write(items), run=3, wait=7)
        play(Write(obs))
        self.limpar_cena()

    def exemplo_probabilidade(self):
        def play(*anim, run=2, wait=2):
            self.play(*anim, run_time=run)
            self.wait(wait)
        
        intro = Tex(
            r'\raggedright Por exemplo, ao jogar um dado, qual a probabilidade do resultado ser um número par.'
        ).scale(0.7).to_corner(UP)
        intro_exemplo = Tex(
            r'\raggedright Temos seguinte espaço amostral:'
        ).scale(0.7).next_to(intro, DOWN, buff=0.7)
        espaco_amostral = VGroup(*[
            Dado(number=i).scale(0.3).move_to(0.5*UP + 3*LEFT + i*0.7*RIGHT).set_color(BLUE) for i in range(1, 7)
        ])
        explicacao_exemplo = Tex(
            r'\raggedright Desse conjunto, pegamos o subconjunto que possui os números pares, ou seja, o evento:'
        ).scale(0.7).move_to(intro_exemplo)
        evento = espaco_amostral[0::2].copy().set_color(YELLOW)
        resultado = Tex(
            r'Assim, a probabilidade de sair um dado par é '
        ).scale(0.7).to_corner(DOWN).shift(0.5*UP + LEFT)
        resultado_formula = MathTex(r'\frac{3}{6} = \frac{1}{2}').scale(0.8).next_to(resultado, RIGHT, buff=0.3)

        play(Write(intro))
        play(Write(intro_exemplo))
        play(FadeIn(espaco_amostral))
        play(FadeOut(intro_exemplo))
        play(Write(explicacao_exemplo))
        play(FadeIn(evento))
        play(evento.animate.shift(DOWN))
        play(Write(resultado), Write(resultado_formula))
        self.limpar_cena()
        

    def abertura(self):
        titulo = Tex(r'Combinatória e\\ Probabilidade').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)
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
CENA = CombinatoriaProbabilidade.__name__
ARGS = '-s'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')