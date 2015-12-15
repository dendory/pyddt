import pyddt

a = pyddt.DDT()
a.set_schema({'a':"STR", 'b':"datetime", 'c':"ARRAY"})
print(str(a.get_schema()))
c = a.add({'a': "sdfsd sddf", 'b': "2015-12-15 10:23:12", 'c': [3,2,23]})
print(a.add({'a': "dffgdf werewew", 'b': "2011-02-12 02:43:12", 'c': [5,12]}))
print(str(a.get(c)))
a.remove(c)


