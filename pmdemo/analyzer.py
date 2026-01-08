"""
Data analysis module for statistical operations.

This module provides the DataAnalyzer class for performing statistical analysis.
"""

from typing import List, Dict, Any, Optional


class DataAnalyzer:
    """
    DataAnalyzer performs statistical analysis on data.
    
    This class provides methods to compute statistics, aggregations, and
    generate summary reports from data.
    
    Attributes:
        data (Optional[List[Dict[str, Any]]]): The data to analyze.
        
    Examples:
        >>> analyzer = DataAnalyzer()
        >>> stats = analyzer.calculate_stats(data, "value")
    """
    
    def __init__(self):
        """Initialize a new DataAnalyzer instance."""
        self.data: Optional[List[Dict[str, Any]]] = None
    
    def calculate_mean(self, data: List[Dict[str, Any]], key: str) -> float:
        """
        Calculate the mean (average) of a numeric column.
        
        Args:
            data (List[Dict[str, Any]]): Data containing numeric values.
            key (str): The key/column to calculate mean for.
            
        Returns:
            float: The mean value.
            
        Raises:
            ValueError: If the column contains non-numeric values or is empty.
            
        Examples:
            >>> analyzer = DataAnalyzer()
            >>> mean = analyzer.calculate_mean(data, "price")
        """
        values = []
        for row in data:
            if key in row:
                try:
                    values.append(float(row[key]))
                except (ValueError, TypeError):
                    continue
        
        if not values:
            raise ValueError(f"No valid numeric values found for key: {key}")
        
        return sum(values) / len(values)
    
    def calculate_stats(self, data: List[Dict[str, Any]], 
                       key: str) -> Dict[str, float]:
        """
        Calculate comprehensive statistics for a numeric column.
        
        Args:
            data (List[Dict[str, Any]]): Data containing numeric values.
            key (str): The key/column to analyze.
            
        Returns:
            Dict[str, float]: Dictionary with mean, min, max, and count.
            
        Examples:
            >>> analyzer = DataAnalyzer()
            >>> stats = analyzer.calculate_stats(data, "age")
            >>> print(stats["mean"])
        """
        values = []
        for row in data:
            if key in row:
                try:
                    values.append(float(row[key]))
                except (ValueError, TypeError):
                    continue
        
        if not values:
            return {"count": 0, "mean": 0.0, "min": 0.0, "max": 0.0}
        
        return {
            "count": len(values),
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
        }
    
    def group_by(self, data: List[Dict[str, Any]], 
                 key: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Group data by a specific key.
        
        Args:
            data (List[Dict[str, Any]]): Data to group.
            key (str): The key to group by.
            
        Returns:
            Dict[str, List[Dict[str, Any]]]: Dictionary mapping key values to rows.
            
        Examples:
            >>> analyzer = DataAnalyzer()
            >>> grouped = analyzer.group_by(data, "category")
        """
        groups: Dict[str, List[Dict[str, Any]]] = {}
        for row in data:
            group_key = row.get(key, "unknown")
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(row)
        return groups
