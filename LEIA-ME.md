# Cobrança de extrato bancário via Digisac

## O que você precisa antes de rodar

1. **Python 3** instalado no seu computador
2. Instalar as bibliotecas:
   ```
   pip install requests openpyxl --break-system-packages
   ```
   (no Windows, sem o `--break-system-packages`)

## Passo a passo

### 1. Preencha `config.py`
Abra o arquivo `config.py` e preencha:

- **SUBDOMAIN**: a parte antes de `.digisac.chat` quando você está logado no
  Digisac (ex.: se a URL é `https://mastro.digisac.chat/...`, o subdomínio é `mastro`)
- **API_TOKEN**: já preenchi com o token que você me passou
- **CONNECTION_ID**: vá em Digisac → **Conexões** → clique nos três pontinhos
  da conexão de WhatsApp que você usa → **Visualizar** → copie o código no
  final da URL que abrir
- **MENSAGEM_TEMPLATE**: ajuste o texto da cobrança como preferir (o
  `{nome}` é trocado automaticamente pelo primeiro nome do cliente)

### 2. Coloque a planilha
Salve sua planilha de clientes (mesmo formato que você me mandou: colunas
NOME, CPF, NUMERO DE TELEFONE, STATUS DE ENVIO DO EXTRATO) como `clientes.xlsx`
na mesma pasta do script — ou ajuste o caminho em `PLANILHA` no `config.py`.

### 3. Rode em modo teste primeiro
Com `DRY_RUN = True` (padrão), rode:
```
python3 cobranca_extrato.py
```
Isso só mostra no terminal quem receberia a mensagem e qual seria o texto —
nada é enviado de verdade. Confira se a lista e o texto estão certos.

### 4. Envie de verdade
Mude `DRY_RUN = False` no `config.py` e rode o script novamente. Ele vai:
- Buscar (ou criar) o contato de cada cliente pendente no Digisac
- Enviar a mensagem de cobrança pelo WhatsApp
- Salvar um log em `log_envios.csv` com o resultado de cada envio

## ⚠️ Importante — sobre a integração com o Digisac

Montei o script com base no padrão comum da API do Digisac (autenticação por
token, URL `https://SEU_SUBDOMINIO.digisac.chat/api/v1`, endpoints
`/contacts` e `/messages`). **Não tenho como testar contra a sua conta real**,
então é bem possível que algum nome de campo precise de ajuste fino na
primeira tentativa (por exemplo, `data` vs `number` para o telefone do contato).

Se der erro na primeira tentativa (modo `DRY_RUN = False` com 1 ou 2 clientes
apenas, antes do lote todo), me mande a mensagem de erro que aparecer no
terminal — normalmente dá para ver na resposta da API qual campo está errado,
e eu ajusto o script rapidinho.

Uma forma de confirmar os campos certos antes de rodar em produção: dentro do
próprio Digisac, em **Conta → API**, geralmente tem um link para a
documentação (Postman) específica da sua conta, com exemplos prontos de
requisição — vale dar uma conferida lá também.

## Segurança

- Não compartilhe o arquivo `config.py` com ninguém (ele tem seu token de API)
- Se algum dia esse token vazar, gere um novo em Digisac → Conta → API e
  revogue o antigo
