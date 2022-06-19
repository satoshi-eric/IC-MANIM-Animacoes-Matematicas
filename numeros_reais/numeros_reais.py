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

class DivSymbol(VMobject):
    def __init__(self):
        super().__init__()
        self.add(
            Line(3*LEFT, 3*RIGHT).set_opacity(0.3),
            Line(3*UP, 3*DOWN).set_opacity(0.3),
            MathTex('\\div').shift(3*RIGHT + 3*DOWN).scale(0.8)
        )

class Utils:
    class cor:
        conjunto_reais = YELLOW
        conjunto_irracionais = RED
        conjunto_racionais = BLUE
    class scale:
        texto_normal = 0.7
        texto_pequeno = 0.6


class NumerosReais(Scene):
    def construct(self):
        # self.add(Grade())
        self.abertura()
        self.definicao()
        self.definicao_2()
        # self.operacoes()
        self.explicacao_reta_reais()
        self.intervalos()
        self.fechamento()

    def abertura(self):
        titulo = Tex('Números Reais').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)

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

        self.clear_cena()

    def definicao_2(self):
        def play(*anim, anim_time=2, wait_time=2):
            self.play(*anim, run_time=anim_time)
            self.wait(wait_time)

        introducao = Tex(
            '\\raggedright O conjunto do reais pode ser definido de outra forma, a união entre os conjuntos dos racionais($\\mathbb{Q}$) e irracionais ($\\mathbb{I}$).'
        ).scale(0.7).to_edge(UP)

        conjunto_racionais = Tex(
            '\\raggedright O conjunto dos racionais se refere ao conjunto dos números que podem ser representados por uma fração'
        ).scale(0.7).to_edge(UP)
        racionais_exemplo = MathTex(
            r'\frac{12}{10} = 1,2 = 1 + 0,2'
        ).scale(0.7).next_to(conjunto_racionais, DOWN)

        conjunto_irracionais = Tex(
            '\\raggedright O conjunto dos irracionais se refere ao conjunto dos números com casas decimais, mas não podem ser representados como fração.'
        ).scale(0.7).next_to(racionais_exemplo, DOWN)
        irracionais_exemplo = MathTex(
            r'\pi = 3,141592653589793... \\ e = 2,718281828459045...'
        ).scale(0.7).next_to(conjunto_irracionais, DOWN)

        diagrama_texto = Tex(
            'Dessa forma, temos o seguinte diagrama de Venn'
        ).scale(0.7).to_edge(UP)
        diagrama_venn = VDict({
            'reais': VDict({
                'diagrama': Ellipse(5, 6),
                'simbolo': MathTex(r'\mathbb{R}').shift(2*UP + LEFT),
            }).set_color(Utils.cor.conjunto_reais),
            'racionais': VDict({
                'diagrama': Ellipse(2, 3),
                'simbolo': MathTex(r'\mathbb{Q}').shift(0.5*UP + 0.5*LEFT)
            }).shift(1.1*RIGHT).set_color(Utils.cor.conjunto_racionais),
            'irracionais': VDict({
                'diagrama': Ellipse(2, 2),
                'simbolo': MathTex(r'\mathbb{I}').shift(0.25*UP + 0.5*LEFT)
            }).shift(1.1*LEFT).set_color(Utils.cor.conjunto_irracionais),
        })

        play(Write(introducao))
        play(FadeOut(introducao))
        play(Write(conjunto_racionais))
        play(Write(racionais_exemplo))
        play(Write(conjunto_irracionais))
        play(Write(irracionais_exemplo))
        play(FadeOut(conjunto_racionais, racionais_exemplo, conjunto_irracionais, irracionais_exemplo))
        play(Write(diagrama_texto))
        play(Write(diagrama_venn['racionais']))
        play(Write(diagrama_venn['irracionais']))
        play(Write(diagrama_venn['reais']))

        self.clear_cena()

    def operacoes(self):
        def play(*anim, anim_time=2, wait_time=2):
            self.play(*anim, run_time=anim_time)
            self.wait(wait_time)
            
        introducao = Tex('Podemos realizar operações entre frações.')\
            .scale(Utils.scale.texto_normal)\
            .shift(3*UP + 2.5*LEFT)

        ################# Adição #################

        ad_label = Tex('$\\bullet$ Adição')\
            .scale(Utils.scale.texto_normal)\
            .move_to(introducao.get_center() + 0.75*DOWN + 2*LEFT)
        ad_passos = Tex(
            '\\raggedright Mínimo múltiplo comum', 
            '$\\rightarrow$ Divide pelo de baixo\\\\',
            '$\\rightarrow$ Multiplica pelo de cima',
            '$\\rightarrow$ Soma os numeradores',
        ).scale(Utils.scale.texto_pequeno)\
            .move_to(ad_label.get_center() + 0.75*DOWN + 3*RIGHT)
        
        ad_fracoes = MathTex(
            '{2', '\\over', '3}', '+', '{1', '\\over', '2}',
            '=', '{{4', '+', '3}', '\\over', '6}', '=',
            '{7', '\\over', '6}'
        ).scale(Utils.scale.texto_normal)\
            .move_to(ad_label.get_center() + 2.25*DOWN + 2*RIGHT)
        ad_divide_pelo_de_baixo_1 = MathTex(
            '{6', ' \\divisionsymbol ', ' 3}', '=', '2'
        ).scale(Utils.scale.texto_normal)\
            .next_to(ad_fracoes, DOWN, buff=0.6)
        ad_multiplica_pelo_de_cima_1 = MathTex(
            '{2', ' \\cdot ', ' 2}', '=', '4'
        ).scale(Utils.scale.texto_normal)\
            .next_to(ad_divide_pelo_de_baixo_1, DOWN)
        ad_divide_pelo_de_baixo_2 = MathTex(
            '{6', ' \\divisionsymbol ', ' 2}', '=', '3'
        ).scale(Utils.scale.texto_normal)\
            .next_to(ad_fracoes, DOWN, buff=0.6)
        ad_multiplica_pelo_de_cima_2 = MathTex(
            '{3', ' \\cdot ', ' 1}', '=', '3'
        ).scale(Utils.scale.texto_normal)\
            .next_to(ad_divide_pelo_de_baixo_1, DOWN)

        ################# Subtração #################

        sub_label = Tex('$\\bullet$ Subtração')\
            .scale(Utils.scale.texto_normal)\
            .move_to(introducao.get_center() + 0.75*DOWN + 2*LEFT)
        sub_passos = Tex(
            '\\raggedright Mínimo múltiplo comum', 
            '$\\rightarrow$ Divide pelo de baixo\\\\',
            '$\\rightarrow$ Divide pelo de cima',
            '$\\rightarrow$ Subtrai os numeradores',
        ).scale(Utils.scale.texto_pequeno)\
            .move_to(sub_label.get_center() + 0.75*DOWN + 3*RIGHT)
        
        sub_fracoes = MathTex(
            '{2', '\\over', '3}', '-', '{1', '\\over', '2}',
            '=', '{{4', '-', '3}', '\\over', '6}', '=',
            '{1', '\\over', '6}'
        ).scale(Utils.scale.texto_normal)\
            .move_to(sub_label.get_center() + 2.25*DOWN + 2*RIGHT)
        sub_divide_pelo_de_baixo_1 = MathTex(
            '{6', ' \\divisionsymbol ', ' 3}', '=', '2'
        ).scale(Utils.scale.texto_normal)\
            .next_to(sub_fracoes, DOWN, buff=0.6)
        sub_multiplica_pelo_de_cima_1 = MathTex(
            '{2', ' \\cdot ', ' 2}', '=', '4'
        ).scale(Utils.scale.texto_normal)\
            .next_to(ad_divide_pelo_de_baixo_1, DOWN)
        sub_divide_pelo_de_baixo_2 = MathTex(
            '{6', ' \\divisionsymbol ', ' 2}', '=', '3'
        ).scale(Utils.scale.texto_normal)\
            .next_to(sub_fracoes, DOWN, buff=0.6)
        sub_multiplica_pelo_de_cima_2 = MathTex(
            '{3', ' \\cdot ', ' 1}', '=', '3'
        ).scale(Utils.scale.texto_normal)\
            .next_to(ad_divide_pelo_de_baixo_1, DOWN)

        ################# Multiplicação #################

        mult_label = Tex('$\\bullet$ Multiplicação')\
            .scale(Utils.scale.texto_normal)\
            .move_to(introducao.get_center() + 0.75*DOWN + 2*LEFT)
        mult_passos = Tex(
            '\\raggedright Multiplica numeradores e denominadores'
        ).scale(Utils.scale.texto_pequeno)\
            .move_to(sub_label.get_center() + 0.75*DOWN + 3*RIGHT)
        
        mult_fracoes = MathTex(
            '\\frac{2}{3} \\cdot \\frac{1}{2}',
            ' = \\frac{2 \\cdot 1}{3 \\cdot 2}',
            ' = \\frac{2}{6}',
            ' = \\frac{1}{3}'
        ).scale(Utils.scale.texto_normal)\
            .move_to(sub_label.get_center() + 2.25*DOWN + 2*RIGHT)

        ################# Divisão #################

        div_label = Tex('$\\bullet$ Divisão')\
            .scale(Utils.scale.texto_normal)\
            .move_to(introducao.get_center() + 0.75*DOWN + 2*LEFT)
        div_passos = Tex(
            '\\raggedright Inverte segunda fração e realiza mutiplicação'
        ).scale(Utils.scale.texto_pequeno)\
            .move_to(sub_label.get_center() + 0.75*DOWN + 3*RIGHT)
        
        div_fracoes = MathTex(
            '\\frac{2}{3} \\divisionsymbol \\frac{1}{2}',
            ' = \\frac{2}{3} \\cdot \\frac{2}{1}',
            ' = \\frac{4}{3}'
        ).scale(Utils.scale.texto_normal)\
            .move_to(sub_label.get_center() + 2.25*DOWN + 2*RIGHT)

        play(Write(introducao))

        def adicao():
            play(Write(ad_label))
            play(FadeIn(ad_fracoes[0:7]))
            play(Write(ad_passos[0]))
            play(FadeIn(ad_fracoes[7], ad_fracoes[11:13]))
            play(FadeIn(ad_passos[1]))
            play(FadeIn(ad_divide_pelo_de_baixo_1[:-2]))
            play(
                ad_divide_pelo_de_baixo_1[0].animate.scale(1.3).set_color(RED),
                ad_fracoes[12].animate.scale(1.3).set_color(RED)
            )
            play(
                ad_divide_pelo_de_baixo_1[0].animate.scale(1/1.3).set_color(WHITE),
                ad_fracoes[12].animate.scale(1/1.3).set_color(WHITE)
            )
            play(
                ad_divide_pelo_de_baixo_1[2].animate.scale(1.3).set_color(RED),
                ad_fracoes[2].animate.scale(1.3).set_color(RED)
            )
            play(
                ad_divide_pelo_de_baixo_1[2].animate.scale(1/1.3).set_color(WHITE),
                ad_fracoes[2].animate.scale(1/1.3).set_color(WHITE)
            )
            play(FadeIn(ad_divide_pelo_de_baixo_1[-2:]))
            play(ReplacementTransform(
                    ad_divide_pelo_de_baixo_1[-1].copy(), 
                    ad_multiplica_pelo_de_cima_1[0]
            ))
            play(FadeIn(ad_passos[2]))
            play(FadeIn(ad_multiplica_pelo_de_cima_1[1:]))
            play(
                ad_fracoes[0].animate.scale(1.3).set_color(RED),
                ad_multiplica_pelo_de_cima_1[2].animate.scale(1.3).set_color(RED)
            )
            play(
                ad_fracoes[0].animate.scale(1/1.3).set_color(WHITE),
                ad_multiplica_pelo_de_cima_1[2].animate.scale(1/1.3).set_color(WHITE)
            )
            play(ReplacementTransform(
                ad_multiplica_pelo_de_cima_1[-1].copy(),
                ad_fracoes[8]
            ))
            play(FadeOut(ad_divide_pelo_de_baixo_1, ad_multiplica_pelo_de_cima_1))
            play(FadeIn(ad_divide_pelo_de_baixo_2[0:3]))
            play(
                ad_divide_pelo_de_baixo_2[0].animate.scale(1.3).set_color(RED),
                ad_fracoes[12].animate.scale(1.3).set_color(RED)
            )
            play(
                ad_divide_pelo_de_baixo_2[0].animate.scale(1/1.3).set_color(WHITE),
                ad_fracoes[12].animate.scale(1/1.3).set_color(WHITE)
            )
            play(
                ad_divide_pelo_de_baixo_2[2].animate.scale(1.3).set_color(RED),
                ad_fracoes[6].animate.scale(1.3).set_color(RED)
            )
            play(
                ad_divide_pelo_de_baixo_2[2].animate.scale(1/1.3).set_color(WHITE),
                ad_fracoes[6].animate.scale(1/1.3).set_color(WHITE) 
            )
            play(FadeIn(ad_divide_pelo_de_baixo_2[-2:]))
            play(ReplacementTransform(
                    ad_divide_pelo_de_baixo_2[-1].copy(), 
                    ad_multiplica_pelo_de_cima_2[0]
            ))
            play(FadeIn(ad_multiplica_pelo_de_cima_2[1:-2]))
            play(
                ad_fracoes[4].animate.scale(1.3).set_color(RED),
                ad_multiplica_pelo_de_cima_2[2].animate.scale(1.3).set_color(RED)
            )
            play(
                ad_fracoes[4].animate.scale(1/1.3).set_color(WHITE),
                ad_multiplica_pelo_de_cima_2[2].animate.scale(1/1.3).set_color(WHITE)
            )
            play(FadeIn(ad_multiplica_pelo_de_cima_2[-2:]))
            play(ReplacementTransform(
                ad_multiplica_pelo_de_cima_1[-1].copy(),
                ad_fracoes[10]
            ))
            play(FadeOut(ad_divide_pelo_de_baixo_2, ad_multiplica_pelo_de_cima_2))
            play(FadeIn(ad_fracoes[9]))
            play(Write(ad_passos[3]))
            play(FadeIn(ad_fracoes[13:]))

            play(FadeOut(ad_label, ad_fracoes, ad_passos))

        def subtracao():
            play(Write(sub_label))
            play(FadeIn(sub_fracoes[0:7]))
            play(Write(sub_passos[0]))
            play(FadeIn(sub_fracoes[7], sub_fracoes[11:13]))
            play(FadeIn(sub_passos[1]))
            play(FadeIn(sub_divide_pelo_de_baixo_1[:-2]))
            play(
                sub_divide_pelo_de_baixo_1[0].animate.scale(1.3).set_color(RED),
                sub_fracoes[12].animate.scale(1.3).set_color(RED)
            )
            play(
                sub_divide_pelo_de_baixo_1[0].animate.scale(1/1.3).set_color(WHITE),
                sub_fracoes[12].animate.scale(1/1.3).set_color(WHITE)
            )
            play(
                sub_divide_pelo_de_baixo_1[2].animate.scale(1.3).set_color(RED),
                sub_fracoes[2].animate.scale(1.3).set_color(RED)
            )
            play(
                sub_divide_pelo_de_baixo_1[2].animate.scale(1/1.3).set_color(WHITE),
                sub_fracoes[2].animate.scale(1/1.3).set_color(WHITE)
            )
            play(FadeIn(sub_divide_pelo_de_baixo_1[-2:]))
            play(ReplacementTransform(
                    sub_divide_pelo_de_baixo_1[-1].copy(), 
                    sub_multiplica_pelo_de_cima_1[0]
            ))
            play(FadeIn(sub_passos[2]))
            play(FadeIn(sub_multiplica_pelo_de_cima_1[1:]))
            play(
                sub_fracoes[0].animate.scale(1.3).set_color(RED),
                sub_multiplica_pelo_de_cima_1[2].animate.scale(1.3).set_color(RED)
            )
            play(
                sub_fracoes[0].animate.scale(1/1.3).set_color(WHITE),
                sub_multiplica_pelo_de_cima_1[2].animate.scale(1/1.3).set_color(WHITE)
            )
            play(ReplacementTransform(
                sub_multiplica_pelo_de_cima_1[-1].copy(),
                sub_fracoes[8]
            ))
            play(FadeOut(sub_divide_pelo_de_baixo_1, sub_multiplica_pelo_de_cima_1))
            play(FadeIn(sub_divide_pelo_de_baixo_2[0:3]))
            play(
                sub_divide_pelo_de_baixo_2[0].animate.scale(1.3).set_color(RED),
                sub_fracoes[12].animate.scale(1.3).set_color(RED)
            )
            play(
                sub_divide_pelo_de_baixo_2[0].animate.scale(1/1.3).set_color(WHITE),
                sub_fracoes[12].animate.scale(1/1.3).set_color(WHITE)
            )
            play(
                sub_divide_pelo_de_baixo_2[2].animate.scale(1.3).set_color(RED),
                sub_fracoes[6].animate.scale(1.3).set_color(RED)
            )
            play(
                sub_divide_pelo_de_baixo_2[2].animate.scale(1/1.3).set_color(WHITE),
                sub_fracoes[6].animate.scale(1/1.3).set_color(WHITE) 
            )
            play(FadeIn(sub_divide_pelo_de_baixo_2[-2:]))
            play(ReplacementTransform(
                    sub_divide_pelo_de_baixo_2[-1].copy(), 
                    sub_multiplica_pelo_de_cima_2[0]
            ))
            play(FadeIn(sub_multiplica_pelo_de_cima_2[1:-2]))
            play(
                sub_fracoes[4].animate.scale(1.3).set_color(RED),
                sub_multiplica_pelo_de_cima_2[2].animate.scale(1.3).set_color(RED)
            )
            play(
                sub_fracoes[4].animate.scale(1/1.3).set_color(WHITE),
                sub_multiplica_pelo_de_cima_2[2].animate.scale(1/1.3).set_color(WHITE)
            )
            play(FadeIn(sub_multiplica_pelo_de_cima_2[-2:]))
            play(ReplacementTransform(
                sub_multiplica_pelo_de_cima_2[-1].copy(),
                sub_fracoes[10]
            ))
            play(FadeOut(sub_divide_pelo_de_baixo_2, sub_multiplica_pelo_de_cima_2))
            play(FadeIn(sub_fracoes[9]))
            play(Write(sub_passos[3]))
            play(FadeIn(sub_fracoes[13:]))

            play(FadeOut(sub_label, sub_fracoes, sub_passos))
        
        def multiplicacao():
            play(Write(mult_label))
            play(FadeIn(mult_fracoes[0]))
            play(Write(mult_passos[0]))
            play(FadeIn(mult_fracoes[1]))
            play(FadeIn(mult_fracoes[2]))
            play(FadeIn(mult_fracoes[3]))

            play(FadeOut(mult_label, mult_fracoes, mult_passos))

        def divisao():
            play(Write(div_label))
            play(FadeIn(div_fracoes[0]))
            play(Write(div_passos))
            play(FadeIn(div_fracoes[1]))
            play(FadeIn(div_fracoes[2]))

            play(FadeOut(div_label, div_fracoes, div_passos))

        adicao()
        subtracao()
        multiplicacao()
        divisao()

        self.clear_cena()

    def explicacao_reta_reais(self):
        def play(*anim, play_time=2, wait_time=0):
            self.play(*anim, run_time=play_time)
            self.wait(wait_time)

        introducao = Tex('\\ Podemos enxergar esse conjunto como uma reta, a reta dos reais')\
            .scale(Utils.scale.texto_normal)\
            .shift(3*UP + LEFT)
        reta_reais = NumberLine(
            x_range=[-2.6, 2.6, 0.5], 
            length=10.4, 
            include_numbers=True,
            font_size=30
        )
        obs = Tex(
            '\\raggedright Perceba que existem valores quebrados na reta. Ou seja, podemos posicionar um ponto em qualquer lugar da reta'
        ).scale(Utils.scale.texto_pequeno).shift(2*DOWN)
        valor = Tex('0,00').scale(Utils.scale.texto_normal).shift(1.7*UP)
        ponto = Dot(color=RED)
        seta_ponto = Arrow(1.5*UP, 0.2*UP)

        play(Write(introducao))
        play(Write(reta_reais))
        play(Write(obs))
        play(Write(ponto), Write(seta_ponto))
        play(Write(valor))

        def update_valor(mob: Tex, dt):
            mob.become(Tex(f'{ponto.get_x()/2:.2f}'.replace('.', ',')).scale(Utils.scale.texto_normal).move_to(ponto.get_center() + 1.7*UP))

        def update_ponto_direita(mob: Dot, dt):
            mob.shift(dt*RIGHT)

        def update_ponto_esquerda(mob, dt):
            mob.shift(dt*LEFT)
            
        def update_seta_ponto(mob: Arrow, dt):
            mob.become(Arrow(1.5*UP + ponto.get_x()*RIGHT, 0.2*UP + ponto.get_x()*RIGHT))

        ponto.add_updater(update_ponto_direita)
        valor.add_updater(update_valor)
        seta_ponto.add_updater(update_seta_ponto)
        self.wait(4.1)
        ponto.remove_updater(update_ponto_direita)
        valor.remove_updater(update_valor)
        seta_ponto.remove_updater(update_seta_ponto)

        self.wait(2)

        ponto.add_updater(update_ponto_esquerda)
        valor.add_updater(update_valor)
        seta_ponto.add_updater(update_seta_ponto)
        self.wait(6.3)
        ponto.remove_updater(update_ponto_esquerda)
        valor.remove_updater(update_valor)
        seta_ponto.remove_updater(update_seta_ponto)

        self.wait(2)

        self.clear_cena()
        

    def intervalos(self):
        def play(*anim, play_time=2, wait_time=0):
            self.play(*anim, run_time=play_time)
            self.wait(wait_time)

        introducao = Tex(
            'Também podemos definir intervalos entre 2 valores'
        ).scale(Utils.scale.texto_normal).shift(3*UP + LEFT)

        reta_reais = NumberLine(
            x_range=[-2.6, 2.6, 0.5],
            length=10.4,
            include_numbers=True,
            font_size=30
        )

        valor_min = Tex('-1')\
            .scale(Utils.scale.texto_normal)\
            .move_to(reta_reais.n2p(-1) + UP)\
            .set_color(RED)
        valor_max = Tex('2')\
            .scale(Utils.scale.texto_normal)\
            .move_to(reta_reais.n2p(2) + UP)\
            .set_color(RED)

        delimitador = VGroup(
            Line(2*LEFT + 0.5*UP, 4*RIGHT + 0.5*UP),
            Line(0.3*UP, 0.7*UP).shift(2*LEFT),
            Line(0.3*UP, 0.7*UP).shift(4*RIGHT)
        ).set_color(RED)

        intervalo = Tex(
            r'\raggedright Escrevemos da seguinte forma\\ $I=\{x \in \mathbb{R} | -1 \leq x \leq 3\}$'
        ).scale(Utils.scale.texto_pequeno).shift(2*DOWN + 2*LEFT)

        intervalo_simples = Tex(
            r'\raggedright Ou de forma mais simples\\I=[-1, 2]'
        ).scale(Utils.scale.texto_pequeno).next_to(intervalo, RIGHT, buff=0.5)

        

        valor_min2 = Tex('-2,5')\
            .scale(Utils.scale.texto_normal)\
            .move_to(reta_reais.n2p(-2.5) + UP)\
            .set_color(RED)
        valor_max2 = Tex('0,5')\
            .scale(Utils.scale.texto_normal)\
            .move_to(reta_reais.n2p(0.5) + UP)\
            .set_color(RED)

        delimitador2 = VGroup(
            Line(5*LEFT + 0.5*UP, 1*RIGHT+0.5*UP),
            Line(0.3*UP, 0.7*UP).shift(5*LEFT),
            Line(0.3*UP, 0.7*UP).shift(1*RIGHT)
        ).set_color(RED)

        intervalo2 = Tex(
            r'\raggedright $I=\{x \in \mathbb{R} | -2,5 \leq x \leq 0,5\}$'
        ).scale(Utils.scale.texto_pequeno).shift(2*DOWN + 2*LEFT)

        intervalo_simples2 = Tex(
            r'\raggedright I=[-2,5; 0,5]'
        ).scale(Utils.scale.texto_pequeno).next_to(intervalo, RIGHT, buff=0.5)

        play(Write(introducao))
        play(Write(reta_reais))
        play(Write(valor_min))
        play(Write(valor_max))
        play(Write(delimitador))
        play(Write(intervalo))
        play(Write(intervalo_simples))
        play(FadeOut(intervalo), FadeOut(intervalo_simples), FadeOut(valor_min), FadeOut(valor_max), FadeOut(delimitador))
        play(Write(valor_min2))
        play(Write(valor_max2))
        play(Write(delimitador2))
        play(Write(intervalo2))
        play(Write(intervalo_simples2))

        self.clear_cena()
        

    def clear_cena(self):
        self.play(FadeOut(*[mob for mob in self.mobjects if type(mob) != Grade]))

ARQ_NOME = Path(__file__).resolve()
CENA = NumerosReais.__name__
ARGS = '-s'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')