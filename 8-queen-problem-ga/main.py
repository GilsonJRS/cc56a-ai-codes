import random
import argparse
import numpy as np

STOP_FLAG = False

def fitness(chromosome):
    global STOP_FLAG
    attacks = abs(len(chromosome) - len(np.unique(chromosome)))
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if(i!=j):
                dx = abs(i-j)
                dy = abs(chromosome[i]-chromosome[j])
                if(dx == dy):
                    attacks+=1
    if(attacks == 0):
        print(chromosome)
        STOP_FLAG = True
    return 28 - attacks

def getPopulation(size):
    population = []
    for _ in range(size):
        population.append(random.sample(range(1,9), 8))
    return population

def reproduce(x,y):
    c = random.randint(0,7)
    child = x[0:c]+y[c:8]
    return child

def mutate(child, mutprob):
    for i in range(len(child)):
        if(random.random() < mutprob):
            child[i] = random.randint(1,8)

parser = argparse.ArgumentParser()
parser.add_argument('--maxiter', type=int, default=100000)
parser.add_argument('--popsize', type=int, default=10)
parser.add_argument('--mutprob', type=float, default=0.05)
args = parser.parse_args()

population = getPopulation(args.popsize)

for i in range(args.maxiter):
    fit_prob = [(fitness(i)/len(population))*100 for i in population]
    if(STOP_FLAG):
        break
    new_pop = []
    for j in range(len(population)):
        x = random.choices(population, weights=fit_prob)[0]
        y = random.choices(population, weights=fit_prob)[0]
        while(y == x):
           y = random.choices(population, weights=fit_prob)[0]
        child = reproduce(x,y)
        mutate(child, args.mutprob)
        new_pop.append(child)
    population = new_pop.copy()