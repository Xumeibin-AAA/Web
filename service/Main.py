import sys, os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from Web.unit.unit import md5, getpwd
from flask import Flask, request, jsonify, render_template, url_for, Response, redirect
from Web.service.manager import manager
from flask_cors import *
from datetime import timedelta
import uuid, time
from Web.unit.calc import login_judge
from Web.unit.db import update_cookie, get_sql_time, login_log, find_data, add_data, del_data, load, \
    update_book_list, book_count, update_image_list
from loguru import logger
from Web.unit.selfrsa import self_rsa, get_pwd

app = Flask(__name__, template_folder='../templates', static_folder="../", static_url_path="")
CORS(app, suppoorts_credentisls=True)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=60)
app.register_blueprint(manager)
re = ''
# 日志
logger.add(f"../data/Log/{time.strftime('%Y-%m-%d')}.log")


# 查找用户
@app.route('/static/find', methods=['GET', 'POST'])
def find():
    if request.method == "GET":
        if interceptor():
            data = find_data()
            logger.info(f"查询结果为:{data}")
            return render_template('find.html', data=data)
        else:
            return redirect(url_for('login'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    logger.info("添加用户")
    if interceptor():
        if request.method == "POST":
            name = request.form['name']
            password = request.form['password']
            password = md5(password)
            result = add_data(name, password)
            logger.info(f"添加{name}")
            return result
        else:
            return render_template("add.html")
    else:
        return redirect(url_for('login'))


# 主页面
@app.route('/', methods=['GET', 'POST'])
def main_page():
    logger.info("首次登录")
    if request.method == "GET":
        return redirect('login')


# 删除
@app.route('/static/del')
def delete():
    if interceptor():
        logger.info("开始删除用户")
        name = request.args.get('name')
        logger.info(f"删除{name}")
        msg = del_data(name)
        data = find_data()
        logger.info(f"删除返回值为{data}")
        return msg
    else:
        return redirect(url_for('login'))


# 获取book_name
@app.route('/load')
def book_name():
    if interceptor():
        name = request.args.get("name")
        content = load(name)
        name = name[:name.index("-")]
        logger.info("获取所有书列表")
        return render_template('content_page.html', data={"name": name, "content": content})
    else:
        return redirect(url_for('login'))


@app.route('/index', methods=['GET', 'POST'])
def index():
    name = request.args.get("user")
    r = redirect('main')
    uu = uuid.uuid4()
    cookie_id = md5(str(uu))
    update_cookie(cookie_id, time.time(), name)
    r.set_cookie(key='Cookie_id', value=cookie_id, max_age=10000)
    logger.info(f"生成cookie_id:{cookie_id}")
    return r


@app.route('/getkey')
def getkey():
    global re
    re = self_rsa()
    logger.info(f"RSA加密,公共钥匙为{re[0]}")
    return re[0]


@app.route('/main')
def main():
    if request.method == "GET":
        if interceptor():
            logger.info("更新数据库里内容")
            update_image_list()
            update_book_list()
            count = book_count()
            return render_template('main.html', data={"list": count})
        else:
            return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    global re
    if request.method == "GET":
        return render_template('index.html', data={"msg": '首次加载页面', "code": 404})
    if request.method == "POST":
        name = request.form['name']
        logger.info(f"{name}开始登录")
        password = request.form['password']
        arrs = getpwd(password)
        brr = []
        for arr in arrs:
            brr.append(chr(get_pwd(re[1], arr)))
        mingwen_pwd = ""
        for b in brr:
            mingwen_pwd+=b;
        data = login_judge(name, md5(mingwen_pwd))
        if data["Code"] == 403:
            logger.warning(f"{name}登录失败")
            return {"msg": '用户名或者密码错误', "code": 403}
        else:
            logger.info(f"{name}登录成功")
            login_log(name)
            return {"msg": 'succeed', "code": 200, "user": name}


# 更新数据库和文件小说列表
# @app.route('/update_book_list')
# def update_book_list():
#     if request.method == "GET":
#         if interceptor():
#             update_book_list()
#             data={"msg":"刷新成功","code":1}
#             logger.info("更新数据库和文件小说列表")
#             return data
#         else:
#             return redirect(url_for('login'))


# 拦截器
def interceptor():
    c = request.cookies.get('Cookie_id')
    save_cookie = get_sql_time(c)
    logger.info(f"当前cookie_id为:{c}")
    logger.info(f"数据库储存的用户cookie为:{save_cookie}")
    if c != "":
        if save_cookie:
            if time.time() - save_cookie < 1000:
                return True
            return False
    else:
        return False


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
