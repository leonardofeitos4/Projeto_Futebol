import mysql.connector
import pandas as pd

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='35661545',
    database='brasileirao'
)

cursor = conexao.cursor()

# Função para formatar datas
def formatar_data(data):
    return pd.to_datetime(data, format='%d/%m/%Y').strftime('%Y-%m-%d')

# Função para extrair a data, mês e ano de uma string de data
def extrair_mes_ano(data_str):
    data = pd.to_datetime(data_str, format='%d/%m/%Y', errors='coerce')
    return data.strftime('%Y-%m-%d'), data.month, data.year

# Desativar autocommit para confirmar as transações manualmente
conexao.autocommit = False

# 1 - Inserir dados na tabela "campeonato_brasileiro"
campeonato_brasileiro_df = pd.read_csv('dados/campeonato_brasileiro.csv', delimiter=';')
campeonato_brasileiro_df['data'] = campeonato_brasileiro_df['data'].apply(formatar_data)

sql_campeonato = """
INSERT INTO campeonato_brasileiro (id_partida, rodada, data, hora, id_time_mandante, mandante, visitante, vencedor, arena, 
mandante_Placar, visitante_Placar, mandante_Estado, visitante_Estado, mandante_vencedor, visitante_vencedor)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in campeonato_brasileiro_df.iterrows():
    cursor.execute(sql_campeonato, (
        row['id_partida'], 
        row['rodada'], 
        row['data'], 
        row['hora'],
        row['id_time_mandante'], 
        row['mandante'], 
        row['visitante'], 
        row['vencedor'], 
        row['arena'], 
        row['mandante_Placar'], 
        row['visitante_Placar'], 
        row['mandante_Estado'], 
        row['visitante_Estado'],
        row['mandante_vencedor'],
        row['visitante_vencedor']
    ))

print("Dados da tabela 'campeonato_brasileiro' inseridos com sucesso.")

# 2 - Inserir dados na tabela "estatisticas"
estatisticas_df = pd.read_csv('dados/estatisticas.csv', delimiter=';')
estatisticas_df['data'] = estatisticas_df['data'].apply(formatar_data)

# Remover símbolo de porcentagem e substituir vírgula por ponto
estatisticas_df['posse_de_bola'] = estatisticas_df['posse_de_bola'].str.replace('%', '').str.replace(',', '.').astype(float)
estatisticas_df['precisao_passes'] = estatisticas_df['precisao_passes'].str.replace('%', '').str.replace(',', '.').astype(float)

sql_estatisticas = """
INSERT INTO estatisticas (id_partida, data, id_time, time, chutes, chutes_no_alvo, posse_de_bola, passes, precisao_passes,
faltas, cartao_amarelo, cartao_vermelho, impedimentos, escanteios)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(sql_estatisticas, [
    (
        row['id_partida'], 
        row['data'], 
        row['id_time'],  
        row['time'],
        row['chutes'], 
        row['chutes_no_alvo'], 
        row['posse_de_bola'], 
        row['passes'], 
        row['precisao_passes'], 
        row['faltas'], 
        row['cartao_amarelo'], 
        row['cartao_vermelho'], 
        row['impedimentos'], 
        row['escanteios']
    ) for _, row in estatisticas_df.iterrows()
])

print("Dados da tabela 'estatisticas' inseridos com sucesso.")

# 3 - Inserir dados na tabela "gols"
gols_df = pd.read_csv('dados/gols.csv', delimiter=';', encoding='latin1')
gols_df['data'] = gols_df['data'].apply(formatar_data)
gols_df['minuto'] = pd.to_numeric(gols_df['minuto'], errors='coerce').fillna(0).astype(int)


sql_gols = """
INSERT INTO gols (id_partida, data, id_time, time, atleta_marcador, minuto, tipo_de_gol, Tempo)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    cursor.executemany(sql_gols, [
        (
            row['id_partida'], 
            row['data'], 
            row['id_time'],
            row['time'], 
            row['atleta_marcador'], 
            row['minuto'], 
            row['tipo_de_gol'],
            row['Tempo'] 
        ) for _, row in gols_df.iterrows()
    ])
    print("Dados da tabela 'gols' inseridos com sucesso.")
except Exception as e:
    print(f"Erro ao inserir dados na tabela 'gols': {e}")




# 4 - Inserir dados na tabela "data"
data_df = pd.read_csv('dados/data.csv', delimiter=';')
data_df[['data', 'mes', 'ano']] = data_df['data'].apply(lambda x: pd.Series(extrair_mes_ano(x)))

sql_data = """
INSERT INTO data (data, mes, ano)
VALUES (%s, %s, %s)
"""

cursor.executemany(sql_data, [
    (
        row['data'],
        row['mes'],
        row['ano']
    ) for _, row in data_df.iterrows()
])

print("Dados da tabela 'data' inseridos com sucesso.")

# 5 - Inserir dados na tabela "clubes"
clube_df = pd.read_csv('dados/Clubes.csv', delimiter=';')

sql_clube = """
INSERT INTO clubes (id_time, time)
VALUES (%s, %s)
"""

cursor.executemany(sql_clube, [
    (
        row['id_time'],
        row['time']
    ) for _, row in clube_df.iterrows()
])

print("Dados da tabela 'clubes' inseridos com sucesso.")

# Confirmar transações
conexao.commit()
print("Todas as transações foram confirmadas.")

# Fechar a conexão
cursor.close()
conexao.close()
print("Conexão encerrada.")


gols_df = pd.read_csv('dados/gols.csv', delimiter=';', encoding='latin1')
print(gols_df.columns)  # Mostra os nomes das coluna
