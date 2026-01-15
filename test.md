# Testing Guide for Your Calorie Calculator

This guide will teach you how to write tests for your Python code using your calorie calculator as an example.

---

## Why Test?

- **Catch bugs early** before they reach users
- **Confidence to refactor** - change code without fear of breaking things
- **Documentation** - tests show how code is supposed to work
- **Better design** - testable code is often better structured

---

## Types of Tests

### 1. Unit Tests
Test individual functions in isolation. This is the most common type.

**What to test:** Single functions with no external dependencies.

**Example functions from your code that are easy to unit test:**
- `calculate_bmr()` - pure calculation, no I/O
- `see_activity_level()` - pure calculation, no I/O

### 2. Integration Tests
Test how multiple components work together.

**Example:** Testing that `calculate_bmr()` output works correctly with `see_activity_level()`.

### 3. End-to-End (E2E) Tests
Test the entire application flow from start to finish.

**Example:** Simulating a user entering weight, gender, age, height, and activity level, then checking the final output.

### 4. Functional Tests
Test specific features or user stories work as expected.

---

## Python Testing Framework: `unittest`

Python has a built-in testing framework called `unittest`.

### Basic Structure

```python
import unittest
from protein_and_calorie_calculator import calculate_bmr, see_activity_level

class TestCalculateBMR(unittest.TestCase):

    def test_male_bmr_calculation(self):
        # Arrange: Set up test data
        weight = 70
        gender = "male"
        age = 25
        height = 175

        # Act: Call the function
        result = calculate_bmr(weight, gender, age, height)

        # Assert: Check the result
        # Expected: 88.362 + (13.397 * 70) + (4.799 * 175) - (5.677 * 25)
        # = 88.362 + 937.79 + 839.825 - 141.925 = 1724.052
        self.assertAlmostEqual(result, 1724.052, places=2)

if __name__ == '__main__':
    unittest.main()
```

---

## Best Practices

### 1. Use the AAA Pattern

Every test should follow **Arrange-Act-Assert**:

```python
def test_female_bmr_calculation(self):
    # ARRANGE - Set up your test data
    weight = 60
    gender = "female"
    age = 30
    height = 165

    # ACT - Execute the code being tested
    result = calculate_bmr(weight, gender, age, height)

    # ASSERT - Verify the result
    expected = 447.593 + (9.247 * 60) + (3.098 * 165) - (4.33 * 30)
    self.assertAlmostEqual(result, expected, places=2)
```

### 2. One Assertion Per Test (When Possible)

Each test should verify one thing:

```python
# Good - focused test
def test_activity_level_1_multiplier(self):
    bmr, protein = see_activity_level(1000, 70, 1)
    self.assertAlmostEqual(bmr, 1200)  # 1000 * 1.2

def test_activity_level_1_protein(self):
    bmr, protein = see_activity_level(1000, 70, 1)
    self.assertAlmostEqual(protein, 56)  # 0.8 * 70
```

### 3. Use Descriptive Test Names

```python
# Bad
def test1(self):

# Good
def test_calculate_bmr_returns_correct_value_for_male(self):

def test_see_activity_level_applies_correct_multiplier_for_sedentary(self):
```

### 4. Test Edge Cases

```python
class TestEdgeCases(unittest.TestCase):

    def test_bmr_with_minimum_weight(self):
        result = calculate_bmr(1, "male", 25, 170)
        self.assertGreater(result, 0)

    def test_bmr_with_maximum_age(self):
        result = calculate_bmr(70, "female", 150, 165)
        self.assertGreater(result, 0)
```

### 5. Test Boundary Values

Test at the edges of valid input ranges:

```python
def test_activity_level_boundary_1(self):
    bmr, protein = see_activity_level(1000, 70, 1)
    self.assertEqual(bmr, 1200)

def test_activity_level_boundary_5(self):
    bmr, protein = see_activity_level(1000, 70, 5)
    self.assertEqual(bmr, 1900)
```

---

## Complete Test File Example

Create a file called `test_calculator.py`:

```python
import unittest
from protein_and_calorie_calculator import (
    calculate_bmr,
    see_activity_level,
    GENDER_MALE,
    GENDER_FEMALE
)


class TestCalculateBMR(unittest.TestCase):
    """Unit tests for the calculate_bmr function."""

    def test_male_bmr_basic(self):
        """Test BMR calculation for a typical male."""
        result = calculate_bmr(70, GENDER_MALE, 25, 175)
        expected = 88.362 + (13.397 * 70) + (4.799 * 175) - (5.677 * 25)
        self.assertAlmostEqual(result, expected, places=2)

    def test_female_bmr_basic(self):
        """Test BMR calculation for a typical female."""
        result = calculate_bmr(60, GENDER_FEMALE, 30, 165)
        expected = 447.593 + (9.247 * 60) + (3.098 * 165) - (4.33 * 30)
        self.assertAlmostEqual(result, expected, places=2)

    def test_male_bmr_uppercase(self):
        """Test that gender comparison is case-insensitive."""
        result = calculate_bmr(70, "MALE", 25, 175)
        expected = 88.362 + (13.397 * 70) + (4.799 * 175) - (5.677 * 25)
        self.assertAlmostEqual(result, expected, places=2)


class TestActivityLevel(unittest.TestCase):
    """Unit tests for the see_activity_level function."""

    def test_sedentary_level(self):
        """Test activity level 1 (sedentary)."""
        bmr, protein = see_activity_level(1000, 70, 1)
        self.assertAlmostEqual(bmr, 1200)      # 1000 * 1.2
        self.assertAlmostEqual(protein, 56)    # 0.8 * 70

    def test_lightly_active_level(self):
        """Test activity level 2 (lightly active)."""
        bmr, protein = see_activity_level(1000, 70, 2)
        self.assertAlmostEqual(bmr, 1375)      # 1000 * 1.375
        self.assertAlmostEqual(protein, 77)    # 1.1 * 70

    def test_moderately_active_level(self):
        """Test activity level 3 (moderately active)."""
        bmr, protein = see_activity_level(1000, 70, 3)
        self.assertAlmostEqual(bmr, 1550)      # 1000 * 1.55
        self.assertAlmostEqual(protein, 98)    # 1.4 * 70

    def test_very_active_level(self):
        """Test activity level 4 (very active)."""
        bmr, protein = see_activity_level(1000, 70, 4)
        self.assertAlmostEqual(bmr, 1725)      # 1000 * 1.725
        self.assertAlmostEqual(protein, 133)   # 1.9 * 70

    def test_extremely_active_level(self):
        """Test activity level 5 (extremely active)."""
        bmr, protein = see_activity_level(1000, 70, 5)
        self.assertAlmostEqual(bmr, 1900)      # 1000 * 1.9
        self.assertAlmostEqual(protein, 175)   # 2.5 * 70


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple functions."""

    def test_full_calculation_male(self):
        """Test complete flow for a male user."""
        # Calculate BMR
        bmr = calculate_bmr(80, GENDER_MALE, 30, 180)
        # Apply activity level
        final_bmr, protein = see_activity_level(bmr, 80, 3)

        # Verify results are in expected ranges
        self.assertGreater(final_bmr, 2000)
        self.assertLess(final_bmr, 4000)
        self.assertGreater(protein, 100)
        self.assertLess(protein, 150)


if __name__ == '__main__':
    unittest.main()
```

---

## Running Tests

### Run all tests:
```bash
python -m unittest test_calculator.py
```

### Run with verbose output:
```bash
python -m unittest test_calculator.py -v
```

### Run a specific test class:
```bash
python -m unittest test_calculator.TestCalculateBMR
```

### Run a specific test:
```bash
python -m unittest test_calculator.TestCalculateBMR.test_male_bmr_basic
```

---

## Common Assertions

| Assertion | What it checks |
|-----------|---------------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `x` is True |
| `assertFalse(x)` | `x` is False |
| `assertAlmostEqual(a, b, places=7)` | `a` and `b` are equal to `places` decimal places |
| `assertGreater(a, b)` | `a > b` |
| `assertLess(a, b)` | `a < b` |
| `assertIn(a, b)` | `a` is in `b` |
| `assertRaises(Error)` | Function raises `Error` |
| `assertIsNone(x)` | `x` is None |
| `assertIsNotNone(x)` | `x` is not None |

---

## Testing Functions with Input (Mocking)

Your `get_weight()` and `get_other_user_input()` functions use `input()`, which makes them harder to test. Use `unittest.mock` to simulate user input:

```python
from unittest.mock import patch

class TestGetWeight(unittest.TestCase):

    @patch('builtins.input', return_value='70')
    def test_get_weight_valid_input(self, mock_input):
        from protein_and_calorie_calculator import get_weight
        result = get_weight()
        self.assertEqual(result, 70)

    @patch('builtins.input', side_effect=['abc', '-5', '70'])
    def test_get_weight_invalid_then_valid(self, mock_input):
        """Test that invalid inputs are rejected before valid one."""
        from protein_and_calorie_calculator import get_weight
        result = get_weight()
        self.assertEqual(result, 70)
```

---

## Alternative: pytest (Recommended for New Projects)

`pytest` is a popular third-party testing framework that's simpler to use:

### Install:
```bash
pip install pytest
```

### Write tests (simpler syntax):
```python
# test_calculator_pytest.py
from protein_and_calorie_calculator import calculate_bmr, see_activity_level

def test_male_bmr():
    result = calculate_bmr(70, "male", 25, 175)
    expected = 88.362 + (13.397 * 70) + (4.799 * 175) - (5.677 * 25)
    assert abs(result - expected) < 0.01

def test_activity_level_sedentary():
    bmr, protein = see_activity_level(1000, 70, 1)
    assert bmr == 1200
    assert protein == 56
```

### Run:
```bash
pytest test_calculator_pytest.py -v
```

---

## Tips for Your Code

1. **Start with `calculate_bmr()` and `see_activity_level()`** - they're pure functions (no I/O), making them easy to test.

2. **Consider refactoring** - Extract validation logic into separate functions that can be tested:
   ```python
   def is_valid_weight(weight):
       return 0 < weight <= 1250
   ```

3. **Test the formulas** - Verify the BMR calculations match the Harris-Benedict equation.

4. **Test each activity level** - Make sure all 5 levels have correct multipliers.

---

## Next Steps

1. Create `test_calculator.py` in your project folder
2. Copy the example tests above
3. Run `python -m unittest test_calculator.py -v`
4. Add more tests for edge cases
5. Try using `pytest` for simpler syntax
