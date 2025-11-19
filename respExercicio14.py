from abc import ABC, abstractmethod

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

# Classe abstrata para cálculo de descontos
class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        """Método abstrato para calcular o desconto"""
        pass

# Implementação de diferentes tipos de desconto
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.9  # 10% de desconto

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto

# Classe para processar pagamentos com diferentes descontos
class ProcessadorPagamento:
    def processar(self, valor, calculador_desconto):
        return calculador_desconto.calcular(valor)

# Classe base Veiculo
class Veiculo(ABC):
    def __init__(self, velocidade_maxima):
        self.velocidade_atual = 0
        self.velocidade_maxima = velocidade_maxima

    @abstractmethod
    def acelerar(self):
        """Aumenta a velocidade do veículo"""
        pass

    @abstractmethod
    def frear(self):
        """Diminui a velocidade do veículo"""
        pass

    def get_velocidade(self):
        """Retorna a velocidade atual"""
        return self.velocidade_atual

# Classe Carro
class Carro(Veiculo):
    def __init__(self):
        super().__init__(180)  # Velocidade máxima de 180 km/h

    def acelerar(self):
        self.velocidade_atual = min(self.velocidade_atual + 20, self.velocidade_maxima)

    def frear(self):
        self.velocidade_atual = max(self.velocidade_atual - 20, 0)

# Classe Bicicleta
class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(50)  # Velocidade máxima de 50 km/h

    def acelerar(self):
        self.velocidade_atual = min(self.velocidade_atual + 10, self.velocidade_maxima)

    def frear(self):
        self.velocidade_atual = max(self.velocidade_atual - 10, 0)

# Classe Aviao
class Aviao(Veiculo):
    def __init__(self):
        super().__init__(900)  # Velocidade máxima de 900 km/h

    def acelerar(self):
        self.velocidade_atual = min(self.velocidade_atual + 100, self.velocidade_maxima)

    def frear(self):
        self.velocidade_atual = max(self.velocidade_atual - 100, 0)

# Interfaces específicas
class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Alimentavel(ABC):
    @abstractmethod
    def comer(self):
        pass

class Descansavel(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Programavel(ABC):
    @abstractmethod
    def programar(self):
        pass

# Classes concretas
class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    def programar(self):
        print(f"{self.nome} está programando.")

class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

class Robo(Trabalhavel, Programavel):
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

    def programar(self):
        print(f"{self.nome} está programando.")

# Exemplo de Uso
if __name__ == "__main__":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    # Desenvolvedor faz tudo
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()

    # Gerente não programa
    gerente.trabalhar()
    gerente.comer()

    # Robô não come nem dorme
    robo.trabalhar()
    robo.programar()