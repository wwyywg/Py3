class People(object):
    country = 'china'

    # 类方法，用classmethod来进行修饰
    @classmethod
    def setCountry(cls, country):
        cls.country = country

    @staticmethod
    def getCountry():
        return People.country

    @classmethod
    def getCountry(cls):
        return cls.country

p = People()
print(p.getCountry())   #可以用过实例对象引用
print(People.getCountry())  #可以通过类对象引用

p.setCountry('japan')
print(p.getCountry())
print(People.getCountry())

print(People.getCountry())