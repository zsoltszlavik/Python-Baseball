import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import *

from stats import offense

@pytest.mark.test_select_all_plays_module4
def test_select_all_plays_module4():
    assert 'plays:games:games:type:play' in get_assignments(offense), ''
    assert 'plays:columns:type:inning:team:player:count:pitches:event:game_id:year' in get_assignments(offense), ''

@pytest.mark.test_select_only_hits_module4
def test_select_only_hits_module4():
    assert 'hits:plays:loc:plays:event:str:contains:^(?:S(?!B)|D|T|HR):inning:event' in get_assignments(offense), ''

@pytest.mark.test_convert_column_type_module4
def test_convert_column_type_module4():
    assert 'hits:loc:None:None:None:inning:pd:to_numeric:hits:loc:None:None:None:inning' in get_assignments(offense), ''

@pytest.mark.test_replace_dictionary_module4
def test_replace_dictionary_module4():
    assert 'replacements:^S(.*):^D(.*):^T(.*):^HR(.*):single:double:triple:hr' in get_assignments(offense), ''

@pytest.mark.test_replace_function_module4
def test_replace_function_module4():
    assert 'hit_type:hits:event:replace:replacements:regex:True' in get_assignments(offense), ''

@pytest.mark.test_add_a_new_column_module4
def test_add_a_new_column_module4():
    assert 'hits:hits:assign:hit_type:hit_type' in get_assignments(offense), ''

@pytest.mark.test_group_by_inning_and_hit_type_module4
def test_group_by_inning_and_hit_type_module4():
    assert 'hits:hits:groupby:inning:hit_type:size:reset_index:name:count' in get_assignments(offense), ''

@pytest.mark.test_convert_hit_type_to_categorical_module4
def test_convert_hit_type_to_categorical_module4():
    assert 'hits:hit_type:pd:Categorical:hits:hit_type:single:double:triple:hr' in get_assignments(offense), ''

@pytest.mark.test_sort_values_module4
def test_sort_values_module4():
    assert 'hits:hits:sort_values:inning:hit_type' in get_assignments(offense), ''

@pytest.mark.test_reshape_with_pivot_module4
def test_reshape_with_pivot_module4():
    assert 'hits:hits:pivot:index:inning:columns:hit_type:values:count' in get_assignments(offense), ''

@pytest.mark.test_stacked_bar_plot_module4
def test_stacked_bar_plot_module4():
    assert 'hits:plot:bar:stacked:True' in get_calls(offense), ''
    assert 'plt:show' in get_calls(offense), ''
