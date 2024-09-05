#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Test the Person class
if __name__ == "__main__":
    guido = Person("Guido")
    guido.talk()  # Should print: Hello World!
    guido.walk()  # Should print: The person is walking.
