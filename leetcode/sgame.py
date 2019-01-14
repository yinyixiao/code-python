import functools

def log(args=0):
    def wrapper(func):
        print('call method: %s' % func.__name__)
        return func

    if isinstance(args,str):
        print(args)
        return wrapper
    else:
        return wrapper(args)

@log('test')#next = log('text')(next)
def next():
    print('next')

@log#now = log(now)
def now():
     print('now')

next()
now()
