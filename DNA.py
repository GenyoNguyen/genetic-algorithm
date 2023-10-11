import random


def newChar():
    return chr(random.randint(32, 122))


class DNA:

    def __init__(self, length):
        self.genes = []
        self.fitness = 0.0
        for i in range(length):
            self.genes.append(newChar())

    def getPhrase(self):
        return "".join(self.genes)

    def calcFitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = (float(score / len(target))) ** 3 + 0.01

    def crossover(self, other):
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = other.genes[i]
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random.uniform(0, 1) < mutationRate:
                self.genes[i] = newChar()
