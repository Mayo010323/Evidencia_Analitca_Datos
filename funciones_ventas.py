import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.subplots as sp

def cargar_datos(ruta_archivo):
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv(ruta_archivo, encoding='latin1')

def limpiar_datos_ventas(ventas):
    """Realiza las transformaciones y limpieza de datos en el DataFrame de ventas."""
    ventas['Fecha'] = pd.to_datetime(ventas['Fecha'], format='%d/%b/%Y', errors='coerce')
    ventas.set_index('Fecha', inplace=True)
    ventas['ValorStock'] = ventas['ExistenciaTotal'] * ventas['CostoUnitario']
    ventas['CostoUnitario'] = pd.to_numeric(ventas['CostoUnitario'], errors='coerce')
    ventas['Salidas'] = pd.to_numeric(ventas['Salidas'], errors='coerce')
    return ventas

def obtener_ultima_fecha_por_producto(ventas):
    """Obtiene la fecha más reciente para cada producto."""
    return ventas.groupby('CodigoProducto').apply(lambda group: group.index.max())

def filtrar_ventas_ultima_fecha(ventas, ultima_fecha_por_producto):
    """Filtra el DataFrame de ventas para incluir solo las filas con la fecha más reciente para cada producto."""
    return ventas.loc[ultima_fecha_por_producto]

def obtener_top_productos(ventas, columna, top_n=5):
    """Obtiene los top N productos según la columna especificada."""
    return ventas.groupby('CodigoProducto')[columna].sum().nlargest(top_n).index

def filtrar_productos_seleccionados(ventas, productos_salidas_totales, productos_mayor_precio):
    """Filtra el DataFrame de ventas para incluir solo los productos seleccionados."""
    return ventas[ventas['CodigoProducto'].isin(productos_salidas_totales.union(productos_mayor_precio))]

def obtener_resultados_agrupados(productos_seleccionados_df):
    """Agrupa por CodigoProducto y obtiene los valores para la fecha más reciente."""
    return productos_seleccionados_df.groupby('CodigoProducto').agg({'ValorStock': 'sum', 'ExistenciaTotal': 'sum'}).reset_index()

def graficar_salidas(ventas):
    """Crea gráficas de serie de tiempo para Salidas y ValorSalidas."""
    # Convertir las columnas 'Salidas' y 'CostoUnitario' a tipos numéricos
    ventas['Salidas'] = pd.to_numeric(ventas['Salidas'], errors='coerce')
    ventas['CostoUnitario'] = pd.to_numeric(ventas['CostoUnitario'], errors='coerce')

    # Crear una nueva columna para el valor de las Salidas
    ventas['ValorSalidas'] = ventas['Salidas'] * ventas['CostoUnitario']

    # Agrupar por fecha y sumar las Salidas y el valor de las Salidas
    ventas_agrupadas = ventas.groupby(ventas.index)[['Salidas', 'ValorSalidas']].sum()

    # Crear gráfico de serie de tiempo para Salidas
    fig_salidas = px.line(ventas_agrupadas, x=ventas_agrupadas.index, y='Salidas',
                          labels={'Salidas': 'Cantidad de Salidas'},
                          title='Cantidad de Salidas a lo largo del tiempo')

    # Crear gráfico de serie de tiempo para ValorSalidas
    fig_valor_salidas = px.line(ventas_agrupadas, x=ventas_agrupadas.index, y='ValorSalidas',
                                labels={'ValorSalidas': 'Valor de las Salidas'},
                                title='Valor de las Salidas a lo largo del tiempo')

    # Mostrar los gráficos en Streamlit
    st.plotly_chart(fig_salidas)
    st.plotly_chart(fig_valor_salidas)