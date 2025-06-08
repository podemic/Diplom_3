import allure
import requests

from scr.constants import BaseUrl


class StellarBurgersAPI:
    @staticmethod
    @allure.step('Запрос на авторизацию пользователя')
    def login_user(email, password):
        url = f"{BaseUrl.BASE_URL}/auth/login"
        payload = {"email": email, "password": password}
        return requests.post(url, json=payload)

    @staticmethod
    @allure.step("Запрос на удаление пользователя")
    def delete_user(token, email, password, name):
        url = f"{BaseUrl.BASE_URL}/auth/register"
        headers = {"Authorization": token}
        payload = {"email": email, "password": password, "name": name}
        return requests.delete(url, json=payload, headers=headers)