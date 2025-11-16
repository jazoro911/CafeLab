# Datos de Difracción de Rayos X (DRX) - Muestras de Café

## Descripción General

Este directorio contiene datos de difracción de rayos X (DRX) de diversas muestras de café y materiales de referencia. Los datos han sido limpiados y preprocesados, eliminando parámetros iniciales y metadatos del difractómetro.

## Formato de Datos

Todos los archivos están en formato CSV con tres columnas:
- **Columna 1**: Índice secuencial (0, 1, 2, ...)
- **Angle**: Ángulo de difracción 2θ (grados), típicamente en el rango de ~5° a 60-80°
- **PSD**: Conteos de intensidad del Detector Sensible a Posición

## Descripción de Muestras

### xCafeina.csv
- **Material**: Tabletas de cafeína (no es cafeína pura)
- **Tipo**: Estándar de referencia
- **Notas**: Tabletas comerciales de cafeína usadas como material de referencia cristalino

### xCh.csv
- **Procedencia**: Pantelhó, Chiapas, México
- **Beneficiado**: Lavado
- **Nivel de tueste**: Medio-alto
- **Tipo**: Granos de café procesados

### xIlly.csv
- **Marca**: Illy
- **Tipo**: Café comercial
- **Notas**: Muestra de referencia comercial de la empresa Illy

### xMh.csv
- **Procedencia**: Tancítaro, Michoacán, México
- **Beneficiado**: Natural
- **Nivel de tueste**: Desconocido
- **Tipo**: Granos de café procesados

### xPergamino.csv
- **Material**: Pergamino
- **Tipo**: Capa de pergamino del café
- **Notas**: La cáscara protectora de pergamino que cubre los granos verdes de café (pergamino del grano verde)

### xPh.csv
- **Procedencia**: Pluma Hidalgo, Oaxaca, México
- **Beneficiado**: Desconocido
- **Nivel de tueste**: Desconocido
- **Tipo**: Granos de café procesados

### xSpOb.csv
- **Procedencia**: Chiapas, México
- **Variedad**: Obata
- **Beneficiado**: Lavado
- **Nivel de tueste**: Medio-oscuro
- **Tipo**: Granos de café procesados

### xVerde.csv
- **Material**: Café verde (café oro verde)
- **Procesamiento**: Sin tostar
- **Tipo**: Granos crudos de café verde
- **Notas**: Sin aplicación de tostado, semillas de café crudas

## Propósito del Análisis

El análisis de DRX permite:
- Identificación de estructuras cristalinas vs. amorfas en muestras de café
- Comparación de cambios estructurales debido a procesos de tostado
- Detección de compuestos cristalinos (p. ej., cafeína, trigonelina, ácidos clorogénicos)
- Diferenciación entre métodos de procesamiento (lavado vs. natural)
- Caracterización de la estructura del pergamino

## Procesamiento de Datos

- **Estado**: Datos limpios
- **Preprocesamiento**: Parámetros iniciales del instrumento y metadatos eliminados
- **Formato**: Listos para análisis con Python (pandas, matplotlib), Origin, MATLAB o software cristalográfico

## Notas de Uso

- Las posiciones de los picos pueden usarse para identificar fases cristalinas
- Los valores de intensidad (PSD) indican cristalinidad relativa
- Puede ser necesaria la sustracción de fondo para análisis cuantitativo
- Se recomienda usar patrones de referencia (base de datos ICDD/PDF) para identificación de fases

## Análisis Relacionados

Estos datos son parte del proyecto CafeLab en la FCFM-BUAP, que incluye técnicas espectroscópicas complementarias:
- Espectroscopía de absorbancia
- Espectroscopía de transmitancia
- Espectroscopía de fluorescencia

---

**Proyecto**: CafeLab  
**Institución**: FCFM-BUAP  
**Investigador Principal**: Prof. Martín Rodolfo Palomino Merino  
**Investigadores**: Lizeth Jazmín Orozco García, Julio Alfredo Ballinas García
