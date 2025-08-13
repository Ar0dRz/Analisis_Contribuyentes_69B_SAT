import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Nueva import para Seaborn

# Carga el CSV con encoding ajustado para manejar acentos (latin-1 en lugar de utf-8)
df = pd.read_csv('Listado_Completo_69-B.csv', skiprows=2, encoding='latin-1', on_bad_lines='skip')

# Imprime los nombres de las columnas para debug (¡mira aquí para ver el nombre exacto de 'Situación del contribuyente'!)
print("Nombres de columnas en el DataFrame:")
print(df.columns.tolist())

# Convierte la columna 'No' a string para poder usar métodos de texto (evita el error)
df['No'] = df['No'].astype(str)

# Limpia el DataFrame: filtra solo filas donde la columna 'No' sea numérica (para ignorar headers repetidos)
df = df[df['No'].str.isnumeric().fillna(False)]

# Renombra la columna de situación para que sea fácil (ajusta esto basado en el print de arriba)
situacion_col = 'Situación del contribuyente'  # Confirmado por tu output

# Calcula el total de contribuyentes (número de filas válidas)
total_contribuyentes = len(df)

# Cuenta las categorías en la columna de situación (usando value_counts)
categorias = df[situacion_col].value_counts()

# Extrae los counts específicos (ajusta los strings si varían en el archivo completo)
presuntos = categorias.get('Presunto', 0)
definitivos = categorias.get('Definitivo', 0)
desvirtuados = categorias.get('Desvirtuado', 0)  # Asumiendo esto para "desvirtuaron"
otros = total_contribuyentes - (presuntos + definitivos + desvirtuados)  # Por si hay más categorías como Sentencia Favorable

# Imprime los resultados
print(f"Total de contribuyentes: {total_contribuyentes}")
print(f"Presuntos: {presuntos}")
print(f"Definitivos: {definitivos}")
print(f"Desvirtuados: {desvirtuados}")
print(f"Otras categorías (ej. Sentencia Favorable): {otros}")

# Define etiquetas y valores
etiquetas = ['Presuntos', 'Definitivos', 'Desvirtuados', 'Otros']
valores = [presuntos, definitivos, desvirtuados, otros]

# Calcula porcentajes con NumPy
import numpy as np
porcentajes = np.array(valores) / total_contribuyentes * 100
print("Porcentajes:")
for et, por in zip(etiquetas, porcentajes):
    print(f"{et}: {por:.2f}%")

# Pie chart con matplotlib (para porcentajes)
plt.figure(figsize=(8, 6))
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', colors=['blue', 'red', 'green', 'orange'])
plt.title('Porcentajes de Contribuyentes por Situación')
plt.show()

# Bar chart mejorado con Seaborn (más look pro: grid, colores, etc.)
plt.figure(figsize=(8, 6))
sns.set_theme(style="darkgrid")  # Tema chido
sns.barplot(x=etiquetas, y=valores, palette=['blue', 'red', 'green', 'orange'])
plt.title('Distribución de Contribuyentes por Situación (Seaborn)')
plt.xlabel('Categorías')
plt.ylabel('Cantidad')
ax = sns.barplot(x=etiquetas, y=valores, palette=['blue', 'red', 'green', 'orange'])
for i, v in enumerate(valores):
    ax.text(i, v + 100, str(v), ha='center', va='bottom')  # Agrega el número arriba
plt.show()