#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


def get_shop(shops_load, name, product, price, file_name):
    shops_load.append({
        'name': name,
        'product': product,
        'price': price,
    })
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(shops_load, fout, ensure_ascii=False, indent=4)
    return shops_load


def display_shops(shops_load):
    """
    Отображает данные о товаре в виде таблицы и
    Сортирует данные, по названию маганзина
    """
    if shops_load:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 8,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Название.",
                "Товар",
                "Цена"
            )
        )
        print(line)
        for idx, shop in enumerate(shops_load, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(

                    idx,
                    shop.get('name', ''),
                    shop.get('product', ''),
                    shop.get('price', 0)

                )
            )
            print(line)


def select_shops(shops_load, name):
    """
    По заданому магазину находит товары, находящиеся в нем,
    если магазина нет - показывает соответсвующее сообщение
    """
    cout = 0
    for i, shop in enumerate(shops_load, 1):
        if (shop.get('name') == name):
            cout = 1
            print(
                ' | {:<5} | {:<5} '.format(
                    shop.get('product', ''),
                    shop.get('price', 0),
                )
            )
        elif cout == 0:
            print("Такого магазина нет")


def load_shops(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        loadfile = json.load(fin)
    return loadfile


@click.command()
@click.option("-c", "--command")
@click.argument('file_name')
@click.option("-n", "--name")
@click.option("-p", "--product")
@click.option("-pr", "--price")
def main(command, name, product, price, file_name):
    shops_load = load_shops(file_name)
    if command == 'add':
        get_shop(shops_load, name, product, price, file_name)
        click.secho('Данные добавлены')
    elif command == 'display':
        display_shops(shops_load)
    elif command == 'select':
        select_shops(shops_load, name)


if __name__ == '__main__':
    main()