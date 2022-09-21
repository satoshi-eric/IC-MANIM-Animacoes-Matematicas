from manim import *


class DiagonalQuadrado(Scene):
    def construct(self):
        quadrado = Square(side_length=4)\
            .set_color(WHITE)\
            .move_to(2*LEFT)
        lados_label = VGroup(
            MathTex('a').next_to(quadrado, direction=LEFT, buff=0.5),
            MathTex('a').next_to(quadrado, direction=DOWN, buff=0.5)
        ).set_color(WHITE)
        pontos_diagonal = (
            quadrado.point_from_proportion(0.25),
            quadrado.point_from_proportion(0.75)
        )
        diagonal = Line(*pontos_diagonal).set_color(RED)
        x_label = MathTex('x=', '?').next_to(quadrado, direction=RIGHT, buff=0.5).set_color(RED)
        cantos_triangulo = (
            quadrado.point_from_proportion(0.25),
            quadrado.point_from_proportion(0.5),
            quadrado.point_from_proportion(0.75)
        )
        triangulo = Polygon(*cantos_triangulo).set_color(PURPLE)
        ponto_angulo_retangulo = quadrado.point_from_proportion(0.5)\
                + 0.5*0.4*UP\
                + 0.5*0.4*RIGHT
        angulo_retangulo = VGroup(
            Square(side_length=0.4)\
            .move_to(ponto_angulo_retangulo)
            .set_color(BLUE),
            Dot(ponto_angulo_retangulo).scale(0.15*4)
        )
        equacao1 = MathTex('x^2', '=', 'a^2', '+', 'a^2').move_to(3*RIGHT)
        equacao2 = MathTex('x^2=2x^2').move_to(3*RIGHT)
        equacao3 = MathTex('x=\sqrt{2a^2}').move_to(3*RIGHT)
        equacao4 = MathTex('x=', '\sqrt{2}a').move_to(3*RIGHT)
        resultado = MathTex('x=', '\sqrt{2}a')\
            .move_to(triangulo.get_center() + 0.5*UP + 0.8*RIGHT)\
            .set_color(RED)

        self.play(Write(quadrado))
        self.play(Write(lados_label))
        self.play(Write(diagonal), Write(x_label))
        self.play(Write(triangulo))
        self.play(FadeOut(quadrado))
        self.play(x_label.animate.move_to(triangulo.get_center() + 0.5*UP + 0.5*RIGHT))
        self.play(Write(angulo_retangulo))
        self.play(
            ReplacementTransform(x_label.copy(), equacao1[0]),
            ReplacementTransform(lados_label[0].copy(), equacao1[2]),
            ReplacementTransform(lados_label[1].copy(), equacao1[4]),
            t=3
        )
        self.play(FadeIn(equacao1[1], equacao1[3]))
        self.wait()
        self.play(TransformMatchingTex(equacao1, equacao2), t=3)
        self.wait()
        self.play(TransformMatchingTex(equacao2, equacao3), t=3)
        self.wait()
        self.play(TransformMatchingTex(equacao3, equacao4), t=3)
        self.wait()
        self.play(
            TransformMatchingTex(x_label, resultado),
            ReplacementTransform(equacao4[1].copy(), resultado[1])
        )
        self.wait()