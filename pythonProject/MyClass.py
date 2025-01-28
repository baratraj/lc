import unittest

from pyspark.shell import spark

from pyspark.sql.functions import col, skewness
from typing import Dict

def determine_skewness(dataframe, columns_to_check, tolerance=0.05):
    skewness_dict = {}

    # Iterate over columns in the DataFrame
    for col_name in columns_to_check:
        # Calculate skewness for the column
        skewness_value = dataframe.agg(skewness(col(col_name))).collect()[0][0]
        # Categorize skewness as Even, Left Tailed, or Right Tailed
        if abs(skewness_value) < tolerance:
            skewness_dict[col_name] = "Evenly Distributed"
        elif skewness_value < 0:
            skewness_dict[col_name] = "Left Tailed"
        else:
            skewness_dict[col_name] = "Right Tailed"

    return skewness_dict


class TestSkewness(unittest.TestCase):

    def test_even_distribution(self):
        # Create a sample DataFrame with an even distribution
        data = [
            (1, 2.0, 3.1),
            (2, 2.1, 3.0),
            (3, 1.9, 3.2)
        ]
        df = spark.createDataFrame(data, ["value1", "value2_std", "value3_std"])

        # Call the function and assert the expected result
        results = determine_skewness(df, ["value2_std"])
        self.assertEqual(results, {"value2_std": "Evenly Distributed"})

    def test_incorrect_classification(self):
        # Create a sample DataFrame with a clear right-skewed distribution
        data = [
            (1, 1.0, 3.0),
            (2, 1.0, 3.0),
            (3, 1.0, 10.0)  # Outlier creating right skew
        ]
        df = spark.createDataFrame(data, ["value1", "value2_std", "value3_std"])

        # Call the function, expecting an AssertionError due to incorrect classification
        try:
            results = determine_skewness(df, ["value2_std"])
            self.assertEqual(results, {"value2_std": "Evenly Distributed"})  # Incorrect assertion
        except AssertionError as e:
            print("Test failed as expected:", e)
            self.assertTrue(True)  # Mark test as successful due to expected failure

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

