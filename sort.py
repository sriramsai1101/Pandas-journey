import pandas as pd
data={
    "names":["ram","sai","sri"],
    "marks":[80,90,10]
}
student=pd.DataFrame(data)
print("sorting values:  ")
print("ascending values: ")
print(student.sort_values("marks"))
print("descending values")
print(student.sort_values("marks",ascending=False))
print("csv file:  ")
fram=pd.read_csv("students.csv")
print(fram)
print(fram.shape)
print(fram.columns)
print(fram.head())
print("greater than 20:  ")
print(fram[fram["marks"]>20])
