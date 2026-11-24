# Primeiro fluxo com LLM

Projeto de terminal que usa LangChain e o modelo Google Gemini `gemini-3.5-flash-lite` para resumir textos. As dependências e suas versões estão listadas em `requirements.txt`.

## Requisitos

- Python 3.12 ou superior.
- Uma chave de API do Google AI Studio.
- Acesso à internet para instalar dependências e consultar o modelo.

## Configuração

Siga os passos na raiz do projeto.

### 1. Obtenha uma chave de API

1. Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey) e entre na sua conta Google.
2. Crie uma chave de API e copie o valor. A disponibilidade do modelo e as condições de uso dependem da sua conta e das regras atuais do Google.
3. Crie o arquivo `.env` a partir do exemplo.

No Windows, pelo PowerShell:

```powershell
Copy-Item .env_example .env
```

No macOS ou Linux:

```bash
cp .env_example .env
```

Abra `.env`, substitua `SUA CHAVE DA API` pela chave criada e salve:

```dotenv
GOOGLE_API_KEY="sua-chave-de-api"
```

Não publique nem compartilhe sua chave. O arquivo `.env` está listado no `.gitignore`.

### 2. Instale as dependências globalmente

Os instaladores usam o Python 3 instalado no computador e instalam nele os pacotes e versões definidos em `requirements.txt`.

No Windows, abra o PowerShell na pasta do projeto e execute:

```powershell
.\install.bat
```

No macOS ou Linux, abra o terminal na pasta do projeto e execute:

```bash
sh ./install.sh
```

Se preferir, também pode instalar os pacotes diretamente:

No Windows:
```powershell
py -3 -m pip install -r requirements.txt
```

No macOS ou Linux:

```bash
python3 -m pip install -r requirements.txt
```

Uma instalação global pode afetar outros projetos que usam o mesmo Python. Algumas distribuições Linux e instalações do Python gerenciadas pelo sistema operacional bloqueiam instalações globais pelo `pip`; não force a instalação ignorando essa proteção. Nesses casos, use uma instalação do Python 3.12 ou superior que permita instalar pacotes globalmente.

## Próximos passos

Depois de configurar o ambiente e instalar as dependências, consulte [USE.md](USE.md) para saber como executar e usar o projeto.

## Arquivos principais

```text
.env_example   # Exemplo de configuração da chave da API
install.bat    # Instala as dependências no Windows
install.sh     # Instala as dependências no macOS e Linux
requirements.txt
run.bat        # Executa o projeto no Windows
run.sh         # Executa o projeto no macOS e Linux
src/
USE.md         # Instruções de execução e uso
```
