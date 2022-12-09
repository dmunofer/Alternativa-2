result=0
def count_patterns(node, length):

    nodos = ['A','B','C','D','E','F','G','H','I']
    if length == 1:
        return len(nodos[node])
    global result
    for neighbor in nodos[node]:
        if neighbor not in nodos:
            result += count_patterns(neighbor, length - 1, nodos.append(neighbor))
    return result