from datetime import date
from decimal import Decimal

from comissao import comissao
from estoque import Estoque
from juros import calcular_juros

assert comissao(Decimal("99.99")) == 0
assert comissao(Decimal("100")) == Decimal("1.00")
assert comissao(Decimal("499.99")) == Decimal("5.00")
assert comissao(Decimal("500")) == Decimal("25.00")

e = Estoque([{"codigoProduto": 1, "descricaoProduto": "X", "estoque": 10}])
assert e.movimentar(1, "entrada", 5, "Compra") == 15
assert e.movimentar(1, "saida", 15, "Venda") == 0
try:
    e.movimentar(1, "saida", 1, "Venda")
    assert False
except ValueError:
    pass
assert e.movimentacoes[0]["id"] != e.movimentacoes[1]["id"]

assert calcular_juros(Decimal("1000"), date(2026, 1, 1), date(2026, 1, 11)) == (10, Decimal("250.00"))
assert calcular_juros(Decimal("1000"), date(2026, 1, 11), date(2026, 1, 1)) == (0, Decimal("0.00"))

print("ok")
