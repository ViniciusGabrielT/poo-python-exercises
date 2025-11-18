# Resposta 10 - Relatório dos Erros Encontrados e Soluções

## Erro 1: Nome da classe `pessoa`
- **Descrição do problema**: O nome da classe `pessoa` não segue a convenção de nomenclatura do Python (PEP 8), que recomenda o uso de PascalCase para nomes de classes.
- **Solução**: Renomeei a classe para `Pessoa`.
- **Conceito POO**: Convenção de nomenclatura.

---

## Erro 2: Atributo `nome` não inicializado corretamente
- **Descrição do problema**: No construtor da classe `pessoa`, o atributo `nome` foi atribuído diretamente ao parâmetro, sem usar `self`.
- **Solução**: Corrigi a inicialização para `self.nome = nome`.
- **Conceito POO**: Inicialização de atributos.

---

## Erro 3: Atributo privado `__cpf` não utilizado
- **Descrição do problema**: O atributo `__cpf` foi declarado, mas não foi utilizado ou acessado em nenhum lugar do código.
- **Solução**: Mantive o atributo como privado, respeitando o encapsulamento, mas ele pode ser acessado futuramente com métodos `getter` e `setter`.
- **Conceito POO**: Encapsulamento.

---

## Erro 4: Método `apresentar` sem o parâmetro `self`
- **Descrição do problema**: O método `apresentar` não possui o parâmetro `self`, o que impede o acesso aos atributos da instância.
- **Solução**: Adicionei o parâmetro `self` ao método.
- **Conceito POO**: Definição de métodos.

---

## Erro 5: Construtor da classe `Estudante` não chama o construtor da superclasse
- **Descrição do problema**: O construtor da classe `Estudante` não chama o construtor da superclasse `Pessoa`, o que resulta na ausência de inicialização dos atributos herdados.
- **Solução**: Adicionei a chamada ao construtor da superclasse com `super().__init__(nome, idade)`.
- **Conceito POO**: Herança e uso de `super()`.

---

## Erro 6: Divisão por zero no método `calcular_media`
- **Descrição do problema**: O método `calcular_media` não trata o caso em que a lista de notas está vazia, o que pode causar uma divisão por zero.
- **Solução**: Adicionei uma verificação para retornar `0` caso a lista de notas esteja vazia.
- **Conceito POO**: Lógica de negócio.

---

## Erro 7: Método `calcular_media` chamado sem adicionar notas
- **Descrição do problema**: No exemplo de uso, o método `calcular_media` é chamado antes de adicionar notas ao estudante, o que resulta em uma lista vazia.
- **Solução**: Adicionei notas ao estudante antes de chamar o método `calcular_media`.
- **Conceito POO**: Lógica de negócio.

---

## Conclusão
Após corrigir os 7 erros, o código agora segue as boas práticas de Programação Orientada a Objetos, respeitando os princípios de encapsulamento, herança, inicialização de atributos e lógica de negócio.