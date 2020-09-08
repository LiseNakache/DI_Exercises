class Farm:
    """
    creates Farm object.
    #Params:
        name (str): name of the farm
        optional :
        animals (dict) : dictionary of animals consisting of cows, sheep, and goats
    """

    def __init__(self, name, animals={"cows": 0, "sheep": 0, "goats": 0, }):
        self.name = name
        animals = {
            'cows': 0,
            'sheep': 0,
            'goats': 0,
        }
        self.animals = animals

    def add_animal(self, animal, number=1):
        """
        updates dict animals in Farm object iteration.
        #Params:
            animal(str): animal to add
            number: number of animals to add
        #return: returns updated dict animals of Farm instance
        """

        self.animals[animal] += number
        return self.animals

    def get_info(self):
        inventory = ""
        for k, v in self.animals.items():
            inventory +=f"{k}\t\t\t{v}\n"
        info = f"{self.name}\n" f"{inventory}" f"    E-I-E-I-O    "
        return info

    def get_animal_types(self):
        animals = list(self.animals.keys())
        animals.sort()
        return animals


def main():
    mcdonald = Farm("McDonald")
    mcdonald.add_animal('cows', 5)
    mcdonald.add_animal('sheep')
    mcdonald.add_animal('sheep')
    mcdonald.add_animal('goats', 12)

    print(mcdonald.get_info())


if __name__ == '__main__':
    main()
