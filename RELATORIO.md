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
| Memória da lista / memória do `uint16` | 4 | 18 |
| Tempo do laço / tempo vetorizado | 10 | 57 |
| Tempo da compreensão / tempo do laço | 0.1 | 0,71 |

A lista sempre ocupa pelo menos o espaço de 64bits (um registrado) mais a sobreposição das informações de classe enquanto o uint16 é apenas a informação que está na memória.
O laço sempre é lento pois em uma linguagem script é interpretado enquanto a operação com Vetor NumPy é otimizada para vetor.
O tempo de compreesão no python é otimizado, por isso é melhor.
Eu usária o Vetorizado para contar pela sua velocidade.

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | SerieTemporal | SerieTemporal |
| `s[1:]` | SerieTemporal | SerieTemporal |
| `s * 2` | SerieTemporal | SerieTemporal |
| `s.sum()` | SerieTemporal | SerieTemporal |
| `s[0]` | float | float64 |

Nenhum me surpreendeu

### R7 — Issue #4

test_media_movel, testa o resultado levando em conta o vetor inteiro conforme descrito com resultado comparando numero a numero, enquanto os outros testes só levam en consideração a chamada da função sem conferir o resultado.
