class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance

class User(metaclass=Singleton):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<User: {self.name}>'

print(User('Гоша'))

u1 = User('Иорик')
u2 = User('Жорик')
print(id(u1) == id(u2))