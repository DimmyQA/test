from config.api_client import ApiClient

api_client = ApiClient()
url = 'https://restful-booker.herokuapp.com/booking/1'
response = api_client.send_request(method='GET', url=url)

print(response.json())
api_client.close_conn()


