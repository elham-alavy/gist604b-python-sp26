"""
Pandas Basics for GIS Data Analysis - Student Implementation

Complete the four functions in this file.
Use the notebooks to learn and test each function.

📋 FUNCTIONS TO IMPLEMENT IN THIS FILE:
=====================================
✅ Function 1: load_and_explore_gis_data()     → notebooks/01_function_...
✅ Function 2: filter_environmental_data()     → notebooks/02_function_...
✅ Function 3: calculate_station_statistics()  → notebooks/03_function_...
✅ Function 4: join_station_data()             → notebooks/04_function_...
"""

import pandas as pd
from pathlib import Path
import os


# =============================================================================
# FUNCTION 1: LOAD AND EXPLORE GIS DATA
# =============================================================================

def load_and_explore_gis_data(file_path):
    """
    Load a CSV file and display comprehensive information about the dataset.

    Args:
        file_path (str): Path to the CSV file to load

    Returns:
        pandas.DataFrame: The loaded dataset, or None if loading failed
    """

    print("=" * 50)
    print("LOADING AND EXPLORING GIS DATA")
    print("=" * 50)

    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found: {file_path}")
        return None

    print(f"📁 Loading data from: {file_path}")

    try:
        df = pd.read_csv(file_path)
        print("✅ File loaded successfully!")
    except Exception as e:
        print(f"❌ ERROR loading file: {e}")
        return None

    print(f"\n📊 DATASET OVERVIEW")
    print(f"Shape: {df.shape} - {df.shape[0]} rows and {df.shape[1]} columns")
    print(f"Columns: {list(df.columns)}")

    print(f"\n🔧 DATA TYPES:")
    for col in df.columns:
        print(f"   {col}: {df[col].dtype}")

    print(f"\n👀 FIRST 5 ROWS:")
    print(df.head())

    print(f"\n📈 SUMMARY STATISTICS:")
    print(df.describe())

    print(f"\n🔍 DATA QUALITY CHECK:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("Missing values found:")
        print(missing[missing > 0])
    else:
        print("✅ No missing values")

    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"⚠️  Found {duplicates} duplicate rows")
    else:
        print("✅ No duplicate rows")

    print(f"\n🎉 Data exploration complete! Dataset is ready for analysis.")

    return df


# =============================================================================
# FUNCTION 2: FILTER ENVIRONMENTAL DATA
# =============================================================================

def filter_environmental_data(df, min_temp=15, max_temp=30, quality="good"):
    """
    Filter environmental data based on temperature range and data quality.

    Args:
        df (pandas.DataFrame): Environmental data with temperature and quality columns
        min_temp (float): Minimum acceptable temperature in Celsius (default: 15)
        max_temp (float): Maximum acceptable temperature in Celsius (default: 30)
        quality (str): Required data quality level (default: "good")

    Returns:
        pandas.DataFrame: Filtered data meeting all specified conditions
    """

    print("=" * 50)
    print("FILTERING ENVIRONMENTAL DATA")
    print("=" * 50)

    if df is None or df.empty:
        print("❌ ERROR: Empty or None DataFrame provided")
        return pd.DataFrame()

    required_columns = ['temperature_c', 'data_quality']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        print(f"❌ ERROR: Missing required columns: {missing_columns}")
        return pd.DataFrame()

    original_count = len(df)
    print(f"📊 Starting with {original_count} rows")

    temp_filter = (df['temperature_c'] >= min_temp) & (df['temperature_c'] <= max_temp)
    quality_filter = df['data_quality'] == quality
    combined_filter = temp_filter & quality_filter

    filtered_df = df[combined_filter].copy()

    final_count = len(filtered_df)
    total_removed = original_count - final_count
    removal_pct = (total_removed / original_count) * 100 if original_count > 0 else 0

    print(f"Original data: {original_count} rows")
    print(f"After filtering: {final_count} rows ({100 - removal_pct:.1f}% of data retained)")
    print(f"Filters applied:")
    print(f"  - Temperature: {min_temp}°C to {max_temp}°C")
    print(f"  - Data quality: {quality}")

    return filtered_df


# =============================================================================
# FUNCTION 3: CALCULATE STATION STATISTICS
# =============================================================================

def calculate_station_statistics(df):
    """
    Calculate station statistics grouped by station_id.

    Args:
        df (pandas.DataFrame): Environmental readings data with 'station_id',
                               'temperature_c' and 'humidity_percent' columns

    Returns:
        pandas.DataFrame: Statistics for each station
    """

    print("=" * 50)
    print("CALCULATING STATION STATISTICS")
    print("=" * 50)

    if df is None or len(df) == 0:
        print("❌ ERROR: DataFrame is empty or None")
        return pd.DataFrame()

    required_columns = ['station_id', 'temperature_c', 'humidity_percent']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        print(f"❌ ERROR: Missing required columns: {missing_columns}")
        return pd.DataFrame()

    unique_stations = df['station_id'].nunique()
    print(f"Calculating statistics for {unique_stations} unique stations...")

    grouped = df.groupby('station_id')

    avg_temperature = grouped['temperature_c'].mean().round(1)
    avg_humidity = grouped['humidity_percent'].mean().round(1)
    reading_count = grouped.size()

    summary = pd.DataFrame({
        'station_id': avg_temperature.index,
        'avg_temperature': avg_temperature.values,
        'avg_humidity': avg_humidity.values,
        'reading_count': reading_count.values
    })

    print(f"Statistics calculated:")
    print(f"  - Total readings analyzed: {summary['reading_count'].sum()}")
    print(f"  - Stations with data: {len(summary)}")
    print(f"  - Average readings per station: {summary['reading_count'].mean():.1f}")

    return summary


# =============================================================================
# FUNCTION 4: JOIN STATION DATA
# =============================================================================

def join_station_data(stations_df, readings_df):
    """
    Join sensor readings with station metadata.

    Args:
        stations_df (pandas.DataFrame): Station information with 'station_id'
        readings_df (pandas.DataFrame): Temperature readings with 'station_id'

    Returns:
        pandas.DataFrame: Combined dataset with readings AND station information
    """

    print("=" * 50)
    print("JOINING STATION DATA")
    print("=" * 50)

    if readings_df is None or readings_df.empty:
        print("❌ ERROR: Readings DataFrame is empty or None")
        return pd.DataFrame()

    if stations_df is None or stations_df.empty:
        print("❌ ERROR: Stations DataFrame is empty or None")
        return pd.DataFrame()

    if 'station_id' not in readings_df.columns:
        print("❌ ERROR: 'station_id' column missing from readings data")
        return pd.DataFrame()

    if 'station_id' not in stations_df.columns:
        print("❌ ERROR: 'station_id' column missing from stations data")
        return pd.DataFrame()

    print(f"Joining station information with readings...")
    print(f"Stations table: {len(stations_df)} stations")
    print(f"Readings table: {len(readings_df)} readings")

    result = pd.merge(readings_df, stations_df, on='station_id', how='left')

    print(f"Joined table: {len(result)} rows with station details added!")

    return result


# =============================================================================
# HELPER FUNCTIONS (You don't need to modify these - they're provided!)
# =============================================================================

def _check_required_columns(df, required_columns, data_name="DataFrame"):
    """
    Helper function to check if required columns exist in a DataFrame.
    """
    if df is None or df.empty:
        return False, required_columns

    missing = [col for col in required_columns if col not in df.columns]
    return len(missing) == 0, missing


def _format_number(value, decimals=1):
    """
    Helper function to format numbers for display.
    """
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return str(value)

# =============================================================================
# HELPER FUNCTIONS (You don't need to modify these - they're provided!)
# =============================================================================

def _check_required_columns(df, required_columns, data_name="DataFrame"):
    """
    Helper function to check if required columns exist in a DataFrame.
    
    Args:
        df (pandas.DataFrame): DataFrame to check
        required_columns (list): List of required column names
        data_name (str): Name to use in error messages
    
    Returns:
        tuple: (bool, list) - (all_present, missing_columns)
    """
    if df is None or df.empty:
        return False, required_columns
    
    missing = [col for col in required_columns if col not in df.columns]
    return len(missing) == 0, missing


def _format_number(value, decimals=1):
    """
    Helper function to format numbers for display.
    
    Args:
        value: Number to format
        decimals (int): Number of decimal places
    
    Returns:
        str: Formatted number
    """
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return str(value)
