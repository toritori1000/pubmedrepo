class ExampleMod2:
    def __init__(self):
        self.a = 'mouse'
        self.b = 'cat'

    def compose(self):
        return "{} catches {}.".format(self.b, self.a)


def new_func(self, a: str, b: int, c: int = 10) -> str:
    """[summary]

    [description]

    Args:
        a (str): [description]
        b (int): [description]
        c (int, optional): Defaults to 10. [description]

    Returns:
        str: [description]
    """

    # regular comment
    # * important comment
    # ! warning
    # TODO: todo stuff
    # ? question???
