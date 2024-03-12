---
Título: TPC4
Data: 12 de Março de 2024
Autor: Joana Pereira
UC: RPCW
---

# Tabela Periódica

Este trabalho tem como objetivo um projeto web que utiliza dados provenientes de um repositório GraphDB após a criação e carregamento do arquivo TTL correspondente. A aplicação consiste em páginas interativas relacionadas a elementos químicos e grupos, aproveitando as funcionalidades fornecidas pelo GraphDB.

## Etapas Realizadas

### 1. Criação de um Repositório no GraphDB

Comecei por criar um repositório no GraphDB através de um arquivo TTL com informações de uma tabela periódica.

### 2.  Páginas Web

De seguida entre outros ficheiros foram criadas 5 páginas web:

- **index.html** - Página inicial com a opção de navegar tanto para a página de grupos como dos elementos.

- **elementos.html** - Página com a informação (nome, símbolo, número atómico, número de grupo e nome de grupo) de cada elemento com link de redireção no nome do elemento e no grupo.

- **grupos.html** - Página com a o nome e número de cada grupo

- **grupo.html** - Página que apresenta as informações dos elementos de um determinado grupo como o nome, símbolo e número atómico de cada elemento

- **elemento.html** - Página que apresenta a informação de um determinado elemento como o nome, símbolo, número atómico, peso atómico, cor, número do grupo, nome do grupo e período.