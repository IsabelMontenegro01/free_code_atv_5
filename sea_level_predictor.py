import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Ler os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Selecionar as colunas de interesse
    anos = df['Year']
    niveis_mar = df['CSIRO Adjusted Sea Level']

    # Criar o gráfico de dispersão
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(anos, niveis_mar)

    # Primeira linha de regressão usando todos os dados
    slope_all, intercept_all, r_all, p_all, std_err_all = linregress(anos, niveis_mar)
    anos_ext = np.arange(anos.min(), 2051)
    pred_all = intercept_all + slope_all * anos_ext
    ax.plot(anos_ext, pred_all)

    # Segunda linha de regressão usando apenas dados a partir de 2000
    dados_recentes = df[df['Year'] >= 2000]
    anos_recentes = dados_recentes['Year']
    niveis_recentes = dados_recentes['CSIRO Adjusted Sea Level']

    slope_rec, intercept_rec, r_rec, p_rec, std_err_rec = linregress(anos_recentes, niveis_recentes)
    anos_rec_ext = np.arange(2000, 2051)
    pred_rec = intercept_rec + slope_rec * anos_rec_ext
    ax.plot(anos_rec_ext, pred_rec)

    # Adicionar rótulos e título ao gráfico
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Salvar a imagem e retornar o objeto Axes
    plt.savefig('sea_level_plot.png')
    return ax
