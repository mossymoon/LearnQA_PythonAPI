import requests
import pytest

class TestCookies2:
    def test_cookies_home(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie", cookies={})

        print(response.cookies)

        cookie_dict = {'value'}
        assert "value" in cookie_dict, "Cookies haven't been collected right"

        print()









