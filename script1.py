import pytest
import pandas as pd


# Sample Data: Simulating an Extracted DataFrame
@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'id': [1 , 2 , 3 , 4] ,
        'name': ['Alice' , 'Bob' , 'Charlie' , 'David'] ,
        'salary': [1000 , 2000 , 3000 , 4000]
    })


# Sample Transformation: Increase salary by 10%
def transform_data(df):
    df['salary'] = df['salary'] * 1.10
    return df


# Test case to validate transformation
def test_transform_data(sample_data):
    transformed_df = transform_data(sample_data)

    # Check if salary increased by 10%
    assert transformed_df['salary'].iloc[0] == 1100  # Alice's salary after transformation
    assert transformed_df['salary'].iloc[1] == 2200  # Bob's salary after transformation


# Test case for data validation
def test_data_validation(sample_data):
    assert sample_data.shape == (4 , 3)  # Check the number of rows and columns
    assert sample_data['salary'].dtype == int  # Ensure the salary column has integer values