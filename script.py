import pandas as pd
import pytest

def test_CheckDuplicates():
    a=pd.read_csv("target.csv",sep=",")
    count=a.duplicated().sum()
    assert count == 0 , "Duplicate rows found"