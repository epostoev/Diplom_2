import pytest
from data import URLS
from methods.users_methods import UserMethods
from methods.order_methods import OrderMethods
from helpers import generate_user_data


@pytest.fixture
def users_methods():
    return UserMethods(url=f"{URLS.BASE_URL}")


@pytest.fixture
def new_user(users_methods):
    user_data = generate_user_data()
    yield user_data
    body, _ = users_methods.login(user_data["email"], user_data["password"])
    token = body.get("accessToken")
    if token:
        body, status_code = users_methods.delete_user(token)


@pytest.fixture
def registered_user(users_methods):
    user_data = generate_user_data()
    body, _ = users_methods.create_user(
        user_data["name"],
        user_data["password"],
        user_data["email"],
    )
    token = body.get("accessToken")
    yield {**user_data, "token": token}
    if token:
        body, status_code = users_methods.delete_user(token)


@pytest.fixture
def order_methods():
    return OrderMethods(url=f"{URLS.BASE_URL}")


@pytest.fixture
def ingredients(order_methods):
    body, _ = order_methods.get_orders()
    items = body.get("data", [])
    result = [item["_id"] for item in items[:2]]
    return result
