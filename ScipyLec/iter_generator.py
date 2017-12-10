# iter

nums = [1, 2, 3]
it = iter(nums)
print('iterations : next(iter([1,2,3]))', next(it))

# generator


def f():
    yield 1
    yield 2


g = f()
print('generator : next(g),', next(g))


# bidirectional

import itertools


def g():
    print('start...')
    for i in itertools.count():
        print('---yielding %i---' % i)
        try:
            ans = yield i
        except GeneratorExit:
            print('---closing---')
            raise
        except Exception as e:
            print('---yield raised %r---' % e)
        else:
            print('---yield returned %s---' % ans)


it = g()
next(it)
it.send(11)
