import pandas as pd
df={
    "names":["sri","ram","sai","bunny","bun"],
    "python":[10,20,30,30,10],
   "pandas":[20,50,80,90,70],
   "numpy":[90,80,50,80,70] 
}
frame=pd.DataFrame(df)
print(frame)
print("average:",frame["python"].mean())
print("average:",frame["pandas"].mean())
print("average:",frame["numpy"].mean())
total=frame["python"]+frame["pandas"]+frame["numpy"]
print(total)
print("this")
print(frame.loc[0])
print(total.idxmax())
print("topper:",frame["names"].idxmax)
print(frame.loc[2,"pandas"])
print(frame[
    (frame["python"]>10) 
    ])


