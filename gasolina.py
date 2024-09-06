# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
gasolina_df = pd.read_csv('gasolina.csv')

# visualização dos dados

grafico_linha = sns.lineplot(x='dia',y='venda',data=gasolina_df)
plt.savefig('gasolina.png')