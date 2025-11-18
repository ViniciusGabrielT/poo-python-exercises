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
        self.disciplinas_inscritas = []  # Lista de disciplinas em que o aluno está inscrito

    def info_aluno(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"
    
    def listar_disciplinas(self):
        print(f"=== Disciplinas de {self.nome} ===")
        for disciplina in self.disciplinas_inscritas:
            print(f"- {disciplina.nome} ({disciplina.codigo})")

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
        self.alunos_matriculados = []  # Lista de alunos matriculados na disciplina

    def info_displina(self):
        return f"Nome: {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria}"
    
    def listar_alunos(self):
        print(f"=== Alunos matriculados em {self.nome} ===")
        for aluno in self.alunos_matriculados:
            print(f"- {aluno.nome} ({aluno.matricula})")

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

class Secretaria:
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        """Inscreve um aluno em uma disciplina e atualiza as listas de ambos."""
        if disciplina not in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.append(disciplina)
        if aluno not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(aluno)

# Exemplo de Uso
aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
disciplina1 = Disciplina("POO", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

# Inscrevendo alunos nas disciplinas
Secretaria.inscrever_aluno(aluno1, disciplina1)
Secretaria.inscrever_aluno(aluno1, disciplina2)
Secretaria.inscrever_aluno(aluno2, disciplina1)

# Listando disciplinas de um aluno
aluno1.listar_disciplinas()

# Listando alunos de uma disciplina
disciplina1.listar_alunos()