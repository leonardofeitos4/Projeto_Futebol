# Título do Projeto

Análise das Estatísticas do Campeonato Brasileiro

Link visualização PowerBi [https://app.powerbi.com/view?r=eyJrIjoiZjI5NWM0NjQtYWExMS00NjFhLWE5MDctYjdiMzdkYzIwODNmIiwidCI6IjVhM2UxZWI5LWM3NzctNDQ1YS04MjQyLWQ4MjVhNDYxYjEyYiJ9]
![image](https://github.com/user-attachments/assets/c15cbbf5-1690-4100-ac3e-da49587df30c)


## Descrição

Este projeto foi desenvolvido para ser apresentado ao professor de Banco de Dados, com o objetivo de analisar as estatísticas do Campeonato Brasileiro. Utilizando dados obtidos do Kaggle, foram adicionadas as tabelas "data" e "clubes" ao banco de dados. 

Além disso, fiz modificações nas tabelas existentes — "campeonato_brasileiro", "estatisticas" e "gols" — para que se adequassem melhor aos requisitos da análise. O projeto se propõe a oferecer uma visão detalhada das estatísticas do campeonato, destacando as porcentagens de ganhos e perdas dos times mandantes, tanto em partidas em casa quanto como visitantes, além de calcular a porcentagem de empates.

## Tecnologias Utilizadas

- Power BI
- DBeaver
- MySQL
- Python
- Dados do Kaggle

## Estrutura do Banco de Dados

O projeto inclui as seguintes tabelas no MySQL:

### Foi adicionado essas tabelas no mysql, as restrisções fiz no proprio powerbi (relacionamentos)
Esta tabela armazena detalhes sobre as partidas, incluindo informações sobre os times mandantes e visitantes, placares e vencedores.
```sql
CREATE TABLE campeonato_brasileiro (
    id_partida INT PRIMARY KEY,
    rodada INT,
    data DATE,
    hora TIME,
    id_time_mandante INT,
    mandante VARCHAR(50),
    visitante VARCHAR(50),
    vencedor VARCHAR(50),
    arena VARCHAR(100),
    mandante_Placar INT,
    visitante_Placar INT,
    mandante_Estado VARCHAR(50),
    visitante_Estado VARCHAR(50),
    Mandante_Vencedor INT,
    Visitante_Vencedor INT
);

CREATE TABLE data (
    data DATE PRIMARY KEY,
    Mes INT,
    Ano INT
);

CREATE TABLE gols (
    id_partida INT,
    data DATE,
    id_time INT,
    time VARCHAR(25),
    atleta_marcador VARCHAR(100),
    minuto INT,
    tipo_de_gol VARCHAR(50)
);

CREATE TABLE estatisticas (
    id_partida INT,
    data DATE,
    id_time INT,
    time VARCHAR(50),
    chutes INT,
    chutes_no_alvo INT,
    posse_de_bola DECIMAL(5,2),
    passes INT,
    precisao_passes DECIMAL(5,2),
    faltas INT,
    cartao_amarelo INT,
    cartao_vermelho INT,
    impedimentos INT,
    escanteios INT
);

CREATE TABLE clubes (
    id_time INT,
    time VARCHAR(50)
);






