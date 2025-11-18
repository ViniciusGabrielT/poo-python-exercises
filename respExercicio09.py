class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome}."


class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso

    def apresentar(self):
        return f"Olá, sou o aluno {self.nome} e estudo no curso {self.curso}."


class Professor(Pessoa):
    def __init__(self, nome, departamento, salario):
        super().__init__(nome)
        self.departamento = departamento
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o professor {self.nome} e leciono no departamento {self.departamento}."


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        return f"Olá, sou o funcionário {self.nome} e meu cargo é {self.cargo}."

# Exemplo de Uso
pessoas = [
    Aluno("João Silva", "2023001", "Engenharia de Software"),
    Professor("Dr. Maria", "Computação", 8000.0),
    Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 3000.0),
]

for pessoa in pessoas:
    print(pessoa.apresentar())