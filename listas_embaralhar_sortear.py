import random
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Marianna']
print(f'Lista: {alunos} ')
# Embaralhar a Lista
random.shuffle(alunos)
print(f'Lista Embaralhada: {alunos}')
# Ordena a Lista Crescente
alunos.sort()
print(f'Lista Crescente: {alunos}')
# Ordena a Lista Decrescente
alunos.sort(reverse=True)
print(f'Lista Decrescente: {alunos} ')