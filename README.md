# SQL_tasks
Задачи на SQL-запросы для анализа продаж:

<connetction.py> - Фукнция подключения к таблицам
<fill_tabs.py> - Генерация данных и заполненеия таблиц
<answers.py> - Выполнения задания

Структура данных в таблицах

1) Users(userId, age)
2) Purchases (purchaseId, userId, itemId, date)
3) Items (itemId, price).

Задание:
Написать SQL запросы для расчета следующих метрик:

a) какую сумму в среднем в месяц тратит:
- пользователи в возрастном диапазоне от 18 до 25 лет включительно
- пользователи в возрастном диапазоне от 26 до 35 лет включительно

b) в каком месяце года выручка от пользователей в возрастном диапазоне 35+ самая большая

c) какой товар обеспечивает  наибольший вклад в выручку за последний год

d) топ-3 товаров по выручке и их доля в общей выручке за любой год
