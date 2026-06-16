# ⚡ ChargeGrid Hub — Smart Demand Hub

> **FIAP EV Challenge 2026 — Solução Completa para o Challenge GoodWe**

O **ChargeGrid Hub** é uma plataforma inteligente projetada para a gestão de eletropostos **comerciais** da GoodWe. Ele integra controle de demanda, tarifação dinâmica, inteligência artificial preditiva e um chatbot operacional. A solução tem como objetivo transformar o carregador residencial HCA G2 da GoodWe em um ecossistema comercial completo, adicionando camadas de pagamento, comunicação e inteligência, sem a necessidade de alterar o hardware existente.

---

## 🎯 O Problema

O carregador HCA G2 da GoodWe é um excelente produto residencial, no entanto, para aplicações comerciais, ele enfrenta algumas limitações:

- ❌ **Sem mecanismo de cobrança:** Não há gateways de pagamento integrados.
- ❌ **Sem OCPP:** Dificulta a integração com plataformas de gestão e billing.
- ❌ **Gestão isolada:** Falta de monitoramento integrado para gerenciamento inteligente de demanda e precificação dinâmica.

---

## 💡 A Solução: ChargeGrid Hub

A solução propõe um ecossistema completo dividido em 3 camadas principais:

1. **Camada 1: O Tótem Físico (ChargeGrid Terminal)**
   - Funciona como um gateway de pagamento físico e *middleware*.
   - Conecta-se ao HCA G2 via **Modbus RS-485**.
   - Habilita autenticação e pagamentos via **RFID, NFC (Cartão) e Pix (QR Code dinâmico)**.
   - Lê dados de energia em tempo real (kWh consumido, potência).

2. **Camada 2: Plataforma Cloud (ChargeGrid Dashboard)**
   - Um sistema de inteligência em nuvem para o operador do eletroposto.
   - Fornece status em tempo real, faturamento, controle de tarifas, gestão de usuários e alertas.
   - Inclui aplicativo para os motoristas localizarem os eletropostos, reservarem horários e acompanharem sessões.

3. **Camada 3: IA Aplicada (ChargeGrid Brain)**
   - **Tarifação Dinâmica:** Ajuste de preços baseados em demanda, horário de pico e disponibilidade de energia solar.
   - **Previsão de Demanda:** IA preditiva para antecipar picos de consumo e otimizar o uso da infraestrutura.
   - **Chatbot Operacional:** Assistente com NLP para tirar dúvidas de motoristas e fornecer relatórios instantâneos aos operadores.

---

## 🤖 ChargeGrid Assistant — Sprint 2

O **ChargeGrid Assistant** é o chatbot operacional implementado na Sprint 2, utilizando a API Anthropic (Claude) com:

- ✅ **System prompt** com contexto completo da solução ChargeGrid Hub
- ✅ **Histórico de mensagens** para diálogos contínuos e coerentes
- ✅ **Few-shot prompting** para calibração de qualidade das respostas
- ✅ **Dois perfis de atendimento**: motoristas (linguagem acessível) e operadores (linguagem técnica)
- ✅ **Tarifação dinâmica** integrada ao contexto (horários de pico, valle e bônus solar)

### Pré-requisitos

- Python 3.9 ou superior
- Conta na [Anthropic Console](https://console.anthropic.com/) com uma API Key ativa
- Git (para clonar o repositório)

### Dependências

```
anthropic>=0.40.0
```

### Variáveis de Ambiente

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `ANTHROPIC_API_KEY` | Chave de API da Anthropic | ✅ Sim |

> ⚠️ **NUNCA** exponha sua API Key no código ou faça commit dela no repositório. Use sempre variáveis de ambiente.

---

## 🚀 Como Executar

### Opção 1 — Google Colab (recomendado)

1. Acesse o notebook: [`pai/ChargeGrid_Assistant_Sprint2.ipynb`](pai/ChargeGrid_Assistant_Sprint2.ipynb)
2. No menu lateral do Colab, clique no ícone 🔑 **Secrets**
3. Adicione um novo secret:
   - **Nome:** `ANTHROPIC_API_KEY`
   - **Valor:** sua chave da Anthropic (começa com `sk-ant-...`)
4. Execute as células em ordem (Shift+Enter ou "Executar tudo")
5. Na célula do **Chat Interativo**, digite suas mensagens e pressione Enter

### Opção 2 — Execução Local (terminal/IDE)

```bash
# 1. Clone o repositório
git clone https://github.com/lucasdorice/challenge-goodwe.git
cd challenge-goodwe

# 2. Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/macOS
# ou
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install anthropic

# 4. Configure a variável de ambiente com sua API Key
export ANTHROPIC_API_KEY="sk-ant-sua-chave-aqui"   # Linux/macOS
# ou
set ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui         # Windows CMD

# 5. Execute o chatbot
python pai/chatbot.py
```

### Comandos especiais no chat

| Comando | Ação |
|---------|------|
| `/limpar` | Reinicia o histórico de conversa |
| `/exportar` | Salva o histórico em `historico_conversa.json` |
| `/sair` | Encerra o chatbot |

---

## 💬 Exemplos de Uso

```
Você: Como faço para iniciar uma sessão de recarga?
ChargeGrid Assistant: Para iniciar sua recarga no ChargeGrid Terminal:
(1) Aproxime seu cartão RFID ou celular via NFC ao leitor, OU escaneie
o QR Code para pagar via Pix. (2) Conecte o cabo ao seu veículo.
(3) A sessão inicia automaticamente após confirmação do pagamento...

Você: Qual tarifa está disponível agora?
ChargeGrid Assistant: A tarifa atual depende do horário de uso. O sistema
ChargeGrid Hub adota tarifação dinâmica: Horário de Pico (18h-21h): +40%
sobre a tarifa base; Horário Normal: tarifa base; Horário Valle (23h-06h):
-25% sobre a tarifa base...

Você: Sou operador, o consumo está 35% acima do normal. O que faço?
ChargeGrid Assistant: Um consumo 35% acima do padrão é classificado como
anomalia moderada-alta. Verifique no Dashboard quais carregadores estão
com leitura fora do padrão...
```

---

## 📁 Estrutura do Repositório

```
challenge-goodwe/
├── README.md
├── pai/                               # Projeto de IA (Sprint 1 e 2)
│   ├── chatbot.py                     # ← SPRINT 2: Chatbot Python (execução local)
│   ├── ChargeGrid_Assistant_Sprint2.ipynb  # ← SPRINT 2: Notebook Google Colab
│   ├── resultados_testes.md           # ← SPRINT 2: Resultados dos 5 casos de teste
│   ├── fluxograma.png                 # Sprint 1: Fluxo do ChargeGrid Assistant
│   ├── system_prompt.md               # Sprint 1: Prompt base do assistente
│   └── modelo_teste.md                # Sprint 1: Base de perguntas e respostas
│
├── pcp/                               # Pensamento Computacional
├── dsa/                               # Estruturas de Dados e Algoritmos
├── cs/                                # Computer Science (Circuitos Lógicos)
├── coa/                               # Organização e Arquitetura de Computadores
├── mlpam/                             # Modelagem Linear
├── mmc/                               # Modelagem Matemática
└── sers/                              # Sustentabilidade e Energia Renovável
```

---

## 📊 Resultados dos Testes (Sprint 2)

5 casos de teste executados com base no modelo da Sprint 1:

| ID | Perfil | Pergunta (resumo) | Avaliação |
|----|--------|-------------------|-----------|
| CT-01 | Motorista | Como iniciar sessão de recarga | ✅ Adequada |
| CT-02 | Motorista | Tarifa no horário de pico | ✅ Adequada |
| CT-03 | Operador | Integração ChargeGrid com HCA G2 | ✅ Adequada |
| CT-04 | Operador | Anomalia de consumo 35% acima do normal | ✅ Adequada |
| CT-05 | Motorista | Estimativa de recarga BYD Dolphin 44.9 kWh | ✅ Adequada |

**Taxa de acerto: 5/5 (100%)** — Ver detalhes em [`pai/resultados_testes.md`](pai/resultados_testes.md)

---

## 💰 Modelos de Negócio e Sustentabilidade

A implementação do **ChargeGrid Hub** desbloqueia novas linhas de receita para a GoodWe e operadores: venda do tótem, planos SaaS da plataforma, taxas de transação e publicidade nos displays ociosos.

A solução promove **sustentabilidade** incentivando o carregamento em horários fora de pico e oferecendo descontos atrelados ao uso de **Inversores Solares GoodWe**.

---

## 👥 Equipe

| Nome | RM |
|------|----|
| Arthur Primo Brandão | 573572 |
| Felipe Gouveia Braga | 568956 |
| Isaías Hörlle Sobral | 568990 |
| Leandro Cavaccini Brito | 570556 |
| Lucas Dorice Dos Santos | 568692 |
| Vinicius de Oliveira Coppola | 571699 |

**Data de Entrega Sprint 1:** 22/05/2026  
**Data de Entrega Sprint 2:** [a definir]
