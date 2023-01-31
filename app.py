class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

lucas = Pessoa("Lucas", 28, "Programador")

# Acessando as propriedades do objeto

print(lucas.nome)
print(lucas.idade)
print(lucas.profissao)