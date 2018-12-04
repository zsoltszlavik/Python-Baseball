import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import *
from stats import attendance

@pytest.mark.test_imports_module1
def test_imports_module1():
    assert 'os' in dir(attendance), 'Have you imported the `os` built-in library?'
    assert 'pd' in dir(attendance), 'Have you imported `pandas` as `pd`?'
    assert 'plt' in dir(attendance), 'Have you imported the `matplotlib.pyplot` as `plt`?'

@pytest.mark.test_event_files_module1
def test_event_files_module1():
    pass

@pytest.mark.test_loop_through_files_module1
def test_loop_through_files_module1():
    pass

@pytest.mark.test_open_event_files_module1
def test_app_import_flask_module1():
    pass

@pytest.mark.test_loop_through_lines_module1
def test_app_import_flask_module1():
    pass

@pytest.mark.test_find_attendances_module1
def test_app_import_flask_module1():
    pass

@pytest.mark.test_pandas_dataframe_module1
def test_app_import_flask_module1():
    pass

@pytest.mark.test_convert_to_numeric_module1
def test_app_import_flask_module1():
    pass

@pytest.mark.test_plot_dataframe_module1
def test_app_import_flask_module1():
    pass

@pytest.mark.test_formatting_and_mean_module1
def test_app_import_flask_module1():
    pass
