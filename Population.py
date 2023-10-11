import random
from DNA import DNA


class Population:

    def __init__(self, target, maxpop, mutationRate):
        self.target = target
        self.maxpop = maxpop
        self.mutationRate = mutationRate
        self.pop = []
        self.maxFitness = 0.0
        self.best = ""
        self.isFinished = False
        self.perfectScore = 1.0
        self.generation = 0

        for _ in range(maxpop):
            self.pop.append(DNA(len(self.target)))

    def calFitness(self):
        for i in range(len(self.pop)):
            self.pop[i].calcFitness(self.target)

    def naturalSelection(self):
        # Calculate Max Fitness
        for i in range(len(self.pop)):
            if self.pop[i].fitness > self.maxFitness:
                self.maxFitness = self.pop[i].fitness

    def acceptReject(self):
        besafe = 0
        while True:
            currDNA = self.pop[random.randrange(0, len(self.pop))]
            r = currDNA.fitness
            if r > random.uniform(0, self.maxFitness) or besafe == 1000:
                return currDNA
            besafe += 1

    def generate(self):
        temp = []
        for i in range(self.maxpop):
            parentA = self.acceptReject()
            parentB = self.acceptReject()
            child = parentA.crossover(parentB)
            child.mutate(self.mutationRate)
            temp.append(child)
        self.pop = temp
        self.generation += 1

    def evaluate(self):
        wr = 0.0
        index = 0
        for i in range(len(self.pop)):
            if self.pop[i].fitness > wr:
                wr = self.pop[i].fitness
                index = i

        self.best = self.pop[index].getPhrase()
        if self.best == self.target:
            self.isFinished = True
