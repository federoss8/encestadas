import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Configuración
SPREADSHEET_ID = "1X6uzhtFut0YsxOm9Hpy49rfkwpJJ1X-4e7caaaUiCsY"
HOJA_DATOS = "Abril 2025"
CREDENTIALS_FILE = "encestadas.json"

def main():
    # Autenticación
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    # Acceder a la hoja
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(HOJA_DATOS)
    datos = sheet.get_all_values()
    
    # Procesar filas modificadas
    for i, fila in enumerate(datos[1:], start=2):  # Saltar encabezado
        if necesita_procesamiento(fila):
            procesar_fila(sheet, fila, i)

def necesita_procesamiento(fila):
    """Determina si una fila necesita ser procesada"""
    # Verifica si las celdas clave tienen datos
    return (len(fila) > 6 and all(fila[:6]) and  # Columnas A-F llenas
            (len(fila) < 14 or not fila[13]))    # Columna N vacía (puntaje)

def procesar_fila(sheet, fila, row_num):
    """Calcula y actualiza el puntaje para una fila"""
    # Aquí va tu lógica de cálculo de puntaje
    # Ejemplo simplificado:
    puntaje = calcular_puntaje(fila)
    
    # Actualizar hoja
    sheet.update_cell(row_num, 14, puntaje)  # Columna N
    print(f"Fila {row_num} actualizada - Puntaje: {puntaje}")

def calcular_puntaje(fila):
    """Tu lógica completa de cálculo de puntaje"""
    # Implementa aquí todas tus reglas de cálculo
    return 100  # Valor de ejemplo

if __name__ == "__main__":
    print(f"{datetime.datetime.now()} - Iniciando procesamiento...")
    main()
    print("Proceso completado")
