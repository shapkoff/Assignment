import json
import os

from dataclasses import asdict

from models import Menu


def serialize_menu_to_json(menu: Menu) -> str:
    menu_dict = asdict(menu)

    base_name = 'serialized_menu'
    counter = 0
    filename = f'{base_name}.json'

    while os.path.exists(filename):
        counter += 1
        filename = f'{base_name}_{counter}.json'

    with open(filename, 'w') as file:
        json.dump(menu_dict, file)

    return filename
