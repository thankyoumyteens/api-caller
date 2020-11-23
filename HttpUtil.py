import requests


class HttpResponse:
    def __init__(self, body, headers):
        self.body = body
        self.headers = headers


class HttpUtil:

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.193 Safari/537.36'
        }

    def set_header(self, key, value):
        self.headers[key] = value

    def set_headers(self, headers):
        self.headers = headers

    def set_cookies(self, cookies):
        # k=v;k=v;k=v
        self.headers['Cookie'] = cookies

    def clear_cookies(self):
        if 'Cookie' in self.headers:
            del self.headers['Cookie']

    def set_json_request_header(self):
        self.headers['Content-Type'] = 'application/json'

    def set_bearer_auth_token(self, key, token):
        self.headers[key] = 'bearer {}'.format(token)

    def post_json(self, url, params):
        self.set_json_request_header()
        r = requests.post(url, json=params, headers=self.headers)
        try:
            text = r.json()
        except ValueError:
            text = r.text
        return HttpResponse(text, r.headers)
