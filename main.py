import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
from datetime import datetime
from sklearn.linear_model import LinearRegression

def Describe(df): 
    return df.describe() 

def get_median(df):
    return df.median()

def PlotHistOfTotalConfirmed(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["TotalConfirmed"], bins=20, edgecolor="black")
    plt.title("TotalConfirmed Distribution")
    plt.xlabel("TotalConfirmed")
    plt.ylabel("Count")
    plt.show() 

def PlotHistTotalConfirmedVsDate(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(10, 6))
    for i in range(44870):
        general_df["Date"][i] = datetime.strptime(general_df["Date"][i], '%Y-%m-%d').date()
    #print(type(general_df["Date"][0]))
    df = general_df.groupby("Date").sum()
    #print(df)
    df2 =df.reset_index()
    plt.bar(df2["Date"], df2["TotalConfirmed"])
    plt.title("TotalConfirmed vs Date")
    plt.xlabel("Date")
    plt.ylabel("TotalConfirmed")
    plt.show() 

def PlotScatter(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(10, 6))
    for i in range(44870):
        general_df["Date"][i] = datetime.strptime(general_df["Date"][i], '%Y-%m-%d').date()
    #print(type(general_df["Date"][0]))
    df = general_df.groupby("Date").sum()
    #print(df)
    df2 =df.reset_index()
    plt.scatter(df2["Date"], df2["TotalConfirmed"])
    plt.title("TotalConfirmed vs Date")
    plt.xlabel("Date")
    plt.ylabel("TotalConfirmed")
    plt.show() 

def LROfTotalConfirmedVsDate(csv):
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    plt.figure(figsize=(10, 6))
    df = general_df.groupby("Date").sum()
    df2 =df.reset_index()
    x = []
    a = 0
    for i in range(1282):
        x.append(a)
        a = a + 1
    df2["date_index"] = x
    lr = LinearRegression()  # create object for the class
    lr.fit(df2["date_index"].values.reshape(-1, 1), df2["TotalConfirmed"])  # perform linear regression
    Y_pred = lr.predict(df2["date_index"].values.reshape(-1, 1))  # make predictions
    plt.scatter(df2["date_index"].values.reshape(-1, 1), df2["TotalConfirmed"])
    plt.plot(df2["date_index"].values.reshape(-1, 1), Y_pred, color='red')
    plt.title("TotalConfirmed vs Date")
    plt.xlabel("Date")
    plt.ylabel("TotalConfirmed")
    plt.show()

def Summary(csv):
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
