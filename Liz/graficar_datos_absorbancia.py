import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Supongamos que ya tienes cargados todos los DataFrames necesarios
# ACh_copy, AGo_copy, AIlly_copy, AMi_copy, AOx_copy con columnas 'nm' y '15'
# RACh, RAMi, RAGo, RAOx, RAIlly, RAVerde, RAMucilago, RACafeina

# Primero, crear DataFrames con columna 'grupo' para las muestras de 15g
def agregar_grupo_15g(df, grupo_nombre, valor_columna='15'):
    """
    Función para agregar columna de grupo a los datos de 15g
    """
    df_temp = df[['nm', valor_columna]].copy()
    df_temp['grupo'] = grupo_nombre
    # Renombrar la columna de valor para que sea consistente
    df_temp = df_temp.rename(columns={valor_columna: 'value'})
    return df_temp

# Crear los DataFrames con grupos para las muestras de 15g
ACh_15g = agregar_grupo_15g(ACh_copy, 'ACh_15g')
AGo_15g = agregar_grupo_15g(AGo_copy, 'AGo_15g') 
AIlly_15g = agregar_grupo_15g(AIlly_copy, 'AIlly_15g')
AMi_15g = agregar_grupo_15g(AMi_copy, 'AMi_15g')
AOx_15g = agregar_grupo_15g(AOx_copy, 'AOx_15g')

# Preparar los DataFrames de file_abs_acota (asumiendo que tienen las columnas correctas)
def preparar_df_acota(df, columna_valor, grupo_nombre):
    """
    Función para preparar los DataFrames de file_abs_acota
    """
    df_temp = df[['Wavelength', columna_valor]].copy()
    df_temp['grupo'] = grupo_nombre
    df_temp = df_temp.rename(columns={'Wavelength': 'nm', columna_valor: 'value'})
    return df_temp

# Preparar los DataFrames de file_abs_acota
RACh_prep = preparar_df_acota(file_abs_acota, 'Ch', 'rACh')
RAMi_prep = preparar_df_acota(file_abs_acota, 'Mi', 'rAMi')
RAGo_prep = preparar_df_acota(file_abs_acota, 'Go', 'rAGo')
RAOx_prep = preparar_df_acota(file_abs_acota, 'Ox', 'rAOx')
RAIlly_prep = preparar_df_acota(file_abs_acota, 'Illy', 'rAIlly')
RAVerde_prep = preparar_df_acota(file_abs_acota, 'Verde', 'rAVerde')
RAMucilago_prep = preparar_df_acota(file_abs_acota, 'Mucilago', 'rAMucilago')
RACafeina_prep = preparar_df_acota(file_abs_acota, 'Cafeina', 'rACafeina')

# Combinar todos los DataFrames
df_todo = pd.concat([
    ACh_15g, AGo_15g, AIlly_15g, AMi_15g, AOx_15g,
    RACh_prep, RAMi_prep, RAGo_prep, RAOx_prep, 
    RAIlly_prep, RAVerde_prep, RAMucilago_prep, RACafeina_prep
], ignore_index=True)

print(f"DataFrame combinado creado con {df_todo.shape[0]} filas y {df_todo.shape[1]} columnas")
print(f"Grupos únicos: {df_todo['grupo'].unique()}")

# Función para graficar
def plot_absorbancia_con_bandas(df, titulo='Absorbancia de distintas muestras'):
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Obtener grupos únicos
    grupos = df['grupo'].unique()
    
    # Colores para cada grupo
    colors = plt.cm.tab20(np.linspace(0, 1, len(grupos)))
    
    for i, grupo in enumerate(grupos):
        datos_grupo = df[df['grupo'] == grupo]
        if not datos_grupo.empty:
            ax.plot(datos_grupo['nm'], datos_grupo['value'], 
                   label=grupo, color=colors[i], linewidth=1.5)
    
    # Agregar líneas verticales para las bandas
    ax.axvspan(270, 280, alpha=0.2, color='blue', label='Banda 1 (270-280 nm)')
    ax.axvspan(320, 330, alpha=0.2, color='red', label='Banda 2 (320-330 nm)')
    
    ax.set_xlabel('Longitud de Onda (nm)')
    ax.set_ylabel('Absorbancia')
    ax.set_title(titulo)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Graficar todos los datos
plot_absorbancia_con_bandas(df_todo, 'Absorbancia de distintas muestras')
