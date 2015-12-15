import pyddt

a = pyddt.DDT()
a.set_schema({'a':"STR", 'b':"Date"})
print(str(a.get_schema()))
c = a.add({'a': "sdfsd sddf", 'b': "2015-12-15"})
print(a.add({'a': "dffgdf werewew", 'b': "2011-02-12"}))
print(str(a.get(c)))
a.remove(c)


