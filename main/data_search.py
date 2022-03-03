import json


def search(post_str):
    """Поиск постов в файле по заданной строке"""
    file_name = 'posts.json'
    posts_to_return = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        data_file = json.load(file)

    if post_str:
        for item in data_file:
            if post_str.strip().lower() in item.get('content').lower():
                posts_to_return.append(item)

    return posts_to_return
