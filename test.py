import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path="ilk_yuzexcel.xlsx"

data=pd.read_excel(file_path)


a=data["Start_Time"].dt.month
print(a)

