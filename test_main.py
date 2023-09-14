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

example_csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
data = pd.read_csv(example_csv)

def test_descirbe():
    data = pd.read_csv(example_csv)
    result = Describe(data)
    assert result.loc['mean', 'TotalConfirmed'] == 1638.5992645420104
    assert result.loc['mean', 'TotalDeaths'] == 5.7825941609092935
    assert result.loc['std', 'TotalConfirmed'] == 1257.5486280119524
    assert result.loc['std', 'TotalDeaths'] == 7.7624562353408635
    assert result.loc['mean', 'DistinctPatientsTested'] == 92.4781814129708
    assert result.loc['mean', 'NewInTheLast14Days'] == 31.482259861823046
    assert result.loc['std', 'DistinctPatientsTested'] == 149.57136794989026
    assert result.loc['std', 'NewInTheLast14Days'] == 96.67810383876467

def test_median():
    data = pd.read_csv(example_csv)
    assert get_median(data['TotalConfirmed']) == 1489.0
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

def test_generate_summary_report():
    Summary(example_csv)
