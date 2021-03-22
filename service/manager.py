import sys, os, time

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from flask import request
from loguru import logger
from flask import Blueprint, render_template, redirect, url_for
from werkzeug.datastructures import FileStorage, ImmutableMultiDict
from werkzeug.useragents import UserAgent
from Web.unit.db import book_list_page, book_count, image_list_page, image_count, get_sql_time

manager = Blueprint('manager', __name__)
# 日志
logger.add(f"../data/Log/{time.strftime('%Y-%m-%d')}.log")


@manager.route('/manager/add_book', methods=['GET', 'POST'])
def add_book():
    if interceptor():
        if request.method == "POST":
            data: FileStorage
            rr = request
            form: ImmutableMultiDict
            data = request.files.get("aaa")
            file_name = data.filename
            data.save(rf"..\data\Novels\load\{file_name}")
            user_agent: UserAgent
            user_agent = request.user_agent
            print(user_agent)
            print(type(user_agent))
            return user_agent.string
        else:
            return render_template("add_book.html")
    else:
        return redirect(url_for('login'))

# book分页
@manager.route('/manager/get_page', methods=['GET', 'POST'])
def get_page():
    page = request.args.get("page")
    Type = request.args.get("type")
    logger.info(f"数据类型为:{Type}")
    logger.info(f"页码为:{page}")
    if interceptor():
        if Type == "book":
            result = book_list_page(page)
            return str(result)
        elif Type == "image":
            result = image_list_page(page)
            return str(result)
    else:
        return redirect(url_for('login'))

# 总数
@manager.route('/manager/count', methods=['GET', 'POST'])
def count():
    if interceptor():
        count_sum = book_count()
        print(count_sum)
        return str(count_sum)
    else:
        return redirect(url_for('login'))

# 显示所有图片
@manager.route('/manager/show_image', methods=['GET', 'POST'])
def show_image():
    if interceptor():
        count = image_count()
        return render_template('main_image.html', data={"list": count})
    else:
        return redirect(url_for('login'))


# 显示单个页面
@manager.route('/manager/show_sole_image', methods=['GET', 'POST'])
def show_sole_image():
    if interceptor():
        name = request.args.get("name")
        return render_template('show_sole_image.html', data={"name": name})
    else:
        return redirect(url_for('login'))
# 显示单个页面
@manager.route('/manager/show_video', methods=['GET', 'POST'])
def show_video():
    # name = request.args.get("name")
    name = "Tom"
    return render_template('show_video.html', data={"name": name})


# 显示单个页面
@manager.route('/manager/open_camera', methods=['GET', 'POST'])
def open_camera():
    # name = request.args.get("name")
    name = "Tom"
    return render_template('open_camera.html', data={"name": name})


# 拦截器
def interceptor():
    c = request.cookies.get('Cookie_id')
    save_cookie = get_sql_time(c)
    logger.info(f"当前cookie_id为:{c}")
    logger.info(f"数据库储存的用户cookie为:{save_cookie}")
    if c != "":
        if save_cookie:
            if time.time() - save_cookie < 100:
                return True
            return False
    else:
        return False
