# Desafio Dev

Solução de três exercícios em Python: comissão de vendedores, movimentação de estoque e cálculo de juros por atraso.

Requisito: **Python 3** (sem dependências externas).

## Estrutura

| Arquivo | Descrição |
|---|---|
| `comissao.py` | Calcula a comissão de cada vendedor a partir de `vendas.json` |
| `estoque.py` | Lança entradas e saídas de produtos do `estoque.json` |
| `juros.py` | Calcula os juros de um valor vencido até a data de hoje |
| `test_desafio.py` | Testes das regras principais |
| `vendas.json` | Vendas do time comercial |
| `estoque.json` | Produtos e quantidades iniciais |

## 1. Comissão dos vendedores

Lê `vendas.json` e aplica a regra venda a venda, somando por vendedor:

| Valor da venda | Comissão |
|---|---|
| Abaixo de R$ 100,00 | 0% |
| De R$ 100,00 até R$ 499,99 | 1% |
| A partir de R$ 500,00 | 5% |

Os cálculos usam `Decimal` para evitar erros de arredondamento com dinheiro.

```bash
python comissao.py
```

Resultado:

```
João Silva           R$     495.69
Maria Souza          R$     465.96
Carlos Oliveira      R$     379.38
Ana Lima             R$     404.99
```

## 2. Movimentação de estoque

Menu no terminal para lançar movimentações nos produtos do `estoque.json`. Cada movimentação tem:

- identificador único (UUID)
- descrição do tipo de movimentação
- tipo (`entrada` ou `saida`), quantidade e data/hora

Ao final, mostra a quantidade final em estoque do produto movimentado.

São recusados: produto inexistente, tipo inválido, quantidade zero ou negativa e saída maior que o estoque disponível.

```bash
python estoque.py
```

Deixe o código do produto vazio e pressione Enter para sair. As movimentações ficam em memória; o `estoque.json` não é alterado.

## 3. Juros por atraso

Recebe um valor e uma data de vencimento (`dd/mm/aaaa`) e calcula os juros até hoje, com taxa de 2,5% ao dia (juros simples):

```
juros = valor × 2,5% × dias de atraso
```

Se o vencimento ainda não passou, os juros são zero. Mostra os dias em atraso, os juros e o total a pagar.

```bash
python juros.py
```

## Testes

```bash
python test_desafio.py
```

Imprime `ok` se todas as verificações passarem.
