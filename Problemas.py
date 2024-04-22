#Problema 1.1:
import pandas as pd

# Datos de los apartamentos
apartamentos = {
    'Nombre': ['City Hotel', 'Tremont House', 'Ritz Hotel'],
    'Puntuación': [3, 4.2, 4.6],
    'Precio': [200, 370, 400]
}

# Convertir el diccionario en un DataFrame de pandas
data = pd.DataFrame(apartamentos)

# Ordenar los apartamentos por puntuación y luego por precio
sorted_data = data.sort_values(by=['Puntuación', 'Precio'], ascending=[False, True])

# Función para buscar el apartamento más cercano al monto dado
def buscar_apartamento_cercano(monto):
    # Filtrar los apartamentos dentro del rango de precio
    filtered_data = sorted_data[sorted_data['Precio'] <= monto]
    if not filtered_data.empty:
        # Tomar el apartamento más cercano al monto dado
        apartamento_cercano = filtered_data.iloc[0]
        return apartamento_cercano
    else:
        return None

# Preguntar al usuario si tiene un monto aproximado para el departamento
respuesta = input("¿Tiene un monto aproximado para el departamento? (si/no): ")

if respuesta.lower() == 'si':
    # Solicitar al usuario que ingrese el monto
    monto_ingresado = float(input("Por favor ingrese el monto en dólares: "))
    # Buscar el apartamento más cercano al monto ingresado
    apartamento_cercano = buscar_apartamento_cercano(monto_ingresado)
    if apartamento_cercano is not None:
        print("El apartamento más cercano a su monto es:")
        print(apartamento_cercano)
    else:
        print("Lo siento, no hay apartamentos dentro de su presupuesto.")
elif respuesta.lower() == 'no':
    # Mostrar la lista de los tres apartamentos y sus precios
    print("Aquí están las tres opciones disponibles:")
    print(sorted_data)
else:
    print("Respuesta no válida. Por favor, responda 'si' o 'no'.")

#Problema 1.2:
import pandas as pd

# Crear diccionarios con los datos de las propiedades de Roberto y Clara
datos_roberto = {
    'ID': [97503],
    'Críticas Totales': [500],
    'Críticas Positivas': [420],
    'Críticas Negativas': [80]
}

datos_clara = {
    'ID': [90387],
    'Críticas Totales': [210],
    'Críticas Positivas': [150],
    'Críticas Negativas': [60]
}

# Convertir los diccionarios en DataFrames
df_roberto = pd.DataFrame(datos_roberto)
df_clara = pd.DataFrame(datos_clara)

# Concatenar los DataFrames de Roberto y Clara
df_roberto_clara = pd.concat([df_roberto, df_clara])

# Guardar el DataFrame como un archivo Excel
df_roberto_clara.to_excel('roberto.xls', index=False)

# Mostrar el DataFrame
print(df_roberto_clara)


#Problema 1.3:   
import pandas as pd
import random

# Generar datos de las propiedades de los hoteles
datos_hoteles = {
    'Nombre': ['Queen Hotel', 'Hotel El Bosque', 'Tea Tree Hotel', 'Candel Resort', 'EcoTel', 
               'Trufa Blanca Hotel', 'Hotel Cachemir', 'La Cabaña Resort', 'Posada El Manantial', 'Hotel Verano Azul'],
    'Precio': [random.randint(10, 15) for _ in range(10)],
    'Puntuación': [3, 3, 3, 3, 4, 4, 4, 2, 2, 2]
}

# Convertir el diccionario en un DataFrame
df_hoteles = pd.DataFrame(datos_hoteles)

# Filtrar las propiedades dentro del presupuesto de Diana y con room_type == Shared room
propiedades_diana = df_hoteles[df_hoteles['Precio'] <= 50]

# Ordenar las propiedades por precio y puntuación en orden ascendente
propiedades_ordenadas = propiedades_diana.sort_values(by=['Precio', 'Puntuación'], ascending=[True, False])

# Tomar las 10 propiedades más baratas
top_10_propiedades = propiedades_ordenadas.head(10)

# Mostrar las 10 propiedades más baratas para Diana
print("Las 10 propiedades más baratas para Diana en Lisboa:")
print(top_10_propiedades)


#Problema 2: 
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('winemag-data-130k-v2.csv')

# Explorar las primeras filas del DataFrame
print(df.head())

# Renombrar columnas
df.rename(columns={'nombre': 'country', 'name': 'nombre_vino', 'nom': 'variety', 'iso2': 'region', 'iso3': 'province', 'phone_code': 'price', 'continente': 'continent'}, inplace=True)

# Crear nuevas columnas
# Crearemos una columna que indique si el país es productor de vino o no
df['wine_producer'] = df['country'].apply(lambda x: 'Yes' if x in df['country'].unique() else 'No')

# Crearemos una columna para la longitud del nombre del vino
df['nombre_vino_length'] = df['nombre_vino'].apply(len)

# Crearemos una columna para la cantidad de caracteres únicos en el nombre del vino
df['nombre_vino_unique_chars'] = df['nombre_vino'].apply(lambda x: len(set(x)))

# Mostrar las primeras filas del DataFrame con las nuevas columnas
print(df.head())

# Reporte 1: Promedio de puntajes por país
reporte1 = df.groupby('country')['points'].mean().reset_index().sort_values(by='points', ascending=False)

# Reporte 2: Cantidad de vinos por variedad de uva
reporte2 = df['variety'].value_counts().reset_index()
reporte2.columns = ['variety', 'cantidad_vinos']

# Reporte 3: Cantidad de vinos producidos por continente
reporte3 = df.groupby('continent')['country'].count().reset_index()
reporte3.columns = ['continent', 'cantidad_vinos']

# Reporte 4: Precio promedio de vinos por región
reporte4 = df.groupby('region')['price'].mean().reset_index().sort_values(by='price', ascending=False)

# Mostrar los reportes
print("Reporte 1: Promedio de puntajes por país")
print(reporte1.head())

print("\nReporte 2: Cantidad de vinos por variedad de uva")
print(reporte2.head())

print("\nReporte 3: Cantidad de vinos producidos por continente")
print(reporte3)

print("\nReporte 4: Precio promedio de vinos por región")
print(reporte4.head())

# Guardar el Reporte 1 en un archivo CSV
reporte1.to_csv('promedio_puntajes_por_pais.csv', index=False)
print("El reporte ha sido guardado en 'promedio_puntajes_por_pais.csv'")    


#Problema 3:    
import pandas as pd
import requests

def limpieza_datos(df):
    # Renombrar columnas eliminando espacios, tildes y convirtiendo a minúsculas
    df.rename(columns=lambda x: x.strip().lower().replace(' ', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u'), inplace=True)
    
    # Cambiar el nombre de columnas si es necesario
    
    # Eliminar columnas ID y TipoMoneda repetidas
    df = df.loc[:, ~df.columns.duplicated()]
    
    # Eliminar coma de la columna 'DISPOSITIVO LEGAL'
    df['dispositivo_legal'] = df['dispositivo_legal'].str.replace(',', '')
    
    return df

def dolarizar_valores(df):
    # Obtener el valor actual del dólar desde el API de SUNAT
    try:
        response = requests.get('http://api.sunat.cloud/cambio_dolar').json()
        valor_dolar = response['venta']
    except:
        print("Error al obtener el valor del dólar desde el API de SUNAT")
        valor_dolar = None
    
    # Dolarizar montos de inversión y montos de transferencia
    if valor_dolar:
        df['monto_inversion_dolar'] = df['monto_inversion'] / valor_dolar
        df['monto_transferencia_dolar'] = df['monto_transferencia'] / valor_dolar
    
    return df

def transformar_estado(df):
    # Cambiar valores de la columna 'estado'
    df['estado'] = df['estado'].replace({'Actos Previos': 1, 'Resuelto': 0, 'Ejecucion': 2, 'Concluido': 3})
    
    # Crear nueva columna puntaje_estado
    df['puntaje_estado'] = df['estado'].map({'Actos Previos': 1, 'Resuelto': 0, 'Ejecucion': 2, 'Concluido': 3})
    
    return df

# Leer el archivo Excel
df = pd.read_excel('reactiva.xlsx')

# Realizar limpieza de datos
df = limpieza_datos(df)

# Eliminar la columna ID y TipoMoneda repetidas
df = df.drop(['ID', 'TipoMoneda'], axis=1)

# Dolarizar los valores de montos de inversión y montos de transferencia
df = dolarizar_valores(df)

# Transformar la columna Estado
df = transformar_estado(df)

# Guardar el DataFrame procesado en un nuevo archivo Excel
df.to_excel('reactiva_procesada.xlsx', index=False)
