import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression

def Describe(df): 
    return df.describe() 

def get_median(df):
    return df.median()

def PlotHistOfTotalConfirmed(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(7.2, 4.32))
    plt.hist(general_df["TotalConfirmed"], bins=20, edgecolor="black")
    plt.title("TotalConfirmed Distribution")
    plt.xlabel("TotalConfirmed")
    plt.ylabel("Count")
    plt.show() 

def PlotHistTotalConfirmedVsDate(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(7.2, 4.32))
    a = []
    for i in range(len(general_df.index)):
        a.append(datetime.strptime(general_df["Date"][i], '%Y-%m-%d').date())
    general_df["DateInt"] = a
    #print(type(general_df["Date"][0]))
    df = general_df.groupby("DateInt").sum()
    df2 =df.reset_index()
    plt.bar(df2["DateInt"], df2["TotalConfirmed"])
    plt.title("TotalConfirmed vs Date")
    plt.xlabel("Date")
    plt.ylabel("TotalConfirmed")
    plt.show() 

def PlotScatter(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(7.2, 4.32))
    a = []
    for i in range(len(general_df.index)):
        a.append(datetime.strptime(general_df["Date"][i], '%Y-%m-%d').date())
    general_df["DateInt"] = a
    #print(type(general_df["Date"][0]))
    df = general_df.groupby("DateInt").sum()
    df2 =df.reset_index()
    plt.scatter(df2["DateInt"], df2["TotalConfirmed"])
    plt.title("TotalConfirmed vs Date")
    plt.xlabel("Date")
    plt.ylabel("TotalConfirmed")
    plt.show() 

def LROfTotalConfirmedVsDate(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(7.2, 4.32))
    df = general_df.groupby("Date").sum()
    df2 =df.reset_index()
    x = []
    a = 0
    for i in range(len(df2.index)):
        x.append(a)
        a = a + 1
    df2["date_index"] = x
    lr = LinearRegression()  # create object for the class
    # perform linear regression
    lr.fit(df2["date_index"].values.reshape(-1, 1), df2["TotalConfirmed"]) 
    # make predictions
    Y_pred = lr.predict(df2["date_index"].values.reshape(-1, 1)) 
    plt.scatter(df2["date_index"].values.reshape(-1, 1), df2["TotalConfirmed"])
    plt.plot(df2["date_index"].values.reshape(-1, 1), Y_pred, color='red')
    plt.title("TotalConfirmed vs Date")
    plt.xlabel("Date_Increasement")
    plt.ylabel("TotalConfirmed")
    plt.show()
