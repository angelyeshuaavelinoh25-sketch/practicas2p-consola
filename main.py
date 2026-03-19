if __name__ == "__main__":
    from holaMundo import Mensaje
    from operacionesMatematicas import OperacionesMatematicas
    from tringulo import Triangulo
    from cuadrado import Cuadrado
    from rectangulo import Rectangulo
    from persona import Persona
   
    print("este es el programa principal")
    print("elige la opcion que deseas ejecutar:")
    print("1. hola mundo programacion en clases")
    print("2.Reliza operaciones matematicas") 
    print("3. calcuar la edad de una persona ") 
    print("4. calcular el area y perimetro de un triangulo")
    print("5. calcular el area y perimetro de un cuadrado") 
    print("6. calcular el area y perimetro de un rectangulo")
    opcion = input("Ingresa el numero de la opcion que deseas ejecutar: ")
    if opcion == "1":
        saludo = Mensaje("Hola Mundo, este es un mensaje desde la clase Mensaje")
        saludo.mostrar()
    elif opcion == "2": 
        operaciones = OperacionesMatematicas()
        print("Has elegido realizar operaciones matematicas")
        print("ingresa los numeros que deseas operar")
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
    
        print(f"Suma: {operaciones.sumar(a, b)}")
        print(f"Resta: {operaciones.restar(a, b)}")
        print(f"Multiplicación: {operaciones.multiplicar(a, b)}") 
        print(f"División: {operaciones.dividir(a, b)}")
    elif opcion == "3":
        from persona import Persona
        nombre = input("Ingresa el nombre de la persona: ")
        anio_nacimiento = int(input("Ingresa el año de nacimiento de la persona: "))
        persona = Persona(nombre, anio_nacimiento, 0)
        anio_actual = int(input("Ingresa el año actual: "))
        edad_calculada = persona.calcular_edad(anio_actual)
        print(f"{persona.nombre} tiene {edad_calculada} años.")   
    elif opcion == "4":
        base = float(input("Ingresa la base del triangulo: "))
        altura = float(input("Ingresa la altura del triangulo: "))
        triangulo = Triangulo(base, altura)
        print(f"Area del triangulo: {triangulo.area()}")
        print(f"Perimetro del triangulo: {triangulo.perimetro()}")
    elif opcion == "5": 
        lado = float(input("Ingresa el lado del cuadrado: "))
        cuadrado = Cuadrado(lado)
        print(f"Area del cuadrado: {cuadrado.area()}")
        print(f"Perimetro del cuadrado: {cuadrado.perimetro()}")
    elif opcion == "6":
        base = float(input("Ingresa la base del rectangulo: "))
        altura = float(input("Ingresa la altura del rectangulo: "))
        rectangulo = Rectangulo(base, altura)
        print(f"Area del rectangulo: {rectangulo.area()}")
        print(f"Perimetro del rectangulo: {rectangulo.perimetro()}")
    else:
        print("Opcion no valida, por favor ingresa un numero del 1 al 6")   
