import random


class GameEngine:

    # Diccionario dinámico de configuración
    LEVELS = {
        "easy": {
            "points": 1,
            "description": "Modo fácil"
        },

        "normal": {
            "points": 2,
            "description": "Modo normal"
        },

        "hard": {
            "points": 3,
            "description": "Modo difícil"
        }
    }

    @staticmethod
    def clean_country_list(countries):
        """
        Recibe una lista enviada desde JavaScript
        y elimina datos inválidos o duplicados.
        """

        if not isinstance(countries, list):
            return []

        cleaned = []

        for country in countries:

            if not isinstance(country, str):
                continue

            country = country.strip()

            if country and country not in cleaned:
                cleaned.append(country)

        return cleaned

    @classmethod
    def choose_country(cls, countries):
        countries = cls.clean_country_list(countries)

        if not countries:
            return None

        return random.choice(countries)

    @staticmethod
    def check_answer(target, clicked):
        if not target or not clicked:
            return False

        return target.lower().strip() == clicked.lower().strip()