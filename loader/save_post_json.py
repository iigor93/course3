import json


def save_post(image_link, post_text):
    """Запись в файл"""
    file_name = 'posts.json'
    post_ = {'pic': image_link, 'content': post_text}

    with open(file_name, 'r', encoding='UTF-8') as file:
        try:
            file_data = json.load(file)
        except json.decoder.JSONDecodeError:
            return False
        else:
            file_data.append(post_)

    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(file_data, file, ensure_ascii=False)
    return True
