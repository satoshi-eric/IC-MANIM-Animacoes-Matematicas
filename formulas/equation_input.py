import re
import pandas as pd
from typing import *

def read_text_file(file_path: str) -> List[str]:
    '''
    Reads a text and return a list of lines.

    Example:
        \tread_text_file('path/to/file')

    Parameters
    ----------
    file_path: str
        Path to the text file.

    Returns
    -------
    List[str]
        A list of lines in the text file.
    '''
    with open(file_path) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line.strip() != '']
        return lines

def split_equations_parts(lines: List[str]) -> List[str]:
    '''
    Splits a list of strings into a list of equations.

    Example:
        \tsplit_equations_parts(['2x = 3']) -> ['2', 'x', '=', '3']

    Parameters
    ----------
    lines: List[str]
        A list of lines to split.

    Returns
    -------
    List[str]
        A list of lines split by line.
    '''
    equations = []
    latex_symbols = [
        r'\\over',
        r'\\cdot'
        r'\^[0-9]',
        r'\_[0-9]',
        r'[a-z]',
        r'[A-Z]',
        # r'[0-9]',
        # r'\{',
        # r'\}',
        r'\[',
        r'\]',
        r'\(',
        r'\)',
        r'\+',
        r'\-',
        r'\*',
        r'\=',
        r'\s'
    ]
    for line in lines:
        line = re.split(r'(' + '|'.join(latex_symbols) + ')', line)
        line = [part.strip() for part in line if part.strip()]
        equations.append(line)
    return equations


def convert_to_df(equation_parts: List[List[str]]) -> pd.DataFrame:
    '''
    Convert list of equation parts into a Dataframe

    Examples:
        \tconvert_to_df([['2', 'x', '=', '3'], ['y', '=', '{', '2', '\over', '3', '}'])

    Parameters
    ----------
    equation_parts: List[List[str]]
        A list of equation parts.

    Returns
    -------
    pd.DataFrame
        A Dataframe of the equation parts.
    '''
    largest_equation_length = max([len(equation) for equation in equation_parts])
    df = pd.DataFrame(equation_parts, columns=range(largest_equation_length))
    return df
    
def convert_to_csv(df: pd.DataFrame, file_path: str) -> None:
    '''
    Converts a Dataframe into a csv file.

    Example:
        \tconvert_to_csv(df, 'path/to/file')

    Parameters
    ----------
    df: pd.DataFrame
        A Dataframe to convert.
    file_path: str
        Path to the csv file.

    Returns
    -------
    None
    '''
    df.to_csv(file_path, index=False)

def parse_equations(input_file: str) -> pd.DataFrame:
    '''
    Parses a text file, write to csv files  and returns the Dataframe.

    Example:
        \tparse_equations('input_file.txt', 'output_file.csv')

    Parameters
    ----------
    input_file: str
        Path to the text file.

    output_file: str
        Path to the csv file.

    Returns
    -------
    pd.DataFrame
        A Dataframe of the equations.
    '''
    lines = read_text_file(input_file)
    equation_parts = split_equations_parts(lines)
    df = convert_to_df(equation_parts)
    csv_filename = input_file.replace('.txt', '.csv')
    convert_to_csv(df, csv_filename)
    convert_to_csv(df, '_map.'.join(csv_filename.split('.')))
    return df


if __name__ == '__main__':
    parse_equations('equations.txt')
    