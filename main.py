#Matheus Melara Girardi, Pedro Bastos Leite


with open('conjunto3.txt', 'r') as f:
    lines = f.readlines()  
    sets = [] 
    indices = list(range(2, len(lines)))
    for i in indices:
        s = set(lines[i].strip().split(', '))
        sets.append(s)


for indice in range(0, len(lines) - 2, 3):
  if sets[indice] == {'U'}:
    print("---------------------")
    print(f"União: conjunto 1 {sets[indice + 1]}, conjunto 2 {sets[indice + 2]}. Resultado: {sets[indice + 1].union(sets[indice + 2])}")
    print("---------------------")

  elif sets[indice] == {'I'}:
    print("---------------------")
    print(f"Interseção: conjunto 1 {sets[indice + 1]}, conjunto 2 {sets[indice + 2]}. Resultado: {sets[indice + 1].intersection(sets[indice + 2])}")
    print("---------------------")

  elif sets[indice] == {'D'}:
    print("---------------------")
    print(f"Diferença: conjunto 1 {sets[indice + 1]}, conjunto 2 {sets[indice + 2]}. Resultado: {sets[indice + 1].difference(sets[indice + 2])}")
    print("---------------------")

  elif sets[indice] == {'C'}:
    print("---------------------")
  

    cartesiano = []
    for elemento in sets[indice + 1]:
      for elemento2 in sets[indice + 2]:
        temp = [elemento, elemento2]
        cartesiano.append(temp)
            

    print(f"Cartesiano: conjunto 1 {sets[indice + 1]}, conjunto 2 {sets[indice + 2]}. Resultado: {cartesiano}")
    print("---------------------")
    



