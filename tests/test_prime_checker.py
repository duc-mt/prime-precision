from unittest.mock import patch

import pytest

import main
import prime_checker_functions as func


def test_is_prime_a() -> None:
    assert func.is_prime_a(2) is True
    assert func.is_prime_a(3) is True
    assert func.is_prime_a(4) is False
    assert func.is_prime_a(1) is False
    assert func.is_prime_a(0) is False
    assert func.is_prime_a(-5) is False
    assert func.is_prime_a(97) is True


def test_is_prime_b() -> None:
    assert func.is_prime_b(2) is True
    assert func.is_prime_b(3) is True
    assert func.is_prime_b(4) is False
    assert func.is_prime_b(1) is False
    assert func.is_prime_b(0) is False
    assert func.is_prime_b(-5) is False
    assert func.is_prime_b(97) is True


def test_is_prime_c() -> None:
    assert func.is_prime_c(2) is True
    assert func.is_prime_c(3) is True
    assert func.is_prime_c(4) is False
    assert func.is_prime_c(1) is False
    assert func.is_prime_c(0) is False
    assert func.is_prime_c(-5) is False
    assert func.is_prime_c(97) is True


def test_prime_lessthan(capsys: pytest.CaptureFixture[str]) -> None:
    func.prime_lessthan(func.is_prime_a)
    captured = capsys.readouterr()
    assert "In a list of all prime numbers less than 10,000:" in captured.out
    assert "The first ten are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]" in captured.out


def test_line(capsys: pytest.CaptureFixture[str]) -> None:
    func.line()
    captured = capsys.readouterr()
    assert (
        "-----------------------------------------------------------------------"
        in captured.out
    )


@patch("builtins.input", return_value="97")
def test_main_valid_input(
    mock_input: object, capsys: pytest.CaptureFixture[str]
) -> None:
    main.main()
    captured = capsys.readouterr()
    assert "A program to check if a number is prime." in captured.out
    assert "97 is True" in captured.out
    assert "Function A: time taken =" in captured.out


@patch("builtins.input", return_value="abc")
def test_main_invalid_input(
    mock_input: object, capsys: pytest.CaptureFixture[str]
) -> None:
    main.main()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter an integer." in captured.out
