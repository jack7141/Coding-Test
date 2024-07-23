
def coroutine():
    while True:
        x = (yield)
        print(x)

co = coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)
co.send(5)
