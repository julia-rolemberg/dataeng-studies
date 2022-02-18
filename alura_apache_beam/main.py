import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText

pipeline_options =  PipelineOptions(argv=None)
pipeline  = beam.Pipeline(options=pipeline_options)

def texto_para_lista(elemento, delimitador='|'):
    """
    Recebe um texto e um delimitador
    Retorna uma lista com cada linha string do txt, dividida pelo delimitador
    """
    return elemento.split(delimitador)


dengue = (
    pipeline
    | "Leitura do dataset de dengue" >> ReadFromText('data/casos_dengue.txt', skip_header_lines=1)
    | "De  texto para lista" >> beam.Map(texto_para_lista)
    | "Mostrar Resultados" >> beam.Map(print)
)

pipeline.run()
