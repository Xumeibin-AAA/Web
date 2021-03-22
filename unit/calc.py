import sys, os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from Web.unit.db import connect, disconnect, execute


def login_judge(name, password):
    conn = connect()
    pwd = execute(conn, f"select pwd from user where Name='{name}';")
    try:
        if pwd[0][0] == password:
            data = execute(conn, f"select * from user;")
            s = ""
            for i in data:
                for j in i:
                    s = s + str(j) + ','
            data = {"Code": 200, "Msg": "OK", "data": s[:-1]}
            disconnect(conn)
            return data
        else:
            raise ValueError("error")
    except Exception as e:
        disconnect(conn)
        data = {"Code": 403, "Msg": "error"}
        return data




