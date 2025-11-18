class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
       self.nome = nome
       self.cpf = cpf
       self.data_nascimento = data_nascimento

    def apresentar(self):   
        return f"Olá! Meu nome é {self.nome}, o meu CPF é {self.cpf} e eu nasci em {self.data_nascimento}."
    
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome}, o meu CPF é {self.cpf}, eu nasci em {self.data_nascimento} e sou {self.cargo}."
    
    def exibir_dados(self):
        return f"=== Dados do Funcionário ===\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nCargo: {self.cargo}\nSalário: {self.salario}"

class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.area_atuacao = area_atuacao

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome}, o meu CPF é {self.cpf}, eu nasci em {self.data_nascimento} e atuo na área de {self.area_atuacao}."

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def info_aluno(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        
        return sum(self.notas) / len(self.notas)

    def status(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado!"
        else:
            return "Reprovado!"
        
class Professor:
    def __init__(self, nome, departamento, salarioInicial):
        self.nome = nome
        self.departamento = departamento        
        self._salario = salarioInicial

    def getSalario(self): # getter
        return self._salario

    def setSalario(self, novoSalario): #setter
        if novoSalario > 0:
            self._salario = novoSalario
        else:
            return "Erro! O novo salário não pode ser uma valor negativo."

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def info_displina(self):
        return f"Nome {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria}"

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        print(f"=== Disciplinas do Curso: {self.nome} ===")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome} ({disciplina.codigo})")

    def carga_horaria_total(self):
        return sum(disciplina.carga_horaria for disciplina in self.disciplinas)

# Exemplo de Uso
curso = Curso("Engenharia de Software", "ES001") # objeto da classe Curso
disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", 60) # objeto da classe Disciplina
disciplina2 = Disciplina("Banco de Dados", "BD001", 80) # objeto da classe Disciplina

# Adicionando disciplinas ao curso
curso.adicionar_disciplina(disciplina1) # objeto da classe Curso chamando um método da classe disciplina
curso.adicionar_disciplina(disciplina2)

# Listando disciplinas
curso.listar_disciplinas()

# Exibindo a carga horária total
print(f"Carga horária total: {curso.carga_horaria_total()}h")