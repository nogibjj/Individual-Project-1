from lib import (
    Describe,
    get_median,
    PlotHistOfTotalConfirmed,
    PlotHistTotalConfirmedVsDate,
    PlotScatter,
    LROfTotalConfirmedVsDate,
)
import pandas as pd

example_csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
data = pd.read_csv(example_csv)

def test_descirbe():
    data = pd.read_csv(example_csv)
    result = Describe(data)
    assert result.loc['mean', 'TotalConfirmed'] == 1640.2458611481975
    assert result.loc['mean', 'TotalDeaths'] == 5.785291499777481
    assert result.loc['std', 'TotalConfirmed'] == 1258.190961170143
    assert result.loc['std', 'TotalDeaths'] == 7.763615960765412
    assert result.loc['mean', 'DistinctPatientsTested'] == 92.36203827325323
    assert result.loc['mean', 'NewInTheLast14Days'] == 31.447797062750332
    assert result.loc['std', 'DistinctPatientsTested'] == 149.49585064537303
    assert result.loc['std', 'NewInTheLast14Days'] == 96.6095005292558

def test_median():
    data = pd.read_csv(example_csv)
    assert get_median(data['TotalConfirmed']) == 1490.0
    assert get_median(data['TotalDeaths']) == 2.0
    assert get_median(data['DistinctPatientsTested']) == 39.0
    assert get_median(data['NewInTheLast14Days']) == 2.000000

def test_plot1():
    PlotHistOfTotalConfirmed(example_csv)

def test_plot2():
    PlotHistTotalConfirmedVsDate(example_csv)

def test_plot3():
    PlotScatter(example_csv)

def test_plot4():
    LROfTotalConfirmedVsDate(example_csv)

