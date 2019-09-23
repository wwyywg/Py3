import hashlib
import datetime

KEY_VALUE = "Itcast"

if __name__ == '__main__':
    # m = hashlib.md5()  # 创建hash对象，md5
    # print(m)
    # m.update("itcast".encode("utf-8"))
    # print(m.hexdigest())
    now = datetime.datetime.now()
    m = hashlib.md5()
    str = '%s%s' %(KEY_VALUE, now.strftime("%Y%m%d"))
    print(str)
    m.update(str.encode("utf-8"))
    value = m.hexdigest()
    print(value)
