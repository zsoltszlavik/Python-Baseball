import pytest

from .utils import *

from stats import attendance


@pytest.mark.test_imports_module1
def test_imports_module1():
    assert 'Flask' in dir(app), 'Have you imported the `Flask` class from `flask`?'
    assert inspect.isclass(app.Flask), '`Flask` is not a class.'
    assert 'render_template' in dir(app), '`render_template` has not been imported.'
    assert inspect.isfunction(app.render_template), '`render_template` is not a function.'

@pytest.mark.test_event_files_module1
def test_event_files_module1():

@pytest.mark.test_loop_through_files_module1
def test_loop_through_files_module1():

@pytest.mark.test_open_event_files_module1
def test_app_import_flask_module1():

@pytest.mark.test_loop_through_lines_module1
def test_app_import_flask_module1():

@pytest.mark.test_find_attendances_module1
def test_app_import_flask_module1():

@pytest.mark.test_pandas_dataframe_module1
def test_app_import_flask_module1():

@pytest.mark.test_convert_to_numeric_module1
def test_app_import_flask_module1():

@pytest.mark.test_plot_dataframe_module1
def test_app_import_flask_module1():

@pytest.mark.test_formatting_and_mean_module1
def test_app_import_flask_module1():
