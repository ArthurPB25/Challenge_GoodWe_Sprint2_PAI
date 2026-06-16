"""
ChargeGrid Assistant — Chatbot Inteligente para Eletropostos GoodWe
EV Challenge 2026 — FIAP + GoodWe | Sprint 2

Chatbot conversacional baseado em Google Gemini com:
- System prompt injetado para definir comportamento e identidade
- Dados operacionais simulados do eletroposto (sessões, faturamento, status, demanda, energia solar)
- Histórico de conversa (memória de contexto) para diálogos contínuos
- Interface interativa via terminal

Uso:
    1. Configure a variável de ambiente GOOGLE_API_KEY com sua chave da API Gemini
    2. Instale as dependências: pip install -r requirements.txt
    3. Execute: python chatbot.py
"""

import os
import sys
from datetime import datetime, timedelta

# Forçar encoding UTF-8 no terminal Windows para suportar emojis
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from google import genai


# ──────────────────────────────────────────────
# 1. DADOS SIMULADOS DO ELETROPOSTO
# ──────────────────────────────────────────────

def gerar_dados_operacionais():
    """
    Gera um bloco de texto com dados operacionais simulados do eletroposto,
    representando informações que em produção viriam de um banco de dados real.
    Esses dados são injetados no contexto do LLM junto com o system prompt.
    """

    hoje = datetime.now()
    ontem = hoje - timedelta(days=1)

    dados = f"""
=== DADOS OPERACIONAIS DO ELETROPOSTO (Atualização: {hoje.strftime('%d/%m/%Y %H:%M')}) ===

--- INFORMAÇÕES GERAIS ---
Nome do Eletroposto: ChargeGrid Station — Shopping Paulista
Endereço: Av. Paulista, 1000 — São Paulo/SP
Quantidade de Pontos de Carga: 4 (Ponto 1, Ponto 2, Ponto 3, Ponto 4)
Modelo dos Carregadores: GoodWe HCA G2 (11 kW AC)
Tarifa Atual: R$ 1,30/kWh (padrão) | R$ 1,50/kWh (horário de pico: 17h-20h)

--- SESSÕES DE RECARGA — ONTEM ({ontem.strftime('%d/%m')}) ---
Total de sessões: 12
Energia total consumida: 180 kWh
Receita total: R$ 234,00
Ticket médio por sessão: R$ 19,50
Duração média por sessão: 1h15min
Sessões por ponto:
  - Ponto 1: 4 sessões (62 kWh)
  - Ponto 2: 3 sessões (48 kWh)
  - Ponto 3: 2 sessões (30 kWh) — offline a partir das 14:30
  - Ponto 4: 3 sessões (40 kWh)

--- FATURAMENTO SEMANAL (últimos 7 dias) ---
Segunda: R$ 198,00 (10 sessões, 152 kWh)
Terça:   R$ 221,00 (11 sessões, 170 kWh)
Quarta:  R$ 245,50 (13 sessões, 189 kWh)
Quinta:  R$ 210,00 (11 sessões, 162 kWh)
Sexta:   R$ 260,00 (14 sessões, 200 kWh)
Sábado:  R$ 312,00 (16 sessões, 240 kWh)
Domingo: R$ 234,00 (12 sessões, 180 kWh)
Total semanal: R$ 1.680,50 | 87 sessões | 1.293 kWh

--- FATURAMENTO MENSAL (mês atual, parcial) ---
Receita acumulada: R$ 5.420,00
Sessões acumuladas: 278
Energia acumulada: 4.169 kWh
Projeção para o mês completo: R$ 7.800,00

--- STATUS DOS EQUIPAMENTOS (tempo real) ---
Ponto 1: ✅ Online — Disponível
Ponto 2: ✅ Online — Em uso (sessão iniciada às {(hoje - timedelta(minutes=45)).strftime('%H:%M')}, veículo Tesla Model 3)
Ponto 3: ❌ Offline — Desde {ontem.strftime('%d/%m')} às 14:30. Erro: Falha na comunicação Modbus (código E-0x03). Última manutenção: {(hoje - timedelta(days=30)).strftime('%d/%m/%Y')}.
Ponto 4: ✅ Online — Disponível

--- DEMANDA POR HORÁRIO (média dos últimos 7 dias) ---
06h-09h: 1,2 sessões/hora (ocupação: 30%)
09h-12h: 2,0 sessões/hora (ocupação: 50%)
12h-14h: 2,5 sessões/hora (ocupação: 63%)
14h-17h: 2,8 sessões/hora (ocupação: 70%)
17h-20h: 3,2 sessões/hora (ocupação: 92%) ← HORÁRIO DE PICO
20h-22h: 1,8 sessões/hora (ocupação: 45%)
22h-06h: 0,3 sessões/hora (ocupação: 8%)

--- GERAÇÃO DE ENERGIA SOLAR (hoje, {hoje.strftime('%d/%m')}) ---
Inversores GoodWe instalados: 2x GW10K-ET (10 kW cada)
Capacidade instalada total: 20 kWp
Geração hoje até agora: 45 kWh
Geração estimada para o dia completo: 62 kWh
Demanda total de recarga hoje até agora: 150 kWh
Percentual coberto por energia solar: 30%
Economia estimada com energia solar hoje: R$ 38,25 (considerando tarifa da rede R$ 0,85/kWh)
Geração acumulada no mês: 820 kWh

--- ALERTAS ATIVOS ---
⚠️ Ponto 3 offline há mais de 24 horas — verificar conexão Modbus e alimentação de rede
⚠️ Ocupação no horário de pico atingiu 92% — considerar ajuste de tarifação dinâmica
"""
    return dados


# ──────────────────────────────────────────────
# 2. SYSTEM PROMPT
# ──────────────────────────────────────────────

def carregar_system_prompt():
    """
    Carrega o system prompt do arquivo system_prompt.md (definido na Sprint 1)
    e combina com os dados operacionais simulados para formar o contexto completo.
    """

    # Caminho do system_prompt.md (mesmo diretório deste script)
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_prompt = os.path.join(diretorio_atual, "system_prompt.md")

    try:
        with open(caminho_prompt, "r", encoding="utf-8") as f:
            system_prompt_base = f.read()
    except FileNotFoundError:
        print(f"⚠️  Arquivo '{caminho_prompt}' não encontrado. Usando system prompt padrão.")
        system_prompt_base = (
            "Você é o ChargeGrid Assistant, o assistente virtual do sistema ChargeGrid Hub. "
            "Auxilie operadores de eletropostos GoodWe com informações sobre sessões de recarga, "
            "faturamento, status dos equipamentos, demanda e energia solar."
        )

    # Combinar system prompt com dados operacionais
    dados_operacionais = gerar_dados_operacionais()

    prompt_completo = f"""{system_prompt_base}

--- DADOS OPERACIONAIS DISPONÍVEIS PARA CONSULTA ---
{dados_operacionais}

--- INSTRUÇÕES ADICIONAIS ---
- Ao responder sobre faturamento, sessões ou métricas, utilize EXCLUSIVAMENTE os dados fornecidos acima.
- Formate valores monetários em Reais (R$) e energia em kWh.
- Se o operador perguntar algo cujos dados não estão disponíveis, informe de forma transparente.
- Mantenha respostas concisas e orientadas a ação.
"""
    return prompt_completo


# ──────────────────────────────────────────────
# 3. CONFIGURAÇÃO DO CHATBOT (Google Gemini SDK)
# ──────────────────────────────────────────────

def configurar_chatbot():
    """
    Configura o chatbot usando o SDK Google GenAI com:
    - Gemini 2.0 Flash como modelo
    - System instruction com contexto operacional injetado
    - Chat com histórico de mensagens automático
    """

    # Validar API Key
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("=" * 60)
        print("❌ ERRO: Variável de ambiente GOOGLE_API_KEY não configurada.")
        print()
        print("Configure sua API key antes de executar:")
        print()
        print("  Windows (PowerShell):")
        print('    $env:GOOGLE_API_KEY = "sua-chave-aqui"')
        print()
        print("  Windows (CMD):")
        print('    set GOOGLE_API_KEY=sua-chave-aqui')
        print()
        print("  Linux/Mac:")
        print('    export GOOGLE_API_KEY="sua-chave-aqui"')
        print()
        print("  Google Colab:")
        print("    from google.colab import userdata")
        print('    import os')
        print('    os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")')
        print()
        print("Obtenha sua chave em: https://aistudio.google.com/apikey")
        print("=" * 60)
        sys.exit(1)

    # Inicializar o cliente Gemini
    client = genai.Client(api_key=api_key)

    # Carregar system prompt completo (com dados operacionais)
    system_prompt = carregar_system_prompt()

    # Criar o chat com system instruction e histórico automático
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=genai.types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3,  # Baixa temperatura para respostas mais precisas e consistentes
        ),
    )

    return client, chat


# ──────────────────────────────────────────────
# 4. INTERFACE DE INTERAÇÃO
# ──────────────────────────────────────────────

def exibir_banner():
    """Exibe o banner de boas-vindas do chatbot."""
    print()
    print("=" * 60)
    print("  ⚡ ChargeGrid Assistant — Sprint 2")
    print("  EV Challenge 2026 | FIAP + GoodWe")
    print("=" * 60)
    print()
    print("  Assistente inteligente para gestão do seu eletroposto.")
    print("  Pergunte sobre faturamento, sessões, status dos")
    print("  equipamentos, demanda e energia solar.")
    print()
    print("  Comandos especiais:")
    print("    'sair'   — Encerrar o chatbot")
    print("    'limpar' — Limpar histórico da conversa")
    print()
    print("-" * 60)
    print()


def main():
    """Loop principal do chatbot."""

    exibir_banner()

    # Configurar chatbot
    print("🔄 Inicializando ChargeGrid Assistant...")
    try:
        client, chat = configurar_chatbot()
    except Exception as e:
        print(f"\n❌ Erro ao inicializar o chatbot: {e}")
        sys.exit(1)

    print("✅ Chatbot pronto! Faça sua pergunta.\n")

    # Loop de conversa
    while True:
        try:
            pergunta = input("👤 Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Até logo! ChargeGrid Assistant encerrado.")
            break

        # Verificar comandos especiais
        if not pergunta:
            continue

        if pergunta.lower() in ("sair", "exit", "quit"):
            print("\n👋 Até logo! ChargeGrid Assistant encerrado.")
            break

        if pergunta.lower() in ("limpar", "clear", "reset"):
            # Recriar o chat para limpar o histórico
            client, chat = configurar_chatbot()
            print("🗑️  Histórico de conversa limpo.\n")
            continue

        # Enviar pergunta ao chatbot (o histórico é gerenciado automaticamente pelo SDK)
        try:
            resposta = chat.send_message(pergunta)
            texto_resposta = resposta.text
            print(f"\n🤖 ChargeGrid: {texto_resposta}\n")
        except Exception as e:
            print(f"\n⚠️  Erro ao processar a pergunta: {e}")
            print("   Tente novamente ou verifique sua conexão.\n")


if __name__ == "__main__":
    main()
