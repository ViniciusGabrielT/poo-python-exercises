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

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def info_displina(self):
        return f"Nome {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria}"
    
aluno = Aluno("João Silva", "2023001", "Engenharia de Software")

aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)

print(f"Média: {aluno.calcular_media()}")

aluno.status()