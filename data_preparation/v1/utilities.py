import pandas as pd
import chardet
from typing import Tuple, Optional, Dict, Any
from pathlib import Path

def read_csv(file_path: str) -> Optional[pd.DataFrame]:
    """
    Read a CSV file with automatic encoding detection.

    Args:
        file_path (str): Path to the CSV file to be read

    Returns:
        Optional[pd.DataFrame]: DataFrame containing the CSV data if successful, None otherwise
    """
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except UnicodeDecodeError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def save_csv(df: pd.DataFrame, file_path: str) -> bool:
    """
    Save a DataFrame to a CSV file with UTF-8 encoding.

    Args:
        df (pd.DataFrame): DataFrame to be saved
        file_path (str): Path where the CSV file will be saved

    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        df.to_csv(file_path, index=False, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Error saving file {file_path}: {e}")
        return False

def compare_files(file1_path: str, file2_path: str) -> Dict[str, Any]:
    """
    Compare two Excel or CSV files and check for differences.

    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file

    Returns:
        Dict[str, Any]: Dictionary containing comparison results with keys:
            - 'are_equal' (bool): True if files are identical
            - 'differences' (pd.DataFrame): DataFrame showing differences if files are not equal
            - 'file1_extension' (str): Extension of the first file
            - 'file2_extension' (str): Extension of the second file
    """
    file1_ext = Path(file1_path).suffix.lower()
    file2_ext = Path(file2_path).suffix.lower()
    
    # Read files based on their extensions
    try:
        if file1_ext == '.xlsx':
            df1 = pd.read_excel(file1_path)
        elif file1_ext == '.csv':
            df1 = read_csv(file1_path)
        else:
            return {
                'are_equal': False,
                'error': f'Unsupported file extension for file1: {file1_ext}'
            }
            
        if file2_ext == '.xlsx':
            df2 = pd.read_excel(file2_path)
        elif file2_ext == '.csv':
            df2 = read_csv(file2_path)
        else:
            return {
                'are_equal': False,
                'error': f'Unsupported file extension for file2: {file2_ext}'
            }
            
        # Check if DataFrames are equal
        are_equal = df1.equals(df2)
        
        # If not equal, get the differences
        differences = None
        if not are_equal:
            try:
                differences = df1.compare(df2)
            except ValueError as e:
                differences = str(e)
        
        return {
            'are_equal': are_equal,
            'differences': differences,
            'file1_extension': file1_ext,
            'file2_extension': file2_ext
        }
        
    except Exception as e:
        return {
            'are_equal': False,
            'error': f'Error comparing files: {str(e)}'
        }