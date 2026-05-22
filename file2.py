class Bird:
    def fly(self):
        return "Flying"


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")  # violates LSP


def make_bird_fly(bird: Bird):
    return bird.fly()  # assumes all birds can fly


penguin = Penguin()
print(make_bird_fly(penguin))  # runtime failure