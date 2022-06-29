
from connection import connect_to_db
from task_a import avg_sum
from task_b import max_month
from task_c import useful_item
from task_d import top_3

conn, curr = connect_to_db()


def show_top3(top):
    for i in top:
        print(f'Индекс - {i[0]}, сумма - {i[1]}')


if __name__ == '__main__':
    print(f'Задание A: \n'
          f'Пользователь в диапазоне\n'
          f'18-25 {avg_sum(curr, 18, 25)} \n'
          f'26-35 {avg_sum(curr, 26, 35)}\n')
    print(f'Задание B:\n'
          f'Самая большая выручка в от людей 35+\n'
          f'Была в  {max_month(curr, 2020)} месяце, 2020 года\n')
    print(f'Задание С:\n'
          f'Наибольший вклад в выручку за последний год принёс\n'
          f'Товар под индексом {useful_item(curr)}\n')
    # print(f'Задание D:\n'
    #       f'Топ три товара за 2020:')
    # show_top3(top_3(curr, 2020))

