from astropy.io.fits.hdu import BinTableHDU
from astropy.table import Table
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTabWidget

__all__ = ["TableTabs", "BinTableTabs"]


class TableTabs(QTabWidget):
    def __init__(self, table, parent=None, main_window=None):
        super().__init__(parent)

        if not isinstance(table, Table):
            raise TypeError("table must be an instance of astropy.table.Table.")
        self.table = table
        self.table_table = self.init_table(self.table)

        self.header = self.init_header(self.table.meta)

        self.main_window = main_window

        self.setTabPosition(QTabWidget.North)
        self.setMovable(True)
        self.addTab(self.table_table, "Table")
        self.addTab(self.header, "Header")

        self.main_window.setCentralWidget(self)

    @staticmethod
    def init_header(data):
        # Create a QTableWidget with two columns
        header_table = QTableWidget()
        header_table.setColumnCount(2)
        header_table.setHorizontalHeaderLabels(["Key", "Value"])

        # Populate the table with dictionary data
        for row, (key, value) in enumerate(data.items()):
            header_table.insertRow(row)
            header_table.setItem(row, 0, QTableWidgetItem(str(key)))
            header_table.setItem(row, 1, QTableWidgetItem(str(value)))
        return header_table

    @staticmethod
    def init_table(data):
        table_table = QTableWidget()
        table_table.setColumnCount(len(data.colnames))
        table_table.setHorizontalHeaderLabels(data.colnames)

        for row_idx, row in enumerate(data):
            table_table.insertRow(row_idx)
            for col_idx, col in enumerate(data.columns):
                table_table.setItem(
                    row_idx, col_idx, QTableWidgetItem(str(data[row_idx][col_idx]))
                )
        return table_table


class BinTableTabs(QTabWidget):
    def __init__(self, bin_table, parent=None, main_window=None):
        super().__init__(parent)

        if not isinstance(bin_table, BinTableHDU):
            raise TypeError(
                "bin_table must be an instance of astropy.io.fits.BinTableHDU."
            )
        self.bin_table = bin_table

        self.main_window = main_window

        self.setTabPosition(QTabWidget.North)
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
