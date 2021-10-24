import random
import argparse
import numpy as np

#return de fitness of a member in the population
def fitness(chromosome, n_queen):
    attacks = abs(len(chromosome) - len(np.unique(chromosome)))
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if(i!=j):
                dx = abs(i-j)
                dy = abs(chromosome[i]-chromosome[j])
                if(dx == dy):
                    attacks+=1
    if(attacks == 0):
        print('\n')
        printBoard(chromosome, n_queen)
        print(chromosome)
        return True, (((n_queen-1)*n_queen)/2)-attacks
    
    return False, (((n_queen-1)*n_queen)/2)-attacks

#create a population
def getPopulation(size, n_queen):
    population = []
    for _ in range(size):
        #population.append(random.sample(range(1,n_queen+1), n_queen))
        population.append([random.randint(1,n_queen) for _ in range(n_queen)])
    return population

#reproduce two individuals and return a child
def reproduce(x,y, n_queen):
    c = random.randint(0,n_queen-1)
    child = x[0:c]+y[c:n_queen]
    return child

#performs a mutation with a small probability
def mutate(child, mutprob, n_queen):
    for i in range(len(child)):
        if(random.random() < mutprob):
            child[i] = random.randint(1,n_queen)

#function to print the board
def printBoard(chromosome, n_queen):
    for i in reversed(range(n_queen)):
        for j in range(n_queen):
            if(chromosome[j] == i+1):
                print("\t X ", end='')
            else:
                print("\t . ", end='')
        print("\n")

#getting arguments
parser = argparse.ArgumentParser()
parser.add_argument('--maxiter', type=int, default=100000)
parser.add_argument('--popsize', type=int, default=10)
parser.add_argument('--mutprob', type=float, default=0.05)
parser.add_argument('--nqueen', type=int, default=8)
args = parser.parse_args()

population = getPopulation(args.popsize,args.nqueen)
best = None
best_prob = 0
best_find = False

#----- Main Loop -----
for i in range(args.maxiter):
    print('Iteration: ' + str(i+1), end="\r")
    fit_prob = []
    for k in population:
        best_find, prob = fitness(k, args.nqueen)
        prob = (prob/len(population))*100
        fit_prob.append(prob)
        if(prob > best_prob):
            best = k
            best_prob = prob
        if(best_find):
            best = None
            break    
    if(best_find):
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

if(best!=None):
    print('\n')
    printBoard(best, args.nqueen)
    print(best)