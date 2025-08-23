import numpy as np

def calculate(list):
    #Verificar se tem nove números
    if len(list) != 9:
        raise ValueError("List must contain nine list.")

    #Transformar em uma mtriz 3x3 
    array = np.array(list).reshape(3,3)

    #Percorrer o array de funções e criar o dicionário
    methods = ["mean", "var", "std", "max", "min", "sum"]

    calculations = {}
    for name in methods:
        calculations[name] = [getattr(np,name)(array, axis=0).tolist(), getattr(np,name)(array, axis=1).tolist(), getattr(np,name)(array).tolist()]   

    return calculations