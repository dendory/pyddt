import pyddt

a = pyddt.DDT()
a.set_schema({'name': "STR", 'creation': "DATETIME", 'active': "BOOLEAN", 'password': "HASH"})
print("Schema: " + str(a.get_schema()))
print(a.get(a.add({'name': "sdfsd sddf", 'creation': "2015-12-15 10:23:12", 'active': "true", 'password': "test1234"})))
print(a.get(a.add({'name': "dffgdf werewew", 'creation': "2011-02-12 02:43:12", 'active': 0, 'password': "123"})))
a.save("test.ddt")
b = pyddt.DDT()
b.load("test.ddt")
print(str(b._data))
