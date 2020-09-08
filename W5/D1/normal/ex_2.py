# Create a class Dog
class Dog:
    """
    In this class, create a method __init__, that takes two parameters: nameDog
    and heightDog. This function initialises two attributes with the values of the parameters.
    """
    def __init__(self,nameDog, heightDog):
        self.nameDog = nameDog
        self.heightDog = heightDog



    def talk(self):
        """
        Create a method talkthat prints Wouaf
        """
        return "Woof"

    def jump(self):
        """
        Create a method jump that multiplies by two the height of the dog. Print the height of the dog when he jumps.
        """
        try:
            if self.heightDog > 0:
                heightJump = self.heightDog*2
                return heightJump
        except: ValueError

def main():
    # Create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
    # Print the details of his dog by calling the methods.
    davids_dog = Dog("Rex", 50)
    print(
            f"Davids's dog is {davids_dog.nameDog}, he is {davids_dog.heightDog} tall and "
            f"jumps {Dog.jump(davids_dog)} cm high! {davids_dog.talk()}")

    # Create an object sarahs_dog. His dog’s name is “Teacup” and his height is 20cm.
    # Print the details of her dog by calling the methods.


    sarahs_dog = Dog("Teacup", 20)
    print(
            f"Sarah's dog is {sarahs_dog.nameDog}, he is {sarahs_dog.heightDog}"
            f"tall and jumps {Dog.jump(sarahs_dog)} cm high! {sarahs_dog.talk()}")


    # Create an if statement outside of the class to check which dog is bigger. Print the bigger dog’s name.
    if sarahs_dog.heightDog > davids_dog.heightDog:
        print(f"Sarah's dog is taller")
    else:
        print(f"David's dog is taller")


if __name__ == "__main__":
    main()

