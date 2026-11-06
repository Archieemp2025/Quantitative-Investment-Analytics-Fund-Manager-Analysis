import sys
from pathlib import Path
import numpy as np
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from analytics import metrics

def test_constant_positive_returns_have_zero_drawdown():
    r=pd.Series([.001]*100)
    b=pd.Series([.0005]*100)
    assert abs(metrics(r,b)['max_drawdown']) < 1e-10

def test_beta_one_for_identical_series():
    r=pd.Series([.01,-.02,.005,.008,-.003])
    assert np.isclose(metrics(r,r)['beta'],1)

def test_rejects_insufficient_observations():
    import pytest
    with pytest.raises(ValueError):metrics(pd.Series([.01]),pd.Series([.01]))
