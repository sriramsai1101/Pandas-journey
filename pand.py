import pandas as pd
data=pd.Series(
    
        [10,20,30],
        index=["ram","sai","bunny"]
        )
print(data)
df={
    "name":["ram",'sai',"sri"],
    "marks":[80,30,90],
    "branch":["aiml","cse","ece"]
}
fram=pd.DataFrame(df)
print(fram)