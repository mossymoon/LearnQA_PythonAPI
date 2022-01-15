import requests
import pytest

class TestHeaders2:
    def test_headers_home(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header", headers={"x-secret-homework-header" : "some secret header"})

        print(response.headers)

        assert "x-secret-homework-header" in response.headers, "There is no secret in headers"

        print()




