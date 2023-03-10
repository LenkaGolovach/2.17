#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import os



def get_shop(shops, name, product, price):
    shops.append({
        'name': name,
        'product': product,
        'price': price,
    })
    return shops


def display_shops(shops):
    """
    Отображает данные о товаре в виде таблицы и
    Сортирует данные, по названию маганзина
    """
    if shops:
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
        for idx, shop in enumerate(shops, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(

                    idx,
                    shop.get('name', ''),
                    shop.get('product', ''),
                    shop.get('price', 0)

                )
            )
            print(line)


def select_shops(shops, name):
    """
    По заданому магазину находит товары, находящиеся в нем,
    если магазина нет - показывает соответсвующее сообщение
    """
    cout = 0
    for shop in shops:
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


def save_shops(file_name, shops):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(shops, fout, ensure_ascii=False, indent=4)
        print("Данные сохранены")


def load_shops(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        loadfile = json.load(fin)
    return loadfile


def main(command_line=None):
    """
    главная функция программы
    """
    # Создать родительский парсер для определения имени файла.
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="The data file name"
    )
    # Создать основной парсер командной строки.
    parser = argparse.ArgumentParser("shops")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")
    # Создать субпарсер для добавления магазина.
    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new product"
    )
    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        help="The shop's name"
    )
    add.add_argument(
        "-p",
        "--product",
        action="store",
        help="The shop's product"
    )
    add.add_argument(
        "-pr",
        "--price",
        action="store",
        type=int,
        required=True,
        help="The price of product"
    )
    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all product"
    )
    # Создать субпарсер для выбора работников.
    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Select the shops"
    )
    select.add_argument(
        "-s",
        "--selected shop",
        required=True,
        help="The selected shop product"
    )

    args = parser.parse_args(command_line)

    is_dirty = False
    if os.path.exists(args.filename):
        shops = load_shops(args.filename)
    else:
        shops = []
    if args.command == "add":
        shops = get_shop(
            shops,
            args.name,
            args.product,
            args.price
        )
        is_dirty = True
    elif args.command == 'display':
        display_shops(shops)
    elif args.command == 'select ':
        display_shops(select_shops(shops, args.name))

    if is_dirty:
        save_shops(args.filename, shops)


if __name__ == '__main__':
    main()