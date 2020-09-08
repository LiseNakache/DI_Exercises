import random
random.seed()
class Gene:

    def __init__(self):
        self.value = random.choice([True,False])

    def mutate(self):
        self.value = not self.value

    def __repr__(self):
        return "1" if self.value else "0"
    
    def __str__(self):
        return f"the value of this gene is: {self.__repr__} "

class Chromosome():
    def __init__(self):
        self.value = [Gene() for i in range(10)]

    def mutate(self):
        for gene in self.value:
            Gene.mutate(gene)

    


class DNA():

    def __init__(self):
        self.value = [Chromosome() for i in range(10)]

CHANCE_TO_MUTATE = 0.5

def big_bang(gene):
    dice_roll = random.random()

    if dice_roll < CHANCE_TO_MUTATE:
        gene.mutate()



def main():
    g = Gene()
    print(g.value)
    # g.mutate()
    # print(g.value)
    c = Chromosome()
    print(c.value)
    c.mutate()
    print(c.value)
    big_bang(g)
    print(g.value)
    # dna = DNA()
    # print(dna.value)

if __name__ == '__main__':
    main()
