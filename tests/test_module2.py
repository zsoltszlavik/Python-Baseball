import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import *
from stats import attendance

@pytest.mark.test_import_pandas_module2
def test_import_pandas_module2():
    pass

@pytest.mark.test_import_matplotlib_module2
def test_import_matplotlib_module2():
    pass

@pytest.mark.test_import_games_dataframe_module2
def test_import_games_dataframe_module2():
    pass

@pytest.mark.test_select_attendance_module2
def test_select_attendance_module2():
    pass

@pytest.mark.test_column_labels_module2
def test_column_labels_module2():
    pass

@pytest.mark.test_convert_to_numeric_module2
def test_convert_to_numeric_module2():
    pass

@pytest.mark.test_plot_dataframe_module2
def test_plot_dataframe_module2():
    pass

@pytest.mark.test_axis_labels_module2
def test_axis_labels_module2():
    pass

@pytest.mark.test_mean_line_module2
def test_mean_line_module2():
    pass
