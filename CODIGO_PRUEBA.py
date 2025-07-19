import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo
sns.set(style="whitegrid")

# Parámetros de las distribuciones
distribuciones = [
    {"media": 0, "desviacion": 1, "n": 1000, "label": "N(0, 1)"},
    {"media": 5, "desviacion": 2, "n": 1000, "label": "N(5, 2)"},
    {"media": -3, "desviacion": 1.5, "n": 1000, "label": "N(-3, 1.5)"},
]

# Crear figura compuesta
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

# Histograma comparativo
for dist in distribuciones:
    datos = np.random.normal(dist["media"], dist["desviacion"], dist["n"])
    axs[0].hist(datos, bins=30, alpha=0.6, label=dist["label"], edgecolor='black')

axs[0].set_title("Histogramas Comparativos")
axs[0].set_xlabel("Valor")
axs[0].set_ylabel("Frecuencia")
axs[0].legend()

# Curvas de densidad
for dist in distribuciones:
    datos = np.random.normal(dist["media"], dist["desviacion"], dist["n"])
    sns.kdeplot(datos, ax=axs[1], label=dist["label"], fill=True)

axs[1].set_title("Curvas de Densidad")
axs[1].set_xlabel("Valor")
axs[1].set_ylabel("Densidad")
axs[1].legend()

# Boxplot
datos_boxplot = []
etiquetas = []
for dist in distribuciones:
    datos = np.random.normal(dist["media"], dist["desviacion"], dist["n"])
    datos_boxplot.append(datos)
    etiquetas.append(dist["label"])

axs[2].boxplot(datos_boxplot, labels=etiquetas)
axs[2].set_title("Boxplot de Distribuciones")
axs[2].set_ylabel("Valor")

# Estadísticas descriptivas
axs[3].axis('off')
texto = "Estadísticas Descriptivas:\n\n"
for dist in distribuciones:
    datos = np.random.normal(dist["media"], dist["desviacion"], dist["n"])
    texto += f"{dist['label']}:\n"
    texto += f"  Media: {np.mean(datos):.2f}\n"
    texto += f"  Desviación estándar: {np.std(datos):.2f}\n"
    texto += f"  Mínimo: {np.min(datos):.2f}\n"
    texto += f"  Máximo: {np.max(datos):.2f}\n\n"

axs[3].text(0, 0.5, texto, fontsize=12, va='center')

# Ajustar diseño y mostrar
plt.tight_layout()
plt.savefig("distribuciones_normales.png")
plt.show()

