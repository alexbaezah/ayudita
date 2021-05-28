acu = 0
mon = 0
opcion = 0
hom = 0
mujer = 0
socio = 0

while opcion < 4:
    try: 
        print("   entrada|valor\n1) Hombre -> $10.500\n2) Mujer -> $8.000\n3) Socios -> $6.000")
        print("4) opción 4 es ver boleta")
        opcion = int(input("ingrese opción "))
        if opcion < 1:
            raise Exception("número negativo, debe ser entre 1 al 4 positivo")
        if opcion == 1:
            cantidad1 = int(input("¿Cuántos son? "))
            mon = cantidad1 * 1200
            acu += mon
            hom += cantidad1
        elif opcion == 2:
            cantidad2 = int(input("¿Cuántos son? "))
            mon = cantidad2 * 1500
            acu += mon 
            mujer += cantidad2
        elif opcion == 3:
            cantidad3 = int(input("¿Cuántos son? "))
            mon = cantidad3 * 1000
            acu += mon
            socio += cantidad3
        elif opcion == 4:
            print(f"\n{hom} hombre\n{mujer} mujer\n{socio} socio\nMonto total por los integrantes:${acu}")
    except:
            print("los valores deben ser números enteros")
