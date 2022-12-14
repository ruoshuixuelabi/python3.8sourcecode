class Animal(object):
    def run(self):
        print('Animal is running...')

    def jump(self):
        print('Animal is jumpping....')

    def __run(self):
        print('I am a private method.')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_two_times(animal):
    animal.run()
    animal.run()


run_two_times(Animal())
run_two_times(Dog())
run_two_times(Cat())
