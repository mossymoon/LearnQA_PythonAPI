import json
import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        print(response.text)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
        print(response.text)

    #тест1_Создание пользователя с некорректным email - без символа @
    def test_create_user_with_invalid_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_incorrect_email(response, 'Invalid email format')
        assert response.text == "Invalid email format"
        Assertions.assert_code_status(response, 400)

        print(response.text)

    #тест2 Создание пользователя без указания одного из полей
class TestUserDifferentNames:
    names = [
        (""),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]
    @pytest.mark.parametrize('username, firstName, lastName, email, password', names)
    def test_new_user_no_par(self, username, firstName, lastName, email, password):

        url = "https://playground.learnqa.ru/api/user/"
        data = {"username": username, "firstName": firstName, "lastName": lastName, "email": email, "password": password}

        response = requests.post(url, data=data)
        obj = json.loads(response.text)

        assert obj.post("username") == username
        assert obj.post("firstName") == firstName
        assert obj.post("lastName") == lastName

    # тест3 Создание пользователя с очень коротким именем в один символ
    def test_create_user_with_short_name(self):
        username = '1'
        data = self.prepare_registration_data(username)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_incorrect_email(response, 'Invalid email format')
        assert response.text == "User name is too short"
        Assertions.assert_code_status(response, 400)

        print(response.text)
    # тест4 Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_name(self):
        username = len(250)
        data = self.prepare_registration_data(username)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_incorrect_email(response, 'Invalid email format')
        assert response.text == "User name is too long"
        Assertions.assert_code_status(response, 400)

        print(response.text)