# Contributing to 524-pmdemo

Thank you for your interest in contributing to the 524-pmdemo project! This document provides guidelines for contributing to this project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Issue Management](#issue-management)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Git Workflow](#git-workflow)

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors. We expect all participants to:
- Be respectful and considerate
- Accept constructive criticism gracefully
- Focus on what is best for the project
- Show empathy towards other community members

### Unacceptable Behavior
- Harassment, discrimination, or offensive comments
- Personal attacks or trolling
- Publishing others' private information
- Any conduct that could reasonably be considered inappropriate

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- pip package manager

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/524-pmdemo.git
   cd 524-pmdemo
   ```

3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/ilyamusabirov/524-pmdemo.git
   ```

4. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt  # If exists
   ```

## Development Workflow

### Branching Strategy

We follow a feature branch workflow:

- `main` or `master`: Production-ready code
- `develop`: Integration branch for features (if used)
- `feature/<name>`: New features
- `bugfix/<name>`: Bug fixes
- `docs/<name>`: Documentation updates
- `test/<name>`: Test improvements

### Creating a Branch

```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

## Issue Management

### How to Manage Issues Professionally

1. **Before Creating an Issue:**
   - Search existing issues to avoid duplicates
   - Check if the issue has already been addressed
   - Gather relevant information (error messages, steps to reproduce, etc.)

2. **Creating a Good Issue:**
   - Use a clear and descriptive title
   - Provide detailed description of the problem or feature
   - Include steps to reproduce (for bugs)
   - Add relevant labels (bug, enhancement, documentation, etc.)
   - Mention related issues or PRs if applicable

3. **Issue Templates:**
   Use the provided issue templates for:
   - Bug reports
   - Feature requests
   - Documentation improvements

4. **Issue Lifecycle:**
   - **Open**: New issue created
   - **In Progress**: Someone is working on it
   - **Review**: Solution is being reviewed
   - **Closed**: Issue is resolved

5. **Best Practices:**
   - Keep issues focused on a single topic
   - Update issues with progress or new information
   - Close issues when resolved
   - Be respectful in discussions

## Pull Request Process

### Before Submitting a PR

1. **Ensure your code:**
   - Follows the coding standards
   - Includes appropriate tests
   - Passes all existing tests
   - Is properly documented

2. **Update your branch:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

### Creating a Pull Request

1. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a PR on GitHub:**
   - Use a clear title describing the changes
   - Reference related issues (e.g., "Closes #123")
   - Provide detailed description of changes
   - Include any breaking changes or migration notes

3. **PR Requirements:**
   - At least one approval from a team member
   - All CI checks must pass
   - No merge conflicts
   - Up-to-date with base branch

### PR Review Process

- Reviews typically happen within 48 hours
- Address review comments promptly
- Push new commits to update the PR
- Request re-review after making changes

## Coding Standards

### Python Style Guide

We follow **PEP 8** style guide with the following specifics:

- **Line Length**: Maximum 127 characters
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Use double quotes for strings
- **Imports**: 
  - Standard library imports first
  - Third-party imports second
  - Local imports last
  - Alphabetically sorted within each group

### Documentation Standards

- **Module Docstrings**: Every module must have a docstring
- **Function Docstrings**: All public functions must have docstrings with:
  - Brief description
  - Args section
  - Returns section
  - Raises section (if applicable)
  - Examples section (recommended)
- **Format**: Use Google style docstrings

Example:
```python
def calculate_mean(data: List[float]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.
    
    Args:
        data (List[float]): List of numeric values.
        
    Returns:
        float: The arithmetic mean of the input values.
        
    Raises:
        ValueError: If the input list is empty.
        
    Examples:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
    """
    if not data:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(data) / len(data)
```

### Code Quality Tools

- **Linter**: flake8
- **Formatter**: black
- **Type Checker**: mypy (recommended)

Run before committing:
```bash
black pmdemo tests
flake8 pmdemo tests
```

## Testing Guidelines

### Test Requirements

- All new features must include unit tests
- Bug fixes should include regression tests
- Maintain or improve code coverage (target: >80%)

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=pmdemo --cov-report=term

# Run specific test file
python -m pytest tests/test_processor.py
```

### Test Structure

- Unit tests: Test individual functions/methods in isolation
- Integration tests: Test interaction between modules
- Test files: Named `test_*.py`
- Test functions: Named `test_*`

### Writing Good Tests

```python
def test_function_name_expected_behavior(self):
    """Test that function_name does expected_behavior."""
    # Arrange
    input_data = [1, 2, 3]
    expected_result = 6
    
    # Act
    result = sum_numbers(input_data)
    
    # Assert
    self.assertEqual(result, expected_result)
```

## Git Workflow

### Commit Messages

Follow the conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(processor): add CSV export functionality

Implement export_csv method in DataProcessor class to allow
exporting processed data to CSV format.

Closes #42
```

```
fix(analyzer): handle empty dataset in calculate_mean

Add validation to prevent division by zero when calculating
mean of an empty dataset.

Fixes #56
```

### Git Best Practices

1. **Commit Often**: Make small, focused commits
2. **Write Clear Messages**: Describe what and why, not how
3. **Keep History Clean**: Use rebase to maintain linear history
4. **Don't Commit:**
   - Binary files (unless necessary)
   - Generated files
   - IDE-specific files
   - Sensitive information (passwords, API keys)

### Updating Your Branch

```bash
# Fetch latest changes
git fetch upstream

# Rebase your branch
git rebase upstream/main

# If conflicts occur, resolve them and:
git add <resolved-files>
git rebase --continue

# Force push (only to your fork)
git push origin feature/your-feature-name --force-with-lease
```

## GitHub Project Management Tools

### Using GitHub Features

1. **Issues:**
   - Use labels to categorize issues
   - Assign issues to team members
   - Use milestones to track progress
   - Link issues to pull requests

2. **Projects:**
   - Use project boards to visualize workflow
   - Move cards through columns (To Do, In Progress, Done)
   - Track progress on milestones

3. **Milestones:**
   - Group related issues
   - Set due dates
   - Track completion percentage

4. **Labels:**
   - `bug`: Something isn't working
   - `enhancement`: New feature or request
   - `documentation`: Documentation improvements
   - `good first issue`: Good for newcomers
   - `help wanted`: Extra attention needed
   - `wontfix`: This will not be worked on

## Questions?

If you have questions or need help:
- Check existing issues and discussions
- Create a new issue with the `question` label
- Reach out to the maintainers

## License

By contributing, you agree that your contributions will be licensed under the project's GPL-3.0 License.

---

Thank you for contributing to 524-pmdemo! 🎉
