def registrar_venta():
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        if cantidad <= 0 or precio < 0:
            raise ValueError ("La cantidad o el Precio no pueden ser negativos")
        total = cantidad * precio
        
    except ValueError as error:
        print(error)
    else:
        print(f"Venta correcta. Total: {total}")
    finally:
        print("Programa finalzado.")


registrar_venta()