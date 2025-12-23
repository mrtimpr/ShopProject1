# 🛍 ShopProject1

**ShopProject1** — это учебный Python-проект магазина, реализующий работу с товарами и категориями через классы, загрузку данных из JSON и тестирование кода с помощью pytest.

---

## 📌 Оглавление

- 💡 Обзор  
- 🚀 Быстрый старт  
- 📁 Структура проекта  
- 📦 Установка  
- 🧠 Использование  
- 📊 Формат JSON  
- 🧪 Тестирование  
- 📋 Классы  
- 🧩 Авторы и лицензия

---

## 💡 Обзор

Проект содержит:
- модели `Product` и `Category` для товаров и категорий;
- функцию для загрузки данных из JSON;
- примеры использования;
- тесты с `pytest`.

---

## 🚀 Быстрый старт

Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone https://github.com/mrtimpr/ShopProject1.git
cd ShopProject1
```

## 📁 Структура проекта
```
ShopProject1/
├── data/
│   └── products.json
├── src/
│   ├── models.py
│   └── utils.py
├── tests/
│   └── test_models.py
├── main.py
├── requirements.txt
└── README.md
```

## 📦 Установка

Создайте виртуальное окружение (рекомендуется):
```
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

Установите зависимости:
```
pip install -r requirements.txt
```

## 🧠 Использование

Запуск примера из main.py:
```
python main.py
```

Пример загрузки и использования категорий из JSON:
```
from src.utils import load_categories_from_json

categories = load_categories_from_json("data/products.json")
for category in categories:
    print(category.name, len(category.products))
```
## 📊 Формат JSON

Исходный файл data/products.json должен иметь формат:
```
[
  {
    "name": "Смартфоны",
    "description": "Описание категории",
    "products": [
      {
        "name": "Название товара",
        "description": "Описание товара",
        "price": 123.45,
        "quantity": 10
      }
    ]
  }
]
```
## 🧪 Тестирование

В проекте используются тесты на базе pytest. Запуск:
```
pytest
```

Тесты проверяют:

- инициализацию классов;

- корректное количество категорий и товаров;

- работу загрузчика JSON.

## 📋 Классы
### 📦 Product

Представляет товар с полями:

- name: str — название

- description: str — описание

- price: float — цена

- quantity: int — количество

### 🗂 Category

Представляет категорию товаров с полями:

- name: str — название

- description: str — описание

- products: List[Product] — список товаров этой категории

Также хранит классовые счётчики:

- Category.category_count — количество категорий

- Category.product_count — общее число товаров

## 🧩 Авторы и лицензия

Этот проект по лицензии MIT .