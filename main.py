import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def load_secrets(path="secrets.yaml"):
    with open(path, "r") as file:
        secrets = yaml.safe_load(file)
    return secrets


def export_envs(environment: str = "dev") -> None:
    match environment:
        case "dev":
            load_dotenv(".env.dev")
        case "test":
            load_dotenv(".env.test")
        case "prod":
            load_dotenv(".env.prod")
        case _:
            raise ValueError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)

    secrets = load_secrets()
    print("API_KEY: ", secrets["fake_api"])
