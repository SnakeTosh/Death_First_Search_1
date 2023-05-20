import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways

def creation_dico(j, i, indice_exit, dico):
    for c in indice_exit:
        if c == j:
            valeur = c
            for a in i:
                if a != valeur:
                    dico[a] = c
    return dico

n, l, e = [int(i) for i in input().split()]
indice_exit = []
dico = {}
dico_base = {}
coord_lien = []
for i in range(l):
    liste = []
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    dico_base[n1] = n2
    liste.append(n1)
    liste.append(n2)
    coord_lien.append(liste)

for i in range(e):
    liste = []
    ei = int(input())  # the index of a gateway node
    indice_exit.append(ei)

# game loop

for i in coord_lien:
    for j in i:
        creation_dico(j, i, indice_exit, dico)

while True:
    c1 = 1
    c2 = 0
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    if si in dico:
        c1 = si
        c2 = dico[si]
    else:
        c1 = si
        c2 = dico_base[si]
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(c1, c2)
