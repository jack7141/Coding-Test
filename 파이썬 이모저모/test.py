from urllib.parse import urljoin


class ABCUpdater:
    token = None
    endpoint = None

    @property
    def headers(self):
        return self.get_headers()

    @property
    def url(self):
        return self.get_base_url()

    def get_headers(self, **kwargs):
        headers = {
            'Authorization': f"Token {self.token}"
        }
        return headers

    def get_base_url(self, **kwargs):
        base = 'https://dev-litchi.fount.co'
        api_url = urljoin(base, self.endpoint)
        return api_url


class AccountUpdater(ABCUpdater):
    # 부모 클래스의 변수와 이름을 맞춰, 오버라이딩하거나 하위의 방식처럼 따로 변수를 지정하고, 데코레이터로 프로퍼티로 선언해서 할 수도 있음
    def __init__(self, token, endpoint):
        self.litch_token = token
        self.litch_endpoint = endpoint

    @property
    def token(self):
        return self.litch_token

    @property
    def endpoint(self):
        return self.litch_endpoint

    def get_accounts(self, params=None):
        print(self.headers)
        print(self.url)


updater = AccountUpdater(token='tes123123t', endpoint='/api/v2/swagger')
updater.get_accounts()


ABCUpdater.token = 'zzzzztest'
ABCUpdater.endpoint = '/api/v1/swagger'
updater = ABCUpdater()
print(updater.get_headers())
print(updater.get_base_url())
