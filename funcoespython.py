def calculadora(numero1, numero2, operacao):
    resultado = 0
    if operacao == 1:  # Soma
        resultado = numero1 + numero2
    elif operacao == 2:  # Subtração
        resultado = numero1 - numero2
    elif operacao == 3:  # Multiplicação
        resultado = numero1 * numero2
    elif operacao == 4:  # Divisão
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Operação inválida."
    
    return resultado

print(calculadora(2,2,2))