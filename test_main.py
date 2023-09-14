from main import (
    Describe,
    get_median,
    PlotHistOfTotalConfirmed,
    PlotHistTotalConfirmedVsDate,
    PlotScatter,
    LROfTotalConfirmedVsDate,
    Summary,
)
import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
from datetime import datetime
from sklearn.linear_model import LinearRegression

example_csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
data = pd.read_csv(example_csv)

def test_descirbe():
    data = pd.read_csv(example_csv)
    result = Describe(data)
    assert result.loc['mean', 'TotalConfirmed'] == 1638.599265
    assert result.loc['mean', 'TotalDeaths'] == 5.782594
    assert result.loc['std', 'TotalConfirmed'] == 1257.548628
    assert result.loc['std', 'TotalDeaths'] == 7.762456

def test_median():
    data = pd.read_csv(example_csv)
    assert get_median(data['Shape_Leng']) == 60896.5746
    assert get_median(data['Shape_Area']) == 230060526.252

def test_plot1():
    PlotHistOfTotalConfirmed(example_csv)

def test_plot2():
    PlotHistTotalConfirmedVsDate(example_csv)

def test_plot3():
    PlotScatter(example_csv)

def test_plot4():
    LROfTotalConfirmedVsDate(example_csv)

def test_generate_summary_report():
    Summary(example_csv)
