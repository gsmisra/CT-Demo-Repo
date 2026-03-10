import pytest


def test_always_passes():
    assert True


def test_basic_math():
    assert 1 + 1 == 2


def test_string_contains():
    assert "demo" in "ct-demo-repo"


if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q"]))