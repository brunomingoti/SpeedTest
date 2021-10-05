#                                          Teste de Velocidade da Internet :signal_strength:



> Status do Projeto: :heavy_check_mark: (pronto)

### Tópicos :writing_hand:


- [Descrição do projeto](#descrição-do-projeto-file_folder)

- [Deploy da Aplicação](#deploy-da-aplicação-dash)

- [Pré-requisitos](#pré-requisitos-pushpin)

- [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)
- [Observações](#observações-eyes)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas-books) 
- [Possíveis aplicações](#possíveis-aplicações)
- [Possíveis melhorias](#possíveis-melhorias-rocket)
- [Desenvolvedores e Contribuintes](#desenvolvedores-e-contribuintes-computer)
- [Licença](#licença-grey_exclamation)



## Descrição do projeto :file_folder:

<p align="justify">
Código desenvolvido com a finalidade de verificar a conexão com a internet e realizar uma quantidade de testes de velocidade espaçados por um intervalo. Os valores de "quantidade" e "intervalo" são pré-determinados pelo usuário antes da execução do teste.
  
Os dados da velocidade de download, upload e ping que foram gerados durante os testes serão armazenados em um arquivo de texto e, em seguida, plotados em gráficos, que poderão ser acessados na mesma pasta em que o código está salvo. Por fim, como forma de facilitar a visualização, todos os gráficos são salvos em um arquivo único em PDF.
  
Além disso, foi elaborada uma interface gráfica para o programa, de modo a ficar o mais amigável possível para o usuário.
</p>



## Pré-requisitos :pushpin:

No Python:

```
pip install urllib3
```

```
pip install speedtest-cli
```

```
pip install pandas
```

```
pip install fpdf
```

```
pip install Pillow
```

```
pip install matplotlib
```

```
pip install plotly
```

```
pip install pycaw
```


O arquivo "logo.png" deve estar na mesma pasta do código.


## Como rodar a aplicação :arrow_forward:

- Coloque o arquivo "logo.png" na mesma pasta do código;
- Instale todos os pacotes necessários;
- Execute a aplicação normalmente;
- Selecione os valores de "quantidade" e "intervalo" e clique em "Start Test".



## Observações :eyes:

Arquivos gerados:
- "dados.txt" - arquivo com informações apresentadas de maneira mais organizada separada por teste;
- "resumo.txt" - arquivo que será utilizado na plotagem dos gráficos;
- "grafico_down.png" - gráfico 1 - download - velocidade de download pelo tempo;
- "grafico_upl.png" - gráfico 2 - upload - velocidade de upload pelo tempo;
- "grafico_ping.png" - gráfico 3 - ping - ping pelo tempo;
- "report.pdf" - documento com relatório das informações obtidas a partir dos programa. 



## Bibliotecas utilizadas :books:


- [Warnings](https://docs.python.org/pt-br/3.11/library/warnings.html)
- [PyFPDF](https://pypi.org/project/fpdf/)
- [pandas](https://pypi.org/project/pandas/)
- [urllib3](https://urllib3.readthedocs.io/en/latest/user-guide.html)
- [time](https://docs.python.org/3/library/time.html)
- [speedtest](https://github.com/sivel/speedtest-cli)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pypi.org/project/Pillow/)
- [os](https://docs.python.org/3/library/os.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [threading](https://docs.python.org/3/library/threading.html)
- [matplotlib](https://pypi.org/project/matplotlib/)



## Possíveis aplicações :dart:

- Encontrar os melhores horários em que a conexão é estável;
- Auxíliar na verificação de pontos que se faz necessário o uso de repetidores;
- Verificar se o plano contratado está condizente com a velocidade prometida pela operadora;



## Possíveis melhorias :rocket:

:memo: Resolver erro ao encerrar o programa

:memo: Biblioteca urllib3 apresentou problemas ao ser executada em sistemas Mac e Linux.



## Desenvolvedores e Contribuintes :computer:


- Bruno Mingoti - [LinkedIn]( https://www.linkedin.com/in/brunomingoti/) - [Email](brunomingoti@gmail.com)
- Luigi Remor - [LinkedIn](https://www.linkedin.com/in/luigiremor/) - [Email](luigiremor@gmail.com)
- Matheus Hrihorowitsch - [LinkedIn](https://www.linkedin.com/in/matheushrihorowitsch/) - [Email](mhrihorowitsch@gmail.com)



## Licença :grey_exclamation:

MIT License

Copyright :copyright: 2021 - Teste de Velocidade da Internet
