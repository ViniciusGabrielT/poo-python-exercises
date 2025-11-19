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
class ProcessadorPagamentoDesconto:
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

# Abstração para serviços de notificação
class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        """Método abstrato para enviar notificações"""
        pass

# Implementação do serviço de email
class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

# Implementação do serviço de SMS
class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

# Implementação do serviço de notificação push
class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando push: {mensagem}")

# Classe NotificacaoService que depende da abstração
class NotificacaoService:
    def __init__(self, servico_notificacao: ServicoNotificacao):
        self.servico_notificacao = servico_notificacao

    def notificar(self, mensagem):
        self.servico_notificacao.enviar(mensagem)

# Interface esperada pelo sistema
class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor, cartao):
        pass

# Implementação interna do processador de pagamento
class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        print(f"Processador Interno: Processando R$ {valor:.2f} no cartão {cartao}")

# Serviço externo (não pode ser modificado)
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"

# Adapter para integrar PayPalAPI com o sistema
class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        resultado = self.paypal_api.make_payment(valor, cartao)
        print(resultado)

# Classe SistemaPagamento que usa qualquer ProcessadorPagamento
class SistemaPagamento:
    def __init__(self, processador_pagamento: ProcessadorPagamento):
        self.processador_pagamento = processador_pagamento

    def realizar_pagamento(self, valor, cartao):
        self.processador_pagamento.processar_pagamento(valor, cartao)

# Interface base para bebidas
class Bebida(ABC):
    @abstractmethod
    def get_descricao(self):
        pass

    @abstractmethod
    def get_preco(self):
        pass

# Bebidas concretas
class Cafe(Bebida):
    def get_descricao(self):
        return "Café"

    def get_preco(self):
        return 5.0

class Cha(Bebida):
    def get_descricao(self):
        return "Chá"

    def get_preco(self):
        return 3.0

# Decorator base
class BebidaDecorator(Bebida):
    def __init__(self, bebida: Bebida):
        self.bebida = bebida

    @abstractmethod
    def get_descricao(self):
        pass

    @abstractmethod
    def get_preco(self):
        pass

# Decorators concretos
class LeiteDecorator(BebidaDecorator):
    def get_descricao(self):
        return f"{self.bebida.get_descricao()} com Leite"

    def get_preco(self):
        return self.bebida.get_preco() + 2.0

class AcucarDecorator(BebidaDecorator):
    def get_descricao(self):
        return f"{self.bebida.get_descricao()} com Açúcar"

    def get_preco(self):
        return self.bebida.get_preco() + 0.5

class ChantillyDecorator(BebidaDecorator):
    def get_descricao(self):
        return f"{self.bebida.get_descricao()} com Chantilly"

    def get_preco(self):
        return self.bebida.get_preco() + 3.0

# Sistema complexo
class Amplificador:
    def ligar(self):
        print("Ligando amplificador")

    def definir_volume(self, volume):
        print(f"Definindo volume para {volume}")

class DVDPlayer:
    def ligar(self):
        print("Ligando DVD player")

    def reproduzir(self, filme):
        print(f"Reproduzindo {filme}")

class Projetor:
    def ligar(self):
        print("Ligando projetor")

    def modo_widescreen(self):
        print("Ativando modo widescreen")

class Luzes:
    def diminuir(self, nivel):
        print(f"Diminuindo luzes para {nivel}%")

class PipocaPopper:
    def ligar(self):
        print("Ligando pipoqueira")

    def fazer_pipoca(self):
        print("Fazendo pipoca")

# Facade para simplificar o uso do sistema
class HomeTheaterFacade:
    def __init__(self):
        self.amplificador = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self, filme):
        print(f"Preparando para assistir {filme}...")
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.luzes.diminuir(10)
        self.projetor.ligar()
        self.projetor.modo_widescreen()
        self.amplificador.ligar()
        self.amplificador.definir_volume(5)
        self.dvd.ligar()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("Filme finalizado!")
        print("Desligando todos os componentes...")

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade, pressao):
        pass

# Classe Subject (Estação Meteorológica)
class EstacaoMeteorologica:
    def __init__(self):
        self.observers = []
        self.temperatura = None
        self.umidade = None
        self.pressao = None

    def adicionar_observer(self, observer: Observer):
        self.observers.append(observer)

    def remover_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for observer in self.observers:
            observer.update(self.temperatura, self.umidade, self.pressao)

    def definir_medicoes(self, temperatura, umidade, pressao):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.notificar_observers()

# Observadores concretos
class DisplayTemperatura(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Temperatura: {temperatura}°C")

class DisplayUmidade(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Umidade: {umidade}%")

class DisplayCompleto(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Completo: {temperatura}°C, {umidade}%, {pressao} hPa")

# Exemplo de Uso
if __name__ == "__main__":
    estacao = EstacaoMeteorologica()

    # Criando displays
    display_temp = DisplayTemperatura()
    display_umidade = DisplayUmidade()
    display_completo = DisplayCompleto()

    # Registrando observadores
    estacao.adicionar_observer(display_temp)
    estacao.adicionar_observer(display_umidade)
    estacao.adicionar_observer(display_completo)

    # Mudança de estado notifica todos
    estacao.definir_medicoes(25.5, 65.0, 1013.2)
    estacao.definir_medicoes(27.0, 70.0, 1015.1)