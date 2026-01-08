"""
Unit tests for the DataProcessor class.
"""

import unittest
import tempfile
import os
from pmdemo.processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    """Test cases for DataProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()
        
    def test_init(self):
        """Test DataProcessor initialization."""
        processor = DataProcessor()
        self.assertIsNone(processor.data)
    
    def test_load_csv_file_not_found(self):
        """Test load_csv with non-existent file."""
        with self.assertRaises(FileNotFoundError):
            self.processor.load_csv("nonexistent.csv")
    
    def test_load_csv_success(self):
        """Test successful CSV loading."""
        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("name,age,city\n")
            f.write("Alice,30,NYC\n")
            f.write("Bob,25,LA\n")
            temp_path = f.name
        
        try:
            data = self.processor.load_csv(temp_path)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['name'], 'Alice')
            self.assertEqual(data[1]['age'], '25')
        finally:
            os.unlink(temp_path)
    
    def test_clean_data_empty_rows(self):
        """Test cleaning data with empty rows."""
        data = [
            {"name": "Alice", "age": "30"},
            {"name": "", "age": ""},
            {"name": "Bob", "age": "25"},
        ]
        cleaned = self.processor.clean_data(data)
        self.assertEqual(len(cleaned), 2)
        self.assertEqual(cleaned[0]['name'], 'Alice')
        self.assertEqual(cleaned[1]['name'], 'Bob')
    
    def test_filter_data(self):
        """Test filtering data by key-value."""
        data = [
            {"name": "Alice", "status": "active"},
            {"name": "Bob", "status": "inactive"},
            {"name": "Charlie", "status": "active"},
        ]
        filtered = self.processor.filter_data(data, "status", "active")
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]['name'], 'Alice')
        self.assertEqual(filtered[1]['name'], 'Charlie')


if __name__ == '__main__':
    unittest.main()
