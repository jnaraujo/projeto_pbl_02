def find(elm, arr):
    '''
        Função que procura um elemento em um array e retorna o index do elemento encontrado.
        Se não encontrar, retorna -1.
    '''
    arr = sorted(arr.copy()) # ordena uma cópia do array
    
    low = 0 # define o index inicial
    high = len(arr) - 1 # define o index final

    while low <= high: # enquanto o index inicial for menor ou igual ao index final
        mid = (low + high) // 2 # define o index do meio (aproximado para baixo)

        if arr[mid] == elm: # se elm for igual ao elemento do meio, retorna o index
            return mid
        elif arr[mid] < elm: # se elm é maior, ignora o lado esquerdo
            low = mid + 1
        elif arr[mid] > elm: # se elm é menor, ignora o lado direito
            high = mid - 1

    return -1