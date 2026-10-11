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

## Marco 2

### Ambiente

=== Etapa 0: ambiente ===
Python 3.9.6 | NumPy 2.0.2 | SciPy 1.13.1 | fornecido 2.0 | matrícula 20045

### R8 — Derivada numérica

Para h grande, domina o erro de truncamento: a diferença adiante erra na proporção de h, e por isso o erro cai 10× cada vez que h diminui 10×. Para h pequeno, domina o erro de arredondamento: f(x + h) e f(x) ficam quase iguais, e a subtração perde dígitos. O melhor h fica no meio, onde os dois se equilibram (aqui, h = 1e-5). Em h = 1e-14, 1000 + 1e-14 == 1000: o numerador dá zero, a aproximação vale 0 e o erro é a própria derivada (0,2134).

### R9 — Issue #7

Em ponto flutuante, t já é o resultado arredondado de s + y. Calcular s + y de novo dá exatamente o mesmo t, então t - (s + y) é sempre zero e a correção nunca age: o algoritmo vira a soma ingênua. Já (t - s) - y mede o que de fato se perdeu no arredondamento. Os testes de aceitação somam só dez parcelas e usam math.isclose, que a soma ingênua também satisfaz.

### R10 — Precisão × exatidão

O desvio (≈ 0,53 kPa, igual nas duas curvas) mede a precisão: o quanto as leituras se espalham. O viés (−1,83 kPa na linear, ≈ 0 na spline) mede a exatidão: o quanto a média se afasta do valor verdadeiro. Mais leituras reduzem o efeito do ruído, mas não o viés, porque a curva linear erra sempre para o mesmo lado.
