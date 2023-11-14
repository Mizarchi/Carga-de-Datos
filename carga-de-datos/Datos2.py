import pandas as pd
import numpy as np

# Datos de ejemplo
data = {
    'Name': ['Persona1', 'Persona2', 'Persona3', 'Persona4'],
    'Age': [25, 30, 22, 35],
    'is_dead': [0, 1, 0, 1],
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Fumador': ['Sí', 'Sí', 'No', 'No']
}

# Convertir el diccionario a un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el DataFrame en dos basado en el valor de 'is_dead'
df_dead = df[df['is_dead'] == 1]
df_alive = df[df['is_dead'] == 0]

# Calcular el promedio de edades para cada dataset
avg_age_dead = np.mean(df_dead['Age'])
avg_age_alive = np.mean(df_alive['Age'])

# Imprimir los resultados
print("Promedio de edades de personas fallecidas: {:.2f}".format(avg_age_dead))
print("Promedio de edades de personas vivas: {:.2f}".format(avg_age_alive))

# Verificar los tipos de datos en cada columna
print("\nTipos de datos en cada columna:")
print(df.dtypes)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
smoking_counts = df.groupby(['Gender', 'Fumador']).size().unstack(fill_value=0)
print("\nCantidad de hombres fumadores vs mujeres fumadoras:")
print(smoking_counts)

