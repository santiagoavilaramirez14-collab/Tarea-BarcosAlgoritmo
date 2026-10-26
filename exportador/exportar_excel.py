# Exportador a Excel para guardar datos de cargas, vehiculos y rutas calculadas
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def generar_reporte_excel(ruta_archivo, lista_paquetes, vehiculos_optimizados, rutas_calculadas, kpis):
    wb = openpyxl.Workbook()
    # Eliminar hoja por defecto
    wb.remove(wb.active)

    # Estilos basicos para el reporte
    font_titulo = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
    font_header = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    font_bold = Font(name="Segoe UI", size=10, bold=True)
    font_normal = Font(name="Segoe UI", size=10)
    font_kpi_num = Font(name="Segoe UI", size=18, bold=True, color="003366")

    fill_azul_oscuro = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    fill_azul_claro = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
    fill_verde_suave = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    fill_gris_cebra = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")

    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    # =========================================================================
    # HOJA 1: RESUMEN Y KPIS
    # =========================================================================
    ws_resumen = wb.create_sheet(title="Resumen")
    ws_resumen.views.sheetView[0].showGridLines = True

    ws_resumen["B2"] = "REPORTE DE ENTREGAS Y RUTAS"
    ws_resumen["B2"].font = font_titulo
    ws_resumen["B2"].fill = fill_azul_oscuro
    ws_resumen["B2"].alignment = Alignment(horizontal="center", vertical="center")
    ws_resumen.merge_cells("B2:G2")
    ws_resumen.row_dimensions[2].height = 32

    ws_resumen["B3"] = "Resumen de optimizacion de paquetes (Mochila) y rutas (Dijkstra)"
    ws_resumen["B3"].font = Font(name="Segoe UI", size=10, italic=True, color="595959")
    ws_resumen.merge_cells("B3:G3")

    kpi_cards = [
        ("Total Paquetes", f"{kpis.get('total_paquetes', len(lista_paquetes))}", "B5", "B6"),
        ("Peso Total", f"{kpis.get('peso_total_kg', 0):,.1f} kg", "C5", "C6"),
        ("Volumen Total", f"{kpis.get('volumen_total_m3', 0):,.2f} m³", "D5", "D6"),
        ("Vehículos Utilizados", f"{len(vehiculos_optimizados)}", "E5", "E6"),
        ("Rutas Calculadas", f"{len(rutas_calculadas)}", "F5", "F6"),
        ("Aprovechamiento Espacio", f"{kpis.get('aprovechamiento_promedio', 0):.1f}%", "G5", "G6")
    ]

    for label, val, c_label, c_val in kpi_cards:
        ws_resumen[c_label] = label
        ws_resumen[c_label].font = font_bold
        ws_resumen[c_label].alignment = Alignment(horizontal="center", vertical="center")
        ws_resumen[c_label].fill = fill_azul_claro
        ws_resumen[c_label].border = thin_border

        ws_resumen[c_val] = val
        ws_resumen[c_val].font = font_kpi_num
        ws_resumen[c_val].alignment = Alignment(horizontal="center", vertical="center")
        ws_resumen[c_val].fill = fill_verde_suave
        ws_resumen[c_val].border = thin_border

    ws_resumen.row_dimensions[5].height = 24
    ws_resumen.row_dimensions[6].height = 36

    # =========================================================================
    # HOJA 2: INVENTARIO DE PAQUETES (DIMENSIONES, PESO, COORDENADAS)
    # =========================================================================
    ws_paquetes = wb.create_sheet(title="1. Inventario Paquetes")
    ws_paquetes.views.sheetView[0].showGridLines = True

    headers_paq = [
        "ID Paquete", "Descripción de Carga", "Alto (m)", "Ancho (m)", "Profundidad (m)",
        "Volumen (m³)", "Peso (kg)", "Origen", "Destino Final", "Latitud", "Longitud", "Modo Preferido", "Prioridad"
    ]

    for col_idx, h in enumerate(headers_paq, start=1):
        cell = ws_paquetes.cell(row=1, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_azul_oscuro
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws_paquetes.row_dimensions[1].height = 28

    for row_idx, p in enumerate(lista_paquetes, start=2):
        fila = [
            p.id_paquete, p.descripcion, p.alto, p.ancho, p.profundidad,
            p.volumen_m3, p.peso_kg, p.origen, p.destino_nombre, p.lat, p.lon,
            p.modalidad_preferida.upper(), p.prioridad
        ]
        fill_actual = fill_gris_cebra if row_idx % 2 == 0 else PatternFill(fill_type=None)
        for col_idx, val in enumerate(fila, start=1):
            cell = ws_paquetes.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_normal
            cell.border = thin_border
            if fill_actual.fill_type: cell.fill = fill_actual
            if col_idx in [1, 3, 4, 5, 6, 7, 10, 11, 13]:
                cell.alignment = Alignment(horizontal="right", vertical="center")
            elif col_idx in [12]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
        ws_paquetes.row_dimensions[row_idx].height = 20

    # =========================================================================
    # HOJA 3: ASIGNACIÓN DE CARGA (ALGORITMO DE LA MOCHILA)
    # =========================================================================
    ws_mochila = wb.create_sheet(title="2. Optimización Mochila")
    ws_mochila.views.sheetView[0].showGridLines = True

    headers_mochila = [
        "ID Barco", "Nombre del Barco", "Tipo", "Capacidad Peso (kg)", "Peso Cargado (kg)",
        "% Peso Usado", "Capacidad Vol (m³)", "Volumen Cargado (m³)", "% Vol Usado", "Cant. Paquetes", "IDs Paquetes Asignados"
    ]

    for col_idx, h in enumerate(headers_mochila, start=1):
        cell = ws_mochila.cell(row=1, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_azul_oscuro
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws_mochila.row_dimensions[1].height = 28

    for row_idx, v in enumerate(vehiculos_optimizados, start=2):
        ids_str = ", ".join(str(p.id_paquete) for p in v.paquetes_asignados)
        fila_v = [
            v.id_vehiculo, v.nombre, v.tipo.upper(), v.capacidad_peso_kg, v.peso_actual_kg,
            f"{v.porcentaje_peso_usado}%", v.capacidad_volumen_m3, v.volumen_actual_m3,
            f"{v.porcentaje_volumen_usado}%", len(v.paquetes_asignados), ids_str
        ]
        fill_actual = fill_gris_cebra if row_idx % 2 == 0 else PatternFill(fill_type=None)
        for col_idx, val in enumerate(fila_v, start=1):
            cell = ws_mochila.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_normal
            cell.border = thin_border
            if fill_actual.fill_type: cell.fill = fill_actual
            if col_idx in [4, 5, 6, 7, 8, 9, 10]:
                cell.alignment = Alignment(horizontal="right", vertical="center")
            elif col_idx in [1, 3]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
        ws_mochila.row_dimensions[row_idx].height = 22

    # =========================================================================
    # HOJA 4: RUTAS ÓPTIMAS (ALGORITMO DE DIJKSTRA)
    # =========================================================================
    ws_dijkstra = wb.create_sheet(title="3. Rutas Óptimas Dijkstra")
    ws_dijkstra.views.sheetView[0].showGridLines = True

    headers_dijkstra = [
        "ID Paquete", "Descripción", "Puerto Origen", "Puerto Destino",
        "Ruta Marítima Óptima", "Escalas", "Distancia Náutica (km)", "Tiempo Estimado (horas)"
    ]

    for col_idx, h in enumerate(headers_dijkstra, start=1):
        cell = ws_dijkstra.cell(row=1, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_azul_oscuro
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws_dijkstra.row_dimensions[1].height = 28

    for row_idx, r in enumerate(rutas_calculadas, start=2):
        camino_str = " ➔ ".join(r["ruta"]) if r.get("ruta") else "No alcanzable"
        escalas = max(0, len(r.get("ruta", [])) - 1)
        fila_r = [
            r["id_paquete"], r["descripcion"], r["origen"], r["destino"],
            camino_str, escalas, r.get("distancia_km", 0), r.get("tiempo_h", 0)
        ]
        fill_actual = fill_gris_cebra if row_idx % 2 == 0 else PatternFill(fill_type=None)
        for col_idx, val in enumerate(fila_r, start=1):
            cell = ws_dijkstra.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_normal
            cell.border = thin_border
            if fill_actual.fill_type: cell.fill = fill_actual
            if col_idx in [1, 6, 7, 8]:
                cell.alignment = Alignment(horizontal="right", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
        ws_dijkstra.row_dimensions[row_idx].height = 22

    # Autoajustar ancho de columnas para todas las hojas
    for ws in [ws_resumen, ws_paquetes, ws_mochila, ws_dijkstra]:
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

    # Guardar archivo
    wb.save(ruta_archivo)
    print(f"Reporte Excel generado exitosamente en: {ruta_archivo}")
    return ruta_archivo
