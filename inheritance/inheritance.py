class Animal:

    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("inhale exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("moving in water")


class Main:

    nemo = Fish
    nemo.swim()
    nemo.breath()
