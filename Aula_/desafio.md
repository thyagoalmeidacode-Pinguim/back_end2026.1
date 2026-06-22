# Estudo de Caso — Login Simples com Session

## Situação

Uma empresa deseja criar uma área restrita para seus funcionários.

Ao acessar o sistema, o usuário deverá informar seu nome. Após o login, o sistema deverá lembrar quem está logado utilizando **Session**.

---

## Requisitos

### Página 1 — Login

Criar uma página com um formulário contendo:

- Nome do usuário

Ao clicar em **Entrar**:

- Salvar o nome do usuário na Session.

---

### Página 2 — Área Restrita

O sistema deverá:

- Verificar se existe uma Session.
- Exibir uma mensagem de boas-vindas com o nome do usuário.

### Exemplo

```text
Bem-vindo, João!
```

Caso não exista Session:

```text
Acesso negado. Faça login primeiro.
```

---

### Página 3 — Logout

Criar uma página ou botão para:

- Encerrar a Session.
- Redirecionar para a página de login.

---

## Objetivos da Atividade

Praticar:

- Criar Sessions
- Ler Sessions
- Verificar se uma Session existe
- Remover Sessions
- Controlar acesso entre páginas

---

## Fluxo Esperado

```text
Login
  ↓
Cria Session
  ↓
Área Restrita
  ↓
Lê Session
  ↓
Logout
  ↓
Remove Session
```

---

## Desafio Extra

Adicionar uma página **Perfil** que exiba:

```text
Usuário logado: João
```

utilizando as informações armazenadas na Session.

---

## Reflexão

Assim como um crachá identifica um funcionário dentro da empresa, a **Session identifica o usuário dentro do sistema**, permitindo que o Django saiba quem está utilizando a aplicação durante a navegação.