# Solicita números al usuarios
amount = int(input("Ingrese la cantidad de números que va ingresar: "))
numbers = []
for i in range(amount):
    numbers.append(int(input("Ingrese el número {}: ".format(i + 1))))

# Calcular si un numero tiene mas de 2 divisores
def divisible_por_2(number):
    if number >= 0:
        for i in range(2, number):
            if number % i == 0:
                return True
        return False
    else:
        for i in range(2, abs(number)):
            if abs(number) % i == 0:
                return True
        return False

# Calcular si un numero es positivo o negativo
def signo(number):
    if number >= 0:
        return "Positivo"
    else:
        return "Negativo"

# Calcular si un numero es par o impar
def par_o_impar(number):
    if number % 2 == 0:
        return "Par"
    else:
        return "Impar"

# Calcular si un numero es primo
def primo(number):
    if number >= 0:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        for i in range(2, abs(number)):
            if abs(number) % i == 0:
                return False
        return True

# Calcular si un numero es perfecto
def perfecto(number):
    suma = 0
    for i in range(1, number):
        if number % i == 0:
            suma += i
    if suma == number:
        return True
    else:
        return False

# Obtener todos los resultados
def get_result(number):
    return {
        "entrada": number,
        "divisible_por_2": divisible_por_2(number),
        "entero": signo(number),
        "par_o_impar": par_o_impar(number),
        "primo": primo(number),
        "perfecto": perfecto(number),
    }

# Imprimir todos los resultados
for i in range(amount):
    print(get_result(numbers[i]))
