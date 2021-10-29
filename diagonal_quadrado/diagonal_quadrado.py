from manim import *
from pathlib import Path
import os


class DiagonalQuadrado(Scene):
    def construct(self):
        self.config_global()
        self.mostrar_quadrado()
        self.mostrar_triangulo()
        self.mostrar_manipulacao_algebrica()

    def config_global(self):
        def get_lados_quadrado(quadrado):
            lados_quadrado = [
                quadrado.point_from_proportion(i) 
                for i in np.arange(0, 1.25, 0.25)
            ]
            return lados_quadrado

        cor_quadrado = WHITE
        cor_lados_label = WHITE
        cor_diagonal = RED
        cor_x_label = cor_diagonal
        cor_triangulo = PURPLE
        cor_angulo_retangulo = BLUE

        tamanho_quadrado = 4
        tamanho_angulo_retangulo = tamanho_quadrado/10

        posicao_equacoes = 3*RIGHT
        posicao_quadrado = 2*LEFT

        self.quadrado = Square(side_length=tamanho_quadrado)\
            .set_color(cor_quadrado)\
            .move_to(posicao_quadrado)

        self.lados_label = VGroup(
            MathTex('a').next_to(self.quadrado, direction=LEFT, buff=0.5),
            MathTex('a').next_to(self.quadrado, direction=DOWN, buff=0.5)
        ).set_color(cor_lados_label)
        
        pontos_diagonal = (
            get_lados_quadrado(self.quadrado)[1],
            get_lados_quadrado(self.quadrado)[3]
        )
        
        self.diagonal = Line(*pontos_diagonal).set_color(cor_diagonal)
        self.x_label = MathTex('x=', '?').next_to(self.quadrado, direction=RIGHT, buff=0.5).set_color(cor_x_label)

        cantos_triangulo = (
            get_lados_quadrado(self.quadrado)[1],
            get_lados_quadrado(self.quadrado)[2],
            get_lados_quadrado(self.quadrado)[3],
        )
        self.triangulo = Polygon(*cantos_triangulo).set_color(cor_triangulo)
        
        ponto_angulo_retangulo = get_lados_quadrado(self.quadrado)[2]\
                + 0.5*tamanho_angulo_retangulo*UP\
                + 0.5*tamanho_angulo_retangulo*RIGHT
        self.angulo_retangulo = VGroup(
            Square(side_length=tamanho_angulo_retangulo)\
            .move_to(ponto_angulo_retangulo)
            .set_color(cor_angulo_retangulo),
            Dot(ponto_angulo_retangulo).scale(0.15*tamanho_quadrado)
        )

        equacoes = [
            MathTex('x^2', '=', 'a^2', '+', 'a^2'),
            MathTex('x^2=2x^2'),
            MathTex('x=\sqrt{2a^2}'),
            MathTex('x=', '\sqrt{2}a')
        ]
        
        self.equacoes = [
            equacao.move_to(posicao_equacoes) 
            for equacao in equacoes
        ]

        self.resultado = MathTex('x=', '\sqrt{2}a')\
            .move_to(self.triangulo.get_center() + 0.5*UP + 0.8*RIGHT)\
            .set_color(cor_x_label)


    def mostrar_quadrado(self):
        write = lambda *mobs: self.play(*(Write(mob) for mob in mobs))

        write(self.quadrado)
        write(self.lados_label)
        write(self.diagonal, self.x_label)


    def mostrar_triangulo(self):
        write = lambda *mobs: self.play(*(Write(mob) for mob in mobs))
        fadeout = lambda *mobs: self.play(FadeOut(*mobs))
        play = lambda *anim: self.play(*anim)

        write(self.triangulo)
        fadeout(self.quadrado)
        play(self.x_label.animate.move_to(self.triangulo.get_center() + 0.5*UP + 0.5*RIGHT))
        write(self.angulo_retangulo)

    def mostrar_manipulacao_algebrica(self):
        wait = lambda t=1: self.wait(t)
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        fadein = lambda *mobs: self.play(FadeIn(*mobs))

        play(
            ReplacementTransform(self.x_label.copy(), self.equacoes[0][0]),
            ReplacementTransform(self.lados_label[0].copy(), self.equacoes[0][2]),
            ReplacementTransform(self.lados_label[1].copy(), self.equacoes[0][4]),
            t=3
        )

        fadein(self.equacoes[0][1], self.equacoes[0][3])
        wait()
        play(TransformMatchingTex(self.equacoes[0], self.equacoes[1]), t=3)
        wait()
        play(TransformMatchingTex(self.equacoes[1], self.equacoes[2]), t=3)
        wait()
        play(TransformMatchingTex(self.equacoes[2], self.equacoes[3]), t=3)
        wait()

        play(
            TransformMatchingTex(self.x_label, self.resultado),
            ReplacementTransform(self.equacoes[3][1].copy(), self.resultado[1])
        )

        wait()

    

        

ARQ_NOME = Path(__file__).resolve()
CENA = DiagonalQuadrado.__name__
ARGS = '-pql'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')