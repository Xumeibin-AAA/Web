from hashlib import md5
import uuid
import string


def public_key():
    '''
    生成随机密码
    @return: 随机密码
    '''
    key = md5(uuid.uuid4().bytes).hexdigest()
    return key
if __name__ == '__main__':
    public = int(public_key(),16)
    pwd = 'as '
    s = pwd.encode()
    print(s)
    ss = [i for i in s]
    print(ss)
    # print(string.printable)
    # print(public)
    # p = public*s
    # print(p)
    # print(hex(p)[2:])
    # h = hex(p)[2:]
    # p1 = int(h,16)
    # print(int(p1/public))


