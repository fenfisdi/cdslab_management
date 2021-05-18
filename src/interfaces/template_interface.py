from src.models.db_models.template import Template


class TemplateInterface:

    @staticmethod
    def find_one(name: str) -> Template:
        filters = dict(
            name__exact=name
        )

        return Template.objects(**filters).first()
