# Estudo de Caso 2 — Sistema de Loja de Games

## Utilizando SOMENTE Programação Orientada a Objetos

---

# Situação

Uma loja de games deseja criar um sistema para cadastrar jogos.

Cada jogo deverá possuir:

- nome
- categoria
- preço

O sistema deverá:

- cadastrar jogos
- mostrar jogos cadastrados

---

# Objetivo do Exercício

Os alunos deverão praticar:

- orientação a objetos pura
- classes
- objetos
- atributos
- métodos
- composição
- listas de objetos

---

# Regras

- ❌ Não utilizar funções procedurais
- ❌ Não utilizar funções fora das classes
- ✅ Tudo deve acontecer através dos objetos

---

# Estrutura Esperada

## Classe Jogo

Representa um jogo.

### Atributos

- nome
- categoria
- preço

### Métodos

- mostrar_dados()

---

## Classe Loja

Responsável por:

- cadastrar jogos
- armazenar jogos
- mostrar jogos
- controlar o menu

### Atributos

- lista_jogos

### Métodos

- cadastrar_jogo()
- mostrar_jogos()
- iniciar()

---

# Desafio

Crie um sistema onde:

1. O usuário possa cadastrar vários jogos
2. Os jogos sejam armazenados dentro da loja
3. O sistema mostre todos os jogos cadastrados
4. O menu permita escolher as opções do sistema

---

# Exemplo de Saída Esperada

```text
Nome: God of War
Categoria: Aventura
Preço: R$ 199.90

Nome: FIFA 25
Categoria: Esporte
Preço: R$ 299.90
```