# ffmpeg -f concat -safe 0 -i list -c copy animação_PI.mp para juntar todas as animações
# onde list possui todos os vídeos em sequencia

from manimlib.imports import *

# Abertura
class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")

      titulo=TextMobject("$\sqrt{2}$: A diagonal do quadrado")
      titulo.scale(2)
      titulo.set_color("#dc6a40")
         
      self.play(FadeIn(explora), run_time=4)
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(1.5)

""" Enunciado do Teorema de Pitágoras """
class EnunciadoTeoremaDePitagoras(Scene):
    def construct(self):

        """ /************************************** Objetos *********************************/"""
        # Objetos utilizados durante animação
        obj = {
            # Título da cena
            'Título': TextMobject("Teorema de Pitágoras"),
            # Retas que formam o triangulo
            'Reta C': Line(start = np.array([0, 0, 0]) , end = np.array([0, 1.25 ,0])).shift(1.5*LEFT + 0.7*DOWN),
            'Reta A': Line(start = np.array([0, 1.25, 0]), end = np.array([3, 0, 0])).shift(1.5*LEFT + 0.7*DOWN),
            'Reta B': Line(start = np.array([0, 0, 0]), end = np.array([3, 0, 0])).shift(1.5*LEFT + 0.7*DOWN),
            # Quadrados que ficam aos lados do triângulo
            'Quadrado A rotacionado': Polygon(
                np.array([0, 1.25, 0]),
                np.array([1.25, 4.25, 0]),
                np.array([4.25, 3, 0]),
                np.array([3, 0, 0])
            ),
            'Quadrado A': Square(side_length = 3.25),
            'Quadrado B': Square(side_length = 3),
            'Quadrado C': Square(side_length = 1.25),
            # Textos dos lados ao quadrado
            'Texto A^2': TexMobject(r"a^{2}"),
            'Texto B^2': TexMobject(r"b^{2}"),
            'Texto C^2': TexMobject(r"c^{2}"),
            # Textos dos sinais da equação
            '=': TexMobject('='),
            '+': TexMobject('+'), 
            'Raiz quadrada': TexMobject("\\sqrt{}"),
            'Barra': Line(start = 0.47*UP + 0.27*LEFT, end = 0.47*UP + 2.2*RIGHT) 
        }

        # Objetos dependentes de outros objetos(VGroup, Brace, etc)
        obj_dep = {
            # Braces das retas representando o tamanho dos lados do triângulo
            'Brace A': Brace(obj['Reta A'], direction = np.array([5/13, 1, 0])),
            'Brace B': Brace(obj['Reta B'], direction = DOWN),
            'Brace C': Brace(obj['Reta C'], direction = LEFT),
            # textos dos braces das retas mostrando o tamanho de cada reta a, b e c
            'Texto A': Brace(obj['Reta A'], direction = np.array([5/13, 1, 0])).get_text("$a$"),
            'Texto B': Brace(obj['Reta B'], direction = DOWN).get_text("$b$"),
            'Texto C': Brace(obj['Reta C'], direction = LEFT).get_text("$c$"),
            # Triangulo formado a partir das retas A, B e C
            'Triangulo': VGroup(
                obj['Reta A'],
                obj['Reta B'],
                obj['Reta C']
            )
        }

        """ /************************************** Configurações dos objetos *********************************/ """
        # Configurando título
        obj['Título'].scale(1.5)

        # Configurando quadrados    
        obj['Quadrado A rotacionado'].shift(1.5*LEFT + 0.7*DOWN).set_color(RED)
        obj['Quadrado B'].next_to(obj_dep['Triangulo'], direction = DOWN, buff = 0).set_color(GREEN)
        obj['Quadrado C'].next_to(obj_dep['Triangulo'], direction = LEFT, buff = 0).set_color(BLUE)

        # configurando textos
        obj['Texto A^2'].move_to(obj['Quadrado A rotacionado'].get_center()).set_color(RED)
        obj['Texto B^2'].move_to(obj['Quadrado B'].get_center()).set_color(GREEN)
        obj['Texto C^2'].move_to(obj['Quadrado C'].get_center()).set_color(BLUE)

        # configurando sinais
        obj['='].move_to(1.5*LEFT)
        obj['+'].move_to(3.5*RIGHT)

        # Configurando raiz quadrada
        obj['Raiz quadrada'].shift(0.5*LEFT + 0.15*UP).scale(1.3)

        """ /************************************** Animações *********************************/ """
        # Animação do título
        self.play(Write(obj['Título']))
        self.wait()
        self.play(FadeOut(obj['Título']))

        # Animação para mostrar o triângulo e seus lados 
        self.play(FadeIn(obj_dep['Triangulo']))
        self.wait()
        self.play(
            FadeIn(obj_dep['Brace A']),
            FadeIn(obj_dep['Brace B']),
            FadeIn(obj_dep['Brace C']),
            FadeIn(obj_dep['Texto A']),
            FadeIn(obj_dep['Texto B']),
            FadeIn(obj_dep['Texto C'])
        )
        self.wait()

        # Animação para transformar os braces em quadrados 
        self.play(
            ReplacementTransform(obj_dep['Brace A'], obj['Quadrado A rotacionado']),
            ReplacementTransform(obj_dep['Brace B'], obj['Quadrado B']),
            ReplacementTransform(obj_dep['Brace C'], obj['Quadrado C']), 
            ReplacementTransform(obj_dep['Texto A'], obj['Texto A^2']),
            ReplacementTransform(obj_dep['Texto B'], obj['Texto B^2']),
            ReplacementTransform(obj_dep['Texto C'], obj['Texto C^2']),
        )
        self.wait()

        # Removendo triângulo
        self.play(FadeOut(obj_dep['Triangulo']))
        self.wait()

        # Reposicionando quadrados para formar uma equação
        self.play(
            ReplacementTransform(obj['Quadrado A rotacionado'], obj['Quadrado A'].move_to(4*LEFT).set_color(RED)),
            obj['Quadrado B'].move_to, RIGHT,
            obj['Quadrado C'].move_to, 5*RIGHT,
            obj['Texto A^2'].move_to, 4*LEFT,
            obj['Texto B^2'].move_to, RIGHT,
            obj['Texto C^2'].move_to, 5*RIGHT
        )
        self.wait()

        # Animação mostrando = e + para simbolizar uma equação
        self.play(
            FadeIn(obj['=']),
            FadeIn(obj['+'])
        )
        self.wait()

        # Animação para transformar remover os quadrados da equação anterior
        self.play(
            FadeOut(obj['Quadrado A']),
            FadeOut(obj['Quadrado B']),
            FadeOut(obj['Quadrado C']),
            obj['Texto A^2'].shift, 2*RIGHT,
            obj['Texto B^2'].shift, LEFT,
            obj['Texto C^2'].shift, 3*LEFT,
            obj['='].shift, 0.5*RIGHT,
            obj['+'].shift, 2.5*LEFT
        )
        self.wait()

        # Animação da equação final
        self.play(
            ReplacementTransform(obj['Texto A^2'], TexMobject("a").set_color(RED).move_to(obj['Texto A^2'])),
            FadeIn(obj['Raiz quadrada']),
            FadeIn(obj['Barra']),
            obj['='].shift, 0.3*LEFT
        )
        self.wait()

class DemonstracaoTeoremaDePitagoras(Scene):
    def construct(self):
        self.titulo()
        self.trianguloRetangulo()
        self.rearranjandoQuadrados()
        self.rearranjandoTriangulos()
        self.mostrandoMedidas()
        self.rearranjandoEquacao()

    def titulo(self):
        titulo = TextMobject("Provando o Teorema de Pitágoras")

        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.wait()

    def trianguloRetangulo(self):
        # linhas que servem de base para criar os braces
        retas = {
            'a': Line(start = np.array([0, 1.25, 0]), end = np.array([3, 0, 0])),
            'b': Line(start = np.array([0, 0, 0]), end = np.array([3, 0, 0])),
            'c': Line(start = np.array([0, 0, 0]), end = np.array([0, 1.25, 0]))
        }

        triangulo = VGroup(retas['a'], retas['b'], retas['c']).move_to(ORIGIN)

        # braces que indicam 
        braces = {
            'a': Brace(retas['a'], direction = np.array([5/13, 12/13, 0])).set_color(RED),
            'b': Brace(retas['b'], direction = DOWN).set_color(GREEN),
            'c': Brace(retas['c'], direction = LEFT).set_color(BLUE)
        }

        textos_braces = {
            'a': braces['a'].get_tex('a').set_color(RED),  
            'b': braces['b'].get_tex('b').set_color(GREEN),
            'c': braces['c'].get_tex('c').set_color(BLUE)
        }

        quadrados = {
            'a': Square(side_length = 3.25).move_to(np.array([0.625, 1.5, 0])).rotate(-np.arcsin(5/13)).set_color(RED),
            'b': Square(side_length = 3).next_to(triangulo, direction = DOWN, buff = 0).set_color(GREEN),
            'c': Square(side_length = 1.25).next_to(triangulo, direction = LEFT, buff = 0).set_color(BLUE)
        }

        textos_quadrados = {
            'a': TexMobject('a^{2}').move_to(quadrados['a']).set_color(RED),
            'b': TexMobject('b^{2}').move_to(quadrados['b']).set_color(GREEN),
            'c': TexMobject('c^{2}').move_to(quadrados['c']).set_color(BLUE)
        }

        self.play(FadeIn(triangulo))
        self.wait()

        for i in ['a', 'b', 'c']:
            self.play(GrowFromCenter(braces[i]), GrowFromCenter(textos_braces[i]))
            self.wait()

        for i in ['a', 'b', 'c']:
            self.play(
                ReplacementTransform(braces[i], quadrados[i]),
                ReplacementTransform(textos_braces[i], textos_quadrados[i])
            )
            self.wait()

        self.remove(triangulo, *quadrados.values(), *textos_quadrados.values())

    def rearranjandoQuadrados(self):
        # linhas que servem de base para criar os braces
        retas = {
            'a': Line(start = np.array([0, 1.25, 0]), end = np.array([3, 0, 0])),
            'b': Line(start = np.array([0, 0, 0]), end = np.array([3, 0, 0])),
            'c': Line(start = np.array([0, 0, 0]), end = np.array([0, 1.25, 0]))
        }

        triangulo = VGroup(retas['a'], retas['b'], retas['c']).move_to(ORIGIN)

        quadrados = {
            'a': Square(side_length = 3.25).move_to(np.array([0.625, 1.5, 0])).rotate(-np.arcsin(5/13)).set_color(RED),
            'b': Square(side_length = 3).next_to(triangulo, direction = DOWN, buff = 0).set_color(GREEN),
            'c': Square(side_length = 1.25).next_to(triangulo, direction = LEFT, buff = 0).set_color(BLUE)
        }

        textos_quadrados = {
            'a': TexMobject('a^{2}').move_to(quadrados['a']).set_color(RED),
            'b': TexMobject('b^{2}').move_to(quadrados['b']).set_color(GREEN),
            'c': TexMobject('c^{2}').move_to(quadrados['c']).set_color(BLUE)
        }

        triangulos = [
            triangulo.copy().move_to(3.5*RIGHT),
            triangulo.copy().move_to(3.5*RIGHT),
            triangulo.copy().move_to(3.5*RIGHT),
            triangulo.copy().move_to(3.5*RIGHT),
        ]

        angulos = [0*DEGREES, 90*DEGREES, 180*DEGREES, 270*DEGREES]


        # Adicionando o triangulo e os quadrados à cena
        self.add(triangulo, *quadrados.values(), *textos_quadrados.values())
        self.wait()

        # movendo os objetos da cenaa para direita
        self.play(
            triangulo.shift, 3.5*RIGHT,
            quadrados['a'].shift, 3.5*RIGHT,
            quadrados['b'].shift, 3.5*RIGHT, 
            quadrados['c'].shift, 3.5*RIGHT,
            textos_quadrados['a'].shift, 3.5*RIGHT,
            textos_quadrados['b'].shift, 3.5*RIGHT,
            textos_quadrados['c'].shift, 3.5*RIGHT, 
        )
        self.wait()

        # Movendo quadrados b e c para a esquerda
        self.play(
            quadrados['b'].move_to, np.array([-4.5, -1, 0]),
            textos_quadrados['b'].move_to, np.array([-4.5, -1, 0])
        )
        self.wait()
        self.play(
            quadrados['c'].move_to, np.array([-2.35, 1.15, 0]),
            textos_quadrados['c'].move_to, np.array([-2.35, 1.15, 0])
        )
        self.wait()

        for i in range(4):
            self.play(triangulos[i].move_to, ORIGIN)

            self.play(triangulos[i].rotate, angulos[i])

            if (i % 2) == 0:
                self.play(triangulos[i].next_to, quadrados['b'], UP, 0.02)
            else:
                self.play(triangulos[i].next_to, quadrados['b'], RIGHT, 0.02)

        self.play(FadeOut(triangulo))
        self.wait()

        self.play(
            quadrados['a'].move_to, np.array([4, -0.375, 0]),
            textos_quadrados['a'].move_to, np.array([4, -0.375, 0])
        )
        self.wait()

        self.remove(*quadrados.values(), *textos_quadrados.values(), *triangulos)

    def rearranjandoTriangulos(self):

        retas = {
            'a': Line(start = np.array([0, 1.25, 0]), end = np.array([3, 0, 0])),
            'b': Line(start = np.array([0, 0, 0]), end = np.array([3, 0, 0])),
            'c': Line(start = np.array([0, 0, 0]), end = np.array([0, 1.25, 0]))
        }

        triangulo = VGroup(retas['a'], retas['b'], retas['c']).move_to(ORIGIN)

        quadrados = {
            'a': Square(side_length = 3.25).move_to(np.array([4, -0.375, 0])).rotate(-np.arcsin(5/13)).set_color(RED),
            'b': Square(side_length = 3).move_to(np.array([-4.5, -1, 0])).set_color(GREEN),
            'c': Square(side_length = 1.25).move_to(np.array([-2.35, 1.15, 0])).set_color(BLUE)
        }

        textos_quadrados = {
            'a': TexMobject('a^{2}').move_to(quadrados['a']).set_color(RED),
            'b': TexMobject('b^{2}').move_to(quadrados['b']).set_color(GREEN),
            'c': TexMobject('c^{2}').move_to(quadrados['c']).set_color(BLUE)
        }

        triangulos = [
            triangulo.copy().rotate(0*DEGREES).next_to(quadrados['b'], UP, 0.02),
            triangulo.copy().rotate(90*DEGREES).next_to(quadrados['b'], RIGHT, 0.02),
            triangulo.copy().rotate(180*DEGREES).next_to(quadrados['b'], UP, 0.02),
            triangulo.copy().rotate(270*DEGREES).next_to(quadrados['b'], RIGHT, 0.02),
            triangulo.copy().rotate(0*DEGREES).next_to(quadrados['b'], UP, 0.02),
            triangulo.copy().rotate(90*DEGREES).next_to(quadrados['b'], RIGHT, 0.02),
            triangulo.copy().rotate(180*DEGREES).next_to(quadrados['b'], UP, 0.02),
            triangulo.copy().rotate(270*DEGREES).next_to(quadrados['b'], RIGHT, 0.02),
        ]

        self.add(*quadrados.values(), *textos_quadrados.values(), *triangulos)
        self.wait()

        self.play(triangulos[4].shift, 7.86*RIGHT + 3.02*DOWN)
        self.play(triangulos[5].shift, 7.85*RIGHT)
        self.play(triangulos[6].shift, 9.12*RIGHT)
        self.play(triangulos[7].shift, 4.87*RIGHT + 1.27*UP)

        self.remove(*quadrados.values(), *textos_quadrados.values(), *triangulos)

    def mostrandoMedidas(self):
        retas = {
            'a': Line(start = np.array([0, 1.25, 0]), end = np.array([3, 0, 0])),
            'b': Line(start = np.array([0, 0, 0]), end = np.array([3, 0, 0])),
            'c': Line(start = np.array([0, 0, 0]), end = np.array([0, 1.25, 0]))
        }

        triangulo = VGroup(retas['a'], retas['b'], retas['c']).move_to(ORIGIN)

        quadrados = {
            'a': Square(side_length = 3.25).move_to(np.array([4, -0.375, 0])).rotate(-np.arcsin(5/13)).set_color(RED),
            'b': Square(side_length = 3).move_to(np.array([-4.5, -1, 0])).set_color(GREEN),
            'c': Square(side_length = 1.25).move_to(np.array([-2.35, 1.15, 0])).set_color(BLUE)
        }

        textos_quadrados = {
            'a': TexMobject('a^{2}').move_to(quadrados['a']).set_color(RED),
            'b': TexMobject('b^{2}').move_to(quadrados['b']).set_color(GREEN),
            'c': TexMobject('c^{2}').move_to(quadrados['c']).set_color(BLUE)
        }

        triangulos = [
            triangulo.copy().rotate(0*DEGREES).next_to(quadrados['b'], UP, 0.02),
            triangulo.copy().rotate(90*DEGREES).next_to(quadrados['b'], RIGHT, 0.02),
            triangulo.copy().rotate(180*DEGREES).next_to(quadrados['b'], UP, 0.02),
            triangulo.copy().rotate(270*DEGREES).next_to(quadrados['b'], RIGHT, 0.02),
            triangulo.copy().rotate(0*DEGREES).next_to(quadrados['b'], UP, 0.02).shift(7.86*RIGHT + 3.02*DOWN),
            triangulo.copy().rotate(90*DEGREES).next_to(quadrados['b'], RIGHT, 0.02).shift(7.85*RIGHT),
            triangulo.copy().rotate(180*DEGREES).next_to(quadrados['b'], UP, 0.02).shift(9.12*RIGHT),
            triangulo.copy().rotate(270*DEGREES).next_to(quadrados['b'], RIGHT, 0.02).shift(4.87*RIGHT + 1.27*UP),
        ]

        braces = [
            Brace(triangulos[0], direction = UP).set_color(GREEN),
            Brace(quadrados['c'], direction = UP).set_color(BLUE),
            Brace(quadrados['c'], direction = RIGHT).set_color(BLUE),
            Brace(triangulos[1], direction = RIGHT).set_color(GREEN),
            Brace(triangulos[4], direction = LEFT).set_color(BLUE),
            Brace(triangulos[7], direction = LEFT).set_color(GREEN),
            Brace(triangulos[7], direction = UP).set_color(BLUE),
            Brace(triangulos[6], direction = UP).set_color(GREEN)
        ]

        medidas_lados = ['b', 'c', 'c', 'b', 'c', 'b', 'c', 'b']
        cores = [GREEN, BLUE, BLUE, GREEN, BLUE, GREEN, BLUE, GREEN]

        textos_braces = [
            braces[i].get_tex(medidas_lados[i]).set_color(cores[i])
            for i in range(len(braces))
        ]

        braces_agrupados = [
            VGroup(braces[0], braces[1]),
            VGroup(braces[2], braces[3]),
            VGroup(braces[4], braces[5]),
            VGroup(braces[6], braces[7]),
        ]

        textos_braces_agrupados = [
            VGroup(textos_braces[0], textos_braces[1]),
            VGroup(textos_braces[2], textos_braces[3]),
            VGroup(textos_braces[4], textos_braces[5]),
            VGroup(textos_braces[6], textos_braces[7]),
        ]

        # braces a + b
        braces_compostos = [
            Brace(VGroup(triangulos[2], quadrados['c']), direction = UP),
            Brace(VGroup(quadrados['c'], triangulos[1]), direction = RIGHT),
            Brace(VGroup(triangulos[4], triangulos[7]), direction = LEFT),
            Brace(VGroup(triangulos[7], triangulos[6]), direction = UP)
        ]

        rotacoes = [0, -PI/2, PI/2, 0]
        distancias = [np.array([0, 0, 0]), 0.3*LEFT, 0.3*RIGHT, np.array([0, 0, 0])]

        textos_braces_compostos = [
            braces_compostos[i].get_tex('b+c').rotate(rotacoes[i]).shift(distancias[i])
            for i in range(len(braces_compostos))
        ]

        igual = TexMobject('=').move_to(0.5*DOWN)

        self.add(*quadrados.values(), *textos_quadrados.values(), *triangulos)
        self.wait()

        for i in range(len(braces)):
            self.play(
                ShowCreation(braces[i]),
                ShowCreation(textos_braces[i])
            )
            self.wait(0.5)

        for i in range(len(braces_agrupados)):
            self.play(
                ReplacementTransform(braces_agrupados[i], braces_compostos[i]),
                ReplacementTransform(textos_braces_agrupados[i], textos_braces_compostos[i])
            )
            self.wait(0.5)
        self.wait()

        self.play(
            FadeOut(braces_compostos[0]),
            FadeOut(braces_compostos[1]),
            FadeOut(braces_compostos[2]),
            FadeOut(braces_compostos[3]),
            FadeOut(textos_braces_compostos[0]),
            FadeOut(textos_braces_compostos[1]),
            FadeOut(textos_braces_compostos[2]),
            FadeOut(textos_braces_compostos[3]),
        )
        self.wait(2)

        self.play(FadeIn(igual))
        self.wait()

        self.play(
            FadeOut(triangulos[0]),
            FadeOut(triangulos[1]),
            FadeOut(triangulos[2]),
            FadeOut(triangulos[3]),
            FadeOut(triangulos[4]),
            FadeOut(triangulos[5]),
            FadeOut(triangulos[6]),
            FadeOut(triangulos[7]),
        )
        self.wait()

        self.remove(*quadrados.values(), *textos_quadrados.values(), *triangulos, igual)

    def rearranjandoEquacao(self):
        quadrados = {
            'a': Square(side_length = 3.25).move_to(np.array([4, -0.375, 0])).rotate(-np.arcsin(5/13)).set_color(RED),
            'b': Square(side_length = 3).move_to(np.array([-4.5, -1, 0])).set_color(GREEN),
            'c': Square(side_length = 1.25).move_to(np.array([-2.35, 1.15, 0])).set_color(BLUE)
        }

        textos_quadrados = {
            'a': TexMobject('a^{2}').move_to(quadrados['a']).set_color(RED),
            'b': TexMobject('b^{2}').move_to(quadrados['b']).set_color(GREEN),
            'c': TexMobject('c^{2}').move_to(quadrados['c']).set_color(BLUE)
        }

        igual = TexMobject('=').move_to(0.5*DOWN)
        mais = TexMobject('+').move_to(3.4*RIGHT)

        sqrt_a = TexMobject('\\sqrt{a^{2}}').move_to(np.array([-4, 0, 0])).set_color(RED)

        sqrt = TexMobject('\\sqrt{}').move_to(np.array([-0.5, 0.1, 0])).scale(1.5)
        reta_sqrt = Line(start = np.array([-0.21, 0.45, 0]), end = np.array([2.5, 0.45, 0]))
        texto_a = TexMobject('a').move_to(np.array([-2.4, 0, 0])).set_color(RED).scale(1.2)
        
        reta = Line(start = np.array([0, 0, 0]), end = np.array([3.25, 0, 0])).next_to(quadrados['a'], direction = DOWN, buff = 0).set_color(RED).shift(np.array([-8, 0.87, 0]))

        self.add(*quadrados.values(), *textos_quadrados.values(), igual)

        self.play(quadrados['a'].rotate, np.arcsin(5/13))
        self.wait()

        # rearranjando quadrados e montando equação
        self.play(
            quadrados['a'].move_to, np.array([-4, 0, 0]),
            quadrados['b'].move_to, np.array([1, 0, 0]),
            quadrados['c'].move_to, np.array([5, 0, 0]),
            textos_quadrados['a'].move_to, np.array([-4, 0, 0]),
            textos_quadrados['b'].move_to, np.array([1, 0, 0]),
            textos_quadrados['c'].move_to, np.array([5, 0, 0]),
            igual.move_to, np.array([-1.5, 0, 0]),
            run_time = 2
        )
        
        self.play(FadeIn(mais))
        self.wait()

        self.play(
            FadeOut(quadrados['b']),
            FadeOut(quadrados['c'])
        )
        self.wait()

        # montando equação
        self.play(
            textos_quadrados['c'].move_to, np.array([2, 0, 0]),
            textos_quadrados['b'].move_to, np.array([0, 0, 0]),
            igual.move_to, np.array([-1.5, 0, 0]),
            mais.move_to, np.array([1, 0, 0]),
        )
        self.wait()

        self.add(reta)
        self.play(
            ReplacementTransform(textos_quadrados['a'], sqrt_a),
            FadeOut(quadrados['a']),
            FadeIn(sqrt),
            FadeIn(reta_sqrt)
        )
        self.wait()

        self.play(
            ReplacementTransform(sqrt_a, texto_a),
            FadeOut(reta)
        )
        self.wait()

class sqrt2(Scene):
    def construct(self):
        self.showTitle()
        self.drawSquare()
        self.drawTriangle()
        self.buildingTheEquation()

    def showTitle(self):
        title = TextMobject('Demonstrando $\\sqrt{2}$')

        self.play(ShowCreation(title))
        self.wait()
        self.play(FadeOut(title))
        self.wait()

    def drawSquare(self):
        square = Square(side_length = 2)
        braces = [
            Brace(square, LEFT),
            Brace(square, DOWN)
        ]
        braces_texts = [
            braces[0].get_tex('1'),
            braces[1].get_tex('1')
        ]

        self.play(ShowCreation(square))
        self.wait()
        for i in range(0, 1+1, 1):
            self.play(ShowCreation(braces[i]), ShowCreation(braces_texts[i]))
            self.wait()

        self.remove(square, *braces, *braces_texts)

    def drawTriangle(self):
        triangle = VGroup(
            Line(start = np.array([0, 0, 0]), end = np.array([2, 0, 0])),
            Line(start = np.array([2, 0, 0]), end = np.array([0, 2, 0])),
            Line(start = np.array([0, 2, 0]), end = np.array([0, 0, 0]))
        ).move_to(ORIGIN)
        square = Square(side_length = 2)
        braces = [
            Brace(triangle, UR),
            Brace(triangle, DOWN),
            Brace(triangle, LEFT),
        ]
        braces_texts = [
            braces[0].get_tex('a'),
            braces[1].get_tex('1'),
            braces[2].get_tex('1')
        ]
        squares = [
            Square(side_length = 2*np.sqrt(2)).rotate(PI/4).next_to(triangle, direction = UR, buff = -2),
            Square(side_length = 2).next_to(triangle, direction = DOWN, buff = 0),
            Square(side_length = 2).next_to(triangle, direction = LEFT, buff = 0)
        ]
        square_texts = [
            TexMobject('a^{2}').move_to(squares[0]),
            TexMobject('1^{2}').move_to(squares[1]),
            TexMobject('1^{2}').move_to(squares[2]),
            TexMobject('1').move_to(squares[1]),
            TexMobject('1').move_to(squares[2])
        ]

        self.add(square, braces[1], braces[2], braces_texts[1], braces_texts[2])
        self.wait()
        self.play(ShowCreation(triangle))
        self.wait()
        self.play(FadeOut(square))
        self.wait()
        self.play(ShowCreation(braces[0]), ShowCreation(braces_texts[0]))
        self.wait()
        self.play(
            ReplacementTransform(braces[0], squares[0]), 
            ReplacementTransform(braces_texts[0], square_texts[0])
        )
        self.wait()
        self.play(
            ReplacementTransform(braces[1], squares[1]),
            ReplacementTransform(braces_texts[1], square_texts[1])
        )
        self.wait()
        self.play(
            ReplacementTransform(braces[2], squares[2]),
            ReplacementTransform(braces_texts[2], square_texts[2])
        )
        self.wait()
        self.play(ReplacementTransform(square_texts[1], square_texts[3]))
        self.wait()
        self.play(ReplacementTransform(square_texts[2], square_texts[4]))
        self.wait()

        self.remove(triangle, square, *braces, *braces_texts, *squares, *square_texts)
    
    def buildingTheEquation(self):
        triangle = VGroup(
            Line(start = np.array([0, 0, 0]), end = np.array([2, 0, 0])),
            Line(start = np.array([2, 0, 0]), end = np.array([0, 2, 0])),
            Line(start = np.array([0, 2, 0]), end = np.array([0, 0, 0]))
        ).move_to(ORIGIN)
        squares = [
            Square(side_length = 2*np.sqrt(2)).rotate(PI/4).next_to(triangle, direction = UR, buff = -2),
            Square(side_length = 2).next_to(triangle, direction = DOWN, buff = 0),
            Square(side_length = 2).next_to(triangle, direction = LEFT, buff = 0)
        ]
        square_texts = [
            TexMobject('a^{2}').move_to(squares[0]),
            TexMobject('1').move_to(squares[1]),
            TexMobject('1').move_to(squares[2])
        ]
        initial_equation = TexMobject(
            'a^{2}', 
            '=', 
            '1', 
            '+', 
            '1'
        ).move_to(2*RIGHT)

        sqrt2 = "%.20f" % np.sqrt(2)

        equation_elements = {
            '2': TexMobject('2').next_to(initial_equation[1], direction = RIGHT, buff = 0.3),
            'sqrt2': TexMobject('\\sqrt{2}').next_to(initial_equation[1], direction = RIGHT, buff = 0.2),
            'a': TexMobject('a').move_to(initial_equation[0]).shift(0.1*DOWN),
            'sqrt(2)': TexMobject('=' + sqrt2)
        }

        braces = [
            Brace(triangle.copy().shift(3.5*LEFT), direction = UR, buff = 0.1),
            Brace(triangle.copy().shift(3.5*LEFT), direction = DOWN, buff = 0.1),
            Brace(triangle.copy().shift(3.5*LEFT), direction = LEFT, buff = 0.1)
        ]

        braces_texts = [
            braces[0].get_tex('a'),
            braces[1].get_tex('1'),
            braces[2].get_tex('1')
        ]
        

        self.add(triangle, *squares, *square_texts)
        self.play(
            triangle.shift, 3.5*LEFT,
            squares[0].shift, 3.5*LEFT,
            squares[1].shift, 3.5*LEFT,
            squares[2].shift, 3.5*LEFT,
            square_texts[0].shift, 3.5*LEFT,
            square_texts[1].shift, 3.5*LEFT,
            square_texts[2].shift, 3.5*LEFT,
        )
        self.wait()
        self.play(ReplacementTransform(square_texts[0].copy(), initial_equation[0]))
        self.play(ReplacementTransform(square_texts[1].copy(), initial_equation[2]))
        self.play(ReplacementTransform(square_texts[2].copy(), initial_equation[4]))
        self.wait()
        self.play(
            FadeIn(initial_equation[1]),
            FadeIn(initial_equation[3])
        )
        self.wait()

        self.play(ReplacementTransform(VGroup(*initial_equation[2:5]), equation_elements['2']))
        self.wait()
        self.play(
            ReplacementTransform(equation_elements['2'], equation_elements['sqrt2']),
            ReplacementTransform(initial_equation[0], equation_elements['a'])
        )
        self.wait()
        self.play(
            ReplacementTransform(squares[0], braces[0]), 
            ReplacementTransform(square_texts[0], braces_texts[0])
        )
        self.wait()
        self.play(
            ReplacementTransform(squares[1], braces[1]), 
            ReplacementTransform(square_texts[1], braces_texts[1])
        )
        self.wait()
        self.play(
            ReplacementTransform(squares[2], braces[2]), 
            ReplacementTransform(square_texts[2], braces_texts[2])
        )
        self.wait()
        self.play(
            FadeOut(braces[1]),
            FadeOut(braces_texts[1]),
            FadeOut(braces[2]),
            FadeOut(braces_texts[2]),
        )
        self.wait()
        self.play(
            equation_elements['sqrt2'].move_to, braces_texts[0],
            FadeOut(initial_equation[1]),
            FadeOut(braces_texts[0]),
            FadeOut(equation_elements['a'])
        )
        self.wait()
        self.play(
            triangle.shift, 3.5*RIGHT,
            braces[0].shift, 3.5*RIGHT,
            equation_elements['sqrt2'].shift, 3.5*RIGHT
        )
        self.wait()
        self.play(
            FadeOut(triangle),
            FadeOut(braces[0])
        )
        self.wait()
        self.play(equation_elements['sqrt2'].move_to, 3*LEFT)
        self.wait()
        self.play(Write(equation_elements['sqrt(2)'].next_to(equation_elements['sqrt2'], direction = RIGHT, buff = 0.2)))
        self.wait(3)


# Fechamento
class Fechamento(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")
      explora.shift(2.5*UP)

      site=TextMobject("https://wordpress.ft.unicamp.br/explora/")
      site.scale(1.0)
      site.set_color(WHITE)
      site.shift(0.8*UP)

      autor=TextMobject("Animações: Eric Satoshi Suzuki Kishimoto")
      autor.scale(1.2)
      autor.set_color("#dc6a40")
      autor.shift(0.3*DOWN)

      ft = ImageMobject("logo-FT.jpg")
      ft.scale(1.5)
      ft.shift(2.3*DOWN+3*RIGHT)

      unicamp = ImageMobject("logo-unicamp.jpg")
      unicamp.scale(1.5)
      unicamp.shift(2.3*DOWN+3*LEFT)
      
      self.play(FadeIn(explora),FadeIn(site))
      self.wait(1)
      self.play(FadeIn(unicamp),FadeIn(ft))
      self.wait(1)
      self.play(FadeOut(unicamp),FadeOut(ft))
      self.wait(0.8)
      self.play(FadeIn(autor))
      self.wait(2)