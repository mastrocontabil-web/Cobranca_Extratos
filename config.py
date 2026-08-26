# ---------------------------------------------------------------------------
# CONFIGURAÇÃO — preencha os valores abaixo antes de rodar o script
# ---------------------------------------------------------------------------

# Modo de teste: True = só mostra no terminal o que seria enviado, sem enviar nada
# Depois de conferir, mude para False para enviar de verdade.
DRY_RUN = False

# Caminho da planilha de clientes (mesma estrutura da que você me enviou)
PLANILHA = "clientes.xlsx"

# --- Credenciais do Digisac ---
# Subdomínio: é o que aparece antes do domínio na URL quando você está
# logado no Digisac. Ex.: em https://mastrocontabil.digisac.biz/ o
# subdomínio é "mastrocontabil".
SUBDOMAIN = "mastrocontabil"

# Domínio: a parte depois do subdomínio na URL (varia por conta — pode ser
# digisac.chat, digisac.biz, etc.). No seu caso é digisac.biz.
DOMINIO = "digisac.biz"

# Token pessoal: Digisac > seu avatar > Conta > aba API > Personal access tokens
API_TOKEN = "e8a4cd8de84b76b50685392c5ea254d34f18a271"

# ID da conexão de WhatsApp: Digisac > Conexões > (três pontinhos na conexão) >
# Visualizar > o ID é o código no final da URL que abrir
CONNECTION_ID = "082948da-3fac-46c8-b425-ce31b12e8f2b"

# --- Mensagem ---
# {nome} é substituído automaticamente pelo primeiro nome do cliente
MENSAGEM_TEMPLATE = (
    "Olá *{nome}*, tudo bem?\n\n"
    "Passando para lembrar que ainda não recebemos o extrato bancário referente ao mês *{mes_competencia} em PDF, CSV e OFX.* "
    "Poderia nos enviar o extrato até dia 06, para não atrasarmos o fechamento contábil?\n\n"
    "Se você utiliza o sistema do *CONTROLEI* para classificação das despesas e receitas, não esqueça de preenchê-lo também.\n\n"
    "A partir de 01/09/2026, o envio dos arquivos deve ser feito sempre por e-mail (documentos@mastrocontabil.com) — não recebemos mais pelo WhatsApp.\n\n"
    "Qualquer dúvida, estamos à disposição!\n"
    "*— Mastro Contábil*"
)

# Intervalo entre envios (em segundos) para não sobrecarregar/tomar bloqueio do WhatsApp
INTERVALO_ENTRE_ENVIOS_SEGUNDOS = 5

# --- Automação contínua ---

# De quanto em quanto tempo (em SEGUNDOS) o programa verifica a planilha em
# busca de pendentes. Essa verificação acontece SEMPRE, esteja a planilha
# alterada ou não. Ex.: 300 = verifica a cada 5 minutos.
INTERVALO_VERIFICACAO_SEGUNDOS = 60

# Quantas HORAS esperar, contando a partir do último envio registrado no
# log, antes de poder cobrar o MESMO cliente de novo. Ex.: 1 = reenvia depois
# de 1 hora; 24 = reenvia depois de 1 dia. Pode usar números quebrados,
# como 0.5 (meia hora).
JANELA_REENVIO_HORAS = 0.08
