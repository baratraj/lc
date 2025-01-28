import pyspark.sql.functions as F

def determine_skewness(df):
    """
    Determines the skewness of each numerical column in a Spark DataFrame.

    Args:
        df (pyspark.sql.DataFrame): The Spark DataFrame to analyze.

    Returns:
        dict: A dictionary mapping column names to their distribution types (Evenly Distributed, Left Tailed, Right Tailed).
    """

    skewness_dict = {}
    for col in df.columns:
        if df.dtypes[col] in ('int', 'double', 'float'):  # Check for numerical columns
            skewness = F.skewness(df[col]).collect()[0][0]
            if abs(skewness) <= 0.5:
                skewness_dict[col] = "Evenly Distributed"
            elif skewness < -0.5:
                skewness_dict[col] = "Left Tailed"
            else:
                skewness_dict[col] = "Right Tailed"
        else:
            skewness_dict[col] = "Not Numerical"  # Handle non-numerical columns

    return skewness_dict
