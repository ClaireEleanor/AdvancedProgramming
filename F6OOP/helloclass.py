class Hello:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = ["I", "Love", "Classes!"]

    def f(self):
        return 'Hello World!!!!!!!!!'


x = Hello()
print x.f()
print x.i
print x.data
