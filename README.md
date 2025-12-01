# Máquina de Turing – Regra 30  
Projeto Final – Linguagens Formais e Autômatos  
Instituto Federal Goiano – Campus Trindade


![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![MT](https://img.shields.io/badge/Máquina%20de%20Turing-Regra%2030-orange)v

## 📌 Descrição do Projeto
Este trabalho implementa uma **Máquina de Turing** capaz de gerar a **próxima linha** de um autômato celular unidimensional segundo a **Regra 30**, proposta por Stephen Wolfram.

A entrada é uma linha de bits `0` e `1`, limitada por `#`, e a saída é escrita após um separador `|` na própria fita.

Exemplo de fita de entrada:

#000100#|

---

## 📘 O que é a Regra 30?
A Regra 30 é um autômato celular de uma dimensão onde cada célula depende de:

- O valor da célula à esquerda  
- O valor da célula atual  
- O valor da célula à direita  

A tabela da regra é:

| Vizinhança | Novo Valor |
|------------|------------|
| 111 | 0 |
| 110 | 0 |
| 101 | 0 |
| 100 | 1 |
| 011 | 1 |
| 010 | 1 |
| 001 | 1 |
| 000 | 0 |

O padrão gerado costuma ser **caótico**, mesmo partindo de uma única célula preta.

Um exemplo visual clássico gerado por várias iterações:

                           1
                          111
                         11001
                        1011110
                       100100110
                     ... (caótico)


---

## 🧠 Descrição Formal da Máquina de Turing

A Máquina de Turing proposta é definida por:

- **Estados:**  
  `Q = { q0, q_scan, q_compute, q_write, q_return, q_accept }`

- **Alfabeto de entrada:**  
  `Σ = { 0, 1 }`

- **Alfabeto da fita:**  
  `Γ = { 0, 1, #, |, B }`

- **Estado inicial:**  
  `q0`

- **Estado de aceitação:**  
  `q_accept`

- **Objetivo:**  
  Para cada célula da entrada, ler sua vizinhança `(esq, atual, dir)` e usar a Regra 30 para calcular a próxima linha, escrevendo na região de saída à direita do caractere `|`.

---

## 🔀 Diagrama da Máquina de Turing (ASCII)

Representação simplificada do comportamento geral:
           +----------------------+
           |                      |
           v                      |
          (q0) -------> (q_scan) ----0/1------> (q_compute)
          | | |
          | | if # |
          | v v
          | (q_accept) <-------- (q_return)
          | |
          +---------------------------------- (q_write)


**Descrição resumida dos estados:**

- **q0:** Pula o primeiro `#` e inicia leitura.  
- **q_scan:** Varre a linha da esquerda para direita.  
- **q_compute:** Obtém vizinhança e aplica Regra 30.  
- **q_write:** Escreve resultado na parte da saída.  
- **q_return:** Volta para a próxima célula da entrada.  
- **q_accept:** Fim da computação.

---

**Execução**:

python3 mt_regra30.py

**Estrutura do Repositório**
/
├── README.md
└── mt_regra30.py




