# Relatório — Emilio (20045)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

/Users/evbrazil/venvs/prog2-venv/bin/python

### R1 — Expressões regulares

"PT1010x" -> Fullmatch rejeita e match aceita

### R2 — Linhas inválidas

Um censor com defeito poderia passar despercebido

### R3 — Late binding

como a função é criada apenas após o última iteração o dfator é o ultimo para todas as funções. Para resolver forcei o fator com um valor padrão o que o briga o interpretador a avaliar a cada iteração. 

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit:

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | 4 | |
| Tempo do laço / tempo vetorizado | 10 | |
| Tempo da compreensão / tempo do laço | 0.1 | |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | | |
| `s[1:]` | | |
| `s * 2` | | |
| `s.sum()` | | |
| `s[0]` | | |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4

<!-- Sintoma; o teste de regressão (nome); a causa, em termos da soma acumulada; a correção; por que os testes de aceitação não pegaram o defeito; mais um caso que eles não cobrem e qual teste seu o cobre. -->
