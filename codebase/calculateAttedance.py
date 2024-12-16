import os
import pandas as pd
def cal():
    fp=os.getcwd()+os.sep+"log"
    no=len(os.listdir(fp))
    df = pd.read_csv("StudentDetails"+os.sep+"StudentDetails.csv")
    col_names = ['Id','Name','Email','number_of_classes']
    attendance = pd.DataFrame(columns=col_names)
    for index,row in df.iterrows():
        attendance.loc[len(attendance)] = [
            row['Id'],
            row['Name'],
            row['Email'],
            row['number_of_classes']
        ]
    print(attendance) 
    attendance.to_csv("StudentDetails\StudentDetails.csv",index=False)