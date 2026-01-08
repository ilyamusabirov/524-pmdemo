"""
Data visualization module for creating charts and graphs.

This module provides the DataVisualizer class for generating visualizations.
"""

from typing import List, Dict, Any, Optional


class DataVisualizer:
    """
    DataVisualizer creates visualizations from data.
    
    This class provides methods to generate various types of charts and graphs
    from data for analysis and presentation.
    
    Attributes:
        data (Optional[List[Dict[str, Any]]]): The data to visualize.
        
    Examples:
        >>> visualizer = DataVisualizer()
        >>> chart = visualizer.create_bar_chart(data, "category", "value")
    """
    
    def __init__(self):
        """Initialize a new DataVisualizer instance."""
        self.data: Optional[List[Dict[str, Any]]] = None
    
    def create_bar_chart(self, data: List[Dict[str, Any]], 
                        x_key: str, y_key: str) -> Dict[str, Any]:
        """
        Create a bar chart configuration from data.
        
        Args:
            data (List[Dict[str, Any]]): Data to visualize.
            x_key (str): Key for x-axis values.
            y_key (str): Key for y-axis values.
            
        Returns:
            Dict[str, Any]: Chart configuration dictionary.
            
        Examples:
            >>> visualizer = DataVisualizer()
            >>> chart = visualizer.create_bar_chart(data, "month", "sales")
        """
        chart_data = {
            "type": "bar",
            "x_values": [row.get(x_key) for row in data],
            "y_values": [row.get(y_key) for row in data],
            "x_label": x_key,
            "y_label": y_key,
        }
        return chart_data
    
    def create_summary_table(self, data: List[Dict[str, Any]]) -> str:
        """
        Create a text-based summary table from data.
        
        Args:
            data (List[Dict[str, Any]]): Data to summarize.
            
        Returns:
            str: Formatted text table.
            
        Examples:
            >>> visualizer = DataVisualizer()
            >>> table = visualizer.create_summary_table(data)
            >>> print(table)
        """
        if not data:
            return "No data available"
        
        # Get keys from first row
        keys = list(data[0].keys())
        
        # Create header
        header = " | ".join(keys)
        separator = "-" * len(header)
        
        # Create rows
        rows = []
        for row in data[:10]:  # Limit to first 10 rows
            row_str = " | ".join(str(row.get(key, "")) for key in keys)
            rows.append(row_str)
        
        return "\n".join([header, separator] + rows)
    
    def generate_report(self, data: List[Dict[str, Any]], 
                       title: str = "Data Report") -> str:
        """
        Generate a comprehensive text report from data.
        
        Args:
            data (List[Dict[str, Any]]): Data to report on.
            title (str): Title for the report.
            
        Returns:
            str: Formatted report text.
            
        Examples:
            >>> visualizer = DataVisualizer()
            >>> report = visualizer.generate_report(data, "Sales Report")
            >>> print(report)
        """
        report = [
            f"# {title}",
            f"\nTotal Records: {len(data)}",
            "\n## Data Summary",
            self.create_summary_table(data),
        ]
        return "\n".join(report)
