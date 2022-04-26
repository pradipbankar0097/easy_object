import easy_object as eo
a = 'hello world'
path = 'testing_file'
eo.osave(path,a)

b = eo.oopen(path)

print(b)
