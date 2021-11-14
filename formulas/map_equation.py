from numpy import NaN
import pandas as pd
from typing import *
from manim import *

def read_csv(filename: str) -> pd.DataFrame:
    """
    Reads a csv file and returns a dataframe.
    """
    return pd.read_csv(filename, dtype=str)

def create_equations(df: pd.DataFrame) -> List[MathTex]:
    equations = []
    for index, row in df.iterrows():
        filtered_line = list(filter(lambda part: part is not NaN, row.iloc[:]))
        equations.append(MathTex(*filtered_line))
    return equations

def map_equation(equation: MathTex, classes: pd.Series, style_equation: Callable[[Mobject], Mobject] = lambda mobject: mobject) -> VGroup:
    map_parts = [VGroup() for _ in range(max([int(class_number) for class_number in classes if class_number is not NaN])+1)]
    for i, part in enumerate(equation):
        map_parts[int(classes[i])].add(style_equation(part))
    return VGroup(*map_parts)

# def df_to_list(df: pd.DataFrame) -> List:
#     """
#     Converts a dataframe to a list of lists.
#     """
#     df_lst = []
#     for index, row in df.iterrows():
#         df_lst += row.to_list()

#     lst = [int(item) for item in df_lst if item is not NaN]
#     return lst

def map_equations(equations: List[MathTex], map_file: str, style_equation: Callable[[Mobject], Mobject] = lambda mobject: mobject) -> List[VGroup]:
    map_df = read_csv(map_file)
    eq_parts = []

    for i, row in map_df.iterrows():
        eq_parts.append(map_equation(equations[i], map_df.iloc[i, :], style_equation))

    return eq_parts




# if __name__ == "__main__":
#     equations = create_equations(read_csv("equacoes.csv"))
#     map_equations(equations, "equacoes_map.csv")


from manim import *
from pathlib import Path
import os

class Test(Scene):
    def construct(self):
        equations = create_equations(read_csv("equations.csv"))
        parts_equations = map_equations(equations, "equations_map.csv")
        self.play(Write(parts_equations[0]))
        for i in range(len(parts_equations) - 1):
            self.play(FadeOut(parts_equations[i][0]),)
            self.play(ReplacementTransform(parts_equations[i][1], parts_equations[i + 1][1]),)
            self.play(ReplacementTransform(parts_equations[i][2], parts_equations[i + 1][2]),)
            self.play(ReplacementTransform(parts_equations[i][3], parts_equations[i + 1][3]),)
            self.play(FadeIn(parts_equations[i][4]))
        self.wait()


ARQ_NOME = Path(__file__).resolve()
CENA = Test.__name__
ARGS = '-pql'

if __name__ == '__main__':
    os.system(f'manim {ARQ_NOME} {CENA} {ARGS}')