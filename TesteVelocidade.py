"""

****TESTE DE VELOCIDADE****
Código desenvolvido com a finalidade de verificar a conexão com a internet e realizar uma quantidade de testes de
velocidade espaçados por um intervalo. Os valores de "quantidade" e "intervalo" são pré-determinados pelo usuário antes
da execução do teste.
Além disso, foi elaborada uma interface gráfica para o programa, de modo a ficar o mais amigável possível para o usuário.

Possíveis aplicações:
-> Encontrar os melhores horários em que a conexão é estável
-> Auxíliar na verificação de pontos que faz-se necessário o uso de repetidores
-> Verificar se o plano contratado está condizente com a velocidade prometida pela operadora
O programa irá gerar dois arquivos de texto com os dados de download, upload e ping e gráficos em formato png,
além disso será feito um arquivo pdf que servirá como relatório dos dados, facilitando a visualização em comparação
aos arquivos .txt.

Arquivos gerados:
-> "dados.txt" - arquivo com informações apresentadas de maneira mais organizada separada por teste.
-> "resumo.txt" - arquivo que será utilizado na plotagem dos gráficos
-> "grafico_down.png" - gráfico 1 - download - velocidade de download pelo tempo.
-> "grafico_upl.png" - gráfico 2 - upload - velocidade de upload pelo tempo.
-> "grafico_ping.png" - gráfico 3 - ping - ping pelo tempo.
-> "report.pdf" - documento com relatório das informações obtidas a partir dos programa. 

Bibliotecas utilizadas: 
urllib.request: abre uma url. Utilizada para verificar a conexão com a internet.
time(sleep): especifica um delay em segundos que o programa esperará até o próximo teste. Será determinado pelo usuário em "intervalo"
speedtest: realiza o teste de velocidade da internet. Necessário instalar "speedtest-cli" (atenção para o nome)
tkinter: utilizada para a montagem da interface.
PIL: usada para ser possivel utilizar uma imagem .png no tkinter. Necessário instalar "Pillow"
threading: utilizada para não travar a interface, uma vez que a função main como é demorada fazia com que a interface travasse
pandas: usada para facilitar a visualização, modelar e manipular os dados de maneira simples e eficiente.
fpdf: usada para construir e elaborar pdf, facilitando a extração dos dados obtidos no "backend".
os: permite executar ações referentes ao sistema operacional. Nesse caso, está sendo utilizado para acessar a pasta em que está o programa e os dados gerados.
datetime: utilizada para fornecer a data e hora do sistema
matplotlib: lib suplementar para a plotagem dos gráficos feitos com a modelagem do pandas.
warnings: edição das configs do python para "warnings".

POSSÍVEIS MELHORIAS:
- Resolver erro ao encerrar o programa
- biblioteca urllib apresentou problemas ao ser executado em sistemas Mac e Linux.

**OBSERVAÇÃO:**
O arquivo "logo.png" deve estar na mesma pasta desse código.

Criadores:
Bruno Mingoti
Luigi Remor
Matheus Hrihorowitsch

"""


import time
import warnings
from fpdf import FPDF  # necessário instalar "pip install fpdf"
import pandas as pd  # necessário instalar "pip install pandas"
import urllib.request  # necessário instalar "pip install urllib"
from time import sleep
import speedtest  # necessário instalar "pip install speedtest.cli"
import tkinter as tk  # necessário instalar "pip install tkinter"
from tkinter import ttk  # necessário instalar "pip install tkinter"
from PIL import Image, ImageTk  # necessário instalar "pip install Pillow"
import os
from datetime import datetime
import threading
import matplotlib  # necessário instalar "pip install matplotlib"
import matplotlib.pyplot as plt  # necessário instalar "pip install matplotlib"
# Utilizado para omitir avisos da lib "matplotlib"
warnings.filterwarnings("ignore", category=UserWarning)


# Funções de manipulação de arquivo:

def arquivoExiste(nome):
    """
    Verifica se o arquivo em que será armazenado os dados da velocidade
    :param nome: nome do arquivo em que será armazenado os dados da velocidade
    :return: True ou False, dependendo se o arquivo foi ou não encontrado
    """

    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Cria o arquivo em que será armazenado os dados da velocidade
    :param nome: nome do arquivo em que será armazenado os dados da velocidade
    :return: boolean, indicando se foi ou não possível criar o arquivo
    """

    try:
        a = open(nome, "wt+")
        a.close()
        STATUS_text.set(f'Arquivo "{nome}" criado com sucesso!')
        root.update()
        sleep(2)
        return True
    except:
        STATUS_text.set(f"ERRO ao tentar criar o arquivo {nome}!")
        root.update()
        sleep(2)
        return False


def acessarPasta():
    """
    Abre a pasta atual do código no Explorer
    :return: sem retorno
    """
    path = os.getcwd()
    os.startfile(path)


def verificarConexao(site="https://www.google.com.br/"):
    """
    Verifica se o dispositivo está conectado à internet
    :param site: site que será utilizado para verificar a conexão
    :return: boolean, indicando se o dispositivo está ou não conectado
    """

    try:
        urllib.request.urlopen(site)
    except:
        STATUS_text.set(
            "Você não está conectado à internet."
            " Por favor verifique sua conexão antes de começarmos a medir a velocidade."
        )
        root.update()
        return False
    else:
        STATUS_text.set("Verificando conexão...")
        root.update()
        sleep(2)
        STATUS_text.set("Dispositivo conectado!")
        root.update()
        sleep(2)
        return True


# Função para o teste de velocidade
def testeVelocidade(nome1="dados.txt", nome2="resumo.txt", quantidade=1, intervalo=1):
    """
    Realizará o teste de velocidade
    :param nome: nome do arquivo em que será armazenado os dados da velocidade
    :param quantidade: número de vezes que o teste será realizado
    :param intervalo: valor em minutos indicando o intervalo de cada teste
    :return: sem retorno
    """

    # verificar se arquivo com o nome passado com parâmetro já existe, senão criar
    intervalo *= 60  # Convertendo minutos em segundos
    sucesso1 = True
    sucesso2 = True
    if not arquivoExiste(nome1):
        sucesso1 = criarArquivo(nome1)
    else:
        open(nome1, 'w').close()
    if not arquivoExiste(nome2):
        sucesso2 = criarArquivo(nome2)
    else:
        open(nome2, 'w').close()
    if sucesso1 and sucesso2:
        with open(nome1, "a") as arquivoDados:
            for i in range(quantidade):
                try:
                    STATUS_text.set(f"Realizando o teste {i+1}/{quantidade}")
                    root.update()
                    inicio = time.time()
                    s = speedtest.Speedtest()
                    s.get_servers()
                    s.get_best_server()
                    s.download()
                    s.upload()
                    resultados = s.results.dict()
                    download, upload, ping = (
                        resultados["download"],
                        resultados["upload"],
                        resultados["ping"],
                    )
                    fim = time.time()
                    tempo_gasto = fim - inicio
                    data_hora = datetime.today().strftime("%d/%m/%Y - %H:%M")
                    # Preciso converter o valor de download e e upload para a unidade de transmissão de dados que estamos acostumados (Mb/s):
                    download /= 1024000
                    upload /= 1024000
                    arquivoDados.write(f"Teste {i+1}\n")
                    arquivoDados.write(f"Data e hora: {data_hora}\n")
                    arquivoDados.write(f"Download: {download:.2f} Mb/s\n")
                    arquivoDados.write(f"Upload: {upload:.2f} Mb/s\n")
                    arquivoDados.write(f"Ping: {ping:.0f}\n")
                    with open(nome2, "a") as arquivoResumo:
                        arquivoResumo.write(
                            f"{data_hora};{download:.2f};{upload:.2f};{ping:.0f}\n"
                        )
                    if i + 1 != quantidade:
                        STATUS_text.set("Intervalo...")
                        if tempo_gasto > 0:
                            sleep(intervalo - tempo_gasto)
                except:
                    i -= 1
                    continue
        btn_text.set("Sucesso!...")

        # Criando relatório
        hoje = (datetime.today()).strftime(
            "%d/%m/%y").replace("/0", "/").lstrip("0")
        relatorio = CriadorRelatorio()
        relatorio.create_infos()
        relatorio.create_analytics_report(day=hoje)

        INTS2_text.set("Os dados estão disponíveis!")
        root.update()
        sleep(5)
        btn_text.set("Finalizando! 3..2..1")
        root.update()
        sleep(3)
        btn_text.set("Start Test")
        INTS2_text.set(
            "Os dados só estarão disponíveis após o término da execução do programa!"
        )
        STATUS_text.set("Pronto para começar!")
        comboExample2.current(newindex=0)
        comboExample.current(newindex=0)


# Função principal


def main():
    btn_text.set("Analisando...")
    root.update()
    conectado = verificarConexao()
    if conectado:
        while comboExample2.get() == "" or comboExample.get() == "":
            STATUS_text.set("Escolha os parâmetros!")
            root.update()
        STATUS_text.set("Escolha os parâmetros!")
        root.update()
        QNT = int(comboExample2.get())
        INTE = int(comboExample.get())
        testeVelocidade(quantidade=QNT, intervalo=INTE)
    else:
        btn_text.set("Start Test")
        root.update()


# Classe para criação dos relatórios pós obtenção dos dados


class CriadorRelatorio:
    # Função que é automática ao chamar a classe, utilizada para fácil acesso das variáveis.
    def __init__(self):
        self.download_text = ""
        self.upload_text = ""
        self.ping_text = ""
        self.width = 210

    # Criador de dados para o relatório

    def create_infos(self):
        # Define o tamanho do gráfico
        plt.rcParams["figure.figsize"] = (8, 6)
        # Faz a leitura do arquivo com os dados obtidos
        df = pd.read_csv("resumo.txt", sep=";", header=None)
        # Atribui nomes às colunas
        df.columns = ["data", "download", "upload", "ping"]
        # Gera o gráfico do download
        grafico_down = df.plot(
            title="Download em MB/s conforme o tempo",
            y="download",
            x="data",
            xlabel="Data",
            fontsize=14,
            ylabel="Mb/s",
            rot=45,
        )
        plt.tight_layout()
        plt.savefig("grafico_down.png")

        # Gera o gráfico do upload
        grafico_upl = df.plot(
            title="Upload em MB/s conforme o tempo",
            y="upload",
            x="data",
            xlabel="Data",
            fontsize=14,
            ylabel="Mb/s",
            color="g",
            rot=45,
        )
        plt.tight_layout()
        plt.savefig("grafico_upl.png")

        # Gera o gráfico do ping
        grafico_ping = df.plot(
            title="Ping em ms conforme o tempo",
            y="ping",
            x="data",
            xlabel="Data",
            fontsize=14,
            ylabel="ms",
            color="y",
            rot=45,
        )
        plt.tight_layout()
        plt.savefig("grafico_ping.png")

        # Análise de dados para o download
        download_mean = df["download"].mean()  # Média dos valores de download
        download_min = df["download"].min()  # Mínimo valor de download
        download_max = df["download"].max()  # Máximo valor de download

        # Análise de dados para o upload
        upload_mean = df["upload"].mean()  # Média dos valores de upload
        upload_min = df["upload"].min()  # Mínimo valor de upload
        upload_max = df["upload"].max()  # Máximo valor de upload

        # Análise de dados para o ping
        ping_mean = df["ping"].mean()  # Média dos valores de ping
        ping_min = df["ping"].min()  # Mínimo valor de ping
        ping_max = df["ping"].max()  # Máximo valor de ping

        # Gerar os textos com as infos obtidas
        self.download_text = f"     A média da velocidade de download foi de {download_mean:.2f} mb/s. O máximo foi de {download_max:.2f} mb/s e o mínimo foi de {download_min:.2f} mb/s"
        self.upload_text = f"     A média da velocidade de upload foi de {upload_mean:.2f} mb/s. O máximo foi de {upload_max:.2f} mb/s e o mínimo foi de {upload_min:.2f} mb/s"
        self.ping_text = f"     O ping médio foi de {ping_mean:.2f} ms. O máximo foi de {ping_min:.2f} ms e o mínimo foi de {ping_max:.2f} ms."

    # Criando a capa do relatório -> "report.pdf"
    def create_title(self, day, pdf):
        pdf.set_font("Arial", "BU", 24)
        pdf.ln(60)
        pdf.write(5, f"Relatorio de internet")
        pdf.ln(10)
        pdf.set_font("Arial", "", 16)
        pdf.write(4, f"{day}")
        pdf.ln(5)

    # Criando as páginas com os dados do backand
    def create_analytics_report(self, day, filename="report.pdf"):
        pdf = FPDF()

        # Pagina 1
        pdf.add_page()
        self.create_title(day, pdf)

        # Pagina 2
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.write(5, f"1. Download")
        pdf.ln(10)
        pdf.set_font("Arial", "", 14)
        pdf.write(5, self.download_text)
        pdf.image("grafico_down.png", 5, 40, self.width - 20)

        # Pagina 3
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.write(5, f"2. Ping")
        pdf.ln(10)
        pdf.set_font("Arial", "", 14)
        pdf.write(5, self.ping_text)
        pdf.image("grafico_ping.png", 5, 40, self.width - 20)

        # Pagina 4
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.write(5, f"3. Upload")
        pdf.ln(10)
        pdf.set_font("Arial", "", 14)
        pdf.write(5, self.upload_text)
        pdf.image("grafico_upl.png", 5, 40, self.width - 20)

        pdf.output(filename, "F")


# INTERFACE GRÁFICA - GUI
# inicio da janela
root = tk.Tk()
# Configuração da janela
canvas = tk.Canvas(root, width=800, height=400)
canvas.grid(columnspan=5, rowspan=7)
root.title("INTERNET SPEED TEST")

# ComboBox TESTES(texto)
labelTop = tk.Label(root, text="Insira o intervalo entre os testes(min)!")
labelTop.grid(column=0, row=0)

# ComboBox TESTES(Escolhas)
comboExample = ttk.Combobox(
    root, state="readonly", values=["", 1, 5, 10, 15, 20, 30, 45, 60]
)
comboExample.grid(column=0, row=1)

# ComboBox QNTD(texto)
labelTop2 = tk.Label(root, text="Insira a quantidade de testes!")
labelTop2.grid(column=4, row=0)

# ComboBox QNTD(Escolhas)
comboExample2 = ttk.Combobox(
    root, state="readonly", values=["", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)
comboExample2.grid(column=4, row=1)

# LOGO....a imagem precisa estar na mesma pasta do codigo!
# logo.png tem quer ser o nome do arquivo da LOGO
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo

# posição da LOGO
logo_label.grid(columnspan=5, column=0, row=0)

# Titulo
titulo = tk.Label(root, text="Internet Speed Test", font="Raleway")
# posição do titulo
titulo.grid(columnspan=5, column=0, row=1)

# instruções
INTS2_text = tk.StringVar()
instructions2 = tk.Label(root, textvariable=INTS2_text, font="Raleway")
# Instruções iniciais
INTS2_text.set(
    "Os dados só estarão disponíveis após o término da execução do programa!"
)
# posição das instruçoes
instructions2.grid(columnspan=5, column=0, row=4)

# instruções3
INTS3_text = tk.StringVar()
instructions3 = tk.Label(root, textvariable=INTS3_text, font="Raleway")
# Instruções iniciais
INTS3_text.set(
    "A capacidade de processamento do computador influencia no tempo dos testes!"
)
# posição das instruçoes
instructions3.grid(columnspan=5, column=0, row=5)

# botão Start Test
btn_text = tk.StringVar()
start_btn = tk.Button(
    root,
    textvariable=btn_text,
    command=lambda: threading.Thread(target=main).start(),
    font="Raleway",
    fg="white",
    bg="#407E93",
    height=2,
    width=15,
)
# textoinicial
btn_text.set("Start Test")
# Posiçãodobotão
start_btn.grid(columnspan=5, column=0, row=2)

# botão para acessar diretório com os arquivos
btn_text2 = tk.StringVar()
start_btn2 = tk.Button(
    root,
    textvariable=btn_text2,
    command=lambda: acessarPasta(),
    font="Raleway",
    fg="white",
    bg="#407E93",
    height=2,
    width=15,
)
# textoinicial
btn_text2.set("Acessar pasta")
# Posiçãodobotão
start_btn2.grid(columnspan=5, column=0, row=3)

# status
STATUSFIXO = tk.Label(root, text="Status", font="Raleway")
# posição do statusfixo
STATUSFIXO.grid(columnspan=5, column=0, row=6)
# StatusVAR
STATUS_text = tk.StringVar()
STATUS = tk.Label(root, textvariable=STATUS_text, font="Raleway", fg="#407E93")
# posição do StatusVAR
STATUS.grid(columnspan=5, column=0, row=7)
# StatusInicial
STATUS_text.set("Pronto para começar!")
# FimdaJanela
root.mainloop()
# fim da janela
