from utilities.excel_reader import ExcelReader


class DataProvider:

    @staticmethod
    def get_login_data():

        return ExcelReader.get_data(
            "testdata/login_data.xlsx",
            "Sheet1"
        )
        