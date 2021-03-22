import logging,time
import sys
import xml.dom.minidom
import hashlib


def getxml(element_name, parameter):
    dom = xml.dom.minidom.parse('../inf/db.xml')
    data = dom.documentElement
    temp = data.getElementsByTagName(element_name)
    return temp[0].getAttribute(parameter)


def md5(pwd):
    p = hashlib.md5()
    p.update(pwd.encode('utf-8'))
    return p.hexdigest()

def remainder(p1,p2,p3):
    '''
    计算一个数的的幂次方后取余
    @param p1: 底数
    @param p2: 幂
    @param p3: 取余数
    @return: 余数
    '''
    result = 1
    for i in range(p2):
        result = result*p1%p3

    return result
def getpwd(pwd):
    arr = []
    j = 0
    for i in range(len(pwd)):
        l = int(pwd[len(pwd) - i - 1:len(pwd) - i])
        if l != 0:
            l = j+l
            arr.append(pwd[j:l])
            j = l
        else:
            return arr

if __name__ == '__main__':
    url = getxml('db', 'url')
    print(url)
