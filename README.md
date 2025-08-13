# Análisis de Contribuyentes 69-B (SAT México)

¡Hola! Este script en Python analiza el archivo CSV "Listado_Completo_69-B.csv" del SAT, contando categorías de contribuyentes (Presuntos, Definitivos, Desvirtuados y Otros) y generando gráficos con Seaborn y Matplotlib. Basado en datos hasta junio 2025, calcula totales, porcentajes y visualizaciones. Es ideal obtener visualización rápida sobre operaciones presuntamente inexistentes.

## Requisitos
- **Python 3.8+** (recomendado 3.10).
- **Librerías**: pandas, matplotlib, seaborn, numpy.
- **Archivo de datos**: Descarga "Listado_Completo_69-B.csv" del portal del SAT (https://www.gob.mx/sat) y ponlo en la misma carpeta que el script.
- **Entorno**: Usa Conda (como Anaconda/Miniconda) para manejar paquetes fácilmente. Si no lo tienes, descarga de anaconda.com.

## Instalación
1. **Crea y activa un entorno Conda** (para evitar conflictos):
   ```
   conda create -n mi_entorno python=3.10
   conda activate mi_entorno
   ```

2. **Instala las librerías necesarias**:
   ```
   conda install pandas matplotlib seaborn numpy
   ```

3. **Descarga el script**: Copia el código de `analisis_69b.py` (del repo o de esta guía) y guárdalo en una carpeta (ej. "69B_CFF").

## Uso
1. **Coloca el CSV**: Asegúrate de que "Listado_Completo_69-B.csv" esté en la misma carpeta que `analisis_69b.py`.

2. **Ejecuta el script**:
   - Abre una terminal en la carpeta y corre:
     ```
     python analisis_69b.py
     ```

3. **Qué verás**:
   - Prints en la terminal: Total de contribuyentes, cantidad por categoría y porcentajes.
   - Dos gráficos: Uno con porcentajes y uno de barras (se abren en ventanas).
   - Ejemplo de output:
     ```
     Total de contribuyentes: 13451
     Presuntos: 519
     Definitivos: 10994
     Desvirtuados: 338
     Otras categorías (ej. Sentencia Favorable): 1600
     Porcentajes:
     Presuntos: 3.86%
     Definitivos: 81.73%
     Desvirtuados: 2.51%
     Otros: 11.90%
     ```

## Código del Script (analisis_69b.py)
Copia y pega esto en un archivo `.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carga el CSV con encoding ajustado
df = pd.read_csv('Listado_Completo_69-B.csv', skiprows=2, encoding='latin-1', on_bad_lines='skip')

# Debug: Imprime columnas
print("Nombres de columnas en el DataFrame:")
print(df.columns.tolist())

# Convierte 'No' a string
df['No'] = df['No'].astype(str)

# Filtra filas válidas
df = df[df['No'].str.isnumeric().fillna(False)]

# Columna de situación
situacion_col = 'Situación del contribuyente'

# Calcula totals y counts
total_contribuyentes = len(df)
categorias = df[situacion_col].value_counts()
presuntos = categorias.get('Presunto', 0)
definitivos = categorias.get('Definitivo', 0)
desvirtuados = categorias.get('Desvirtuado', 0)
otros = total_contribuyentes - (presuntos + definitivos + desvirtuados)

# Imprime resultados
print(f"Total de contribuyentes: {total_contribuyentes}")
print(f"Presuntos: {presuntos}")
print(f"Definitivos: {definitivos}")
print(f"Desvirtuados: {desvirtuados}")
print(f"Otras categorías (ej. Sentencia Favorable): {otros}")

# Etiquetas y valores
etiquetas = ['Presuntos', 'Definitivos', 'Desvirtuados', 'Otros']
valores = [presuntos, definitivos, desvirtuados, otros]

# Porcentajes
porcentajes = np.array(valores) / total_contribuyentes * 100
print("Porcentajes:")
for et, por in zip(etiquetas, porcentajes):
    print(f"{et}: {por:.2f}%")

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', colors=['blue', 'red', 'green', 'orange'])
plt.title('Porcentajes de Contribuyentes por Situación')
plt.show()

# Bar chart con Seaborn
plt.figure(figsize=(8, 6))
sns.set_theme(style="darkgrid")
ax = sns.barplot(x=etiquetas, y=valores, palette=['blue', 'red', 'green', 'orange'])
for i, v in enumerate(valores):
    ax.text(i, v + 100, str(v), ha='center', va='bottom')
plt.title('Distribución de Contribuyentes por Situación (Seaborn)')
plt.xlabel('Categorías')
plt.ylabel('Cantidad')
plt.show()
```

## Notas y Tips
- **Problemas comunes**:
  - **Encoding error**: Si falla al leer el CSV, prueba `encoding='cp1252'` en lugar de `'latin-1'`.
  - **Columna no encontrada**: Revisa el print de columnas y ajusta `situacion_col` si el nombre varía.
  - **Gráficos no se muestran**: Asegúrate de que no estés en un entorno headless (ej. server); corre en local.
- **Personaliza**: Agrega filtros (ej. por fecha) editando el código. Ejemplo: `df_filtrado = df[df['Publicación DOF definitivos'].str.contains('202[1-9]', na=False)]`.
- **Actualizaciones**: El CSV es público del SAT; descarga la versión más reciente si necesitas datos recientes.
- **Créditos**: Basado en análisis de datos abiertos. 

¡Prueba! Si necesitas más features, fork el repo y contribuye. 
