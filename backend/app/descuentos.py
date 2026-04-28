# Comienzo de la función como nos la da el ejercicio
def calcular_precio_final(precio, descuento):
    
    precio_final = 0
    
    # Usamos matematicas basicas para sacar el precio final
    precio_final = precio + (precio * descuento)
    print(precio_final)
    
    return

# Llamamos a la funcion con los descuentos que nos pide el ejercicio
calcular_precio_final(5, 0.0)

calcular_precio_final(5, 0.20)

calcular_precio_final(5, 0.50)