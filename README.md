# easy_object

### Easy operations over object in serialized file form
#### Install :
    pip install easy_object
     or 
    pip3 install easy_object

#### Usage :
    import easy_object as eo
    
    a = 'hello world'
    path = 'testing_file'
    
    eo.osave(path,a)
    b = eo.oopen(path)

    print(b)
