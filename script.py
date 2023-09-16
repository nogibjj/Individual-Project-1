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

if __name__ == "__main__":
    result = Describe(data)
    print("The descriptive statistics of the csv is: ")
    print(result)
    print("The median of TotalConfirmed is:")
    print(get_median(data['TotalConfirmed']))
    print("The median of TotalDeaths is:")
    print(get_median(data['TotalDeaths']))
    print("The median of DistinctPatientsTested is:")
    print(get_median(data['DistinctPatientsTested']))
    print("The median of NewInTheLast14Days is:")
    print(get_median(data['NewInTheLast14Days']))
    print("The distribution TotalConfirmed of by cout is:")
    PlotHistOfTotalConfirmed(example_csv)
    print("The distribution TotalConfirmed of by Date is:")
    PlotHistTotalConfirmedVsDate(example_csv)
    print("Simplify it to a scatter plot:")
    PlotScatter(example_csv)
    print("The graph indicates a linear relation, do linear regression:")
    LROfTotalConfirmedVsDate(example_csv)



    