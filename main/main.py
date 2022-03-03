from flask import Blueprint, render_template, request
from .data_search import search

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', static_folder='static')


@main_blueprint.route('/')
def main_page():
    """Страница поиска постов, Начальная страница"""
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_post():
    """Поиск постов по строке"""
    search_str = request.args.get('s')
    posts_to_return = search(search_str.strip())
    if posts_to_return:
        search_str = f'Посты по запросу {search_str.title()}'
    else:
        search_str = f'Посты по запросу {search_str} не найдены'

    return render_template('post_list.html', posts_to_return=posts_to_return, search_str=search_str)

