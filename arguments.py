import pandas as pd
import argparse

parse = argparse.ArgumentParser(description='Testando anova simples')

parse.add_argument("-i","--input",
                    default='O input não foi carregado!',
                    required=True,
                    help='Path do input')

parse.add_argument("-o",
                    dest="--output",
                    type=
                    required=True,
                    default='Arquivo de saida',
                    help='Path do output')


args = vars(parse.parse_args())
print(args["input"])
df = pd.read_csv(args["input"])
print(df.head(3))

df.to_csv(args["output"]) 
