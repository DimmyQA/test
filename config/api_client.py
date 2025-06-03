from requests import Request, Session

class ApiClient:
    def __init__(self):
        self.session = Session()

    def send_request(self, url, method, headers=None, payload=None, query_params=None):
        req = Request(method=method, url=url, headers=headers, data=payload, params=query_params)
        prep_req = self.session.prepare_request(req)
        response = self.session.send(prep_req, timeout=5)
        return response

    def close_conn(self):
        self.session.close()