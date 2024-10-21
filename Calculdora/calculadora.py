def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero."

def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    while True:
        opcion = input("Ingresa el número de la operación (1/2/3/4): ")
        
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            
            siguiente = input("¿Quieres realizar otra operación? (sí/no): ")
            if siguiente.lower() != 'sí':
                break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
