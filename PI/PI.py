# ffmpeg -f concat -safe 0 -i list -c copy animação_PI.mp para juntar todas as animações
# onde list possui todos os vídeos em sequencia
# leave_progress_bars -> remove_progress_bars
# adicionar argumento --remove_progress_bars para remover as barras de progresso durante compilação


""" Animação para demonstração do cálculo de PI por meio do método de Arquimedes """
""" Autor: Eric Satoshi Suzuki Kishimoto """

from manimlib.imports import *

class Abertura(Scene):
    def construct(self):
      explora=TexMobject("\\vec{E}\\hspace{-1mm}\\times\\hspace{-1mm}\\vec{p}\\mathcal{L}0\\mathbb{R}a")
      explora.scale(4.5)
      explora.set_color("#43bfca")

      titulo=TextMobject("$\\pi$: Uma abordagem geométrica")
      titulo.scale(2)
      titulo.set_color("#dc6a40")
         
      self.play(FadeIn(explora), run_time=4)
      self.wait(1)
      self.play(Transform(explora,titulo))
      self.wait(1.5)


class Formula(Scene):
    def construct(self):
        formula_arq = TexMobject(r"n\cdot \sin \left ( \frac{{\pi}}{n} \right )").move_to(1.75 * UP).scale(1.75)
        formula_arq.set_color("#f5e342")
        explicacao1 = TextMobject("Quanto maior for o valor", "$n$, ").next_to(formula_arq, direction = DOWN, buff = 0.5).scale(1.5)

        explicacao1[1].shift(0.3 * RIGHT)

        explicacao2 = TextMobject("mais próximo de", "$\pi$", "será o valor").next_to(explicacao1, direction = DOWN, buff = 0.5).scale(1.5)
        explicacao2[1].shift(0.3 * RIGHT)
        explicacao2[2].shift(0.6 * RIGHT)

        # Alterando cores
        explicacao1[1].set_color("#f21707")
        explicacao2[1].set_color("#f21707")

        self.play(Write(formula_arq), run_time=2)
        self.play(Write(explicacao1))
        self.play(Write(explicacao2))
        self.wait(3)

#  Cena não usada
"""
class ExplicacaoRaioMeio(Scene):
    def construct(self):
        explicacao = TextMobject(r"Usaremos raio $\frac{1}{2}$ pois o comprimento do círculo é dado por ")
        formula1 = TexMobject("2", "\pi", "r").scale(1.5)
        metade = TexMobject(r"\frac{1}{2}").scale(1.5)

        explicacao.move_to(UP)
        formula1.next_to(explicacao, DOWN, buff=1)
        metade.next_to(formula1, RIGHT, buff=-0.3)
        
        

        self.play(Write(explicacao))
        self.play(Write(formula1))
        self.play(Transform(formula1[2], metade))
        self.play(FadeOutAndShift(formula1[0]), FadeOutAndShift(formula1[2]))
"""

class DemonstracaoGeometrica(Scene):
    def construct(self):
        # Circulo e poligono regular
        poligono_regular = RegularPolygon(n=8).scale(2.5).rotate(PI/8)
        circulo = Circle(radius = 2.5)
        circulo_opaco = Circle(radius = 2.5, stroke_opacity = 0.2)
        
        # objetos para criar as retas
        distancia_A = 2.5
        distancia_B = 2.5 * np.cos(PI/8)
        distancia_C = 2.5 * np.sin(PI/8)

        ponto_A = np.array([0, 0, 0])
        ponto_B = np.array([0, distancia_B, 0])
        ponto_C = np.array([distancia_C, distancia_B, 0])
        ponto_D = np.array([-distancia_C, distancia_B, 0])

        reta_A = Line(start = ponto_A, end = ponto_C)
        reta_B = Line(start = ponto_A, end = ponto_B)
        reta_C = Line(start = ponto_B, end = ponto_C)
        reta_D = Line(start = ponto_B, end = ponto_D)
        

        # Angulo
        angulo_theta = PI/8
        angulo = Arc(start_angle = 3*angulo_theta , angle = angulo_theta, radius = 0.5)

        # distâncias em braces
        objeto_distancia_A = Brace(reta_A, direction = DOWN + 2.5 * RIGHT)
        objeto_distancia_B = Brace(reta_B, LEFT)
        objeto_distancia_C = Brace(reta_C, UP)
        objeto_distancia_D = Brace(reta_D, UP)

        texto_objeto_distancia_A = objeto_distancia_A.get_text(
            "a",             # 0: a
            "=",             # 1: =
            r"$\frac{1}{2}$" # 2: fração 1/2
        )  # este objeto será utilizado nas equações

        texto_objeto_distancia_B = objeto_distancia_B.get_text("$b$")
        texto_objeto_distancia_C = objeto_distancia_C.get_text("$c$")
        texto_objeto_distancia_D = objeto_distancia_D.get_text("$c$")

        # Textos
        texto_theta = TexMobject(r"\theta")
        texto_theta.move_to(angulo.get_center() + 0.5 * UP + 0.1 * RIGHT)

        # triângulo formado a partir das retas
        triangulo_inicial = VGroup(reta_A, reta_B, reta_C, objeto_distancia_A, objeto_distancia_B, objeto_distancia_C, texto_objeto_distancia_A, texto_objeto_distancia_B, texto_objeto_distancia_C, angulo, texto_theta)


        # Animação do octágono inscrito no circulo
        self.play(Write(circulo))
        self.wait()
        self.play(Write(poligono_regular))
        self.wait()
        self.play(Transform(circulo, circulo_opaco))
        self.wait()

        # Animação do triângulo formado pelas retas A, B e C
        # self.play(Write(triangulo_inicial), FadeIn(objeto_distancia_D), FadeIn(texto_objeto_distancia_D), run_time = 2)
        self.play(Write(reta_A), Write(objeto_distancia_A), Write(texto_objeto_distancia_A))
        self.wait(1.5)
        self.play(Write(reta_B), Write(objeto_distancia_B), Write(texto_objeto_distancia_B))
        self.wait(1.5)
        self.play(Write(reta_C), Write(objeto_distancia_C), Write(texto_objeto_distancia_C))
        self.wait(1.5)
        self.play(Write(texto_theta), Write(angulo))
        self.wait(1.5)
        self.play(Write(objeto_distancia_D), Write(texto_objeto_distancia_D))
        self.wait(1.5)

        

        # Retirando o círculo e o octágono da cena
        self.play(
            FadeOut(circulo),
            FadeOut(poligono_regular),
            FadeOut(objeto_distancia_D),
            FadeOut(texto_objeto_distancia_D)
        )

        # triângulo à esquerda
        triangulo_esquerda = triangulo_inicial.copy()
        triangulo_esquerda.move_to(3 * LEFT)

        self.play(Transform(triangulo_inicial, triangulo_esquerda))

        """ Fórmulas """

        formula_seno = TexMobject(r"\sin(\theta)", "= ", r"{cateto\ oposto \over hipotenusa}").move_to(2.5 * RIGHT)
        f1 = TexMobject(r"\frac{c}{a}").next_to(formula_seno[1], RIGHT, buff = 0.2)
        f2 = TexMobject(r"\frac{c}{\frac{1}{2}}").next_to(formula_seno[1], RIGHT, buff = 0.2) 
        f3 = TexMobject(r"2c").next_to(formula_seno[1], RIGHT, buff = 0.2)
        
        self.play(Write(formula_seno))
        self.wait(1.5)
        self.play(Transform(formula_seno[2], f1))
        self.wait(1.5)
        self.play(Transform(formula_seno[2], f2))
        self.wait(1.5)
        self.play(Transform(formula_seno[2], f3))
        self.wait(1.5)

        # Movendo os objetos para a esquerda
        circulo.shift(3 * LEFT)
        poligono_regular.shift(3 * LEFT)
        texto_objeto_distancia_D.shift(3 * LEFT)
        objeto_distancia_D.shift(3 * LEFT)
        reta_D.shift(3 * LEFT)

        # objetos para as novas animações
        reta_C_copy = Line(start = ponto_B, end = ponto_C).shift(3 * LEFT)
        reta_D_copy = Line(start = ponto_B, end = ponto_D).shift(3 * LEFT)
        brace_reta_C = Brace(reta_C_copy, UP)
        brace_reta_D = Brace(reta_D_copy, UP)
        texto_brace_C = brace_reta_C.get_text("c") 
        texto_brace_D = brace_reta_D.get_text("c")
        braces = VGroup(brace_reta_C, brace_reta_D)
        texto_braces = VGroup(texto_brace_C, texto_brace_D)

        reta_C_D = Line(start = ponto_D, end = ponto_C).shift(3 * LEFT)
        brace_dois_C = Brace(reta_C_D, UP)
        texto_brace_dois_C = brace_dois_C.get_text("2c")

        # Animação para aparecer o circulo, o octágono e as distancias 'c' 
        self.play(
            FadeOut(objeto_distancia_A),
            FadeOut(objeto_distancia_B),
            FadeOut(objeto_distancia_C),
            FadeOut(texto_objeto_distancia_A),
            FadeOut(texto_objeto_distancia_B),
            FadeOut(texto_objeto_distancia_C),
            FadeOut(reta_A),
            FadeOut(reta_B),
            FadeOut(reta_C),
            FadeOut(texto_theta),
            FadeOut(angulo),
            FadeIn(circulo),
            FadeIn(poligono_regular), 
            FadeIn(reta_C_copy),
            FadeIn(reta_D_copy),
            FadeIn(braces),
            FadeIn(texto_braces)
        )
        self.wait()

        # pega os dois braces e transforma em um
        self.play(
            Transform(braces, brace_dois_C),
            Transform(texto_braces, texto_brace_dois_C)
        )
        self.wait()
        # substitui o 2c pelo sen(theta)
        self.play(
            FadeOut(texto_braces),
            formula_seno[0].copy().move_to, texto_braces
        )
        self.wait()


class DescobrindoTheta(Scene):
    def construct(self):
        # Constantes usadas
        theta = PI/8
        raio = 2.5
        
        # Objetos matemáticos
        circulo = Circle(radius = 2.5).shift(3*LEFT)
        octagono = RegularPolygon(n = 8).rotate(PI/8).scale(2.5).shift(3*LEFT)

        # listas para criação das retas
        angulos = [i for i in np.arange(PI/8, 2*PI + PI/8 + 1, PI/4)]
        coordenadas = [np.array([np.cos(angulo) * 2.5, np.sin(angulo) * 2.5, 0]) for angulo in angulos]

        # Objetos matemáticos
        retas = [Line(start = ORIGIN, end = coord).shift(3*LEFT) for coord in coordenadas]
        arcos = [Arc(start_angle = i * 2 * theta + PI/8 + 2 * theta, angle = -2 * theta, radius = 0.3).shift(3*LEFT) for i in range(0, 8)]
        retas_poligono = [] # retas que formam o polígono
        for i in range(8):
            retas_poligono.append(Line(start = coordenadas[i], end = coordenadas[i+1]).shift(3*LEFT))
            if i == 7:
                retas_poligono.append(Line(start = coordenadas[i], end = coordenadas[0]).shift(3*LEFT))

        # Textos e fórmulas
        thetas = [TexMobject(r"2\theta").scale(0.8).move_to(np.array([np.cos(i), np.sin(i), 0])).shift(3*LEFT) for i in np.arange(0*PI + 2*theta, 2*PI + 2*theta, PI/4)]

        textos_theta = VGroup(thetas[0], thetas[1], thetas[2], thetas[3], thetas[4], thetas[5], thetas[6], thetas[7])

        dezesseis_thetas = TexMobject(r"16\theta").scale(0.8).shift(3*LEFT) 
        oito_dois_theta = TexMobject(r"8\times2\theta").shift(3*LEFT)

        n_lados = [TexMobject("n={}\\ lados".format(i)).next_to(circulo, direction = DOWN, buff = 0.5) for i in range(0, 9)]

        formula_theta = TexMobject(r"8\times2\theta=2\pi").shift(2*RIGHT)
        f1 = TexMobject(r"8\times\theta=\pi").shift(2*RIGHT)
        f2 = TexMobject(r"n\times\theta=\pi").shift(2*RIGHT)
        f3 = TexMobject(r"\theta=\frac{\pi}{n}").shift(2*RIGHT)
        formula_perimetro = TexMobject(r"\text{perímetro}=8\times \sin(\theta)").shift(3*RIGHT)
        f4 = TexMobject(r"\text{perímetro} = 8 \times \sin\left ( \frac{\pi}{8} \right )").shift(3*RIGHT)
        f5 = TexMobject(r"\text{perímetro} = n \times \sin\left ( \frac{\pi}{n} \right )").shift(3*RIGHT)

        # Animações
        self.play(FadeIn(circulo))
        self.play(FadeIn(retas[0]), FadeIn(n_lados[0]))
        for i in range(0, 8):
            if i == 7:
                self.play(FadeIn(arcos[i]), FadeIn(thetas[i]), FadeIn(retas_poligono[i]), Transform(n_lados[0], n_lados[i+1]))
                break
            self.play(FadeIn(retas[i+1]), FadeIn(arcos[i]), FadeIn(thetas[i]), Transform(n_lados[0], n_lados[i+1]), FadeIn(retas_poligono[i]), run_time = 0.5)

        self.play(
            FadeOut(retas[0]),
            FadeOut(retas[1]),
            FadeOut(retas[2]),
            FadeOut(retas[3]),
            FadeOut(retas[4]),
            FadeOut(retas[5]),
            FadeOut(retas[6]),
            FadeOut(retas[7]),
            FadeOut(retas[8]),
            FadeOut(arcos[0]),
            FadeOut(arcos[1]),
            FadeOut(arcos[2]),
            FadeOut(arcos[3]),
            FadeOut(arcos[4]),
            FadeOut(arcos[5]),
            FadeOut(arcos[6]),
            FadeOut(arcos[7])
        )
        self.play(ReplacementTransform(textos_theta, dezesseis_thetas))
        self.wait()
        self.play(ReplacementTransform(dezesseis_thetas, oito_dois_theta))
        self.wait()
        self.play(ReplacementTransform(oito_dois_theta, formula_theta))
        self.wait()
        self.play(ReplacementTransform(formula_theta, f1))
        self.wait()
        self.play(ReplacementTransform(f1, f2))
        self.wait()
        self.play(ReplacementTransform(f2, f3))
        self.play(f3.shift, 1.5 * UP)
        self.wait()
        self.play(Write(formula_perimetro))
        self.wait()
        self.play(ReplacementTransform(formula_perimetro, f4))
        self.wait()
        self.play(ReplacementTransform(f4, f5))
        self.wait()


class Poligonos_regulares(Scene):
    def construct(self):

        # Fórmula para cálculo do PI
        formula_PI = lambda n: n * np.sin(PI/n)
        
        # Objetos usados na animação
        poligonos_regulares = [RegularPolygon(n) for n in range(1, 16)]
        circulo = Circle().shift(3*LEFT).scale(2)
        circulo_transformar = Circle().shift(3*LEFT).scale(2)

        # Formulas

        saidas_formula = [format(formula_PI(i), '.4f') for i in range(1, 16)]
        n_lados = [TexMobject(f"n={i}").move_to(2*RIGHT + UP) for i in range(1, 16)]
        n_formula = [
            TexMobject(rf"{i} \times \sin \left ( \pi \over {i} \right ) = {saidas_formula[i]}")
            .move_to(2*RIGHT + DOWN) 
            for i in range(1, 15)
        ]

        # objetos com numero de lado ímpar tem suas posições distorcidas ao usar o comando scale. Lista usada para corrigir esses erros
        correcao_de_posicao = [0, 0, 0.5, 0, 0.2, 0, 0.1, 0, 0.05, 0, 0.0375, 0.025]

        poligonos_regulares[1].scale(1.95)
        poligonos_regulares[1].move_to( circulo.get_center()+(UP*correcao_de_posicao[0]) )


        self.play(Write(circulo))
        self.play(Write(poligonos_regulares[1]), Write(n_lados[1]), Write(n_formula[1]))

        for i in range(2, 15):
            # Há algum problema com os poligonos reegulares e não é possível inscrevê-los perfeitamente na circunferência. 
            # O scale(1.95) está aí para corrigir esse erro
            

            # Esse if é usado para corrgir os erros dos primeiros 10 objetos utilizando a lista acima
            if i < 10:
                poligonos_regulares[i].move_to( circulo.get_center()+(UP*correcao_de_posicao[i]) )
                poligonos_regulares[i].scale(1.95)
            
            # Após os 10 primeiros polígonos serem corrigidos, a correção é muito pequena, por isso usa-se somente 0.02  
            else:
                poligonos_regulares[i].move_to( circulo.get_center()+(UP*0.02) )
                poligonos_regulares[i].scale(2)

        for i in range(1, 9):
            self.play(
                ReplacementTransform(poligonos_regulares[i], poligonos_regulares[i+1]), 
                ReplacementTransform(n_lados[i], n_lados[i+1]), 
                ReplacementTransform(n_formula[i], n_formula[i+1])
            )
            self.wait(0.3)
        self.wait(1.5)
        
        # polígonos de 20 e 200 lados
        saidas_formula.append(format(formula_PI(20), '.4f'))
        poligonos_regulares.append(RegularPolygon(n = 20).scale(2).move_to(circulo.get_center()))
        n_lados.append(TexMobject("n=20").move_to(2*RIGHT + UP)) 
        n_formula.append(
            TexMobject(rf"{20} \times \sin \left ( \pi \over {20} \right ) = {saidas_formula[15]}")
            .move_to(2*RIGHT + DOWN) 
        )

        saidas_formula.append(format(formula_PI(200), '.4f'))
        poligonos_regulares.append(RegularPolygon(n = 200).scale(2).move_to(circulo.get_center()))
        n_lados.append(TexMobject("n=200").move_to(2*RIGHT + UP)) 
        n_formula.append(
            TexMobject(rf"{200} \times \sin \left ( \pi \over {200} \right ) = {saidas_formula[16]}")
            .move_to(2*RIGHT + DOWN) 
        )

        # Animações de polígono de lados 20 e 200
        self.play(
            ReplacementTransform(poligonos_regulares[9], poligonos_regulares[15]),
            ReplacementTransform(n_lados[9], n_lados[15]),
            ReplacementTransform(n_formula[9], n_formula[14])
        )
        self.wait(1.5)        
        self.play(
            ReplacementTransform(poligonos_regulares[15], poligonos_regulares[16]),
            ReplacementTransform(n_lados[15], n_lados[16]),
            ReplacementTransform(n_formula[14], n_formula[15])
        )
        self.wait(1.5)

        formula = TexMobject(r"\infty  \times \sin \left ( \pi \over \infty  \right ) = \pi").move_to(2*RIGHT + DOWN)
        infinito = TexMobject(r"n=\infty ").move_to(2*RIGHT + UP)
        self.play(
            ReplacementTransform(n_lados[16], infinito), 
            ReplacementTransform(n_formula[15], formula), 
            ReplacementTransform(poligonos_regulares[16], circulo_transformar)
        )
        
        self.wait()

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
