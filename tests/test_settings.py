import sys
import os
import pytest

from settings import Settings

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

# test_settings.py


def test_valid_environment():
    settings = Settings(ENVIRONMENT="dev", APP_NAME="TestApp")
    assert settings.ENVIRONMENT == "dev"


def test_invalid_environment():
    with pytest.raises(ValueError):
        Settings(ENVIRONMENT="invalid_env", APP_NAME="TestApp")


def test_valid_app_name():
    settings = Settings(ENVIRONMENT="prod", APP_NAME="MyApp")
    assert settings.APP_NAME == "MyApp"


def test_invalid_app_name():
    with pytest.raises(ValueError):
        Settings(ENVIRONMENT="test", APP_NAME="")
