# 🚗 Company Cars - Sistema CRUD com Python e Oracle

Este projeto é um sistema simples de gerenciamento de concessionária (Company Cars) desenvolvido em Python, utilizando o banco de dados Oracle para persistência dos dados. O projeto foi criado como parte das atividades de [Ánalise e Desenvolvimento de Sistemas] na [FIAP].

## 🧑‍💻 Desenvolvedores

| Nome | RM |
| [João Victor Veronesi] | [RM: 565290] |
| [Alvaro Freitas Miranda] | [RM: 565364] |

## ✨ Funcionalidades

O sistema Company Cars implementa todas as operações CRUD (Create, Read, Update, Delete) na tabela de carros:

1.  **Cadastrar Carros (Create):** Adiciona novos veículos ao banco de dados.
2.  **Pesquisar Carros (Read):** Consulta um carro específico por ID.
3.  **Listar todos os Carros (Read):** Exibe todos os registros em formato de tabela (usando Pandas).
4.  **Editar registro do carro (Update):** Atualiza os dados de um veículo existente (modelo, marca, ano, cor, proprietário).
5.  **Apagar registro do carro (Delete):** Exclui permanentemente um registro por ID.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 
* **Banco de Dados:** Oracle (Conexão via DSN da FIAP)
* **Driver:** `oracledb`
* **Manipulação de Dados:** `pandas` (para exibição de tabelas)

## 🗄️ Estrutura do Banco de Dados (SQL)

A tabela utilizada no projeto é a `CARROS`, criada com a seguinte estrutura:

```sql
CREATE TABLE carros (
    id_carro INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    ano DECIMAL(4) NOT NULL,            
    cor VARCHAR(30),            
    proprietario VARCHAR(100)  
);
