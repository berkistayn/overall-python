# Better than above one:

from multipledispatch import dispatch

class A:
    @dispatch()
    def print_type(self):
        print("Empty!")

    @dispatch(tuple)
    def print_type(self, var):
        print("It is a tuple!")

    @dispatch(str)
    def print_type(self, var):
        print("It is a string!")

a = A()
a.print_type("asd")
a.print_type((1,3))

############

import functools

def multidispatch(*types):
    def register(function):
        name = function.__name__
        mm = multidispatch.registry.get(name)
        if mm is None:
            @functools.wraps(function)
            def wrapper(self, *args):
                types = tuple(arg.__class__ for arg in args) 
                function = wrapper.typemap.get(types)
                if function is None:
                    raise TypeError("no match")
                return function(self, *args)
            wrapper.typemap = {}
            mm = multidispatch.registry[name] = wrapper
        if types in mm.typemap:
            raise TypeError("duplicate registration")
        mm.typemap[types] = function
        return mm
    return register
multidispatch.registry = {}

class Foo(object):
    @multidispatch(str)
    def render(self, s):
        print('string: {}'.format(s))
    @multidispatch(float)
    def render(self, s):
        print('float: {}'.format(s))
    @multidispatch(float, int)
    def render(self, s, t):
        print('float, int: {}, {}'.format(s, t))

foo = Foo()
foo.render('text')
# string: text
foo.render(1.234)
# float: 1.234
foo.render(1.234, 2)
# float, int: 1.234, 2
