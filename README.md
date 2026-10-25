# Desafio DIO: Criando um Processo de RPA com N8N e Python

## 📌 Descrição do Projeto
Este projeto implementa uma automação híbrida de RPA combinando o poder do **n8n** como orquestrador de fluxo de trabalho e o **Python** para execução da rotina automatizada de coleta e parsing de dados.

## ⚙️ Tecnologias Utilizadas
- **n8n**: Orquestração, agendamento de execução e tratamento de condicionais.
- **Python 3.x**: Script RPA responsável por requisições e normalização dos dados.
- **Formato JSON**: Comunicação e tráfego de dados entre o terminal e o fluxo n8n.

## 🚀 Arquitetura do Fluxo
1. **Schedule Trigger**: Dispara o pipeline automaticamente em horários programados.
2. **Execute Command (Python)**: Executa o script `bot_rpa.py` via CLI.
3. **Parse Output (Node Code)**: Converte a saída `stdout` do terminal em objetos JSON consumíveis pelo n8n.
4. **IF Node (Validação)**: Verifica o status da execução (`sucesso` ou `erro`) para tomada de decisão e notificações.

## 🛠️ Como Executar

### 1. Pré-requisitos
- Python 3 instalado
- Instância do n8n (Desktop, Docker ou Cloud)

### 2. Configuração do Script
Clone o repositório e teste a execução local:
```bash
python bot_rpa.py
