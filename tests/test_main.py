#
# file to tests shared functions file pnlp_functions.py
#
import sys
from pathlib import Path
import pytest
import pandas as pd


# example of test that is skipped
@pytest.mark.skip(reason="Test needs to be implemented")
def test_my_function():
    return

# example of test that passes
def test_var_1():
    tmpvar = 1
    assert tmpvar == 1

# example of test that fails
def test_var_2():
    tmpvar = 1
    assert tmpvar == 0