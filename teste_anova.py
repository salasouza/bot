import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

df = pd.read_csv('database/dataset.csv', sep='\t')

print(df.head())

from bioinfokit.analys import stat 
res = stat()
res.bartlett(df=df, res_var='petal.width', xfac_var='variety')


print(res.bartlett_summary)
