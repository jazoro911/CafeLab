# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

CafeLab is a scientific research project focused on characterizing coffee samples from various Mexican states (Veracruz, Puebla, Guerrero, Chiapas, and Oaxaca) using spectroscopic techniques including absorbance, transmittance, and fluorescence spectroscopy. The project is led by Professor Martín Rodolfo Palomino Merino at FCFM-BUAP, with Lizeth Jazmín Orozco García as the principal researcher and Julio Alfredo Ballinas García as a collaborator.

## Project Structure

The repository is organized into researcher-specific directories:

- **`Liz/`**: Contains absorbance and reflectance analysis code and Origin projects
- **`Julio/`**: Contains comprehensive spectroscopic analysis including:
  - Fluorescence analysis workflows
  - Caffeine absorption studies
  - Veracruz sample data analysis
  - LaTeX documentation
- **`Data2/`**: CSV files containing spectroscopic measurements with wavelength (nm) and various concentration data
- **Root**: Main README and project coordination files

## Common Development Commands

### Python Environment
```bash
# The project uses standard scientific Python libraries
python -m pip install pandas numpy matplotlib seaborn scipy plotly jupyter
```

### Running Jupyter Notebooks
```bash
# Start Jupyter Lab for interactive analysis
jupyter lab

# Convert notebook to Python script (some files use jupytext)
jupyter nbconvert --to script notebook_name.ipynb
```

### Data Analysis Scripts
```bash
# Run fluorescence analysis (from Julio/main_fluorescencia/)
cd Julio/main_fluorescencia/
python main_fluorescencia.py

# Run absorbance data plotting (from Liz/)
cd Liz/
python graficar_datos_absorbancia.py
```

### LaTeX Documentation
```bash
# Compile spectrometer documentation (from Julio/Bitácora_Espectrómetro_VeMN/)
cd "Julio/Bitácora_Espectrómetro_VeMN/Bitácora_Espectrómetro_VeMN/"
pdflatex Espectrómetro.tex
```

## Code Architecture

### Data Processing Pipeline
1. **Raw Data**: Spectroscopic measurements stored as CSV/TXT files with wavelength and intensity columns
2. **Data Cleaning**: Pandas-based preprocessing to handle NaN values and convert data types
3. **Analysis**: Statistical calculations including AUC, wavelength maxima/minima, and regional averages
4. **Visualization**: Matplotlib and Plotly for static and interactive spectral plots

### Key Analysis Components
- **Spectral Regions**: Defined wavelength bands (300-400nm, 400-500nm, etc.) for regional analysis
- **Metrics Calculation**: Maximum/minimum values, mean, standard deviation, area under curve (AUC)
- **Sample Comparison**: Multi-curve plotting for comparative analysis across different coffee samples

### File Naming Conventions
- **A** prefix: Absorbance measurements (e.g., AChMG.csv for Chiapas samples)
- **T** prefix: Transmittance measurements (e.g., TChMG.csv)
- **F** prefix: Fluorescence analysis notebooks and data
- Sample codes: Ch (Chiapas), Go (Guerrero), Mi (Michoacán), Ox (Oaxaca), Illy (Illy brand)
- Concentration suffixes: Numbers indicate sample concentrations/weights (15g, 18g, etc.)

### Core Analysis Functions
- `leer_fluo()`: Standardized function for reading and cleaning fluorescence data
- `plot_absorbancia_con_bandas()`: Specialized plotting function with spectral band highlighting
- `preparar_df_acota()`: Data preparation for comparative analysis
- Regional averaging functions for different spectral windows

### Data Visualization Standards
- Interactive plots use Plotly with consistent color schemes
- Static plots use Matplotlib with scientific formatting
- Spectral band highlighting for regions of interest (270-280nm, 320-330nm)
- Multi-sample overlay plots for comparative analysis

## Spectroscopic Analysis Workflow

1. **Data Import**: Load CSV files with wavelength (nm) and intensity columns
2. **Preprocessing**: Clean data, handle NaN values, ensure proper data types
3. **Feature Extraction**: Calculate key spectroscopic metrics (λmax, AUC, regional averages)
4. **Comparative Analysis**: Overlay multiple samples for pattern identification
5. **Report Generation**: Create HTML reports with tables and visualizations

## Development Notes

- The project uses both Jupyter notebooks (.ipynb) and converted Python scripts (.py)
- Some notebooks use jupytext for version control-friendly Python representations
- Data files are organized by researcher and analysis type
- LaTeX documentation provides detailed experimental procedures and results
- Interactive visualizations are preferred for exploratory analysis
- Statistical analysis focuses on spectral feature comparison between coffee origins
