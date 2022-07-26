import pandas as pd
import numpy as np

# Creating the dataframe 
df = pd.DataFrame({"A":[5, 3, 6, 4], 
                   "B":[11, 2, 4, 3], 
                   "C":[4, 3, 8, 5],  
                   "D":[5, 4, 2, 8]}) 
  
# Print the dataframe 
print(df)

# 
print("Call cumprod(aixs = 0)")
print(df.cumprod(axis = 0))

# 
print("Call cumprod(aixs = 1)")
print(df.cumprod(axis = 1))

#=========================
df2 = pd.DataFrame([1, 2, 3, 5])

print(df2)

# 回傳值再平方
print(df2.cumprod()**2)
#print(aa)



