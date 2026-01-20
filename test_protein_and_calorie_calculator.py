import unittest
from protein_and_calorie_calculator import calculate_bmr, see_activity_level

class TestCalculatingBMR(unittest.TestCase):
    def test_male_bmr_calculation(self):
        # Arrange: Set up test data
        weight = 24
        gender = "male"
        age = 8
        height = 135

        # Act: Call the function
        result = calculate_bmr(weight, gender, age, height)

        # Assert: Check the result
        # Expected: 88.362 + (13.397 * 24) + (4.799 * 135) - (5.677 * 8)
        # = 88.362 + 321.528 + 647.865 - 45.416 = 1012.3390000000002
        self.assertAlmostEqual(result, 1012.3390000000002, places=9)
    def test_female_bmr_calculation(self):
        # ARRANGE - Set up your test data
        weight = 68
        gender = "female"
        age = 42
        height = 166

        # ACT - Execute the code being tested
        result = calculate_bmr(weight, gender, age, height)

        # ASSERT - Verify the result
        expectedfemaleanswer = 447.593 + (9.247 * 68) + (3.098 * 166) - (4.33 * 42)
        self.assertAlmostEqual(result, expectedfemaleanswer, places=4)

class TestBMRMutiplierAndProtein(unittest.TestCase):
    def test_activity_level_1_multiplier(self):
        bmr, protein = see_activity_level(1000, 70, 1)
        self.assertAlmostEqual(bmr, 1200)  # 1000 * 1.2
    def test_activity_level_1_protein(self):
        bmr, protein = see_activity_level(1000, 70, 1)
        self.assertAlmostEqual(protein, 56)  # 0.8 * 70

    def test_activity_level_2_multiplier(self):
        bmr, protein = see_activity_level(1000, 70, 2)
        self.assertAlmostEqual(bmr, 1375)  # 1000 * 1.375
    def test_activity_level_2_protein(self):
        bmr, protein = see_activity_level(1000, 70, 2)
        self.assertAlmostEqual(protein, 77)  # 1.1 * 70

    def test_activity_level_3_multiplier(self):
        bmr, protein = see_activity_level(1000, 70, 3)
        self.assertAlmostEqual(bmr, 1550)  # 1000 * 1.55
    def test_activity_level_3_protein(self):
        bmr, protein = see_activity_level(1000, 70, 3)
        self.assertAlmostEqual(protein, 98)  # 1.4 * 70

if __name__ == "__main__":
    unittest.main()
