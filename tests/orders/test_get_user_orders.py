import allure
from data import ErrorMessages

@allure.suite('Получение заказов пользователя')
class TestGetUserOrders:

    @allure.title('Получение заказов авторизованным пользователем')
    def test_get_orders_with_auth(self, order_methods, registered_user):
        token = registered_user["token"]
        body, status_code = order_methods.get_user_orders(token=token)
        assert (status_code == 200 and body.get(
            "success") is True and "orders" in body)

    @allure.title('Получение заказов неавторизованным пользователем')
    def test_get_orders_without_auth(self, order_methods):
        body, status_code = order_methods.get_user_orders()
        assert (status_code == 401 and body.get("success")
                is False and body.get("message") == ErrorMessages.NOT_AUTHORISED)
