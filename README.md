# Price Monitor

##  Visão Geral

**Price Monitor** é uma solução automatizada de web scraping e monitoramento de preços que coleta, processa e estrutura dados de produtos de forma eficiente e confiável. O projeto foi desenvolvido com foco em robustez, rastreabilidade e facilidade de manutenção.

## O Que o Projeto Faz

O Price Monitor executa um pipeline completo e automatizado:

1. **Web Scraping**: Extrai dados de produtos (título, preço e URL) de websites de forma escalável, com tratamento de paginação automática
2. **Processamento de Dados**: Limpa, valida e transforma dados brutos em informações estruturadas e prontas para análise
3. **Armazenamento**: Persiste os dados em formato CSV para fácil integração com outras ferramentas e sistemas
4. **Logging Avançado**: Registra toda a execução com histórico rotativo de logs para auditoria e debugging


## Valor para do Projeto

### 1. **Inteligência Competitiva**
- Monitore preços de concorrentes em tempo real
- Identifique oportunidades de posicionamento de preço
- Acompanhe tendências de mercado automaticamente

### 2. **Otimização de Estratégia de Preços**
- Dados estruturados para análise comparativa
- Histórico de preços para identificar padrões sazonais
- Base para decisões de precificação dinâmica

### 3. **Redução de Custos Operacionais**
- Automação substitui coleta manual de dados
- Execução agendada reduz carga de trabalho manual
- Logs detalhados eliminam necessidade de investigação manual

### 4. **Confiabilidade e Rastreabilidade**
- **Logging robusto**: Todos os eventos são registrados com timestamp para auditoria completa
- **Validação de dados**: Garante consistência e integridade das informações coletadas
- **Tratamento de erros**: Falhas são capturadas e reportadas de forma estruturada
- **Deduplicação**: Remove dados duplicados automaticamente

### 5. **Escalabilidade e Flexibilidade**
- Facilmente configurável para diferentes fontes via variável de ambiente
- Estrutura modular permite expansão para múltiplas URLs
- Exportação em CSV permite integração com BI, DataLakes, e sistemas analíticos
- Facilmente integrado com ferramentas de automação IA como Zapier, Pluga, RD Station

### 6. **Conformidade e Governança**
- Logs com retenção de 7 dias para rastreamento de operações
- Estrutura limpa facilita auditorias internas
- Transparência completa sobre origem e processamento dos dados

## 🚀 Casos de Uso

- **E-commerce**: Monitorar preços de produtos em marketplaces
- **Varejo**: Acompanhar precificação de concorrentes
- **Pesquisa de Mercado**: Coletar dados públicos para análise de tendências
- **Inteligência de Negócios**: Alimentar dashboards e relatórios executivos

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8+
- pip

### Setup

```
# 1. Clone o repositório:
git clone https://github.com/andreasdecarvalho-prog/Price-Monitor.git
cd Price-Monitor


# 2. Instale as dependências:
pip install -r requirements.txt

# 3. Configure as variáveis de ambiente:
cp .env.example .env
# Edite .env e adicione:
# URL=https://seu-website.com
```

## 📋 Uso

Execute o pipeline:
```bash
python main.py
```

A execução:
- Faz scraping da URL configurada
- Processa e limpa os dados
- Salva em `data/books.csv`
- Registra logs em `logs/pipeline.log`

## 📂 Estrutura do Projeto

```
Price-Monitor/
├── main.py                 # Orquestrador do pipeline
├── src/
│   ├── scraper.py         # Web scraping com tratamento de paginação
│   ├── processor.py       # Limpeza e validação de dados
│   └── reporter.py        # Exportação para CSV
├── logs/
│   ├── logger.py          # Configuração de logging centralizada
│   └── pipeline.log       # Arquivo de logs (gerado)
├── data/
│   └── books.csv          # Saída de dados (gerado)
├── requirements.txt       # Dependências do projeto
└── README.md             # Esta documentação
```

## 📊 Saída de Dados

O CSV gerado contém as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| `title` | Título do produto |
| `price` | Preço em formato numérico (float) |
| `url` | URL do produto |

## 🔍 Recursos Avançados

### Logging Robusto
- **Rotação automática**: Logs são rotacionados diariamente à meia-noite
- **Retenção**: 7 dias de histórico mantidos
- **Duplo destino**: Console + arquivo para máxima visibilidade
- **Rastreamento**: Cada evento inclui timestamp, nível e contexto

### Tratamento de Erros
- Validação de entrada (URL obrigatória)
- Timeout em requisições HTTP
- Tratamento de exceções em cada etapa
- Mensagens de erro descritivas para debugging

### Deduplicação
- Remove produtos duplicados baseado no título
- Mantém primeira ocorrência para preservar consistência

## 👨‍💻 Autor

Desenvolvido por Andreas de Carvalho
