from openpyxl import Workbook
import pandas as pd


def export_excel(df, filename="Finance_Report.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    ws.append(df.columns.tolist())

    for row in df.itertuples(index=False):
        ws.append(list(row))

    wb.save(filename)

    return filename