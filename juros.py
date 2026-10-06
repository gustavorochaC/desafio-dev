from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP

TAXA_DIARIA = Decimal("0.025")


def calcular_juros(valor, vencimento, hoje=None):
    hoje = hoje or date.today()
    dias_atraso = max((hoje - vencimento).days, 0)
    juros = (valor * TAXA_DIARIA * dias_atraso).quantize(Decimal("0.01"), ROUND_HALF_UP)
    return dias_atraso, juros


if __name__ == "__main__":
    valor = Decimal(input("Valor (ex: 1500.00): ").replace(",", "."))
    vencimento = datetime.strptime(input("Data de vencimento (dd/mm/aaaa): "), "%d/%m/%Y").date()

    dias, juros = calcular_juros(valor, vencimento)
    print(f"Dias em atraso: {dias}")
    print(f"Juros: R$ {juros:.2f}")
    print(f"Total a pagar: R$ {valor + juros:.2f}")
