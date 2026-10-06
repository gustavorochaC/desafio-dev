import json
import uuid
from datetime import datetime


class Estoque:
    def __init__(self, produtos):
        self.produtos = {p["codigoProduto"]: p for p in produtos}
        self.movimentacoes = []

    def movimentar(self, codigo, tipo, quantidade, descricao):
        if codigo not in self.produtos:
            raise ValueError(f"Produto {codigo} não encontrado")
        if tipo not in ("entrada", "saida"):
            raise ValueError("Tipo deve ser 'entrada' ou 'saida'")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")

        produto = self.produtos[codigo]
        delta = quantidade if tipo == "entrada" else -quantidade
        if produto["estoque"] + delta < 0:
            raise ValueError(f"Estoque insuficiente (atual: {produto['estoque']})")

        produto["estoque"] += delta
        self.movimentacoes.append({
            "id": str(uuid.uuid4()),
            "codigoProduto": codigo,
            "tipo": tipo,
            "quantidade": quantidade,
            "descricao": descricao,
            "data": datetime.now().isoformat(timespec="seconds"),
        })
        return produto["estoque"]


def main():
    with open("estoque.json", encoding="utf-8") as f:
        estoque = Estoque(json.load(f)["estoque"])

    while True:
        print("\nProdutos:")
        for p in estoque.produtos.values():
            print(f"  {p['codigoProduto']} - {p['descricaoProduto']}: {p['estoque']}")

        codigo = input("\nCódigo do produto (Enter para sair): ").strip()
        if not codigo:
            break
        try:
            tipo = input("Tipo (entrada/saida): ").strip().lower()
            quantidade = int(input("Quantidade: "))
            descricao = input("Descrição da movimentação: ").strip()
            final = estoque.movimentar(int(codigo), tipo, quantidade, descricao)
            mov = estoque.movimentacoes[-1]
            print(f"\nMovimentação {mov['id']} registrada.")
            print(f"Estoque final de {estoque.produtos[int(codigo)]['descricaoProduto']}: {final}")
        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
