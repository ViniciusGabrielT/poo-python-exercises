# Classe Funcionario: Responsável apenas por armazenar os dados do funcionário
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

# Classe CalculadoraSalario: Responsável pelos cálculos relacionados ao salário
class CalculadoraSalario:
    @staticmethod
    def calcular_salario_liquido(funcionario, descontos):
        return funcionario.salario - descontos

# Classe GeradorRelatorio: Responsável pela geração de relatórios
class GeradorRelatorio:
    @staticmethod
    def gerar_relatorio(funcionario):
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario:.2f}"

# Classe RepositorioFuncionario: Responsável pela persistência de dados
class RepositorioFuncionario:
    @staticmethod
    def salvar(funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")

# Exemplo de Uso
if __name__ == "__main__":
    # Criando um funcionário
    funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")

    # Instanciando as classes responsáveis por cada funcionalidade
    calculadora = CalculadoraSalario()
    gerador = GeradorRelatorio()
    repositorio = RepositorioFuncionario()

    # Calculando o salário líquido
    salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

    # Gerando o relatório
    relatorio = gerador.gerar_relatorio(funcionario)
    print(relatorio)

    # Salvando o funcionário no banco de dados
    repositorio.salvar(funcionario)