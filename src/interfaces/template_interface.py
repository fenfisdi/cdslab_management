from src.models.db_models.template import Template


class TemplateInterface:

    @staticmethod
    def find_one() -> Template:
        return Template.objects().first()
