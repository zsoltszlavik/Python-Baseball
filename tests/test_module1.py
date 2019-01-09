import pytest

from .utils import *

from stats import data

# ['glob:glob:os:path:join:os:getcwd:games:*.EVE', 'game_files:sort', 'pd:read_csv:game_file:names:type:multi2:multi3:multi4:multi5:multi6:event', 'game_frames:append:game_frame', 'pd:concat:game_frames', 'games:multi2:str:extract:(.LS(\\d{4})\\d{5})', 'identifiers:fillna:method:ffill', 'pd:concat:games:identifiers:axis:1:sort:False', 'games:fillna: ', 'pd:Categorical:games:loc:None:None:None:type']


@pytest.mark.test_import_builtin_libraries_module1
def test_import_builtin_libraries_module1():
    assert 'os' in dir(data), 'Have you imported the `os` built-in library?'
    assert 'glob' in dir(data), 'Have you imported the `os` built-in library?'

@pytest.mark.test_import_pandas_module1
def test_import_pandas_module1():
    assert 'pd' in dir(data), 'Have you imported `pandas` as `pd`?'

@pytest.mark.test_python_file_management_module1
def test_python_file_management_module1():
    assert 'game_files:glob:glob:os:path:join:os:getcwd:games:*.EVE' in get_assignments(data), 'Do you have a `glob.glob()` function call with the correct arguments?'

@pytest.mark.test_sorting_file_names_module1
def test_sorting_file_names_module1():
    assert 'game_files:sort' in get_calls(data), 'Are you sorting the `game_files` in-place with sort()?'

@pytest.mark.test_read_csvs_module1
def test_read_csvs_module1():
    assert len(get_for_loops(data, 'dict')) != 0, 'Do you have a for loop that loops through the `game_files`?'
    assert get_for_loops(data, 'dict')[0]['target:id'] == 'game_file' and get_for_loops(data, 'dict')[0]['iter:id'] == 'game_files', 'Do you have a for loop that loops through the `game_files`?'
    assert get_for_loops(data, 'dict')[0]['body'] == 'game_frame:pd:read_csv:game_file:names:type:multi2:multi3:multi4:multi5:multi6:event:game_frames:append:game_frame', 'Do you have a for loop that loops through the `game_files`?'

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
