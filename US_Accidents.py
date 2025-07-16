import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path="US_Accidents_March23.csv"

data=pd.read_csv(file_path)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

def grafik(x,y,x_label,y_label,title,save):
    plt.figure()
    plt.bar(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.savefig(save,dpi=300,bbox_inches='tight')
    plt.close()

def number_of_city():
    cities_sum = data["City"].value_counts().head(15)
    grafik(cities_sum.index,cities_sum.values,"City","Number of Accidents","Number of Accidents per City","number_of_city")


def weather_condition():
    weather_sum=data["Weather_Condition"].value_counts().head(10)
    grafik(weather_sum.index,weather_sum.values,"Weather_Condition","Number of Accidents","Number of Accidents per Weather_Condition","weather_condition")


def date_number():
    #error
    month = (data["Start_Time"].dt.month).value_counts()
    grafik(month.index,month.values,"Date","Number of Accidents","Number of Accidents per Date","date")
#weather_condition()
#number_of_city()
date_number()




