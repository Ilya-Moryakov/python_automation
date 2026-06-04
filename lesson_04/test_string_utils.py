import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("   skypro", "skypro"),
    (" ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro ", "skypro "),
    ("sky pro", "sky pro"),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("Skypro", "o", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "Z", False),
    ("Skypro", "", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Skypro", "S", "kypro"),
        ("Skypro", "k", "Sypro"),
        ("Skypro", "o", "Skypr"),
        ("Skypro", "Sky", "pro"),
        ("Skypro", "pro", "Sky"),
    ],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        (None, "Skypro", AttributeError),
        (99999, "99", AttributeError),
    ],
)
def test_delete_symbol_negative(input_str, symbol, expected):
    with pytest.raises(expected):
        string_utils.delete_symbol(input_str, symbol)