from datetime import datetime, date

FORMATO_FECHA = '%Y-%m-%d'

def convertir_fecha_de_str_a_date(fecha_texto):
    try:
        fecha_convertida = datetime.strptime(fecha_texto, FORMATO_FECHA).date()
    except:
        print('La fecha ingresada es invalida, debe seguir el formato año-mes-dia (eje. 2025-07-14)\nAsignando hoy como fecha por defecto')
        return date.today()
    return fecha_convertida