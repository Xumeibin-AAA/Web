import time, pymysql, sys, os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from Web.unit.unit import getxml
from loguru import logger

'''
数据库操作
'''

logger.add(f"../data/Log/{time.strftime('%Y-%m-%d')}.log")


# 连接数据库

def connect():
    host = getxml('db', 'ip')
    port = int(getxml('db', 'port'))
    user = getxml('db', 'username')
    name = getxml('db', 'dbName')
    pwd = getxml('db', 'pwd')
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=name, charset='utf8')
        print(f"连接数据库{host}:{port}成功")
    except Exception  as e:
        print(f"连接数据库异常,异常信息为{e}")
    return conn


# 断开数据库
def disconnect(conn):
    try:
        conn.close()
        print("断开数据库成功")
    except Exception as e:
        print(f"断开数据库失败,异常信息为{e}")


# 执行sql语句
def execute(conn, sql):  # 连接相当于一条到数据库的路
    try:
        cursor = conn.cursor()  # 获取游标 相当于路上的一辆车
        cursor.execute(sql)
        conn.commit()  # 提交
        cursor.close()  # 关闭游标
        print(f"执行Sql语句{sql}成功")
        return cursor.fetchall()
    except Exception as e:
        print(f"执行Sql语句{sql}失败,异常信息为{e}")


# 更新用户的cookie信息
def update_cookie(cookie, time, user):
    conn = connect()
    temp = execute(conn, f"update USER set cookie='{cookie}',save_time='{time}' where Name='{user}'")
    disconnect(conn)
    print(temp)


# 获取cookie的保存时间
def get_sql_time(cookie):
    conn = connect()
    temp = execute(conn, f"select save_time from USER where cookie='{cookie}'")
    disconnect(conn)
    if len(temp):
        return temp[0][0]
    else:
        return False


# 保存用户登录的日志
def login_log(user,request_headers):
    conn = connect()
    execute(conn, f"INSERT INTO login_log(name,login_time,user_inf) VALUES ('{user}','{time.strftime('%Y-%m-%d %H:%M:%S')}','{request_headers}');")
    disconnect(conn)


# 查看用户
def find_data():
    conn = connect()
    data = execute(conn, f"select * from user;")
    s = ""
    x = 1
    for i in data:
        if x == 1:
            s = str(x) + ',' + s
        else:
            s = s + str(x) + ','
        x = x + 1
        for j in i:
            s = s + str(j) + ','
    data = {"Code": 200, "Msg": "OK", "data": s[:-1]}
    disconnect(conn)
    return data


# 添加用户
def add_data(name, pwd):
    conn = connect()
    data = execute(conn, f'insert into user(Name,pwd) values("{name}","{pwd}")')
    print(data)
    if data == ():
        disconnect(conn)
        return {"msg": "ok"}
    else:
        disconnect(conn)
        return {"msg": "error"}


# 删除用户
def del_data(name):
    conn = connect()
    data = execute(conn, f'delete from user where Name="{name}"')
    print(data)
    if data == ():
        disconnect(conn)
        return {"msg": "ok"}
    else:
        disconnect(conn)
        return {"msg": "error"}


# 获取所有小说总数
def book_count():
    conn = connect()
    count = execute(conn, 'select count(name) from book_list')
    return count[0][0]


# 获取所有图片总数
def image_count():
    conn = connect()
    count = execute(conn, 'select count(name) from image_list')
    return count[0][0]


# 获取分页小说
def book_list_page(page):
    conn = connect()
    min = (int(page) * 10) - 10
    max = 10
    name_list = execute(conn, f'select name from book_list limit {min},{max}')
    arr = []
    for i in name_list:
        arr.append(i[0])
    return arr


# 获取分页图片
def image_list_page(page):
    conn = connect()
    min = (int(page) * 30) - 30
    max = 30
    name_list = execute(conn, f'select name from image_list limit {min},{max}')
    arr = []
    for i in name_list:
        arr.append(i[0])
    return arr


# 获取小说在服务器中的路径
def load(name):
    path = f'../data/Novels/load/{name}.txt'
    with open(path, mode="r", encoding='utf8') as file:
        content = file.readlines()
        file.close()
    return content


# 更新数据库和文件里面的内容
def update_book_list():
    con = connect()
    sql = "TRUNCATE TABLE book_list;"
    execute(con, sql=sql)
    for root, dir, files in os.walk("../data/Novels"):
        for file in files:
            print(file[:-4])
            sql = f'INSERT INTO book_list(name) VALUES("{file[:-4]}");'
            r = execute(con, sql=sql)
    disconnect(con)


# 更新数据库和文件里面的内容
def update_image_list():
    con = connect()
    sql = "TRUNCATE TABLE image_list;"
    execute(con, sql=sql)
    for root, dir, files in os.walk("../data/Image"):
        for file in files:
            print(file[:-4])
            sql = f'INSERT INTO image_list(name) VALUES("{file[:-4]}");'
            r = execute(con, sql=sql)
    disconnect(con)


if __name__ == '__main__':
    r = update_image_list()
    print(r)
