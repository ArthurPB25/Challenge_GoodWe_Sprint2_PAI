# ⚡ ChargeGrid Assistant — Chatbot Inteligente para Eletropostos GoodWe

<p align="center">
  <strong>EV Challenge 2026 — FIAP + GoodWe</strong><br>
  Sprint 2 · Implementação e Entrega do Chatbot
</p>

---

## 📋 Sumário

- [Integrantes](#integrantes)
- [Sobre o Projeto](#sobre-o-projeto)
- [Problema Abordado](#problema-abordado)
- [Proposta do Chatbot](#proposta-do-chatbot)
- [Persona Atendida](#persona-atendida)
- [Tecnologias Selecionadas](#tecnologias-selecionadas)
- [Arquitetura e Fluxo de Funcionamento](#arquitetura-e-fluxo-de-funcionamento)
- [System Prompt](#system-prompt)
- [Como Executar](#como-executar)
- [Dependências](#dependências)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Exemplos de Uso](#exemplos-de-uso)
- [Modelo de Teste](#modelo-de-teste)
- [Resultados dos Testes](#resultados-dos-testes)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Roadmap — Próximas Sprints](#roadmap--próximas-sprints)

---

## 👥 Integrantes

Arthur Primo Brandão - RM: 573572
Felipe Gouveia Braga - RM: 568956
Isaías Hörlle Sobral - RM: 568990
Leandro Cavaccini Brito - RM: 570556
Lucas Dorice Dos Santos - RM: 568692
Vinicius de Oliveira Coppola - RM: 571699

> **Turma:** 1CCPY

---

## 📖 Sobre o Projeto

O **ChargeGrid Assistant** é o módulo de Inteligência Artificial da solução **ChargeGrid Hub**, desenvolvida para o EV Challenge 2026 em parceria entre FIAP e GoodWe. Trata-se de um chatbot conversacional projetado para atuar como **assistente operacional** em eletropostos comerciais equipados com carregadores GoodWe da linha HCA G2.

O projeto faz parte da iniciativa **ChargeGrid Intelligence**, cujo objetivo é transformar cada sessão de recarga em dados estruturados e inteligência acionável — migrando de um modelo de hardware isolado para um **hub de inteligência** completo.

---

## 🔍 Problema Abordado

Hoje, operadores e gerentes de eletropostos comerciais enfrentam uma série de dificuldades para gerir suas operações de recarga:

### Ausência de Visibilidade Operacional

O carregador GoodWe HCA G2 não possui um painel de gestão integrado voltado ao operador comercial. As informações sobre sessões de recarga, consumo energético e status dos equipamentos ficam dispersas entre a plataforma SEMS+ (monitoramento) e o aplicativo SolarGo (comissionamento), sem consolidação em uma interface unificada e de fácil consulta.

### Falta de Inteligência sobre os Dados

Mesmo quando os dados estão disponíveis, eles são apresentados de forma técnica e bruta — registros de tensão, corrente, potência e timestamps que não se traduzem facilmente em decisões de negócio. O operador que precisa saber "quanto faturei ontem" ou "qual horário devo aumentar o preço" é obrigado a exportar dados, montar planilhas e calcular manualmente.

### Modelo de Cobrança Inexistente

Conforme apresentado na Mentoria 1, a GoodWe **não possui um modelo padrão de cobrança** para a linha HCA G2 — não há gateway de pagamento, formato de autenticação padronizado ou divisão de receita definida. Isso torna a operação comercial inviável sem uma camada adicional de software e inteligência.

### Dificuldade de Resposta Rápida

Quando um carregador apresenta falha ou a rede elétrica está próxima da sobrecarga, o operador não recebe alertas contextualizados nem recomendações de ação. A identificação de problemas depende de inspeção manual ou do monitoramento constante da plataforma SEMS+.

---

## 💡 Proposta do Chatbot

O **ChargeGrid Assistant** é um chatbot conversacional baseado em LLM (Large Language Model) que atua como **ponte entre os dados técnicos do eletroposto e a linguagem de negócios do operador**.

O chatbot recebe perguntas em linguagem natural e responde com base em dados contextuais das sessões de recarga, status dos equipamentos, tarifas vigentes e métricas históricas de demanda. Ele funciona como um **analista virtual 24/7** que traduz dados complexos em insights acionáveis.

### Capacidades Planejadas

| Categoria | Exemplos de Consultas |
|-----------|----------------------|
| **Faturamento** | Receita diária/semanal/mensal, ticket médio por sessão, comparativo entre períodos |
| **Demanda** | Horários de pico, taxa de ocupação dos pontos, previsão de demanda |
| **Status Técnico** | Carregadores online/offline, alertas de manutenção, status da conexão Modbus |
| **Tarifação** | Tarifa vigente por faixa horária, recomendação de ajuste de preços baseada em dados |
| **Energia** | Geração solar dos painéis GoodWe, percentual de demanda coberto por energia renovável |
| **Relatórios** | Resumos consolidados sob demanda, exportação de métricas |

### O que o Chatbot NÃO Faz

- ❌ Não inventa ou fabrica dados — responde apenas com base em informações disponíveis
- ❌ Não fornece aconselhamento jurídico, médico ou financeiro formal
- ❌ Não executa ações diretas nos carregadores (apenas consulta e recomenda)
- ❌ Não responde sobre temas fora do escopo operacional do eletroposto

---

## 🎯 Persona Atendida

**Persona principal:** Operador / Gerente Comercial do Eletroposto

### Justificativa da Escolha

Entre as possíveis personas (usuário final do EV, técnico de manutenção, gestor corporativo), o **operador/gerente comercial** foi selecionado por ser quem:

1. **Mais precisa de informação rápida** — ele toma decisões diárias sobre tarifas, horários de funcionamento e alocação de recursos sem ter ferramentas adequadas hoje
2. **Interage com múltiplos sistemas** — precisa consultar SEMS+, SolarGo e planilhas separadamente para obter uma visão completa da operação
3. **É o elo entre o técnico e o negócio** — precisa traduzir dados de potência (kW), corrente (A) e consumo (kWh) em receita (R$) e decisões comerciais
4. **Enfrenta a dor principal do Challenge** — a ausência de modelo de cobrança impacta diretamente seu trabalho, e o chatbot pode compensar a falta de um painel de billing integrado

### Perfil da Persona

| Atributo | Descrição |
|----------|-----------| 
| **Nome fictício** | Carlos, Gerente de Operações |
| **Contexto** | Administra um eletroposto comercial com 4 pontos de carga GoodWe HCA G2 em um shopping center |
| **Nível técnico** | Intermediário — entende conceitos básicos de energia, mas não é engenheiro eletricista |
| **Necessidade** | Visão consolidada da operação em linguagem acessível, sem precisar navegar em múltiplas plataformas |
| **Dispositivo** | Acessa via computador no escritório ou celular em trânsito |

---

## 🛠️ Tecnologias Selecionadas

### LLM: Google Gemini API

| Critério | Justificativa |
|----------|---------------|
| **Custo** | Possui tier gratuito generoso (Gemini 1.5 Flash) que permite desenvolvimento e testes sem investimento inicial |
| **Qualidade** | Modelo multimodal com forte capacidade de compreensão de contexto em português |
| **Integração** | SDK oficial para Python (`google-generativeai`), bem documentado e com suporte ativo |
| **Contexto** | Suporta janelas de contexto extensas, permitindo injetar dados operacionais completos sem truncamento |
| **Ecossistema** | Alinhado com o ecossistema Google Cloud, facilitando eventual escalabilidade em produção |

### Framework: LangChain

| Critério | Justificativa |
|----------|---------------|
| **Injeção de contexto** | Permite estruturar facilmente system prompts + dados dinâmicos via `ChatPromptTemplate` e chains |
| **Modularidade** | Arquitetura de chains e agents permite adicionar funcionalidades (consulta a banco de dados, histórico de conversa) de forma incremental |
| **Comunidade** | Maior ecossistema open-source para aplicações LLM, com documentação extensa e exemplos práticos |
| **Flexibilidade de LLM** | Se necessário, permite trocar o modelo (de Gemini para OpenAI, por exemplo) alterando apenas o provedor, sem refatorar a lógica |

### Linguagem: Python

Escolhida por ser o padrão de mercado para aplicações de IA/ML, ter suporte nativo ao Gemini SDK e LangChain, e ser a linguagem utilizada nas disciplinas do curso.

---

## 🏗️ Arquitetura e Fluxo de Funcionamento

O fluxograma completo do chatbot está disponível em: **[fluxograma.png](./fluxograma.png)**

### Fluxo Simplificado

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Operador   │────▶│  Interface Web   │────▶│   LangChain     │
│  (Pergunta)  │     │  (Input texto)   │     │   (Orquestrador)│
└──────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                                              ┌────────▼────────┐
                                              │  System Prompt  │
                                              │  + Contexto de  │◀──── Base de Dados
                                              │     Dados       │      (Sessões, Status,
                                              └────────┬────────┘       Tarifas, Energia)
                                                       │
                                              ┌────────▼────────┐
                                              │   Gemini API    │
                                              │  (Processamento │
                                              │    do LLM)      │
                                              └────────┬────────┘
                                                       │
                                              ┌────────▼────────┐
                                              │    Resposta     │
                                              │ contextualizada │
                                              │  ao operador    │
                                              └────────────────┘
```

### Etapas do Processamento

1. **Entrada** — O operador digita uma pergunta em linguagem natural
2. **Orquestração** — O LangChain recebe a pergunta e monta o prompt completo
3. **Injeção de Contexto** — O system prompt (comportamento) e os dados operacionais (sessões, status, tarifas) são combinados com a pergunta
4. **Memória de Conversa** — O histórico de mensagens anteriores é incluído no prompt para manter a coerência do diálogo
5. **Processamento** — O Gemini API recebe o prompt completo e gera uma resposta contextualizada
6. **Saída** — A resposta é formatada e exibida ao operador na interface

---

## 📝 System Prompt

O system prompt completo que define o comportamento do chatbot está documentado em: **[system_prompt.md](./system_prompt.md)**

Ele estabelece:
- A identidade e propósito do assistente
- O contexto operacional (eletropostos GoodWe HCA G2 em ambiente comercial)
- Os tipos de dados que o chatbot pode referenciar
- As restrições de comportamento (não inventar dados, não sair do escopo)
- O tom de voz e formato de resposta esperado

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- Chave de API do Google Gemini ([obtenha aqui](https://aistudio.google.com/apikey))

### Passo a passo

**1. Clone o repositório** (se ainda não fez):
```bash
git clone https://github.com/seu-usuario/challenge-goodwe.git
cd challenge-goodwe/pai
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Configure a variável de ambiente com sua API key:**

Windows (PowerShell):
```powershell
$env:GOOGLE_API_KEY = "sua-chave-aqui"
```

Windows (CMD):
```cmd
set GOOGLE_API_KEY=sua-chave-aqui
```

Linux/Mac:
```bash
export GOOGLE_API_KEY="sua-chave-aqui"
```

Google Colab:
```python
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
```

Kaggle Notebooks:
```python
from kaggle_secrets import UserSecretsClient
import os
user_secrets = UserSecretsClient()
os.environ["GOOGLE_API_KEY"] = user_secrets.get_secret("GOOGLE_API_KEY")
```

**4. Execute o chatbot:**
```bash
python chatbot.py
```

> ⚠️ **Importante:** Nunca exponha sua API key diretamente no código ou no repositório. Utilize sempre variáveis de ambiente ou secrets do Colab/Kaggle.

---

## 📦 Dependências

| Pacote | Versão Mínima | Descrição |
|--------|---------------|-----------|
| `langchain` | ≥ 0.3.0 | Framework de orquestração para aplicações LLM |
| `langchain-google-genai` | ≥ 2.1.0 | Integração do LangChain com Google Gemini |
| `google-generativeai` | ≥ 0.8.0 | SDK oficial da Google para a API Gemini |

Instale todas com:
```bash
pip install -r requirements.txt
```

---

## 🔑 Variáveis de Ambiente

| Variável | Obrigatória | Descrição |
|----------|-------------|-----------|
| `GOOGLE_API_KEY` | ✅ Sim | Chave de API do Google Gemini. Obtenha em [AI Studio](https://aistudio.google.com/apikey) |

---

## 💬 Exemplos de Uso

Abaixo, exemplos reais de interação com o ChargeGrid Assistant:

### Exemplo 1 — Consulta de Faturamento
```
👤 Você: Qual foi o faturamento de ontem?

🤖 ChargeGrid: Ontem foram realizadas 12 sessões de recarga no total, consumindo
   180 kWh de energia e gerando uma receita de R$ 234,00. O ticket médio por
   sessão foi de R$ 19,50, com duração média de 1h15min por sessão.
```

### Exemplo 2 — Diagnóstico de Equipamentos
```
👤 Você: Tem algum carregador com problema?

🤖 ChargeGrid: Sim, o Ponto 3 está offline desde ontem às 14:30. O erro
   reportado é uma falha na comunicação Modbus (código E-0x03). Recomendo
   verificar imediatamente a conexão Modbus e a alimentação de rede.
```

### Exemplo 3 — Análise de Demanda
```
👤 Você: Qual horário tem mais demanda?

🤖 ChargeGrid: O horário de maior demanda é entre 17h e 20h, com uma média
   de 3,2 sessões por hora e taxa de ocupação de 92% dos pontos de recarga.
   Atualmente já é aplicada uma tarifa diferenciada de R$ 1,50/kWh nesse período.
```

### Exemplo 4 — Memória de Contexto (diálogo contínuo)
```
👤 Você: Qual foi o faturamento da semana?

🤖 ChargeGrid: O faturamento total dos últimos 7 dias foi de R$ 1.680,50,
   com 87 sessões e 1.293 kWh consumidos.

👤 Você: E como isso se compara com a projeção mensal?

🤖 ChargeGrid: A receita acumulada no mês é de R$ 5.420,00, com projeção de
   R$ 7.800,00 para o mês completo. Considerando o ritmo semanal de R$ 1.680,50,
   a tendência está alinhada com a projeção.
```

---

## 🧪 Modelo de Teste

O modelo completo com perguntas e respostas esperadas está em: **[modelo_teste.md](./modelo_teste.md)**

Contém **5 cenários de teste** cobrindo:
1. Consulta de faturamento
2. Diagnóstico de status técnico
3. Análise de demanda por horário
4. Recomendação de ajuste de tarifa
5. Consulta de geração de energia solar

Cada cenário inclui a pergunta do operador e a resposta ideal esperada, servindo como baseline de qualidade para a implementação na Sprint 2.

---

## ✅ Resultados dos Testes

Os resultados detalhados da execução dos 5 cenários de teste estão documentados em: **[resultados_testes.md](./resultados_testes.md)**

### Resumo

| Cenário | Tema | Avaliação |
|---------|------|-----------|
| 1 | Faturamento | ✅ Adequada |
| 2 | Status Técnico | ✅ Adequada |
| 3 | Demanda por Horário | ✅ Adequada |
| 4 | Ajuste de Tarifa | ✅ Adequada |
| 5 | Energia Solar | ✅ Adequada |

**5/5 cenários avaliados como adequados.** O chatbot demonstrou capacidade de consultar dados operacionais, manter coerência com o system prompt e fornecer recomendações proativas ao operador.

---

## 📂 Estrutura do Repositório

```
pai/
├── README.md              # Este documento
├── chatbot.py             # Chatbot funcional (Gemini + LangChain)
├── requirements.txt       # Dependências Python
├── system_prompt.md       # Prompt que define o comportamento do chatbot
├── fluxograma.png         # Diagrama do fluxo de funcionamento
├── modelo_teste.md        # 5 cenários de teste com perguntas e respostas
└── resultados_testes.md   # Resultados da execução dos testes (Sprint 2)
```

---

## 🗺️ Roadmap — Próximas Sprints

| Sprint | Objetivo | Status |
|--------|----------|--------|
| **Sprint 1** | Exploração, planejamento e documentação | ✅ Concluída |
| **Sprint 2** | Implementação funcional do chatbot com Gemini + LangChain | ✅ Atual |
| **Sprint 3** | Integração com dados reais (SEMS+ / simulados) e refinamento | ⏳ Futuro |

---

## 🔗 Integração com o ChargeGrid Hub

O chatbot não funciona isolado — ele é parte do ecossistema **ChargeGrid Hub**:

- **DSA → PAI:** Os dados gerados pelo simulador de sessão de recarga (Python) alimentam o contexto que o chatbot utiliza para responder sobre faturamento, consumo e duração de sessões
- **CS → PAI:** O circuito lógico de decisão (liberar carga, fila, erro) é referenciado pelo chatbot ao explicar o status de funcionamento dos pontos de recarga
- **MLPAM → PAI:** As análises estatísticas de estações de recarga EV fornecem insights que o chatbot pode usar para benchmarking e recomendações

---

<p align="center">
  <strong>ChargeGrid Hub</strong> — Orquestrando o futuro da mobilidade elétrica com Dados, IoT e Inteligência Artificial.
</p>
