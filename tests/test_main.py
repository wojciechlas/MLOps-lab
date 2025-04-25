import os
import sys
import pytest
from unittest.mock import patch, mock_open
from main import load_secrets, export_envs

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)


def test_load_secrets():
    mock_yaml_content = """
    fake_api: test_api_key
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_content)):
        with patch("yaml.safe_load", return_value={"fake_api": "test_api_key"}):
            secrets = load_secrets("mock_secrets.yaml")
            assert secrets["fake_api"] == "test_api_key"


@pytest.mark.parametrize(
    "environment, expected_env_file",
    [
        ("dev", ".env.dev"),
        ("test", ".env.test"),
        ("prod", ".env.prod"),
    ],
)
@patch("main.load_dotenv")
def test_export_envs(mock_load_dotenv, environment, expected_env_file):
    export_envs(environment)
    mock_load_dotenv.assert_called_once_with(expected_env_file)


def test_export_envs_invalid_environment():
    with pytest.raises(ValueError):
        export_envs("invalid_env")
