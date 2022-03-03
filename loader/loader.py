from flask import Blueprint, render_template, request
from .save_post_json import save_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')


@loader_blueprint.route('/post/', methods=['GET'])
def loader_view():
    """Обработка запроса GET. форма создания поста"""
    return render_template('post_form.html')


@loader_blueprint.route('/post_p/', methods=['POST'])
def loader_post():
    """ Запрос POST. создание поста"""
    pic = request.files.get('picture')
    post_text = request.values.get('content')
    pic.save(f'uploads/images/{pic.filename}')
    image_link = f'../uploads/images/{pic.filename}'
    save_post(image_link, post_text)

    return render_template('post_uploaded.html', post_text=post_text, image_link=image_link)
