# Projeto NeoADP

## Sobre

Este projeto tem como objetivo principal a implementação do método PEWS, uma ferramenta de uso dos profissionais da saúde que, com base no estado de uma criança, calcula uma intervenção a partir de um sistema de pontuações. Em outras palavras, esta ferramenta entrega uma solução específica para um(a) menino(a) que apresente determinados sintomas, o que agiliza o processo de diagnóstico e, consequentemente, de tratamento.

## Funcionalidades

1) CRUDS:
	1) CRUD Profissional de saúde responsável;
	2) CRUD Responsável;
	3) CRUD Criança;
	4) CRUD Internação.
	
2) Implementação do PEWS;

## Como rodar o projeto?

### PostgreSQL

1) Será necessário ter instalado em seu computador o SGBD PostgreSQL e ter criado um banco de dados (schema) com nome `neo-adp-project`;
2) No arquivo `caminho-até-a-pasta-do-projeto/NeoADPproject/NeoADPproject/settings.py` faz-se necessário editar a variável `DATABASES`, colocando nela as informações sobre seu servidor PGSQL, como usuário e senha.

### Python
1) Será necessário ter instalado em seu computador a linguagem de programação Python 3.12 ou uma versão mais recente;
2) Será necessário ter instalado em seu computador a framework Django;
3) É necessário satisfazer todas as dependências para que o projeto funcione, instalando todas as bibliotecas contidas no arquivo `caminho-até-a-pasta-do-projeto/requirements.txt`.



## Anotações para os participantes do projeto

### 07/02/2024 - Juliano

* O back-end muito provavelmente será todo feito em Django (Python), pra facilitar no desenvolvimento e agilizar o processo, já que a linguagem é de mais alto nível;
* É interessante manter algumas funcionalidades mais simples em JavaScript mesmo, como o cáculo da soma dos sintomas e a assimilação à intervenção necessária;