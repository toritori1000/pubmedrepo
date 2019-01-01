class ExampleMod2:
    def __init__(self):
        self.a = 'mouse'
        self.b = 'cat'

    def compose(self):
        return "{} catches {}.".format(self.b, self.a)
