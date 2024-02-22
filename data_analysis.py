import matplotlib.pyplot as plt
import csv
import os

# RESGATA O VALOR DA ENV E ORGANIZA DA MANEIRA NECESSÁRIA PARA O CÓDIGO RODAR.
def dict_datapath(data_path):
    dictionary = {}
    with open(data_path) as file_csv:
        reader_csv = csv.DictReader(file_csv)   # --lib nativa do python para ler arquivos csv.
        for row in reader_csv:
            for key, value in row.items():
                if key not in dictionary:
                    dictionary[key] = []
                dictionary[key].append(value)
    return dictionary

# FAZ O PLOT DO GRÁFICO.
def graph_plot(months, sales):
    fig, ax = plt.subplots()
    ax.plot(months, sales)
    ax.set(xlabel='Meses', ylabel='Vendas')
    return plt.show()

#FAZ O TRATAMENTO PARA USAR OS VALORES DE FORMA CORRETA NO PLOT.
def treatment_plot(data):
    months = list(data.keys())
    values = list(data.values())
    sales = []
    for value in values:
        sale = int(value[0])                    # --transformando strings(dentro de listas) em inteiros para o plot do gráfico.
        sales.append(sale)
    return months, sales

# MAIN DO CÓDIGO, RESGATANDO A ENV E AS FUNÇÕES.
def main():
    data_path = os.environ.get('DATA_PATH')
    data = dict_datapath(data_path)
    data.pop('')                                # --removendo um valor null que foi criado sozinho dentro do dicionario.
    months, sales = treatment_plot(data)
    graph_plot(months, sales)

main()







    

