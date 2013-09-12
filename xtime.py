# coding: utf-8

"""xtime 测试过程序调用时间(2013-09-12)

1. 使用

@xtime.xtime
def func():
    pass
    
"""

from uuid import uuid4
from time import time
from traceback import format_stack


class xTime(object):
    _stack_count = -1

    @classmethod
    def xtime(cls, func):
        def wrap(*args, **kwargs):
            magic = uuid4().hex[:5]
            stacks = format_stack()
            start = time()
            cls._stack_count += 1
            # print "%s[%s] %s Current stack: %s" % ("  " * cls._stack_count, func, magic, "<--".join(s.replace("\n", "") for s in stacks))
            print "%s[%s] %s" % ("  " * cls._stack_count, magic, func)
            r = func(*args, **kwargs)
            print "%s[%s] Func: %s time: %.4s ms" % (
                "  " * cls._stack_count,
                magic,
                func, 
                (time() - start) * 1000)
            cls._stack_count -= 1
            return r

        return wrap

xtime = xTime.xtime


@xTime.xtime
def test(name):
    print "hello ", name
    a()


def a():
    print "a"
    b()

@xTime.xtime
def b():
    print "b"
    c()


@xTime.xtime
def c():
    print "c"


if __name__ == "__main__":
    test("jack")
