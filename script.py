
from pandas import read_csv, concat

PATH = 'data/'
NAME_PATTERN_FILE = 'MICRODADOS_CADASTRO_CURSOS_'

def read_file_csv_microdata(year: str):

	file = read_csv(PATH + NAME_PATTERN_FILE + year + '.csv', sep = ';', encoding = 'ISO-8859-1')

	file = file.filter(
		[
			'NU_ANO_CENSO', 'NO_REGIAO', 'NO_UF', 'NO_MUNICIPIO', # ano e localização geográfica
			'TP_ORGANIZACAO_ACADEMICA', 'TP_CATEGORIA_ADMINISTRATIVA', 'TP_REDE' # tipo (pública ou privada)
			'CO_IES', # identificação
			'NO_CINE_ROTULO', 'NO_CINE_AREA_GERAL', 'NO_CINE_AREA_ESPECIFICA', 'CO_CINE_AREA_DETALHADA' # identificação do curso
			'QT_CURSO', 'QT_INSCRITO_TOTAL', 'QT_VG_TOTAL', 'QT_ING', 'QT_ING_FEM', 'QT_ING_MASC', 'QT_ING_ENEM' # sexo
			'QT_ING_0_17', 'QT_ING_18_24', 'QT_ING_25_29', 'QT_ING_30_34', 'QT_ING_35_39', 'QT_ING_40_49', 'QT_ING_50_59', 'QT_ING_60_MAIS', # faixa etária
			'QT_ING_BRANCA', 'QT_ING_PRETA', 'QT_ING_PARDA', 'QT_ING_AMARELA', 'QT_ING_INDIGENA', 'QT_ING_CORND', # cor ou raça
			'QT_CONC', 'QT_CONC_FEM', 'QT_CONC_PRETA', 'QT_CONC_PARDA', 'QT_CONC_INDIGENA' # concluintes
		]
	)

	return file

DB = []

for i in ['2010', '2012', '2016', '2020']:

	print('lendo arquivo referente a ' + i)

	DB.append(read_file_csv_microdata(year = i))

DB = concat(DB)

print('exportando...')

DB.to_csv('2010_2020_microdata_inep_censo_superior.csv', sep = ';', index = False, encoding = 'utf-8-sig')

print('tudo pronto!')
