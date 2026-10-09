from app.main import get_human_age


def test_should_return_zeros_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_ages_are_less_than_15() -> None:
    assert get_human_age(1, 1) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_are_from_15_to_23() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(20, 20) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_ages_are_from_24_to_27() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_cat_should_get_extra_year_every_four_years() -> None:
    assert get_human_age(28, 0) == [3, 0]
    assert get_human_age(31, 0) == [3, 0]
    assert get_human_age(32, 0) == [4, 0]


def test_dog_should_get_extra_year_every_five_years() -> None:
    assert get_human_age(0, 28) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(0, 33) == [0, 3]
    assert get_human_age(0, 34) == [0, 4]


def test_should_calculate_cat_and_dog_independently() -> None:
    assert get_human_age(28, 15) == [3, 1]
    assert get_human_age(15, 28) == [1, 2]


def test_should_convert_big_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
