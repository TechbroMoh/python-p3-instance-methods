#!/usr/bin/env python3

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Test the Dog class
if __name__ == "__main__":
    fido = Dog("Fido")
    fido.bark()  # Should print: Woof!
    fido.sit()   # Should print: The dog is sitting.
