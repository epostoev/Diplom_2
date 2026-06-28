# Diplom_2 — API-тесты для Stellar Burgers

API-тесты для системы заказа бургеров Stellar Burgers.  
Покрыты сценарии создания пользователей, авторизации, обновления данных, создания и получения заказов.

## Список реализованных тестов

### 👤 Создание пользователя (`TestCreateUsers`)

| Тест | Описание |
|:---|:---|
| `test_create_user_success` | Проверяет успешное создание нового пользователя: статус `200` и `success: true` в ответе. |
| `test_create_user_already_exists` | Проверяет, что повторная регистрация существующего пользователя возвращает ошибку `403`. |
| `test_create_user_missing_field` | **Параметризованный тест (3 кейса):** Проверяет, что создание пользователя без обязательного поля (`name`, `password`, `email`) возвращает ошибку `403`. |

### 🔑 Логин пользователя (`TestLoginUsers`)

| Тест | Описание |
|:---|:---|
| `test_login_user_success` | Проверяет успешный логин существующего пользователя: статус `200` и наличие `accessToken` в ответе. |
| `test_login_wrong` | **Параметризованный тест (3 кейса):** Проверяет, что логин с неверным email, неверным паролем или обоими сразу возвращает ошибку `401`. |

### ✏️ Изменение данных пользователя (`TestUpdateUsers`)

| Тест | Описание |
|:---|:---|
| `test_update_user_with_auth` | **Параметризованный тест (3 кейса):** Проверяет успешное обновление полей пользователя (`name`, `password`, `email`) с авторизацией: статус `200` и `success: true`. |
| `test_update_user_no_auth` | **Параметризованный тест (3 кейса):** Проверяет, что обновление данных без авторизации возвращает ошибку `401` с сообщением `You should be authorised`. |

### 🧾 Создание заказа (`TestCreateOrder`)

| Тест | Описание |
|:---|:---|
| `test_order_create_with_auth_and_ingredients` | Проверяет успешное создание заказа с авторизацией и ингредиентами. |
| `test_order_create_without_auth_and_with_ingredients` | Проверяет создание заказа без авторизации, но с ингредиентами. |
| `test_order_create_with_auth_without_ingredients` | Проверяет, что создание заказа без ингредиентов возвращает ошибку `400`. |
| `test_order_create_without_auth_and_without_ingredients` | Проверяет, что создание заказа без авторизации и без ингредиентов возвращает ошибку `400`. |
| `test_order_create_with_invalid_ingredient_hash` | Проверяет, что создание заказа с невалидными хешами ингредиентов возвращает ошибку `400`. |

### 📋 Получение заказов пользователя (`TestGetUserOrders`)

| Тест | Описание |
|:---|:---|
| `test_get_orders_with_auth` | Проверяет успешное получение заказов авторизованным пользователем. |
| `test_get_orders_without_auth` | Проверяет, что получение заказов без авторизации возвращает ошибку `401`. |

---

## 🛠 Технические особенности реализации

- **Фикстуры** — в `conftest.py` реализованы фикстуры `registered_user`, `new_user`, `order_methods`, `users_methods`, `ingredients`. Фикстуры с созданием пользователя автоматически удаляют его после теста через `yield` (teardown).
- **Allure-отчёты** — каждый тест и класс размечен декораторами `@allure.suite` и `@allure.title` для формирования читаемых отчётов. В тестах используются `allure.step` для детализации шагов.
- **Method Object** — логика запросов вынесена в классы `UserMethods` и `OrderMethods`, тесты не содержат прямых вызовов `requests`.
- **Генерация данных** — функция `generate_user_data()` из модуля `helpers` создаёт уникальные данные пользователя для каждого теста, исключая пересечения.
- **Паттерн AAA** — каждый тест разделён на блоки Arrange, Act, Assert.

---

## 🚀 Запуск проекта

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
```bash
pytest -v
```

### Запуск с генерацией Allure-отчёта
```bash
pytest --alluredir=allure_results
allure serve allure_results
```

---

## 📁 Структура проекта

```
Diplom_2/
├── methods/
│   ├── __init__.py
│   ├── users_methods.py
│   └── order_methods.py
├── tests/
│   ├── users/
│   │   ├── __init__.py
│   │   ├── test_login.py
│   │   ├── test_register.py
│   │   └── test_update_user.py
│   └── orders/
│       ├── __init__.py
│       ├── test_order_auth_ing.py
│       └── test_get_user_orders.py
├── conftest.py
├── data.py
├── helpers.py
├── Makefile
├── requirements.txt
└── README.md
```