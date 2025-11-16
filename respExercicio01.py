class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def info_aluno(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}"

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def info_displina(self):
        return f"Nome {self.nome}, Código: {self.codigo}, Carga Horária: {self.carga_horaria}"

aluno1 = Aluno("João", 6325225, "ADS")
discplina1 = Disciplina("Cloud", 12112025, 25)

print(aluno1.info_aluno())
print(discplina1.info_displina())