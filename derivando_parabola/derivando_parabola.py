from math import dist
from manim import *
from pathlib import Path
import os
import itertools as it
from typing import Tuple
from matplotlib import pyplot as plt


class Parabola(VGroup):
    def __init__(
        self,
        p: float = 0.7,
        vertical: bool = False,
        x_linspace: Tuple[int, int] = (-2, 2),
        y_linspace: Tuple[int, int] = (-2, 2),
        num_points: int = 50,
        **kwargs
    ):
        super().__init__(**kwargs)
        def m_point(coord: np.ndarray) -> np.ndarray:
            return np.append(coord, 0)

        x = np.linspace(*x_linspace, num_points)
        y = np.linspace(*y_linspace, num_points)
        x, y = np.meshgrid(x, y)

        self.__p = p
        self.__foco = np.array([p, 0, 0])
        
        if vertical:
            parabola_plot = plt.contour(x, y, x**2 - 4*p*y, [0])
        else:
            parabola_plot = plt.contour(x, y, y**2 - 4*p*x, [0])
        parabola_m_points = np.array(list(map(m_point, parabola_plot.allsegs[0][0])))
        self.__pontos = parabola_m_points

        for p_ini, p_fim in zip(parabola_m_points[0:-2], parabola_m_points[1:-1]):
            self.add(Line(p_ini, p_fim))

    @property
    def p(self):
        return self.__p

    @property
    def foco(self):
        return self.__foco

    @property
    def pontos(self):
        return self.__pontos


class DerivandoParabola(Scene):
    def construct(self):
        self.init_ojects()
        self.definicoes_em_objetos()
        self.propriedades_parabola()
        self.mostrar_equacoes()
        self.func_inversa()

    def init_ojects(self):
        class Cores:
            parabola = RED
            reta_diretriz = GREEN
            foco = YELLOW
            parametro = BLUE
            ponto = PURPLE
            dist_foco = ORANGE
            dist_reta = MAROON

        self.escala_texto = 0.6

        # Objetos da parábola
        parabola = Parabola()
        eixos = Axes(
            x_axis_config={'include_ticks': False, 'include_tip': False},
            y_axis_config={'include_ticks': False, 'include_tip': False},
            x_length=5, y_length=5
        )
        r = eixos.get_axes()[1].copy()
        r.shift(parabola.p*LEFT).set_color(Cores.reta_diretriz)

        p1 = Line(parabola.p*LEFT, ORIGIN).set_color(Cores.parametro).shift(2*DOWN)
        p2 = Line(ORIGIN, parabola.p*RIGHT).set_color(Cores.parametro).shift(2*DOWN)
        p1_label = MathTex('p').scale(self.escala_texto).next_to(p1, UP).set_color(Cores.parametro)
        p2_label = MathTex('p').scale(self.escala_texto).next_to(p2, UP).set_color(Cores.parametro)

        f = Dot(parabola.foco).set_color(Cores.foco)
        f_label = MathTex('F').scale(self.escala_texto).next_to(f, UP).set_color(Cores.foco)
        foco = VGroup(f, f_label)

        p_coord = parabola.pontos[-1]
        p = Dot(p_coord).set_color(Cores.ponto)
        p_label = MathTex('P').scale(self.escala_texto).next_to(p_coord, UP).set_color(Cores.ponto)
        ponto = VGroup(p, p_label)
        
        d_p_foco = Line(p.get_center(), parabola.foco)
        d_p_reta = Line(p.get_center(), 
        (r.get_center()[0], p.get_center()[1], 0))

        d_p_foco.set_color(Cores.dist_foco)
        d_p_reta.set_color(Cores.dist_reta)

        parametro = VGroup(
            p1, p2, p1_label, p2_label,
        )

        parabola_objs = VGroup(
            parabola, 
            eixos, 
            r, 
            parametro, 
            foco, 
            d_p_foco, 
            ponto, 
            d_p_reta
        ).scale(0.8).move_to(4*LEFT + DOWN)

        self.parabola = parabola_objs[0]
        self.eixos = parabola_objs[1]
        self.reta_diretriz = parabola_objs[2]
        self.parametro = parabola_objs[3]
        self.foco = parabola_objs[4]
        self.dist_foco = parabola_objs[5]
        self.ponto = parabola_objs[6]
        self.dist_reta = parabola_objs[7]

        # Textos de definição dos objetos da parábola: MathTex
        definicoes = Tex(
            '\\raggedright $ r $ : reta diretriz \n\n',
            '\\raggedright $ F $ : foco \n\n',
            '\\raggedright $ p $ : parâmetro \n\n',
        ).scale(self.escala_texto).move_to(2.5*UP + 5*RIGHT)

        self.def_reta_diretriz = definicoes[0]
        self.def_foco = definicoes[1]
        self.def_parametro = definicoes[2]

        self.def_reta_diretriz.set_color(Cores.reta_diretriz)
        self.def_foco.set_color(Cores.foco)
        self.def_parametro.set_color(Cores.parametro)

        # Propriedades da parábola
        props = Tex(
            '\\raggedright $ F = (p, 0) $ \n\n',
            '\\raggedright $ P = (x, y) $ \n\n',
            '\\raggedright $ d(P, r) = |x + p| $ \n\n',
            '\\raggedright $ d(P, F) = \\sqrt{(x - p)^2 + y^2} $ \n\n',
            '\\raggedright $ d(P, r) = d(P, F) $ \n\n'
        ).scale(self.escala_texto).move_to(2.5*UP + 4*LEFT)

        self.prop_foco = props[0].set_color(Cores.foco)
        self.prop_ponto = props[1].set_color(Cores.ponto)
        self.prop_dist_reta = props[2].set_color(Cores.dist_reta)
        self.prop_dist_foco = props[3].set_color(Cores.dist_foco)
        self.eq_parabola = props[4]


        equations_positions = it.cycle([
            2.5 * RIGHT,
            2.5 * RIGHT + 0.7*DOWN, 
            2.5 * RIGHT + 1.4*DOWN,
            2.5 * RIGHT + 2.1*DOWN,
        ])

        eqs_str = [
            'd(P, r) = d(P, F)',
            '|x + p| = \\sqrt{(x - p)^2 + y^2}',
            '(|x + p|)^2 = (\\sqrt{(x - p)^2 + y^2})^2',
            'x^2 + 2xp + p^2 = (x - p)^2 + y^2',
            'x^2 + 2xp + p^2 = x^2 - 2xp + p^2 + y^2',
            '2xp + 2xp = y^2',
            'y^2 = 2xp + 2xp',
            'y^2 = 4xp',
        ]

        self.eqs = [
            MathTex(eq_str).scale(self.escala_texto).move_to(eq_pos)
            for eq_str, eq_pos in zip(eqs_str, equations_positions)
        ]

        self.desc_func_inversa = Tex('Se usarmos a função inversa, teremos a \\\\ parábola com a concavidade para cima')
        self.v_parabola = Parabola(vertical=True)
        self.eq_parabola_inversa = MathTex('x^2 = 4yp')
        self.resultado = MathTex('y = \\frac{x^2}{4p}')

        self.desc_func_inversa.scale(self.escala_texto).move_to(RIGHT + UP)
        self.v_parabola.scale(0.5).move_to(RIGHT + 0.75*DOWN)
        self.eq_parabola_inversa.scale(self.escala_texto).move_to(RIGHT + 2*DOWN)
        self.resultado.scale(self.escala_texto).move_to(RIGHT + 2*DOWN)

    def definicoes_em_objetos(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.eixos), t=1.5)
        self.wait()
        play(Write(self.parabola), t=1.5)
        self.wait()
        play(Write(self.def_reta_diretriz), t=1.5)
        self.wait()
        play(ReplacementTransform(self.def_reta_diretriz.copy(), self.reta_diretriz), t=1.5)
        self.wait()
        play(Write(self.def_foco), t=1.5)
        self.wait()
        play(ReplacementTransform(self.def_foco.copy(), self.foco), t=1.5)
        self.wait()
        play(Write(self.def_parametro), t=1.5)
        self.wait()
        play(ReplacementTransform(self.def_parametro.copy(), self.parametro), t=1.5)
        self.wait()
        play(Write(self.dist_foco), t=1.5)
        self.wait()
        play(Write(self.ponto), t=1.5)
        self.wait()
        play(Write(self.dist_reta), t=1.5)
        self.wait()


    def propriedades_parabola(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.prop_foco), t=1.5)
        self.wait()
        play(Write(self.prop_ponto), t=1.5)
        self.wait()
        play(Write(self.prop_dist_reta), t=1.5)
        self.wait()
        play(Write(self.prop_dist_foco), t=1.5)
        self.wait()
        play(Write(self.eq_parabola), t=1.5)
        self.wait()

    def mostrar_equacoes(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)
        play(ReplacementTransform(self.eq_parabola, self.eqs[0]))

        for i in range(len(self.eqs) - 1):
            if i % 4 == 3:
                play(FadeOut(self.eqs[i - 3]), t=1.5)
                self.wait()
            if i % 4 == 0 and i != 0:
                play(FadeOut(*self.eqs[i-3:i]), t=1.5)
                self.wait()
            play(ReplacementTransform(self.eqs[i].copy(), self.eqs[i+1]), t=1.5)
            self.wait()

        play(FadeOut(*self.eqs[-4:-1]), t=1.5)
        play(Write(destaque := SurroundingRectangle(self.eqs[-1])), t=2)
        self.wait()

        play(FadeOut(destaque, self.eqs[-1]), t=2)

    def func_inversa(self):
        play = lambda *anim, t=1: self.play(*anim, run_time=t)

        play(Write(self.desc_func_inversa), t=1.5)
        self.wait()
        play(Write(self.v_parabola), t=1.5)
        self.wait()
        play(Write(self.eq_parabola_inversa), t=1.5)
        self.wait()
        play(ReplacementTransform(self.eq_parabola_inversa, self.resultado), t=1.5)
        self.wait()
        play(Write(SurroundingRectangle(self.resultado)), t=1.5)
        self.wait()

ARQ_NOME = Path(__file__).resolve()
CENA = DerivandoParabola.__name__
ARGS = '-pqh'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')