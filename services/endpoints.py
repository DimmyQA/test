from config.base_url import base_url


class Endpoints:

    @staticmethod
    def get_booking(id):
        return f'{base_url}booking/{id}'