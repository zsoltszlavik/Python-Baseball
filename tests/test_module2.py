import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import get_assignments, get_calls
from stats import attendance

@pytest.mark.test_import_pandas_module2
def test_import_pandas_module2():
    assert 'pd' in dir(attendance), 'Have you imported `pandas` as `pd`?'

@pytest.mark.test_import_matplotlib_module2
def test_import_matplotlib_module2():
    assert 'plt' in dir(attendance), 'Have you imported `matplotlib.pyplot` as `plt`?'

@pytest.mark.test_import_games_dataframe_module2
def test_import_games_dataframe_module2():
    assert 'games' in dir(attendance), 'Have you imported `games` from `data`?'

@pytest.mark.test_select_attendance_module2
def test_select_attendance_module2():
    assert 'attendance:Name:games:Name:loc:Attribute:games:Name:type:Str:Index:Subscript:Eq:info:Str:Compare:BitAnd:games:Name:multi2:Str:Index:Subscript:Eq:attendance:Str:Compare:BinOp:year:Str:multi3:Str:List:Tuple:Index:Subscript:Assign' in get_assignments(attendance, include_type=True) or 'attendance:Name:games:Name:loc:Attribute:games:Name:multi2:Str:Index:Subscript:Eq:attendance:Str:Compare:BitAnd:games:Name:type:Str:Index:Subscript:Eq:info:Str:Compare:BinOp:year:Str:multi3:Str:List:Tuple:Index:Subscript:Assign' in get_assignments(attendance, include_type=True), 'Have you selected the attendance rows with `loc[]`.'

@pytest.mark.test_column_labels_module2
def test_column_labels_module2():
    assert 'attendance:columns:year:attendance' in get_assignments(attendance), 'Have you changed the column labels to `year` and `attendance`.'

@pytest.mark.test_convert_to_numeric_module2
def test_convert_to_numeric_module2():
    assert 'pd:to_numeric:attendance:loc:None:None:None:attendance' in get_calls(attendance), 'Convert the `attendance` column values from strings to numbers.'

@pytest.mark.test_plot_dataframe_module2
def test_plot_dataframe_module2():
    assert 'attendance:plot:x:year:y:attendance:figsize:15:7:kind:bar' in get_calls(attendance), 'Plot the `year` on the x-axis and the `attendance` on the y-axis of a bar plot. Adjust the size of the plot.'
    assert 'plt:show' in get_calls(attendance), 'Have you shown the plot?'

@pytest.mark.test_axis_labels_module2
def test_axis_labels_module2():
    assert 'plt:xlabel:Year' in get_calls(attendance), 'Label the x-axis: Year'
    assert 'plt:ylabel:Attendance' in get_calls(attendance), 'Label the y-axis: Attendance'

@pytest.mark.test_mean_line_module2
def test_mean_line_module2():
    assert 'plt:axhline:y:attendance:attendance:mean:label:Mean:linestyle:--:color:green' in get_calls(attendance), 'Plot a green dashed line at the mean.'
