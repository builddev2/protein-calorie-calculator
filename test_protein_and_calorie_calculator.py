import unittest
from protein_and_calorie_calculator import calculate_bmr, calculate_tdee, calculate_protein

class TestCalculatingBMR(unittest.TestCase):
    def test_male_bmr_calculation(self):
        # Arrange: Set up test data
        weight = 24
        gender = "male"
        age = 8
        height = 135

        # Act: Call the function
        result = calculate_bmr(weight, gender, age, height)

        # Assert: Check the result using Mifflin-St Jeor equation
        # Expected: (10 * 24) + (6.25 * 135) - (5 * 8) + 5
        # = 240 + 843.75 - 40 + 5 = 1048.75
        self.assertAlmostEqual(result, 1048.75, places=2)

    def test_female_bmr_calculation(self):
        # ARRANGE - Set up your test data
        weight = 68
        gender = "female"
        age = 42
        height = 166

        # ACT - Execute the code being tested
        result = calculate_bmr(weight, gender, age, height)

        # ASSERT - Verify the result using Mifflin-St Jeor equation
        # Expected: (10 * 68) + (6.25 * 166) - (5 * 42) - 161
        # = 680 + 1037.5 - 210 - 161 = 1346.5
        expected_female_answer = (10 * 68) + (6.25 * 166) - (5 * 42) - 161
        self.assertAlmostEqual(result, expected_female_answer, places=2)

class TestTDEECalculation(unittest.TestCase):
    def test_activity_level_1_sedentary(self):
        tdee = calculate_tdee(1000, 1)
        self.assertAlmostEqual(tdee, 1200)  # 1000 * 1.2

    def test_activity_level_2_lightly_active(self):
        tdee = calculate_tdee(1000, 2)
        self.assertAlmostEqual(tdee, 1375)  # 1000 * 1.375

    def test_activity_level_3_moderately_active(self):
        tdee = calculate_tdee(1000, 3)
        self.assertAlmostEqual(tdee, 1550)  # 1000 * 1.55

    def test_activity_level_4_very_active(self):
        tdee = calculate_tdee(1000, 4)
        self.assertAlmostEqual(tdee, 1725)  # 1000 * 1.725

    def test_activity_level_5_extremely_active(self):
        tdee = calculate_tdee(1000, 5)
        self.assertAlmostEqual(tdee, 1900)  # 1000 * 1.9

class TestProteinCalculation(unittest.TestCase):
    def test_activity_level_1_sedentary(self):
        protein = calculate_protein(70, 1)
        self.assertAlmostEqual(protein, 56)  # 0.8 * 70

    def test_activity_level_2_lightly_active(self):
        protein = calculate_protein(70, 2)
        self.assertAlmostEqual(protein, 77)  # 1.1 * 70

    def test_activity_level_3_moderately_active(self):
        protein = calculate_protein(70, 3)
        self.assertAlmostEqual(protein, 98)  # 1.4 * 70

    def test_activity_level_4_very_active(self):
        protein = calculate_protein(70, 4)
        self.assertAlmostEqual(protein, 133)  # 1.9 * 70

    def test_activity_level_5_extremely_active(self):
        protein = calculate_protein(70, 5)
        self.assertAlmostEqual(protein, 140)  # 2.0 * 70 (adjusted from 2.5)

if __name__ == "__main__":
    unittest.main()
