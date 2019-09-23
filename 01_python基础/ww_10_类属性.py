class People(object):
    country = 'china'

print(People.country)
p = People()
print(p.country)
p.country = 'japan'
print(p.country)
print(People.country)
del p.country
print(p.country)