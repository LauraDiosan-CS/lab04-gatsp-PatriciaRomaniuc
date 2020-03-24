from GA import GA


def readGraph(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
    i = 0
    line = f.readline()
    while line and i < n:
        args = line.split(",")
        for arg in args:
            mat[i].append(int(arg))
        i = i + 1
        line = f.readline()
    f.close()
    net['mat'] = mat
    return net


def fitness(net, path):
    val = 0
    mat = net['mat']
    for i in range(0, len(path) - 1):
        node = path[i]
        nextNode = path[i + 1]
        val = val + mat[node - 1][nextNode - 1]
    val = val + mat[path[len(path) - 1] - 1][path[0] - 1]
    return val


def main():
    net = readGraph("hard_01_tsp.txt")

    gaParam = {'popSize': 10, 'noGen': 1000, 'pc': 0.8, 'pm': 0.1}
    problParam = {'net': net, 'function': fitness, 'noNodes': net['noNodes']}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    ga.oneGenerationElitism()
    final = ga.bestChromosome()
    print(final)


main()
