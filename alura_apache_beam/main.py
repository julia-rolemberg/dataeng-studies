import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText
import re
pipeline_options =  PipelineOptions(argv=None)
pipeline  = beam.Pipeline(options=pipeline_options)
colunas_dengue = ["id","data_iniSE","casos","ibge_code","cidade","uf","cep","latitude","longitude"]

def texto_para_lista(elemento, delimitador='|'):
    """
    Recebe um texto e um delimitador
    Retorna uma lista com cada linha string do txt, dividida pelo delimitador
    """
    return elemento.split(delimitador)

def lista_para_dict(elemento, colunas):
    """
    Recebe 2 listas
    Retorna um dicionário
    """
    return dict(zip(colunas, elemento))

def trata_data(elemento):
    """
    Recebe um dicionário e cria um novo campo com ANO-MES
    Retorna o mesmo dicionário com o novo campo
    """
    elemento['ano_mes'] = '-'.join(elemento['data_iniSE'].split('-')[:2])
    return elemento

def chave_uf(elemento):
    """
    Recebe um dicionário
    Retorna uma tupla(UF, dicionário)
    """
    chave = elemento['uf']
    return (chave, elemento)

def casos_dengue(elemento):
    """
    Recebe uma tupla('RS', [{},{}])
    Retorna  uma tupla ('RS-2014-12', 8.0)
    """
    uf,registros = elemento
    for registro in registros:
        if bool(re.search(r'\d', registro['casos'])):
            yield (f"{uf}-{registro['ano_mes']}", float(registro['casos'])) # retorna todos os elementos
        else:
            yield (f"{uf}-{registro['ano_mes']}", 0.0) # retorna todos os elementos



# dengue = (
#     pipeline
#     | "Leitura do dataset de dengue" >> ReadFromText('data/casos_dengue.txt', skip_header_lines=1)
#     | "De  texto para lista" >> beam.Map(texto_para_lista)
#     | "De lista para dicionário" >> beam.Map(lista_para_dict, colunas_dengue)
#     | "Criar campo ano_mes" >> beam.Map(trata_data)
#     | "Criar chave pelo estado" >> beam.Map(chave_uf)
#     | "Agrupar pelo estado" >> beam.GroupByKey()
#     | "Descompactar casos  de dengue" >> beam.FlatMap(casos_dengue)
#     | "Somar dos  casos pela chave" >> beam.CombinePerKey(sum)
#     # | "Mostrar Resultados" >> beam.Map(print)   
# )
chuvas = (
    pipeline
    | "Leitura do dataset de chuvas" >> ReadFromText('data/chuvas.csv', skip_header_lines=1)
    | "De  texto para lista(chuvas)" >> beam.Map(texto_para_lista, delimitador=',')
    | "Mostrar Resultados de chuvas" >> beam.Map(print)  
)

pipeline.run()
