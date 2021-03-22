import random,base64,pyprimes
def ed(e,n):
    while True:
        rand = random.randint(n,n*10)
        if((e*rand)% n) == 1:
            return rand

def barck_zhishu():
    r = random.randint(100, 200)
    while True:
        s = int(str(r)[-1])
        if s % 2 == 0:
            r = r + 1
        if pyprimes.isprime(r):
            return r
        else:
            r = r + 1
def get_disaffinity_2_zhishu():
    while True:
        z1 = barck_zhishu()
        z2 = barck_zhishu()
        if z1!=z2:
            return [z1, z2]
def self_rsa():
    z = get_disaffinity_2_zhishu()
    publicKeyModulus = z[0]*z[1]
    n1 = (z[0]-1)*(z[1]-1)
    publicKeyExponent = 65537
    privateKeyModulus = ed(publicKeyExponent,n1)
    return [{"publicKeyModulus":hex(publicKeyModulus)[2:],"publicKeyExponent":hex(publicKeyExponent)[2:]},{"privateKeyModulus":hex(privateKeyModulus)[2:],"publicKeyModulus":hex(publicKeyModulus)[2:]}]

def set_pwd(public,pwd):
    c = pwd**int(public["publicKeyExponent"],16)%int(public["publicKeyModulus"],16)
    return c
def get_pwd(private,pwd):
    m = (pwd**int(private["privateKeyModulus"],16))%int(private["publicKeyModulus"],16)
    return m

if __name__ == '__main__':
    r = self_rsa()
    print(r)
    a = set_pwd(r[0],9999)
    print(a)
    b = get_pwd(r[1],a)
    print(b)
