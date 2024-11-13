import pandas as pd
import matplotlib.pyplot as plt

archivo_original = '/media/manuela/Mis archivos/ProyectoU24/Datos/rips_mental_total2022.2024-1.csv'
archivo_convertido = '/media/manuela/Mis archivos/ProyectoU24/Datos/rips_mental_total2022.2024-1_utf8.csv'

with open(archivo_original, 'r', encoding='ISO-8859-1') as f_original:
    with open(archivo_convertido, 'w', encoding='utf-8') as f_convertido:
        for linea in f_original:
            f_convertido.write(linea)

print(f"Archivo convertido a UTF-8 y guardado en: {archivo_convertido}")

df = pd.read_csv(archivo_convertido, encoding='utf-8', sep=';')
df['Categoria'] = df['Categoria'].replace('Trastornos del Sue¤o-Vigilia', 'Trastornos del sueño - vigilia')
df['Categoria'] = df['Categoria'].replace('Trastornos del Estado de Animo','Trastornos del estado de ánimo')
print('El conteo de valores nulos por columna es:')
null_counts = df.isnull().sum()
print(null_counts)

total_registros = len(df)
print(f"El dataset tiene {total_registros} registros.")

df1 = df.dropna()
total_registros = len(df1)
print(f"El dataset después de eliminar nulos tiene {total_registros} registros.")
df['Categoria'] = df['Categoria'].replace('Trastornos del Sue¤o-Vigilia', 'Trastornos del sueño - vigilia')
df['Categoria'] = df['Categoria'].replace('Trastornos del Estado de Animo','Trastornos del estado de nimo')

category_counts = df1['Categoria'].value_counts().nlargest(5)

plt.figure(figsize=(16, 8))  # Tamaño de la figura (ancho, alto)

category_counts.plot(kind='bar', color='skyblue')

plt.ylim(0, category_counts.max() * 1.1)

plt.title('Principales causas de atención en servicios de salud mental', fontsize=16)
plt.xlabel('Tipo de morbilidad', fontsize=14)
plt.ylabel('Cantidad de casos', fontsize=14)

plt.xticks(rotation=0, ha='center', fontsize=12)  # Rotación y ajuste de texto para mejor visibilidad

plt.tight_layout()
plt.savefig('/media/manuela/Mis archivos/ProyectoU24/Codigo/migrafica.png', dpi=300, bbox_inches='tight')

plt.show()

