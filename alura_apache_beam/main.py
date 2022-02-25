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

def chave_uf_ano_mes_de_lista(elemento):
    """
    Recebe uma lista de elementos
    Retorna uma tupla contendo uma chave e o valor de chuva em mm 
    ('UF-ANO-MES', 1.3)
    
    """
    data, mm, uf = elemento
    ano_mes = '-'.join(data.split('-')[:2])
    chave = f'{uf}-{ano_mes}'
    if float(mm)< 0:
        mm = 0.0
    else:   
        mm = float(mm)
    return chave, mm

def arredonda(elemento):
    """
    Recebe uma tupla 
    Retorna uma tupla com o valor arredondado
    """
    chave, mm = elemento
    return (chave, round(mm, 1))

def filtra_campos_vazios(elemento):
    """
    Remove elementos que tenham chaves vazias
    Recebe uma tupla  com campos vazios e retorna uma tupla sem campos vazios

    """
    chave, dados = elemento
    if all([
        dados['chuvas'],
        dados['dengue']
    ]):
        return True
    return  False
print("Casos de dengue")

dengue = (
    pipeline
    | "Leitura do dataset de dengue" >> ReadFromText('data/sample_casos_dengue.txt', skip_header_lines=1)
    | "De  texto para lista" >> beam.Map(texto_para_lista)
    | "De lista para dicionário" >> beam.Map(lista_para_dict, colunas_dengue)
    | "Criar campo ano_mes" >> beam.Map(trata_data)
    | "Criar chave pelo estado" >> beam.Map(chave_uf)
    | "Agrupar pelo estado" >> beam.GroupByKey()
    | "Descompactar casos  de dengue" >> beam.FlatMap(casos_dengue)
    | "Somar dos  casos pela chave" >> beam.CombinePerKey(sum)
    # | "Mostrar Resultados" >> beam.Map(print)   
)
print("Chuva")
chuvas = (
    pipeline
    | "Leitura do dataset de chuvas" >> ReadFromText('data/sample_chuvas.csv', skip_header_lines=1)
    | "De  texto para lista(chuvas)" >> beam.Map(texto_para_lista, delimitador=',')
    | "Criando a chave UF-ANO-MES" >> beam.Map(chave_uf_ano_mes_de_lista)
    | "Soma do total de chuvas pela chave" >> beam.CombinePerKey(sum)
    | "Arredondar resultados de chuvas" >> beam.Map(arredonda)
    # |  "Mostrar Resultados de chuvas" >> beam.Map(print)  
)

resultado = (
    # (chuvas,dengue)
    # | "Empilha as pcols" >> beam.Flatten()
    # | "Agrupa as pcols" >> beam.GroupByKey()
    ({"chuvas": chuvas, "dengue":  dengue})
    | "Mesclar pcols" >> beam.CoGroupByKey()
    | "Filtrar dados vazios" >> beam.Filter(filtra_campos_vazios)
    |  "Mostrar Resultados da uniao" >> beam.Map(print)  

)

pipeline.run()
