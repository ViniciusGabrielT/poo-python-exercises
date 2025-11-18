class Pessoa:  # Corrigido: Nome da classe com letra maiúscula (convenção PEP 8)
    def __init__(self, nome, idade):
        self.nome = nome  # Corrigido: Atributo `self.nome` foi corretamente inicializado
        self.idade = idade
        self.__cpf = None  # Mantido como atributo privado (encapsulamento)

    def apresentar(self):  # Corrigido: Adicionado `self` como parâmetro do método
        return f"Olá, sou {self.nome}"


class Estudante(Pessoa):  # Corrigido: Nome da classe com letra maiúscula e herança corrigida
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Corrigido: Chamada ao construtor da superclasse
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:  # Mantida a validação de nota
            self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:  # Corrigido: Tratamento para evitar divisão por zero
            return 0
        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):  # Corrigido: Nome da classe com letra maiúscula e herança corrigida
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)  # Corrigido: Chamada ao construtor da superclasse
        self.departamento = departamento
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"


# Testando o código corrigido
estudante = Estudante("João", 20, "Engenharia")
professor = Professor("Dr. Silva", 45, "Computação", 8000)

# Adicionando notas ao estudante
estudante.adicionar_nota(8)
estudante.adicionar_nota(9)

# Exibindo as apresentações e a média do estudante
print(estudante.apresentar())
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")