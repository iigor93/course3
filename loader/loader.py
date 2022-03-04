from flask import Blueprint, render_template, request
from .save_post_json import save_post
from .is_picture import is_pic
import logging


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')
logging.basicConfig(filename='log.log', level=logging.INFO)


@loader_blueprint.route('/post/', methods=['GET'])
def loader_view():
    """Обработка запроса GET. форма создания поста"""
    return render_template('post_form.html')


@loader_blueprint.route('/post_p/', methods=['POST'])
def loader_post():
    """ Запрос POST. создание поста"""
    pic = request.files.get('picture')
    if is_pic(pic.filename):
        post_text = request.values.get('content')
        try:
            pic.save(f'uploads/images/{pic.filename}')
        except:
            logging.error(f'Ошибка загрузки файла')
            return 'Ошибка загрузки файла'
        image_link = f'../uploads/images/{pic.filename}'
        if save_post(image_link, post_text) is False:
            return 'Ошибка сохранения поста'

        return render_template('post_uploaded.html', post_text=post_text, image_link=image_link)
    logging.info(f'Загруженный файл не является картинкой')
    return 'Загруженный файл не является картинкой'
