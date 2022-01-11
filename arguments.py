import pandas as pd
import argparse
from pandas.core.frame import DataFrame

import statsmodels.api as sm
from statsmodels.formula.api import ols

parse = argparse.ArgumentParser(description='Testando anova simples')

parse.add_argument("-i","--input",
                    default='O input não foi carregado!',
                    required=True,
                    help='Path do input')

parse.add_argument("-o","--output",
                    required=True,
                    default='Arquivo de saida',
                    help='Path do output')

parse.add_argument("-a", "--anova-one",
                    required=False,
                    default='Análise de Variância',
                    help='ANOVA one-way')

parse.add_argument("-b", "--anova-two",
                    required=False,
                    default='Análise de Variância',
                    help='ANOVA two-way')

parse.add_argument("-c", "--regression",
                    required=False,
                    default='Regressão linear',
                    help='Regressão linear')

parse.add_argument("-x", "--factor1",
                    required=False,
                    default='Factors',
                    help='Variavel independente')

parse.add_argument("-w", "--factor2",
                    required=False,
                    default='Factors',
                    help='Variavel independente')

parse.add_argument("-z", "--factor3",
                    required=False,
                    default='Factors',
                    help='Variavel independente')

parse.add_argument("-r", "--response",
                    required=False,
                    default='Resposta',
                    help='Variavel dependente')

args = vars(parse.parse_args())
print(args["input"])
print('\n')

df = pd.read_csv(args["input"], sep='\t')
df = pd.DataFrame(df)
print(df.head(3))
print('\n')

print(args["factor1"])
print('\n')


print(args["response"])
print('\n')

df.to_csv(args["output"])
print('Success')
print('\n')

from bioinfokit.analys import stat 
res = stat()
res.bartlett(df=df, res_var=args['response'], xfac_var=args['factor1'])


print(res.bartlett_summary)
print('\n')