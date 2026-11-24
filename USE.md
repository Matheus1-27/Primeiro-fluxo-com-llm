# Como usar o projeto

Este projeto oferece uma interface de terminal para resumir textos usando o modelo Google Gemini `gemini-3.5-flash-lite`. Antes de executar, conclua a configuração descrita no [README.md](README.md): crie o arquivo `.env` com a chave de API e instale globalmente as dependências.

## Iniciar o programa

Execute os comandos a partir da pasta raiz do projeto, após instalar globalmente as dependências.

No Windows, pelo PowerShell:

```powershell
.\run.bat
```

No macOS ou Linux:

```bash
sh ./run.sh
```

Os scripts de execução iniciam `src/main.py`; eles não instalam dependências. Também é possível executar o programa diretamente.

No Windows:

```powershell
py -3 .\src\main.py
```

No macOS ou Linux:

```bash
python3 src/main.py
```

## Interagir com o agente

1. Quando o programa solicitar uma mensagem, cole ou digite o texto que deseja resumir e pressione Enter.
2. O agente foi configurado para resumir textos em tópicos, destacando as informações importantes.
3. Digite `sair` e pressione Enter para encerrar.

Mensagens vazias ou compostas apenas por números são recusadas. O uso do agente requer conexão com a internet e uma chave de API válida no `.env`.

## Solução de problemas

- **Chave vazia ou inválida:** confira se `.env` está na raiz do projeto e se `GOOGLE_API_KEY` contém a chave correta, entre aspas ou sem elas.
- **Dependências ausentes:** execute novamente o instalador do seu sistema, conforme o [README.md](README.md).
- **Python não encontrado:** confirme que o Python 3.12 ou superior está instalado e disponível no terminal.
- **Instalação global bloqueada:** algumas instalações Linux/macOS protegem os pacotes do Python do sistema. Use uma instalação do Python 3.12 ou superior que permita instalar pacotes globalmente; não ignore a proteção do sistema operacional.