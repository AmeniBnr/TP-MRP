from __future__ import annotations
import random
import heapq
from typing import Optional, List

class Reverter:
    """Cette classe représente un tableau à trier et encode formellement les états du problème
    """
    
    def __init__(self, size: int, init: bool = True) -> None:
        """Le constructeur __init__ initialise le tableau avec des nombres de 1 à size mélangés aléatoirement,
          ou laisse le tableau vide si init est False
        """

        if init:
            self.table = list(range(1, size + 1))
            random.shuffle(self.table)
            self.hash()
            self.parent = None
        else:
            self.table = []
    
    
    def __str__(self) -> str:
        """La méthode __str__ renvoie une représentation sous forme de chaîne du tableau
        """
        return str(self.table)

    
    def hash(self) -> None:
       
      self.__hash__ = hash(tuple(self.table))
    
    def __eq__(self, other: Reverter) -> bool:
      return self.__hash__ == other.__hash__
    
    
    def is_the_goal(self) -> bool:
        for i in range(1, len(self.table)):
            if self.table[i - 1] > self.table[i]:
                return False
        return True
    
    
    def clone(self) -> Reverter:
        """La méthode clone crée une copie de l'objet actuel
        """
        res = Reverter(len(self.table), False)
        res.table = [*self.table]
        res.parent = self
        return res
    
    def reverse(self, index: int) -> None:
       
        self.table[index:] = self.table[index:][::-1]
        self.hash()
    
    def actions(self) -> List[Reverter]:
        """La méthode actions construit une liste d'actions possibles en inversant le tableau actuel
        """
        res = []
        sz = len(self.table)
        for i in range(sz):
            r = self.clone()
            r.reverse(i)
            res.append(r)
        return res

    def solveBreadth(self) -> Optional[List[Reverter]]:
        """
            Optional[List[Reverter]]: List of states representing the steps of sorting
        """
        print(self)
        queue = [(self, [])]
        visited = set()
        while queue:
            current, path = queue.pop(0)
            visited.add(current.__hash__)
            if current.is_the_goal():
                print(current)
                return path + [current]
            for action in current.actions():
                if action.__hash__ not in visited:
                    queue.append((action, path + [current]))
        return None

    def solveDepth(self) -> Optional[List[Reverter]]:
       
    
        stack = [(self, [])]
        visited = set()
        while stack:
            current, path = stack.pop()
            visited.add(current.__hash__)
            if current.is_the_goal():
                return path + [current]
            for action in reversed(current.actions()):
                if action.__hash__ not in visited:
                    stack.append((action, path + [current]))
        return None

    def solveRandom(self, max_iterations: int = 10000) -> Optional[List[Reverter]]:
       
        for _ in range(max_iterations):
            current = self.clone()
            path = [current]
            while not current.is_the_goal():
                current = random.choice(current.actions())
                path.append(current)
            if current.is_the_goal():
                return path
        return None

    def heuristic_1(self) -> int:
        """heuristic_1: Calcule la valeur heuristique en comptant le nombre de paires d'éléments non triées
        """
        heuristic_value = 0
        for i in range(len(self.table)):
            for j in range(i + 1, len(self.table)):
                if self.table[i] > self.table[j]:
                    heuristic_value += 1
        return heuristic_value
    
    def solveHeuristic1(self) -> Optional[Reverter]:
       
      
        visited = set()
        heap = [(self.heuristic_1(), self)]
        while heap:
            _, current = heapq.heappop(heap)
            if current.is_the_goal():
                return current
            visited.add(current.__hash__)
            for action in current.actions():
                if action.__hash__ not in visited:
                    heapq.heappush(heap, (action.heuristic_1(), action))
        return None

    def heuristic_2(self) -> int:
       
        heuristic_value = 0
        for i in range(len(self.table)):
            for j in range(i + 1, len(self.table)):
                if self.table[i] > self.table[j]:
                    heuristic_value += 1
        return heuristic_value
    
    def solveHeuristic2(self) -> Optional[Reverter]:
       
        visited = set()
        heap = [(self.heuristic_2(), self)]
        while heap:
            _, current = heapq.heappop(heap)
            if current.is_the_goal():
                return current
            visited.add(current.__hash__)
            for action in current.actions():
                if action.__hash__ not in visited:
                    heapq.heappush(heap, (action.heuristic_2(), action))
        return None
    
    def heuristic_3(self) -> int:
       
    
        # Initialize the heuristic value to 0
        heuristic_value = 0
        # Iterate over the elements of the table
        for i in range(len(self.table)):
            # If the element is already at its correct position
            if self.table[i] == i + 1:
                # Increment the heuristic value
                heuristic_value += 1
        return heuristic_value
    
    def solveHeuristic3(self) -> Optional[List[Reverter]]:
        """implemente la recherch heuristique
        """
        visited = set()
        heap = [(self.heuristic_3(), self, [])]
        while heap:
            _, current, path = heapq.heappop(heap)
            if current.is_the_goal():
                return path + [current]
            visited.add(current.__hash__)
            for action in current.actions():
                if action.__hash__ not in visited:
                    heapq.heappush(heap, (action.heuristic_3(), action, path + [current]))
        return None

# Example usage:
size = 7
rev = Reverter(size, True)
steps = rev.solveBreadth()  # Change to the appropriate method
if steps:
    for i, step in enumerate(steps):
        print(f"Step {i + 1}: {step}")
else:
    print("No solution found.")


import time

# Fonction pour mesurer le temps d'exécution d'une méthode de résolution pour une taille de tableau donnée
def measure_time(method, size):
    rev = Reverter(size, True)
    start_time = time.time()
    steps = method(rev)
    end_time = time.time()
    if steps:
        print(f"Solution found for size {size} using {method.__name__} in {end_time - start_time:.6f} seconds.")
    else:
        print(f"No solution found for size {size} using {method.__name__}.")

# Tester les méthodes pour différentes tailles de tableaux
sizes = range(5, 11) 
for size in sizes:
    print(f"Testing for size {size}:")
    measure_time(Reverter.solveBreadth, size)
    measure_time(Reverter.solveDepth, size)
    measure_time(Reverter.solveRandom, size)
    print()
