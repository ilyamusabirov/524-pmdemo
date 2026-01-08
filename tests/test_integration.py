"""
Integration tests for the pmdemo package.

Tests the interaction between different modules.
"""

import unittest
import tempfile
import os
from pmdemo.processor import DataProcessor
from pmdemo.analyzer import DataAnalyzer
from pmdemo.visualizer import DataVisualizer


class TestIntegration(unittest.TestCase):
    """Integration tests for the pmdemo package."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()
        self.analyzer = DataAnalyzer()
        self.visualizer = DataVisualizer()
        
        # Create a temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', suffix='.csv', delete=False
        )
        self.temp_file.write("name,age,score,category\n")
        self.temp_file.write("Alice,30,85,A\n")
        self.temp_file.write("Bob,25,90,B\n")
        self.temp_file.write("Charlie,35,78,A\n")
        self.temp_file.write("David,28,88,B\n")
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_full_workflow(self):
        """Test complete workflow from loading to visualization."""
        # Load data
        data = self.processor.load_csv(self.temp_file.name)
        self.assertEqual(len(data), 4)
        
        # Clean data
        cleaned_data = self.processor.clean_data(data)
        self.assertEqual(len(cleaned_data), 4)
        
        # Analyze data
        stats = self.analyzer.calculate_stats(cleaned_data, "age")
        self.assertEqual(stats["count"], 4)
        self.assertAlmostEqual(stats["mean"], 29.5, places=1)
        
        # Visualize data
        report = self.visualizer.generate_report(cleaned_data, "Test Report")
        self.assertIn("Test Report", report)
        self.assertIn("Total Records: 4", report)
    
    def test_filter_and_analyze(self):
        """Test filtering data and analyzing subsets."""
        # Load and filter
        data = self.processor.load_csv(self.temp_file.name)
        filtered = self.processor.filter_data(data, "category", "A")
        self.assertEqual(len(filtered), 2)
        
        # Analyze filtered data
        stats = self.analyzer.calculate_stats(filtered, "score")
        self.assertEqual(stats["count"], 2)
        self.assertAlmostEqual(stats["mean"], 81.5, places=1)
    
    def test_group_and_visualize(self):
        """Test grouping data and creating visualizations."""
        # Load and group
        data = self.processor.load_csv(self.temp_file.name)
        grouped = self.analyzer.group_by(data, "category")
        self.assertEqual(len(grouped), 2)
        
        # Create chart for each group
        for category, group_data in grouped.items():
            chart = self.visualizer.create_bar_chart(
                group_data, "name", "score"
            )
            self.assertEqual(chart["type"], "bar")
            self.assertGreater(len(chart["x_values"]), 0)


if __name__ == '__main__':
    unittest.main()
