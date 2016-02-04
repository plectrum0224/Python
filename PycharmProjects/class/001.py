

def f():
    def g():
        print 'g()...'
    print 'f()...'
    print g

f()


