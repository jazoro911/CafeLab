# CORRECCIÓN PARA TU NOTEBOOK
# En lugar de la línea problemática que tenías, usa esto:

# Primero, crear DataFrames preparados para las muestras de 15g
ACh_15g = ACh_copy[['nm','15']].copy()
ACh_15g['grupo'] = 'ACh_15g'
ACh_15g = ACh_15g.rename(columns={'15': 'value'})

AGo_15g = AGo_copy[['nm','15']].copy()
AGo_15g['grupo'] = 'AGo_15g'
AGo_15g = AGo_15g.rename(columns={'15': 'value'})

AIlly_15g = AIlly_copy[['nm','15']].copy()
AIlly_15g['grupo'] = 'AIlly_15g'
AIlly_15g = AIlly_15g.rename(columns={'15': 'value'})

AMi_15g = AMi_copy[['nm','15']].copy()
AMi_15g['grupo'] = 'AMi_15g'
AMi_15g = AMi_15g.rename(columns={'15': 'value'})

AOx_15g = AOx_copy[['nm','15']].copy()
AOx_15g['grupo'] = 'AOx_15g'
AOx_15g = AOx_15g.rename(columns={'15': 'value'})

# Preparar los DataFrames de file_abs_acota con columnas consistentes
RACh_prep = file_abs_acota[['Wavelength', 'Ch']].copy()
RACh_prep['grupo'] = 'rACh'
RACh_prep = RACh_prep.rename(columns={'Wavelength': 'nm', 'Ch': 'value'})

RAMi_prep = file_abs_acota[['Wavelength', 'Mi']].copy()
RAMi_prep['grupo'] = 'rAMi'
RAMi_prep = RAMi_prep.rename(columns={'Wavelength': 'nm', 'Mi': 'value'})

RAGo_prep = file_abs_acota[['Wavelength', 'Go']].copy()
RAGo_prep['grupo'] = 'rAGo'
RAGo_prep = RAGo_prep.rename(columns={'Wavelength': 'nm', 'Go': 'value'})

RAOx_prep = file_abs_acota[['Wavelength', 'Ox']].copy()
RAOx_prep['grupo'] = 'rAOx'
RAOx_prep = RAOx_prep.rename(columns={'Wavelength': 'nm', 'Ox': 'value'})

RAIlly_prep = file_abs_acota[['Wavelength', 'Illy']].copy()
RAIlly_prep['grupo'] = 'rAIlly'
RAIlly_prep = RAIlly_prep.rename(columns={'Wavelength': 'nm', 'Illy': 'value'})

RAVerde_prep = file_abs_acota[['Wavelength', 'Verde']].copy()
RAVerde_prep['grupo'] = 'rAVerde'
RAVerde_prep = RAVerde_prep.rename(columns={'Wavelength': 'nm', 'Verde': 'value'})

RAMucilago_prep = file_abs_acota[['Wavelength', 'Mucilago']].copy()
RAMucilago_prep['grupo'] = 'rAMucilago'
RAMucilago_prep = RAMucilago_prep.rename(columns={'Wavelength': 'nm', 'Mucilago': 'value'})

RACafeina_prep = file_abs_acota[['Wavelength', 'Cafeina']].copy()
RACafeina_prep['grupo'] = 'rACafeina'
RACafeina_prep = RACafeina_prep.rename(columns={'Wavelength': 'nm', 'Cafeina': 'value'})

# AHORA SÍ, COMBINAR TODOS LOS DATAFRAMES CORRECTAMENTE:
df_todo = pd.concat([
    ACh_15g, AGo_15g, AIlly_15g, AMi_15g, AOx_15g,
    RACh_prep, RAMi_prep, RAGo_prep, RAOx_prep, 
    RAIlly_prep, RAVerde_prep, RAMucilago_prep, RACafeina_prep
], ignore_index=True)

print(f"DataFrame combinado creado con {df_todo.shape[0]} filas y {df_todo.shape[1]} columnas")
print(f"Grupos únicos: {df_todo['grupo'].unique()}")

# Verificar que no hay valores NaN
print(f"Valores NaN: {df_todo.isnull().sum().sum()}")

# Función para graficar (puedes usar la función que ya tienes)
def plot_absorbancia_con_bandas(df, titulo):
    fig, ax = plt.subplots(figsize=(14, 8))
    
    grupos = df['grupo'].unique()
    colors = plt.cm.tab20(np.linspace(0, 1, len(grupos)))
    
    for i, grupo in enumerate(grupos):
        datos_grupo = df[df['grupo'] == grupo]
        if not datos_grupo.empty:
            ax.plot(datos_grupo['nm'], datos_grupo['value'], 
                   label=grupo, color=colors[i], linewidth=1.5)
    
    # Bandas
    ax.axvspan(270, 280, alpha=0.2, color='blue', label='Banda 1 (270-280 nm)')
    ax.axvspan(320, 330, alpha=0.2, color='red', label='Banda 2 (320-330 nm)')
    
    ax.set_xlabel('Longitud de Onda (nm)')
    ax.set_ylabel('Absorbancia')
    ax.set_title(titulo)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Graficar
plot_absorbancia_con_bandas(df_todo, 'Absorbancia de distintas muestras')
