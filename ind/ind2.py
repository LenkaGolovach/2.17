#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


@click.group()
def group():
    pass


@group.command()
@click.argument('file_name')
@click.option("-n", "--name")
@click.option("-p", "--product")
@click.option("-pr", "--price")
def get_shop(file_name, name, product, price,):
    shops_load = load_shops(file_name)
    shops_load.append({
        'name': name,
        'product': product,
        'price': price,
    })
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(shops_load, fout, ensure_ascii=False, indent=4)
    return shops_load


@group.command()
@click.argument('file_name')
def display_shops(file_name):
    """
    Отображает данные о товаре в виде таблицы и
    Сортирует данные, по названию маганзина
    """
    shops_load = load_shops(file_name)
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


@group.command()
@click.argument('file_name')
@click.option("-n", "--name")
def select_shops(file_name, name):
    """
    По заданому магазину находит товары, находящиеся в нем,
    если магазина нет - показывает соответсвующее сообщение
    """
    shops_load = load_shops(file_name)
    cout = 0
    for i, shop in enumerate(shops_load, 1):
        if shop.get('name') == name:
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


if __name__ == '__main__':
    group()
