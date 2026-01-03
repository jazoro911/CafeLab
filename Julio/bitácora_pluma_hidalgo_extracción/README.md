# Bitácora - Extracción de Café Pluma Hidalgo

Este directorio contiene la documentación detallada del proceso de extracción realizado con muestras de café de diferentes orígenes mexicanos y colombianos, como parte del proyecto CafeLab.

---

## 📄 Descripción

Esta bitácora documenta el procedimiento experimental de extracción de café para las siguientes muestras:

- 🟢 **Colombia Gourmet**
- 🔵 **Colombia Selecto**
- 🔴 **Pluma Hidalgo** (Oaxaca)
- 🟡 **Pahuatlán** (Puebla)

El documento incluye el protocolo completo de extracción, imágenes del proceso experimental, y observaciones relevantes realizadas durante el trabajo en el Laboratorio de Caracterización de Materiales (FCFM-BUAP).

---

## 📁 Contenido

### Documento Principal
- **`Bitácora_Pluma_Hidalgo.pdf`** (8.1 MB)  
  Documento completo en formato PDF con toda la documentación del proceso de extracción.

- **`Bitácora_Pluma_Hidalgo.tex`** (37 KB)  
  Código fuente LaTeX del documento.

### Imágenes del Proceso
El directorio contiene 13 imágenes (`1.png` a `13.png`) que documentan visualmente cada etapa del proceso de extracción:

- **1.png - 4.png**: Preparación de las muestras
- **5.png - 8.png**: Proceso de extracción
- **9.png - 13.png**: Mediciones y análisis

### Archivos de Soporte LaTeX
- `biblio.bib`: Referencias bibliográficas
- `colores.tex`: Definiciones de colores personalizados
- `LogoFCFMBUAP (1).png`: Logo institucional
- `earthspacex.jpg`: Imagen decorativa

### Archivos Auxiliares
- `*.aux`, `*.log`, `*.out`, `*.toc`: Archivos generados por LaTeX durante la compilación

---

## 🛠️ Compilación del Documento

Para recompilar el documento LaTeX desde el código fuente:

### Requisitos
- **TeX Live** o **MiKTeX**
- **BibLaTeX** con backend `biber`

### Comando de Compilación
```bash
pdflatex Bitácora_Pluma_Hidalgo.tex
biber Bitácora_Pluma_Hidalgo
pdflatex Bitácora_Pluma_Hidalgo.tex
pdflatex Bitácora_Pluma_Hidalgo.tex
```

O usando `latexmk`:
```bash
latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" Bitácora_Pluma_Hidalgo.tex
```

---

## 👥 Equipo de Trabajo

**Responsable del Laboratorio:**  
- Dr. Martín Rodolfo Palomino Merino

**Integrantes del Proyecto:**  
- Lizeth Jazmín Orozco García
- Julio Alfredo Ballinas García

**Colaborador:**  
- Roberto Álvarez Zavala

---

## 📍 Ubicación

**Institución:** Facultad de Ciencias Físico-Matemáticas (FCFM)  
**Universidad:** Benemérita Universidad Autónoma de Puebla (BUAP)  
**Campus:** Ciudad Universitaria BUAP  
**Edificio:** 1FM1  
**Salón:** 301

---

## 📅 Fecha de Trabajo

**15 de octubre de 2025**  
Zona horaria: GMT-6 (Heroica Puebla de Zaragoza, Puebla)

---

## 🔗 Estructura del Documento

El documento incluye:

1. **Portada** con información del laboratorio y equipo
2. **Índice** de contenidos
3. **Introducción** al proceso de extracción
4. **Metodología** detallada paso a paso
5. **Resultados** observados
6. **Imágenes** documentales del proceso
7. **Conclusiones** y observaciones
8. **Referencias bibliográficas**

---

## 📊 Muestras Analizadas

| Muestra | Origen | Color Identificador |
|---------|--------|---------------------|
| Colombia Gourmet | Colombia | Verde (Apple Green) |
| Colombia Selecto | Colombia | Azul (Tarawera) |
| Pluma Hidalgo | Oaxaca, México | Rojo (Cinnabar) |
| Pahuatlán | Puebla, México | Amarillo (Sun) |

---

## 🔬 Laboratorio

**Laboratorio de Caracterización de Materiales**  
FCFM-BUAP

El laboratorio cuenta con equipos especializados para análisis espectroscópico y caracterización fisicoquímica de materiales, incluyendo muestras de café.

---

## 📝 Notas

- Las imágenes están en formato PNG de alta resolución
- El documento utiliza el paquete `tcolorbox` para cajas de color personalizadas
- Se emplean colores específicos para identificar cada muestra
- La bibliografía se gestiona con BibLaTeX/Biber

---

## 🔗 Enlaces Relacionados

- [Directorio principal de Julio](../)
- [Proyecto CafeLab](../../)
- [Fluorescencia de muestras](../Fluorescencia_muestras_café/)
- [Datos de análisis](../DataJulio/)

---

**Última actualización:** 2 de enero de 2026
