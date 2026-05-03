# Python GIS and Containerization

**Student:** Elham Alavy
**Course:** GIST 604B – Open Source GIS
**Module:** Module 3 – Python GIS & Containerization
**University of Arizona**

## Project Description
This repository contains Python-based GIS work completed as part of Module 3, covering tabular, vector, and raster data analysis using pandas, GeoPandas, and Rasterio. I developed and tested Python functions in Jupyter Notebooks, implemented them in standalone scripts, and completed a full remote sensing workflow using satellite imagery. All work was done inside a containerized GitHub Codespaces environment.

## Tools and Technologies
- Python (pandas, GeoPandas, Rasterio)
- Jupyter Notebooks
- pytest
- GitHub Codespaces / Docker (devcontainer)
- STAC API / Cloud-Optimized GeoTIFFs (COGs)

## What I Did
- Completed pandas notebooks to load, filter, summarize, and join tabular environmental datasets, and implemented the functions in `src/pandas_basics.py`
- Completed GeoPandas notebooks covering CRS transformations, geometry operations, spatial joins, and overlay analysis, and implemented the functions in `src/geopandas_basics.py`
- Validated all pandas and GeoPandas implementations using `pytest`
- Completed the Rasterio remote sensing workflow notebook, including NDVI calculation, raster masking with vector geometries, and time series analysis
- Committed work regularly with descriptive commit messages throughout the assignment

## How to View / Run
- Open this repository in GitHub Codespaces to run notebooks in the pre-configured environment
- To run tests: open a terminal and run `uv run pytest tests/test_pandas_basics.py -v` and `uv run pytest tests/test_geopandas_basics.py -v`
- Notebooks are located in `notebooks/pandas/`, `notebooks/geopandas/`, and `notebooks/rasterio/`

## Repository Structure

    .
    ├── README.md
    ├── .devcontainer
    │   ├── devcontainer.json
    │   ├── Dockerfile
    ├── data/
    │   ├── neighborhood_samples.geojson
    │   ├── temperature_readings.csv
    │   └── weather_stations.csv
    ├── notebooks/
    │   ├── pandas/
    │   ├── geopandas/
    │   └── rasterio/
    ├── src/
    │   ├── pandas_basics.py
    │   ├── geopandas_basics.py
    │   └── download_real_data.py
    ├── tests/
    │   ├── test_pandas_basics.py
    │   └── test_geopandas_basics.py
    ├── pyproject.toml
    └── uv.lock

