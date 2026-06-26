from openpyxl import Workbook


def export_excel(df):

    wb = Workbook()

    ws = wb.active

    ws.append(df.columns.tolist())

    for row in df.itertuples(index=False):
        ws.append(list(row))

    wb.save("Finance_Report.xlsx")