# Price Monitor — Pipeline Automatizado de Coleta de Dados da Web

## Visão Geral

Este projeto é um pipeline de automação em Python para coletar, limpar e gerar dados estruturados a partir de sites.

O projeto demonstra como:

- extrair (scrape) dados de sites com paginação
- processar e normalizar dados brutos usando pandas
- exportar conjuntos de dados limpos para CSV
- executar todo o pipeline automaticamente com um único comando

A estrutura do projeto reflete tarefas reais de automação e coleta de dados para trabalhos freelance.

---

## Funcionalidades

- Web scraping com `requests` e `BeautifulSoup`
- Tratamento de paginação
- Limpeza e transformação de dados com `pandas`
- Remoção de duplicados e normalização de tipos
- Geração de relatórios em CSV
- Estrutura modular no estilo de produção
- Configuração orientada por arquivo (sem URLs hardcoded)

---

## Estrutura do Projeto

```
price_monitor/
│
├── app/
│   ├── core/
│   │   └── config.py          # Configuração centralizada
│   │
│   └── services/
│       ├── scraper.py         # Lógica de coleta de dados
│       ├── processor.py       # Limpeza e normalização dos dados
│       ├── reporter.py        # Geração de CSV
│       └── delivery.py        # Utilitários de entrega de dados
│
├── scripts/
│   └── run_pipeline.py        # Ponto de entrada do pipeline
│
├── data/
│   ├── books.csv              # Dados parseados
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## Como Funciona

1. Scraper

   - Busca dados em um site paginado
   - Extrai campos estruturados (ex.: título, preço, URL)
   - Retorna dados brutos como dicionários Python

2. Processor

   - Converte os dados brutos em um DataFrame do pandas
   - Limpa e normaliza valores
   - Remove duplicados
   - Garante tipos de dados corretos

3. Reporter

   - Exporta o conjunto processado para CSV
   - Armazena relatórios em diretórios organizados

4. Pipeline

   - Orquestra todas as etapas, da coleta até a entrega
   - Projetado para rodar de forma não assistida

---

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/andreasdecarvalho-prog/Price-Monitor.git
cd Price-Monitor
pip install -r requirements.txt
```

---

## Configuração

Todos os valores configuráveis ficam centralizados.

Crie um arquivo `.env` com base no exemplo:

```bash
cp .env.example .env
```

Edite os valores em `app/core/config.py` ou no arquivo `.env` conforme necessário.

---

## Executando o Pipeline

Execute todo o pipeline com:

```bash
python scripts/run_pipeline.py
```

Após a execução:

- Os dados limpos serão salvos em CSV em `data/books.csv`
- Logs e mensagens indicarão o progresso do processamento

---

## Casos de Uso

Este projeto espelha tarefas comuns de freelance, como:

- monitoramento de preços
- extração de catálogo de produtos
- coleta de dados para pesquisa de mercado
- substituição de fluxos manuais em Excel
- entrega de dados agendada ou recorrente

---

## Observações

- O site alvo usado no desenvolvimento é um site público de demonstração para prática de scraping.
- A arquitetura é propositalmente simples e extensível.
- O projeto pode ser adaptado para outros sites, esquemas ou formatos de entrega.

---

## Autor

Desenvolvido por Andreas de Carvalho  
Python Automation • Web Scraping • Data Processing
