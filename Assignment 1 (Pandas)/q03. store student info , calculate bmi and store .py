import numpy as np
import pandas as pd

name = []
height = []
weight = []
bmi = []

n = int(input("enter total no of student: "))
for i in range(n):
  name1 = input("enter name: ")
  name.append(name1);
  height1 = int(input("enter height: "))
  height.append(height1);
  weight1 = int(input("enter weight: ",));
  weight.append(weight1);
  bmi1 = weight1/(height1*height1)
  if bmi1<25:
    bmi.append("false")
  else:
    bmi.append("true")

df = pd.DataFrame({"name":name,"height":height,"weight":weight,"BMI":bmi}) 
print(df)
