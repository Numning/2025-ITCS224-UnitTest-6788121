import unittest

def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age: {age}"

class TestChildAge(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a child.")
                self.assertEqual(result, "Child")
                
class TestAdultAge(unittest.TestCase):
    def test_adult_age(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"\n{age} is considered as an adult.")
                self.assertEqual(result, "Adult")

class TestGoldenAge(unittest.TestCase):
    def test_adult_age(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"\n{age} is considered as a golden age.")
                self.assertEqual(result, "Golden age")                

if __name__ == "__main__":
    unittest.main(verbosity=2)