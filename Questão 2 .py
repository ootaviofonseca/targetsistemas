def fibonacci(entrada):
    if entrada == 0 or entrada == 1: #se o valor de entrada for 0 ou 1 nao precisa montar a sequencia só confirma
        return True
    else:
        sequenciaFib = [0, 1] #inicia com 0 e 1
        
        while len(sequenciaFib) < entrada:
            sequenciaFib.append(sequenciaFib[-1] + sequenciaFib[-2]) #cria sequencia ate um valor maior que o numero inserido
        
        if entrada in sequenciaFib: #verifica a existencia do valor dentro da sequencia
            return True 
        else:
            return False

entrada = int(input())
if entrada >= 0 :#verifica se a entrada é um valor positivo pois se não for não da para fazer a sequência
    if fibonacci(entrada): #retorna o resultado
        print(f"O número {entrada} está na sequência")
    else: 
        print(f"O número {entrada} não está na sequência")