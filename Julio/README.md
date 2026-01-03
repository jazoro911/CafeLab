# Julio - Análisis Espectroscópico de Café

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Este directorio contiene los análisis espectroscópicos realizados por **Julio Alfredo Ballinas García** como parte del proyecto CafeLab. El enfoque principal es la caracterización de muestras de café mexicano mediante técnicas de **espectroscopía UV-Vis** (absorbancia y transmitancia) y **fluorescencia**.

---

## 📁 Estructura del Proyecto

```
Julio/
├── main_fluorescencia/              # Análisis principal de fluorescencia
├── main_grafica_tya/                # Gráficas de transmitancia y absorbancia
├── Caffeine_ABS/                    # Análisis de absorbancia de cafeína
├── cafeina_curva_de_calibración/    # Curva de calibración para cafeína
├── Fluorescencia_muestras_café/     # Datos de fluorescencia por muestra
├── DataJulio/                       # Datos de absorbancia/transmitancia
├── Datos_VeMN/                      # Datos de muestra Veracruz MN
├── Colombia_Michoacán_Pahuatlán_PlumaHidalgo_EspírituCafe/  # Muestras de diferentes orígenes
├── graficastya_uvvis_cafe_lab/      # Gráficas UV-Vis (T & A)
├── Bitácora_Espectrómetro_VeMN/     # Documentación del espectrómetro
└── bitácora_pluma_hidalgo_extracción/  # Bitácora de extracción
```

---

## 🔬 Análisis Principales

### 1. **Fluorescencia** (`main_fluorescencia/`)
Análisis espectroscópico de fluorescencia de muestras de café de diferentes estados mexicanos.

**Muestras analizadas:**
- FCh (Chiapas)
- FGo (Guerrero)
- FMi (Michoacán)
- FOx (Oaxaca)
- FIlly (Illy caffè - referencia)
- FCaffeine (Cafeína pura)
- FVerde (Café verde)
- FMucilago (Mucílago)

**Archivos principales:**
- `main_fluorescencia.ipynb` / `main_fluorescencia.py`: Script principal de análisis
- `*_data.csv`: Datos de fluorescencia (nm, CPS)

**Regiones espectrales analizadas:**
- 300–400 nm
- 400–500 nm
- 500–600 nm
- 600–700 nm
- 700–800 nm
- 800–900 nm

**Métricas calculadas:**
- Valor máximo y mínimo de CPS
- Promedio y desviación estándar
- Área bajo la curva (AUC)
- Longitud de onda de máxima/mínima intensidad (λmax, λmin)
- Promedios por región espectral

---

### 2. **Absorbancia y Transmitancia** (`main_grafica_tya/`)
Visualización y análisis de espectros UV-Vis para caracterización comparativa.

**Muestras:**
- Chiapas (ChMN)
- Guerrero (GoMG)
- Michoacán (MiMG)
- Oaxaca (OxMM)
- Veracruz (VeMN)
- Illy (referencia)

**Archivos:**
- `graficatya_matrix.ipynb`: Análisis de matrices de absorbancia/transmitancia
- `*_matrix.csv`: Datos procesados en formato de matriz
- `Reporte_Cafe_UVVis.html`: Reporte interactivo con gráficas

---

### 3. **Curva de Calibración de Cafeína** (`cafeina_curva_de_calibración/`)
Mediciones espectroscópicas para generar una curva de calibración de cafeína.

**Concentraciones medidas:**
- 1 ml, 2 ml, 4 ml, 6 ml, 8 ml

**Archivos:**
- `*ml_limpio.csv`: Datos limpios de cada concentración
- `*ml.csv`: Datos originales

---

### 4. **Datos Regionales** (`Datos_VeMN/`, `DataJulio/`)
Datos espectroscópicos organizados por origen geográfico y concentración.

**Estructura:**
- `VeMN7_5g/`, `VeMN15g/`, `VeMN18g/`, `VeMN22_5g/`: Concentraciones de Veracruz
- `Illycaffè/`: Muestra de referencia comercial

---

## 🛠️ Requisitos

### Dependencias Python
```bash
pip install pandas numpy matplotlib plotly jupyter scipy
```

### Librerías principales
- `pandas`: Manipulación de datos
- `numpy`: Cálculos numéricos y métricas
- `plotly`: Visualización interactiva
- `matplotlib`: Gráficos estáticos
- `scipy`: Análisis científico (integración, AUC)

---

## 🚀 Uso

### Ejecutar análisis de fluorescencia
```bash
cd main_fluorescencia/
jupyter lab main_fluorescencia.ipynb
```

O ejecutar como script Python:
```bash
python main_fluorescencia.py
```

### Generar reportes UV-Vis
```bash
cd main_grafica_tya/
jupyter lab graficatya_matrix.ipynb
```

---

## 📊 Formato de Datos

### Fluorescencia (`*_data.csv`)
```csv
nm,CPS
300.0,1234.56
301.0,1245.78
...
```

### Absorbancia/Transmitancia (`*_matrix.csv`)
```csv
wavelength,sample1,sample2,...
200,0.123,0.456,...
201,0.125,0.458,...
...
```

---

## 📝 Documentación Adicional

- **Bitácora del Espectrómetro**: `Bitácora_Espectrómetro_VeMN/`
- **Documentación LaTeX**: Informes técnicos en formato PDF
- **READMEs específicos**: Cada subdirectorio contiene documentación detallada

---

## 👥 Autor

**Julio Alfredo Ballinas García**  
Colaborador del proyecto CafeLab  
FCFM-BUAP

---

## 📧 Contacto

Para consultas sobre este análisis, contactar a través del repositorio del proyecto CafeLab.

---

## 📄 Licencia

Este proyecto forma parte de una investigación académica en FCFM-BUAP.

---

## 🔗 Enlaces Relacionados

- [Proyecto CafeLab Principal](../README.md)
- [Análisis de Liz](../Liz/)

---

**Última actualización:** 2 de enero de 2026
