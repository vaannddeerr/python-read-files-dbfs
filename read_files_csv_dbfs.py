from pyspark.sql import functions as F
from spark_dataset import spark_session


spark = spark_session()

print('📖 Lendo arquivos')
df = (spark.read
           .format('excel')
           .option('header','true')
           .option('delimiter',',')
           .option('inferSchema','true')
           .option('treatEmptyValuesAsNulls','true')
           .load('/Volumes/workspace/default/landing/*.xlsx'))

# print('📖 Leitura finalizada com sucesso ✔️')


# print('✍️ Escrevendo dados')
# (df.write
#    .format('delta')
#    .mode('overwrite')
#    .saveAsTable('base_clie_full'))

# print('✔️ Tabela salva com sucesso...')

# 2. Pegamos a primeira linha (que contém os nomes reais: id, codigoEmpresa, etc.)
# O collect()[0] pega a primeira linha como um objeto Row
header_row = df.limit(1).collect()[0]

# 3. Criamos uma lista com os novos nomes das colunas de forma dinâmica
# Percorremos cada coluna e pegamos o valor que está na primeira linha
novos_nomes = [header_row[i] for i in range(len(df.columns))]

# 4. Aplicamos a renomeação em massa usando o select e alias
# O zip pareia o nome antigo (_c0) com o novo (id)
for old_col, new_col in zip(df.columns, novos_nomes):
    df = df.withColumnRenamed(old_col, new_col)

# 5. Agora filtramos para remover essa primeira linha que usamos como nomes
# Usamos a primeira coluna (agora renomeada) para filtrar
primeira_coluna = novos_nomes[0]
df_final = df.filter(df[primeira_coluna] != primeira_coluna)

# 6. Salva o resultado
print("🚀 Salvando tabela com nomes corrigidos dinamicamente...")
df_final.write.format('delta').mode('overwrite').saveAsTable('base_clie_full')

print("✅ Sucesso! Todas as colunas foram renomeadas sem digitação manual.")

