from manim import *

class Funcoes(Scene):
    def construct(self):
        self.abertura()
        self.definicao_intuitiva()
        self.notacao_funcao()
        self.grafico()
        self.definicao_formal()
        self.grafico_dominio_contradominio()
        self.condicao_existencia()
        self.fechamento()

    def limpar_tela(self):
        self.play(FadeOut(*self.mobjects))

    def abertura(self):
        titulo = Tex('Funções').scale(2.5).set_color("#dc6a40").move_to(0.5*UP)

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

    def definicao_intuitiva(self):
        def p(*anim, run_time: float = 2, wait_time: float = 2):
            self.play(*anim, run_time=run_time)
            self.wait(wait_time)

        introducao = Tex(
            r'\raggedright Funções é um tema extremamente importante na matemática.\
            Podemos defini-la como uma caixa que transforma coisas em outras.\
            No caso, números em outros.'
        ).shift(UP * 3).scale(0.7)

        input_number = MathTex('1').shift(3*LEFT)
        output_number = MathTex('2').shift(3*RIGHT)
        function_box = VGroup(
            Rectangle(height=1, width=2, color=BLUE),
            MathTex('f(', 'x', ')')
        )

        p(Write(introducao), run_time=4)
        p(Write(input_number), run_time=2)
        p(Write(function_box), run_time=2)
        p(input_number.animate.move_to(function_box).scale(0))
        p(ReplacementTransform(input_number, output_number))

        self.limpar_tela()
        
    def notacao_funcao(self):
        def p(*anim, run_time: float = 2, wait_time: float = 2):
            self.play(*anim, run_time=run_time)
            self.wait(wait_time)
        
        explicacao_notacao = Tex(
            r'\raggedright Aqui, temos uma função que multiplica números por 2.\
            Usamos a notação f(x) para denotar que f é uma função que admite x\
            como entrada. Assim, temos: '
        ).shift(3*UP).scale(0.7)

        notacao = Tex('f(x) = 2x')

        p(Write(explicacao_notacao), run_time=4)
        p(Write(notacao), run_time=2)

        self.limpar_tela()

    def grafico(self):
        def p(*anim, run_time: float = 2, wait_time: float = 2):
            self.play(*anim, run_time=run_time)
            self.wait(wait_time)
        
        introducao = Tex(
            r'''
            \raggedright Mas e se quisermos visualizar vários valores de uma vez. 
            Utilizar apenas números pode tornar a visualização 
            complicada de entender. Para isso, usamos gráficos.  \\
            ''',
            r'\raggedright \quad $\bullet$ O eixo horizontal representa as entradas x\\',
            r'\raggedright \quad $\bullet$ O eixo vertical representa as saídas f(x) '
        ).shift(2*UP).scale(0.7)
        
        g = Axes().shift(1.5*DOWN).scale(0.6)
        x_axis = VGroup(g.get_x_axis(), g.get_x_axis_label('x').scale(0.7))
        y_axis = VGroup(g.get_y_axis(), g.get_y_axis_label('y').scale(0.7))

        func = VGroup(
            Line(g.c2p(-3, -3), g.c2p(3, 3), color=BLUE),
            Tex('y = f(x)').move_to(g.c2p(3.5, 3.5)).scale(0.7).set_color(BLUE)
        )

        p(Write(introducao[0]), run_time=4)
        p(Write(x_axis))
        p(Write(introducao[1]))
        p(Write(y_axis))
        p(Write(introducao[2]))
        p(Write(func))

        self.limpar_tela()

    def definicao_formal(self):
        def p(*anim, run_time: float = 2, wait_time: float = 2):
            self.play(*anim, run_time=run_time)
            self.wait(wait_time)

        introducao = Tex(
            r'\raggedright Demos uma noção intuitiva do que é uma função,\
            mas vamos formalizar um pouco as coisas. Podemos dizer que :\\ \
            \quad $\bullet$ Uma função é a relação entre 2 conjuntos A e B \\ \
            \quad $\bullet$ A é o domínio e B é o contradomínio. \\ \
            \quad $\bullet$ e o conjunto dos números de B correspondentes a A.\\',
            r'\raggedright Talvez tenha ficado um pouco confuso, então vamos visualizar isso com Diagrama de Venn'
        ).shift(2*UP).scale(0.7)

        dominio = VGroup(
            Ellipse(width=1.5, height=3),
            Tex('A').shift(1.5*UP + 0.75*LEFT),
            VGroup(*[Tex(i).scale(0.7) for i in [1, 2, 3, '...']]).arrange(DOWN, buff=0.5)
        ).shift(1.5*DOWN + 3*LEFT).set_color(BLUE)

        contradominio = VGroup(
            Ellipse(width=1.5, height=3),
            Tex('B').shift(1.5*UP + 0.75*LEFT),
            VGroup(*[Tex(i).scale(0.7) for i in [1, 2, 3, 4, 5, 6, '...']]).arrange(DOWN, buff=0.2)
        ).shift(1.5*DOWN + 3*RIGHT).set_color(RED)

        imagem = VGroup(
            CurvedArrow(dominio[2][0].get_center() + 0.25*RIGHT, 
                contradominio[2][1].get_center() + 0.25*LEFT, angle=-0.25*PI, color=BLUE),
            CurvedArrow(dominio[2][1].get_center() + 0.25*RIGHT, 
                contradominio[2][3].get_center() + 0.25*LEFT, angle=-0.25*PI, color=RED),
            CurvedArrow(dominio[2][2].get_center() + 0.25*RIGHT, 
                contradominio[2][5].get_center() + 0.25*LEFT, angle=-0.25*PI, color=RED)
        ).set_color(YELLOW)

        p(Write(introducao[0]), run_time=6)
        p(Write(introducao[1]), run_time=4)
        p(Write(dominio))
        p(Write(contradominio))
        p(Write(imagem))

        self.limpar_tela()

    def grafico_dominio_contradominio(self):
        def p(*anim, run_time: float = 2, wait_time: float = 2):
            self.play(*anim, run_time=run_time)
            self.wait(wait_time)        
        introducao = Tex('Também podemos visualizar isso em um gráfico:').shift(3*UP).scale(0.7)
        eixos = Axes()
        x_axis = eixos.get_x_axis().set_color(BLUE)
        y_axis = eixos.get_y_axis().set_color(RED)
        x_label = eixos.get_x_axis_label('x').set_color(BLUE)
        y_label = eixos.get_y_axis_label('y').set_color(RED)
        func = Line(eixos.c2p(-3, -3), eixos.c2p(3, 3), color=YELLOW)
        grafico = VGroup(
            eixos, x_axis, y_axis, x_label, y_label, func
        ).scale(0.8)

        dominio = VGroup(
            Arrow(eixos.c2p(3, -2), eixos.c2p(1, 0), color=BLUE),
            Tex('dominio', color=BLUE).scale(0.7).shift(eixos.c2p(3, -2) + 0.25*DOWN + 0.25*RIGHT)
        )

        contradominio = VGroup(
            Arrow(eixos.c2p(-3, 3), eixos.c2p(0, 1), color=RED),
            Tex('contradominio', color=RED).scale(0.7).shift(eixos.c2p(-3, 3) + 0.25*UP + 0.25*LEFT)
        )

        imagem = VGroup(
            Arrow(eixos.c2p(6, 3), eixos.c2p(3, 3), color=YELLOW),
            Tex('imagem', color=YELLOW).scale(0.7).shift(eixos.c2p(6, 3) + 0.25*UP + 0.25*RIGHT)
        ).set_color(YELLOW)


        p(Write(introducao), run_time=4)
        p(Write(grafico))
        p(Write(dominio))
        p(Write(contradominio))
        p(Write(imagem))

        self.limpar_tela()

    def condicao_existencia(self):
        def p(*anim, run_time: float = 2, wait_time: float = 2):
            self.play(*anim, run_time=run_time)
            self.wait(wait_time)
        introducao = Tex(
            r'\raggedright Para que essa relação seja uma função seja uma função,\
            não se pode ter mais de um valor de saída para cada entrada.\
            Ou seja, as seguintes situações não são consideradas funções.'
        ).scale(0.7).shift(3*UP)

        a = VGroup(
            Ellipse(width=1.5, height=3),
            Tex('A').shift(1.5*UP + 0.75*LEFT),
            VGroup(*[Tex(i).scale(0.7) for i in [1, 2, 3, '...']]).arrange(DOWN, buff=0.5)
        ).shift(3*LEFT).set_color(BLUE)

        b = VGroup(
            Ellipse(width=1.5, height=3),
            Tex('B').shift(1.5*UP + 0.75*RIGHT),
            VGroup(*[Tex(i).scale(0.7) for i in [1, 2, 3, '...']]).arrange(DOWN, buff=0.5)
        ).shift(3*RIGHT).set_color(RED)

        r = VGroup(
            CurvedArrow(a[2][0].get_center() + 0.25*RIGHT,
                b[2][0].get_center() + 0.25*LEFT, angle=-0.25*PI, color=BLUE),
            CurvedArrow(a[2][1].get_center() + 0.25*RIGHT,
                b[2][0].get_center() + 0.25*LEFT, angle=-0.25*PI, color=RED),
            CurvedArrow(a[2][2].get_center() + 0.25*RIGHT,
                b[2][1].get_center() + 0.25*LEFT, angle=-0.25*PI, color=RED)
        ).set_color(YELLOW)

        eixos = Axes().shift(DOWN)
        x_axis = eixos.get_x_axis().set_color(BLUE)
        y_axis = eixos.get_y_axis().set_color(RED)
        x_label = eixos.get_x_axis_label('x').set_color(BLUE)
        y_label = eixos.get_y_axis_label('y').set_color(RED)
        func = Line(eixos.c2p(3, -3), eixos.c2p(3, 3), color=YELLOW)
        func_label = Tex('f(x)', color=YELLOW).shift(eixos.c2p(4, 3))
        grafico = VGroup(
            eixos, x_axis, y_axis, x_label, y_label, func, func_label
        ).scale(0.8)

        p(Write(introducao), run_time=4)
        p(Write(a))
        p(Write(b))
        p(Write(r))
        p(FadeOut(a, b, r))
        p(Write(grafico))

        self.limpar_tela()
