# 524-pmdemo Documentation

## Overview
The 524-pmdemo package is a Python data analysis toolkit designed to simplify common data processing, analysis, and visualization tasks.

## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [API Reference](#api-reference)
4. [Examples](#examples)
5. [Contributing](#contributing)

## Installation

### From Source
```bash
git clone https://github.com/ilyamusabirov/524-pmdemo.git
cd 524-pmdemo
pip install -e .
```

### Requirements
- Python 3.8 or higher
- Standard library modules (no external dependencies)

## Quick Start

### Loading and Processing Data

```python
from pmdemo import DataProcessor

# Create a processor instance
processor = DataProcessor()

# Load data from CSV
data = processor.load_csv("data.csv")

# Clean the data
cleaned_data = processor.clean_data(data)

# Filter data
filtered_data = processor.filter_data(cleaned_data, "status", "active")
```

### Analyzing Data

```python
from pmdemo import DataAnalyzer

# Create an analyzer instance
analyzer = DataAnalyzer()

# Calculate statistics
stats = analyzer.calculate_stats(data, "age")
print(f"Mean: {stats['mean']}")
print(f"Min: {stats['min']}")
print(f"Max: {stats['max']}")

# Group data
grouped = analyzer.group_by(data, "category")
```

### Visualizing Data

```python
from pmdemo import DataVisualizer

# Create a visualizer instance
visualizer = DataVisualizer()

# Create a bar chart
chart = visualizer.create_bar_chart(data, "month", "sales")

# Generate a report
report = visualizer.generate_report(data, "Monthly Sales Report")
print(report)
```

## API Reference

### DataProcessor

#### Methods

##### `load_csv(filepath: str) -> List[Dict[str, Any]]`
Load data from a CSV file.

**Parameters:**
- `filepath` (str): Path to the CSV file

**Returns:**
- List[Dict[str, Any]]: List of dictionaries representing rows

**Raises:**
- FileNotFoundError: If file doesn't exist
- ValueError: If file is not valid CSV

##### `clean_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]`
Remove empty rows and clean data.

**Parameters:**
- `data` (List[Dict[str, Any]]): Raw data to clean

**Returns:**
- List[Dict[str, Any]]: Cleaned data

##### `filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]`
Filter data by key-value pair.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data to filter
- `key` (str): Dictionary key to filter on
- `value` (Any): Value to match

**Returns:**
- List[Dict[str, Any]]: Filtered data

### DataAnalyzer

#### Methods

##### `calculate_mean(data: List[Dict[str, Any]], key: str) -> float`
Calculate the mean of a numeric column.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data containing numeric values
- `key` (str): Column to calculate mean for

**Returns:**
- float: The mean value

**Raises:**
- ValueError: If column contains no valid numeric values

##### `calculate_stats(data: List[Dict[str, Any]], key: str) -> Dict[str, float]`
Calculate comprehensive statistics.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data containing numeric values
- `key` (str): Column to analyze

**Returns:**
- Dict[str, float]: Dictionary with count, mean, min, max

##### `group_by(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]`
Group data by a specific key.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data to group
- `key` (str): Key to group by

**Returns:**
- Dict[str, List[Dict[str, Any]]]: Grouped data

### DataVisualizer

#### Methods

##### `create_bar_chart(data: List[Dict[str, Any]], x_key: str, y_key: str) -> Dict[str, Any]`
Create a bar chart configuration.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data to visualize
- `x_key` (str): Key for x-axis
- `y_key` (str): Key for y-axis

**Returns:**
- Dict[str, Any]: Chart configuration

##### `create_summary_table(data: List[Dict[str, Any]]) -> str`
Create a text-based summary table.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data to summarize

**Returns:**
- str: Formatted text table

##### `generate_report(data: List[Dict[str, Any]], title: str) -> str`
Generate a comprehensive text report.

**Parameters:**
- `data` (List[Dict[str, Any]]): Data to report on
- `title` (str): Report title

**Returns:**
- str: Formatted report text

## Examples

### Example 1: Basic Data Analysis

```python
from pmdemo import DataProcessor, DataAnalyzer

# Load and process data
processor = DataProcessor()
data = processor.load_csv("sales.csv")

# Analyze
analyzer = DataAnalyzer()
revenue_stats = analyzer.calculate_stats(data, "revenue")

print(f"Average Revenue: ${revenue_stats['mean']:.2f}")
print(f"Total Records: {revenue_stats['count']}")
```

### Example 2: Data Filtering and Grouping

```python
from pmdemo import DataProcessor, DataAnalyzer

processor = DataProcessor()
data = processor.load_csv("customers.csv")

# Filter active customers
active_customers = processor.filter_data(data, "status", "active")

# Group by region
analyzer = DataAnalyzer()
by_region = analyzer.group_by(active_customers, "region")

for region, customers in by_region.items():
    print(f"{region}: {len(customers)} customers")
```

### Example 3: Complete Workflow

```python
from pmdemo import DataProcessor, DataAnalyzer, DataVisualizer

# Load
processor = DataProcessor()
data = processor.load_csv("products.csv")

# Clean
cleaned = processor.clean_data(data)

# Analyze
analyzer = DataAnalyzer()
price_stats = analyzer.calculate_stats(cleaned, "price")

# Visualize
visualizer = DataVisualizer()
report = visualizer.generate_report(cleaned, "Product Analysis")
print(report)

chart = visualizer.create_bar_chart(cleaned, "category", "price")
print(f"Chart type: {chart['type']}")
```

## Contributing

Please read [CONTRIBUTING.md](../CONTRIBUTING.md) for details on our development process and how to submit pull requests.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](../LICENSE) file for details.
