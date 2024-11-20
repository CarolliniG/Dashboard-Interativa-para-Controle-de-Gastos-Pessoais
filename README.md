# Dashboard Interativa para Controle de Gastos Pessoais

**Descrição:**

Este projeto cria um dashboard interativo utilizando o Streamlit para visualizar dados de gastos pessoais a partir de um arquivo CSV. O usuário pode filtrar os dados por categoria e por data, permitindo uma análise mais detalhada dos seus gastos.

**Tecnologias Utilizadas:**

Streamlit: Biblioteca de Python que permite criar aplicativos web.
Pandas: Para manipulação e análise de dados.
Plotly: Para criar gráficos interativos e visualizações de dados.

**Objetivo**
Este projeto foi desenvolvido com o objetivo de estudar e praticar a utilização de Python no desenvolvimento de aplicações interativas e para aprender a utilizar bibliotécas Python para desenvolvimento web.

## Funcionalidades
* **Carregamento de dados:** Carrega dados de um arquivo CSV com a coluna `data` formatada como data.
* **Filtro por categoria:** Permite ao usuário selecionar uma categoria específica para análise.
* **Gráfico de barras:** Visualiza os gastos por categoria em um gráfico de barras.
* **Filtro de data:** Permite ao usuário selecionar um intervalo de datas para análise.
* **Gráfico de linha:** Mostra a evolução dos gastos ao longo do tempo.

## Pré-requisitos

Certifique-se de que você tem os seguintes itens configurados antes de começar:

### Python
Instale a versão mais recente do Python. Você pode baixá-lo [aqui](https://www.python.org/).

### Ambiente virtual
Recomenda-se criar um ambiente virtual para isolar as dependências do projeto. 

### Bibliotecas necessárias
Instale as bibliotecas utilizando o comando abaixo:

```bash

pip install streamlit pandas plotly

Como usar
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/dashboard-gastos-pessoais.git
cd dashboard-gastos-pessoais
Ative o ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute o dashboard:

bash
Copiar código
streamlit run app.py
Acesse o dashboard no seu navegador em http://localhost:8501.
```

###Estrutura do Projeto

plaintext
Copiar código
dashboard-gastos-pessoais/
│
├── app.py                 # Arquivo principal da aplicação
├── data/
│   └── gastos.csv         # Arquivo CSV com os dados de exemplo
├── requirements.txt       # Arquivo com as dependências do projeto
└── README.md              # Documentação do projeto

###Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar um pull request.


**Autor:**
Carollini Gimenes
