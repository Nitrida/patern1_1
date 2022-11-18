class Factory(object):
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)

class Loader(object):
    def load(string, factory):
        sequence = factory.build_sequence()
        for substring in string.split(','):
            item = factory.build_number(substring)
            sequence.append(item)
        return sequence

f = Factory()
result = Loader.load('1.23, 4.56', f)
print(result)
[float('1.23'), float('4.56')]
