"""
Unit tests for the DataAnalyzer class.
"""

import unittest
from pmdemo.analyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):
    """Test cases for DataAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = DataAnalyzer()
        self.sample_data = [
            {"name": "Alice", "age": "30", "score": "85"},
            {"name": "Bob", "age": "25", "score": "90"},
            {"name": "Charlie", "age": "35", "score": "78"},
        ]
    
    def test_init(self):
        """Test DataAnalyzer initialization."""
        analyzer = DataAnalyzer()
        self.assertIsNone(analyzer.data)
    
    def test_calculate_mean(self):
        """Test mean calculation."""
        mean_age = self.analyzer.calculate_mean(self.sample_data, "age")
        self.assertEqual(mean_age, 30.0)
        
        mean_score = self.analyzer.calculate_mean(self.sample_data, "score")
        self.assertAlmostEqual(mean_score, 84.333, places=2)
    
    def test_calculate_mean_invalid_key(self):
        """Test mean calculation with invalid key."""
        with self.assertRaises(ValueError):
            self.analyzer.calculate_mean(self.sample_data, "invalid_key")
    
    def test_calculate_stats(self):
        """Test comprehensive statistics calculation."""
        stats = self.analyzer.calculate_stats(self.sample_data, "age")
        self.assertEqual(stats["count"], 3)
        self.assertEqual(stats["mean"], 30.0)
        self.assertEqual(stats["min"], 25.0)
        self.assertEqual(stats["max"], 35.0)
    
    def test_calculate_stats_empty_data(self):
        """Test statistics with no valid data."""
        stats = self.analyzer.calculate_stats([], "age")
        self.assertEqual(stats["count"], 0)
    
    def test_group_by(self):
        """Test grouping data by key."""
        data = [
            {"name": "Alice", "category": "A"},
            {"name": "Bob", "category": "B"},
            {"name": "Charlie", "category": "A"},
        ]
        grouped = self.analyzer.group_by(data, "category")
        self.assertEqual(len(grouped), 2)
        self.assertEqual(len(grouped["A"]), 2)
        self.assertEqual(len(grouped["B"]), 1)


if __name__ == '__main__':
    unittest.main()
