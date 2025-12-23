import asyncio
import json

from models import Menu
from storage import upload_json_to_s3
from downloader import download_all
from serializer import serialize_menu_to_json


async def main() -> None:
    with open('input_data.json', 'r') as file:
        urls = json.load(file)['url']

    downloaded_files = await download_all(urls)

    menu = Menu()
    for file_name in downloaded_files:
        with open(file_name, 'r') as file:
            menu.add_combo(json.load(file))

    serialized_file = serialize_menu_to_json(menu)

    upload_json_to_s3(
        file_path=serialized_file,
        bucket_name='my-bucket',
        object_name=serialized_file,
    )


if __name__ == '__main__':
    asyncio.run(main())
