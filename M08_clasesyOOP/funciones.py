class Funciones:
    def __init__(self, lista):
        self.lista = lista

    def primos(self):
        for i in self.lista:
            if(self.__primos(i)):
                print(f"{i} es un número primo")
            else:
                print(f"{i} no es un número primo")

    def conversion(self, entrada, salida):
        for i in self.lista:
            print(f"{i} grados {entrada} equivalen a {self.__conversion(i, entrada, salida)}  grados {salida}")

    def factorial(self):
        for i in self.lista:
            print(f"El factorial de {i} es {self.__factorial(i)}")

    def __primos (self, num):
        """"
        Función que recibe un valornumérico y devuelve un valor booleano indicando si es primo o no.
        Parámetros:
        num (int): El número al que se va a verificar si es primo o no.
        Retorna:
        primo: True si el número es primo, False en caso contrario.
        """
        primo = True
        for n in range (2,num):
            if (num % n == 0):
                primo = False
                break
        return primo
    
    def valor_modal(self, lista):
        """"
        Función que recibe una lista de números, crea un diccionario con cada valor único y las veces que se repite.
        Devuelve el valor modal y la cantidad de veces que se repite.
        Parámetros:
        lista (list): La lista de números a analizar.
        Retorna:
        modal: El valor que más se repite.
        cantidad: Cuántas veces se repite ese valor en la lista.
        """
        
        repeticiones = {}
        for num in lista:
            if num in repeticiones:
                repeticiones[num] += 1
            else:
                repeticiones[num] = 1
        modal = None
        cantidad = 0
        for num, repeticion in repeticiones.items():
            if repeticion > cantidad:
                modal = num
                cantidad = repeticion
        return modal, cantidad
    
    def __conversion (self, temp, entrada, salida):
        """"
        Función que realiza la conversión de temperaturas entre las distintas escalas.
        Parámetros:
        temp: el valor de la temperatura que se desea convertir.
        entrada: la escala de la temperatura a convertir.
        salida: la escala de la temperatura ya convertida.
        Retorna: el valor de la temperatura ya convertida.
        """
        if entrada == "Celsius":
            if salida == "Celsius":
                return temp
            elif salida == "Fahrenheit":
                return round((temp * 9/5) + 32, 2)
            elif salida == "Kelvin":
                return round(temp + 273.15, 2)
        elif entrada == "Fahrenheit":
            if salida == "Fahrenheit":
                return temp
            elif salida == "Celsius":
                return round((temp - 32) * 5/9, 2)
            elif salida == "Kelvin":
                return round((temp - 32) * 5/9 + 273.15, 2)
        elif entrada == "Kelvin":
            if salida == "Kelvin":
                return temp
            elif salida == "Celsius":
                return round(temp - 273.15, 2)
            elif salida == "Fahrenheit":
                return round((temp - 273.15) * 9/5 + 32, 2)
        else:
            return "Parámetro inválido. Verifique que las unidades sean: Celsius, Fahrenheit, o Kelvin."
        
    def __factorial(self, n):
        if type(n) != int:
            return "El valor debe ser un número entero"
        if n < 0:
            return "El número debe ser positivo."
        elif n == 0:
            return 1
        elif n > 1:
            n = n * self.__factorial(n - 1)
        return n