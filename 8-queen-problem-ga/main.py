import random
import argparse
import numpy as np

STOP_FLAG = False

def fitness(chromosome, n_queen):
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
        printBoard(chromosome, n_queen)
        print(chromosome)
        STOP_FLAG = True
    return (((n_queen-1)*n_queen)/2)-attacks
    #return 28 - attacks

def getPopulation(size, n_queen):
    population = []
    for _ in range(size):
        population.append(random.sample(range(1,n_queen+1), n_queen))
    return population

def reproduce(x,y, n_queen):
    c = random.randint(0,n_queen-1)
    child = x[0:c]+y[c:n_queen]
    return child

def mutate(child, mutprob, n_queen):
    for i in range(len(child)):
        if(random.random() < mutprob):
            child[i] = random.randint(1,n_queen)

def printBoard(chromosome, n_queen):
    for i in reversed(range(n_queen)):
        for j in range(n_queen):
            if(chromosome[j] == i+1):
                print("X ", end='')
            else:
                print(". ", end='')
        print("\n")

parser = argparse.ArgumentParser()
parser.add_argument('--maxiter', type=int, default=100000)
parser.add_argument('--popsize', type=int, default=10)
parser.add_argument('--mutprob', type=float, default=0.05)
parser.add_argument('--nqueen', type=int, default=8)
args = parser.parse_args()

population = getPopulation(args.popsize,args.nqueen)

for i in range(args.maxiter):
    fit_prob = [(fitness(i, args.nqueen)/len(population))*100 for i in population]
    if(STOP_FLAG):
        break
    new_pop = []
    for j in range(len(population)):
        x = random.choices(population, weights=fit_prob)[0]
        y = random.choices(population, weights=fit_prob)[0]
        while(y == x):
           y = random.choices(population, weights=fit_prob)[0]
        child = reproduce(x,y,args.nqueen)
        mutate(child, args.mutprob,args.nqueen)
        new_pop.append(child)
    population = new_pop.copy()