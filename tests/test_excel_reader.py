from utilities.excel_reader import ExcelReader

def test_excel_reader():

    data = ExcelReader.get_data(
        "testdata/login_data.xlsx",
        "Sheet1"
    )

    for row in data:
        print(row)