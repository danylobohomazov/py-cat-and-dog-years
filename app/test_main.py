# flake8: noqa: *
import pytest

from app.main import get_human_age
from app.errors import OutOfRangeError

@pytest.mark.parametrize(
    'human_cat_age,human_dog_age,expected_result',
    [
        pytest.param(13, 13, [0, 0], id="Ages < 15"),
        pytest.param(22, 22, [1, 1], id="Ages >= 15 and Ages < 24"),
        pytest.param(100, 100, [21, 17], id="Ages >= 24"),
    ])
def test_logic_for_different_ages(human_cat_age, human_dog_age, expected_result) -> None:
    assert get_human_age(human_cat_age, human_cat_age) == expected_result


@pytest.mark.parametrize(
    'human_cat_age,human_dog_age,expected_result',
    [
        pytest.param(-13, 13, OutOfRangeError, id="Negative numbers"),
        pytest.param(2222, 2222, OutOfRangeError, id="Very Large number"),
        pytest.param("2222", 2222, TypeError, id="Wrong type"),
    ])
def test_logic_for_incorrect_numbers(human_cat_age, human_dog_age, expected_result) -> None:
    with pytest.raises(expected_result):
        get_human_age(human_cat_age, human_dog_age)