"""
CONSULTAR EL STOCK DE PRODUCTOS
Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en stock. Si el producto está en la lista, el programa debe informarlo. Si no, debe mostrar un mensaje indicando que no está disponible.

TIPS:
a) Usá una lista para almacenar los productos en stock.
b) Permití que el usuario ingrese el nombre de un producto a consultar.
c) Recorré la lista con un bucle for para verificar si el producto está en stock.
"""

stock_productos = ["Cartuchera", "Lapicera", "Goma", "Lápices de colores", "Carpeta", "Mochila"]

producto_buscado = str(input("\nIngrese el producto que está buscando: ")).capitalize()
    
for producto in stock_productos:
    if producto_buscado in stock_productos:
        print(f"\nHay stock de «{producto_buscado}» actualmente.")
    else:
        print(f"Lo sentimos, pero no hay stock de «{producto_buscado}» en estos momentos.")
        print()
    break