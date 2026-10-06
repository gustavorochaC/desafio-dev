import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP


def comissao(valor):
    if valor < 100:
        return Decimal("0")
    taxa = Decimal("0.01") if valor < 500 else Decimal("0.05")
    return (valor * taxa).quantize(Decimal("0.01"), ROUND_HALF_UP)


def calcular(vendas):
    totais = defaultdict(Decimal)
    for venda in vendas:
        totais[venda["vendedor"]] += comissao(Decimal(str(venda["valor"])))
    return dict(totais)


if __name__ == "__main__":
    with open("vendas.json", encoding="utf-8") as f:
        vendas = json.load(f)["vendas"]

    for vendedor, total in calcular(vendas).items():
        print(f"{vendedor:<20} R$ {total:>10.2f}")
