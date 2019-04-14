import os
import pandas as pd
import numpy as np
import xlrd, xlwt
from Project2 import app


def file_comparison(filename):
    input1 = (pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER']+filename),sheet_name='Sheet1'))
    input2 = (pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'],"input1.xls"),sheet_name='Sheet1'))

    comparision_values = input1.values == input2.values

    print(comparision_values)
    rows,cols=np.where(comparision_values==False)

    def Remove(duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        return final_list

    row_Number = Remove(rows)

    output_Final = pd.DataFrame([])
    for item in row_Number :
        result = input2.iloc[item,:]
        output_Final = output_Final.append(result)
    output = pd.DataFrame(output_Final)
    output.set_index("Sno", inplace=True)
    output.head()
    list = ["First Name","Last Name","Gender","Country","Age","Date","Id"]
    file_output = output[list]

    writer = pd.ExcelWriter(os.path.join(app.config['UPLOAD_FOLDER'],"result.xls"))
    file_output.to_excel(writer,sheet_name='Sheet1')
    writer.save()

    found = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'],"result.xls"))
    if found:
        for file in os.listdir(app.config['UPLOAD_FOLDER']):
            if file == "result.xls":
                return file




'''

    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        if file == "result.xls":
            return file

'''



