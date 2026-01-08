"""
Unit tests for the DataVisualizer class.
"""

import unittest
from pmdemo.visualizer import DataVisualizer


class TestDataVisualizer(unittest.TestCase):
    """Test cases for DataVisualizer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.visualizer = DataVisualizer()
        self.sample_data = [
            {"month": "Jan", "sales": "100"},
            {"month": "Feb", "sales": "150"},
            {"month": "Mar", "sales": "120"},
        ]
    
    def test_init(self):
        """Test DataVisualizer initialization."""
        visualizer = DataVisualizer()
        self.assertIsNone(visualizer.data)
    
    def test_create_bar_chart(self):
        """Test bar chart creation."""
        chart = self.visualizer.create_bar_chart(
            self.sample_data, "month", "sales"
        )
        self.assertEqual(chart["type"], "bar")
        self.assertEqual(len(chart["x_values"]), 3)
        self.assertEqual(chart["x_label"], "month")
        self.assertEqual(chart["y_label"], "sales")
    
    def test_create_summary_table(self):
        """Test summary table creation."""
        table = self.visualizer.create_summary_table(self.sample_data)
        self.assertIn("month", table)
        self.assertIn("sales", table)
        self.assertIn("Jan", table)
    
    def test_create_summary_table_empty(self):
        """Test summary table with empty data."""
        table = self.visualizer.create_summary_table([])
        self.assertEqual(table, "No data available")
    
    def test_generate_report(self):
        """Test report generation."""
        report = self.visualizer.generate_report(
            self.sample_data, "Sales Report"
        )
        self.assertIn("Sales Report", report)
        self.assertIn("Total Records: 3", report)
        self.assertIn("Data Summary", report)


if __name__ == '__main__':
    unittest.main()
