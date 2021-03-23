import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from loguru import logger
from Web.unit.db import get_sql_time, update_cookie


def interceptor(request):
    cookie_id = request.cookies.get('Cookie_id')
    username = request.cookies.get('username')
    save_cookie = get_sql_time(cookie_id)
    logger.info(f"当前用户名为:{username}")
    logger.info(f"当前cookie_id为:{cookie_id}")
    logger.info(f"数据库储存的用户cookie为:{save_cookie}")
    # 更新数据库里面user的最新保存时间
    update_cookie(cookie_id, time.time(), username)
    if cookie_id != "":
        if save_cookie:
            logger.info(f"现在的时间戳:{time.time()}")
            logger.info(f"数据库保存的时间戳:{save_cookie}")
            if time.time() - save_cookie < 1000:
                return True
            return False
    else:
        return False