import inspect

class Class1():
    a = 12 + 17

def introspection_info(item):
    a = type(item)
    b = dir(item)
    attributes = []
    methods = []
    for attr in dir(item):
        if callable(getattr(item, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    d = inspect.getmodule(item)
    return (f'Тип объекта: {a} \nАтрибуты объекта: {attributes} \nМетоды объекта: {methods} \nМодуль объекта: {d}\n')

number_info = introspection_info(42)
print(number_info)

number_info = introspection_info(introspection_info)
print(number_info)

number_info = introspection_info(Class1)
print(number_info)

number_info = Class1()
numbe = introspection_info(number_info)
print(numbe)