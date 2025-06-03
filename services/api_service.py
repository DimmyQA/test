from config.api_client import ApiClient
from services.endpoints import Endpoints

class APIService:
    def __init__(self):
        self.api_client = ApiClient()

    def get_booking(self, id):
        response = self.api_client.send_request(
            url=Endpoints.get_booking(id),
            method='GET'
        )
        return response
