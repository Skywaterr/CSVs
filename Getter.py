import xlrd
import csv
import glob
import os

# Take all the xls files in this folder
# Convert them to CSVs.

def convert_folder_xls_to_csv():
    """Convert all the excel sheets in the cwd to csv files, ordered by number."""
    cwd = os.getcwd()
    index = 0
    for name in glob.glob(cwd + "\\*.xls"):
        wb = xlrd.open_workbook(name)
        sh = wb.sheet_by_index(0)
        your_csv_file = open('csv' + str(index) + '.csv', 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()
        index += 1 

if __name__ == "__main__":
    convert_folder_xls_to_csv()