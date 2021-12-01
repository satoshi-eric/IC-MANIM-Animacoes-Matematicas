from manim import *
from pathlib import Path
import os
import itertools as it
from typing import Tuple
from matplotlib import pyplot as plt


class Hiperbole(VGroup):
    def __init__(
        self, 
        a: float = 2, 
        b: float = 1, 
        x_linspace: Tuple[int, int] = (-5, 5), 
        y_linspace: Tuple[int, int] = (-3, 3), 
        num_points: int = 50,
        **kwargs
    ):
        super().__init__(**kwargs)
        def m_point(coord: np.ndarray) -> np.ndarray:
            return np.append(coord, 0)

        x = np.linspace(*x_linspace, num_points)
        y = np.linspace(*y_linspace, num_points)
        x, y = np.meshgrid(x, y)

        self.__a = a
        self.__b = b
        
        hiperbole_plot = plt.contour(x, y, x**2/a**2 - y**2/b**2, [1])
        h_esq_plot = np.array(list(map(m_point, hiperbole_plot.allsegs[0][0])))
        h_dir_plot = np.array(list(map(m_point, hiperbole_plot.allsegs[0][1])))
        self.__h_esq, self.__h_dir = VGroup(), VGroup()
        
        for p_ini, p_fim in zip(h_esq_plot[0:-2], h_esq_plot[1:-1]):
            self.__h_esq.add(Line(p_ini, p_fim))

        for p_ini, p_fim in zip(h_dir_plot[0:-2], h_dir_plot[1:-1]):
            self.__h_dir.add(Line(p_ini, p_fim))

        self.add(self.__h_esq, self.__h_dir)

        self.__c = np.sqrt(a**2 + b**2)
        self.__f1 = np.array([self.__c, 0, 0])
        self.__f2 = np.array([-self.__c, 0, 0])


    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def f1(self):
        return self.__f1

    @property
    def f2(self):
        return self.__f2

    @property
    def hiperbola_esq(self):
        return self.__h_esq

    @property
    def hiperbola_dir(self):
        return self.__h_dir


class DerivandoHiperbole(Scene):
    def construct(self):
        self.init_ojects()
        self.definicoes_em_objetos()
        self.propriedades_hiperbole()
        self.mostrar_equacoes()

    def init_ojects(self):
        class Cores:
            hiperbole = RED
            focos = GREEN
            seg_focal = MAROON
            dist_focal = BLUE
            a = YELLOW

        self.escala_texto = 0.6

        # Textos de definição dos objetos da hipérbole: MathTex
        definicoes = Tex(
            '\\raggedright $ F_1, F_2 $: focos \n\n',
            '\\raggedright $ \\overline{F_1 F_2} $: segmento focal \n\n',
            '\\raggedright $ 2c $: distância focal \n\n',
        ).move_to(2.5*UP + 5*RIGHT)

        self.def_focos = definicoes[0]
        self.def_seg_focal = definicoes[1].shift(0.3*LEFT)
        self.def_dist_focal = definicoes[2].shift(0.1*LEFT)

        # Configuração de textos de definição dos objetos: scale, move_to
        self.def_focos.scale(self.escala_texto).set_color(Cores.focos)
        self.def_seg_focal.scale(self.escala_texto).set_color(Cores.seg_focal)
        self.def_dist_focal.scale(self.escala_texto).set_color(Cores.dist_focal)
        

        # Objetos da hipérbole
        hiperbole = Hiperbole(a=3, b=2)
        focos = VGroup(
            VGroup(Dot(hiperbole.f1), MathTex('F_1').move_to(hiperbole.f1 + 0.5*UP)), 
            VGroup(Dot(hiperbole.f2), MathTex('F_2').move_to(hiperbole.f2 + 0.5*UP))
        )
        seg_focal = Line(hiperbole.f1, hiperbole.f2)

        # Distância focal: Linha em baixo do segmento focal 
        # simbolizando a distância entre os focos
        o_f1 = Line(ORIGIN, hiperbole.f1)
        o_f2 = Line(ORIGIN, hiperbole.f2)
        dist_focal = VGroup(
            o_f1, o_f2, 
            MathTex('c').scale(1.5).next_to(o_f1, UP, 0.5), 
            MathTex('c').scale(1.5).next_to(o_f2, UP, 0.5)
        )

        # a: distância entre a origem e o ponto de intersecação
        # do eixo x com a hipébole
        a_1 = Line(ORIGIN, np.array([hiperbole.a, 0, 0]))
        a_2 = Line(ORIGIN, np.array([-hiperbole.a, 0, 0]))
        a = VGroup(
            a_1, a_2,
            MathTex('a').scale(1.5).next_to(a_1, UP, 0.5),
            MathTex('a').scale(1.5).next_to(a_2, UP, 0.5),
        )

        eixos = Axes(
            x_axis_config={'include_ticks': False}, 
            y_axis_config={'include_ticks': False}
        )
        
        # Agrupando objetos
        hiperbole_objs = VGroup(
            eixos,
            hiperbole,
            focos,
            seg_focal,
            dist_focal,
            a
        ).scale(0.4).move_to(4*LEFT + DOWN)

        self.eixos = hiperbole_objs[0]
        self.hiperbole = hiperbole_objs[1]
        self.focos = hiperbole_objs[2]
        self.seg_focal = hiperbole_objs[3]
        self.dist_focal = hiperbole_objs[4]
        self.a = hiperbole_objs[5]

        # Configurando objetos
        self.hiperbole.set_color(Cores.hiperbole)
        self.focos.set_color(Cores.focos)
        self.seg_focal.set_color(Cores.seg_focal)
        self.dist_focal.set_color(Cores.dist_focal).shift(0.6*DOWN)
        self.a.set_color(Cores.a).shift(0.6*UP)

        propriedades = VGroup(
            MathTex('X=(x, y)'),
            MathTex('|d(X, F_1) - d(X, F_2)| =  2a \\rightarrow', 'd(X, F_1) - d(X, F_2) = \\pm 2a'),
            MathTex('F_1 = (-c, 0)'),
            MathTex('F_2 = (c, 0)'),
            MathTex('d(X, F_1) = \\sqrt{(x - c)^2 + (y + 0)^2} = \\sqrt{(x - c)^2 + y^2}'),
            MathTex('d(X, F_2) = \\sqrt{(x + c)^2 + (y + 0)^2} = \\sqrt{(x + c)^2 + y^2}'),
        ).scale(self.escala_texto)

        propriedades.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        propriedades.move_to(2.5*LEFT + 2*UP)

        self.x = propriedades[0]
        self.propriedade_hiperbole = propriedades[1]
        self.f1 = propriedades[2]
        self.f2 = propriedades[3]
        self.d1 = propriedades[4]
        self.d2 = propriedades[5]

        self.eq_hiperbole = self.propriedade_hiperbole[1].copy()

        equations_positions = it.cycle([
            2.5 * RIGHT,
            2.5 * RIGHT + 0.7*DOWN, 
            2.5 * RIGHT + 1.4*DOWN,
            2.5 * RIGHT + 2.1*DOWN,
        ])

        eqs_str = [
            'd(X, F_1) - d(X, F_2) = \\pm 2a',
            'd(X, F_1) = \\pm 2a + d(X, F_2)',
            '\\sqrt{(x - c)^2 + y^2} = \\pm 2a + \\sqrt{(x + c)^2 + y^2}',
            '(\\sqrt{(x - c)^2 + y^2})^2 = (\\pm 2a + \\sqrt{(x + c)^2 + y^2})^2',
            '(x - c)^2 + y^2 = 4a^2 + 4a \\sqrt{(x + c)^2 + y^2)} + (x + c)^2 + y^2',
            'x^2 - 2xc + c^2 + y^2 = 4a^2 + 4a \\sqrt{(x + c)^2 + y^2)} + x^2 + 2xc + c^2 + y^2',
            '4a \\sqrt{(x + c)^2 + y^2)} = -4a^2 - 4xc',
            'a \\sqrt{(x + c)^2 + y^2)} = -a^2 - xc',
            '(a \\sqrt{(x + c)^2 + y^2)})^2 = (-a^2 - xc)^2',
            'a^2 [(x + c)^2 + y^2] = a^4 + 2x^2 xc + x^2 c^2',
            'a^2 [x^2 + 2xc + c^2 + y^2] = a^4 + 2x^2 xc + x^2 c^2',
            'a^2 x^2 + 2a^2 xc + a^2c^2 + a^2 y^2 = a^4 + 2a^2 xc + x^2 c^2',
            'a^2 x^2 + a^2 c^2 + a^2 y^2 = a^4 + x^2 c^2',
            'a^2 x^2 + (c^2 -a^2) a^2 + a^2 y^2 = x^2 c^2',
            '(c^2 - a^2) a^2 + a^2 x^2 = x^2 c^2 - a^2 x^2',
            '(c^2 - a^2) a^2 + a^2 y^2 = (c^2 - a^2) x^2',
            'b^2 = c^2 - a^2',
            'b^2 a^2 + a^2 y^2 = b^2 x^2',
            '\\frac{b^2 a^2}{a^2 b^2} + \\frac{a^2 y^2}{a^2 b^2} = \\frac{b^2 x^2}{a^2 b^2}',
            '1 + \\frac{y^2}{b^2} = \\frac{x^2}{a^2}',
            '\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1'
        ]

        self.eqs = [
            MathTex(eq_str).scale(self.escala_texto).move_to(eq_pos)
            for eq_str, eq_pos in zip(eqs_str, equations_positions)
        ]


    def definicoes_em_objetos(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.eixos))
        play(Write(self.hiperbole))
        play(Write(self.def_focos))
        play(ReplacementTransform(self.def_focos.copy(), self.focos))
        play(Write(self.def_seg_focal))
        play(ReplacementTransform(self.def_seg_focal.copy(), self.seg_focal))
        play(Write(self.def_dist_focal))
        play(ReplacementTransform(self.def_dist_focal.copy(), self.dist_focal))
        play(Write(self.a))

    def propriedades_hiperbole(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.x))
        play(Write(self.propriedade_hiperbole))
        play(Write(self.f1))
        play(Write(self.f2))
        play(Write(self.d1))
        play(Write(self.d2))

    def mostrar_equacoes(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        play(ReplacementTransform(self.eq_hiperbole, self.eqs[0]))

        for i in range(len(self.eqs) - 1):
            if i % 4 == 3:
                play(FadeOut(self.eqs[i - 3]), t=2)
                self.wait()
            if i % 4 == 0 and i != 0:
                play(FadeOut(*self.eqs[i-3:i]), t=2)
                self.wait()
            play(ReplacementTransform(self.eqs[i].copy(), self.eqs[i+1]), t=2)
        
        play(FadeOut(*self.eqs[-4:-1]), t=2)
        play(Write(SurroundingRectangle(self.eqs[-1])), t=2)
        self.wait()

       

ARQ_NOME = Path(__file__).resolve()
CENA = DerivandoHiperbole.__name__
ARGS = '-pqh'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')