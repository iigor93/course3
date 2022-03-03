import json


def save_post(image_link, post_text):
    """Запись в файл"""
    file_name = 'posts.json'
    post_ = {'pic': image_link, 'content': post_text}

    with open(file_name, 'r', encoding='UTF-8') as file:
        file_data = json.load(file)
        print(type(file_data))
        print(file_data)
        file_data.append(post_)
        print(type(file_data))
        print(file_data)
        #json.dump(file_data, file, ensure_ascii=False)

    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(file_data, file, ensure_ascii=False)
    return 2
