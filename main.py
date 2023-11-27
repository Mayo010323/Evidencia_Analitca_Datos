# main.py

import streamlit as st
from funciones_ventas import cargar_datos, limpiar_datos_ventas, obtener_ultima_fecha_por_producto, \
    filtrar_ventas_ultima_fecha, obtener_top_productos, filtrar_productos_seleccionados, \
    obtener_resultados_agrupados, graficar_salidas

# Llamar a las funciones según sea necesario
def main():
    st.title("Mi Tablero Streamlit")

    # Cargar datos
    ventastot = '/Users/sepla/Evidencia_main/ventas_concatenadas.csv'
    ventas = cargar_datos(ventastot)

    # Limpiar datos de ventas
    ventas_limpias = limpiar_datos_ventas(ventas)

    # Obtener fecha más reciente por producto
    ultima_fecha_por_producto = obtener_ultima_fecha_por_producto(ventas_limpias)

    # Filtrar ventas para incluir solo la fecha más reciente por producto
    ventas_ultima_fecha = filtrar_ventas_ultima_fecha(ventas_limpias, ultima_fecha_por_producto)

    # Obtener productos con más salidas y productos más caros
    productos_salidas_totales = obtener_top_productos(ventas_ultima_fecha, 'Salidas')
    productos_mayor_precio = obtener_top_productos(ventas_limpias, 'CostoUnitario')

    # Filtrar productos seleccionados
    productos_seleccionados_df = filtrar_productos_seleccionados(ventas_limpias, productos_salidas_totales, productos_mayor_precio)

    # Obtener resultados agrupados
    resultados = obtener_resultados_agrupados(productos_seleccionados_df)

    # Imprimir resultados
    st.subheader("Resultados")
    st.write("Productos con más Salidas en la fecha más reciente:")
    st.write(resultados[resultados['CodigoProducto'].isin(productos_salidas_totales)])

    st.write("Productos más caros en la fecha más reciente:")
    st.write(resultados[resultados['CodigoProducto'].isin(productos_mayor_precio)])

    # Graficar Salidas y ValorSalidas
    graficar_salidas(ventas)

if __name__ == "__main__":
    main()

