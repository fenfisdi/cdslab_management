from src.models.db_models import Configuration


class ConfigurationInterface:

    @staticmethod
    def find_one() -> Configuration:
        return Configuration.objects().first()
