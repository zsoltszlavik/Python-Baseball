import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import *
from stats import data

@pytest.mark.test_import_builtin_libraries_module1
def test_import_builtin_libraries_module1():
    assert 'os' in dir(data), 'Have you imported the `os` built-in library?'
    assert 'pd' in dir(data), 'Have you imported `pandas` as `pd`?'
    assert 'plt' in dir(data), 'Have you imported the `matplotlib.pyplot` as `plt`?'

@pytest.mark.test_import_builtin_libraries_module1
def test_import_builtin_libraries_module1():
    pass

@pytest.mark.test_import_pandas_module1
def test_import_pandas_module1():
    pass

@pytest.mark.test_python_file_management_module1
def test_python_file_management_module1():
    pass

@pytest.mark.test_glob_function_arguments_module1
def test_glob_function_arguments_module1():
    pass

@pytest.mark.test_sorting_file_names_module1
def test_sorting_file_names_module1():
    pass

@pytest.mark.test_read_csvs_module1
def test_read_csvs_module1():
    pass

@pytest.mark.test_read_csv_arguments_module1
def test_read_csv_arguments_module1():
    pass

@pytest.mark.test_append_event_frames_module1
def test_append_event_frames_module1():
    pass

@pytest.mark.test_concatenate_dataframes_module1
def test_concatenate_dataframes_module1():
    pass

@pytest.mark.test_clean_values_module1
def test_clean_values_module1():
    pass

@pytest.mark.test_extract_identifiers_module1
def test_extract_identifiers_module1():
    pass

@pytest.mark.test_forward_fill_identifiers_module1
def test_forward_fill_identifiers_module1():
    pass

@pytest.mark.test_rename_columns_module1
def test_rename_columns_module1():
    pass

@pytest.mark.test_concatenate_identifier_columns_module1
def test_concatenate_identifier_columns_module1():
    pass

@pytest.mark.test_fill_nan_values_module1
def test_fill_nan_values_module1():
    pass

@pytest.mark.test_categorical_event_type_module1
def test_categorical_event_type_module1():
    pass

@pytest.mark.test_print_dataframe_module1
def test_print_dataframe_module1():
    pass
