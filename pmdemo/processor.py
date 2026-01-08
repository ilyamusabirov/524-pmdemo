"""
Data processing module for loading and preprocessing data.

This module provides the DataProcessor class for handling various data operations.
"""

import csv
from typing import List, Dict, Any, Optional


class DataProcessor:
    """
    DataProcessor handles loading and preprocessing of data from various sources.
    
    This class provides methods to load data from CSV files, clean and preprocess
    the data, and prepare it for analysis.
    
    Attributes:
        data (Optional[List[Dict[str, Any]]]): The loaded data.
        
    Examples:
        >>> processor = DataProcessor()
        >>> data = processor.load_csv("data.csv")
        >>> cleaned_data = processor.clean_data(data)
    """
    
    def __init__(self):
        """Initialize a new DataProcessor instance."""
        self.data: Optional[List[Dict[str, Any]]] = None
    
    def load_csv(self, filepath: str) -> List[Dict[str, Any]]:
        """
        Load data from a CSV file.
        
        Args:
            filepath (str): Path to the CSV file to load.
            
        Returns:
            List[Dict[str, Any]]: List of dictionaries representing rows of data.
            
        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the file is not a valid CSV.
            
        Examples:
            >>> processor = DataProcessor()
            >>> data = processor.load_csv("data.csv")
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
                return self.data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {filepath}") from e
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}") from e
    
    def clean_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Clean and preprocess data.
        
        Removes empty rows and handles missing values.
        
        Args:
            data (List[Dict[str, Any]]): Raw data to clean.
            
        Returns:
            List[Dict[str, Any]]: Cleaned data.
            
        Examples:
            >>> processor = DataProcessor()
            >>> cleaned = processor.clean_data(raw_data)
        """
        cleaned = []
        for row in data:
            # Remove rows where all values are empty
            if any(value for value in row.values()):
                cleaned.append(row)
        return cleaned
    
    def filter_data(self, data: List[Dict[str, Any]], 
                   key: str, value: Any) -> List[Dict[str, Any]]:
        """
        Filter data based on a key-value pair.
        
        Args:
            data (List[Dict[str, Any]]): Data to filter.
            key (str): Dictionary key to filter on.
            value (Any): Value to match.
            
        Returns:
            List[Dict[str, Any]]: Filtered data.
            
        Examples:
            >>> processor = DataProcessor()
            >>> filtered = processor.filter_data(data, "status", "active")
        """
        return [row for row in data if row.get(key) == value]
