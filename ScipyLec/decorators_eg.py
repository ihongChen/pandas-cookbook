# encoding:utf8


def simple_decorator(func):
    print('doing decoration')
    return func


@simple_decorator
def function():
    print('inside function')


def decorator_with_args(arg):
    print("defining the decorator")

    def _decorator(function):
        print('doing decoration, %r' % arg)
        return function
    return _decorator


@decorator_with_args('abc')
def function2():
    print('inside function2')


class decorator_class:
    def __init__(self, arg):
        # this method is called in the decorator expression
        print('in decorator init %s' % arg)
        self.arg = arg

    def __call__(self, function):
        # this method is called to do the job
        print('in decorator call %s' % self.arg)
        return function


deco_inst = decorator_class('foo')


@deco_inst
def function3(*args, **kwargs):
    print('in function, %s, %s' % (args, kwargs))


if __name__ == '__main__':
    function3(1, 2, 3, a=1, b=2)
