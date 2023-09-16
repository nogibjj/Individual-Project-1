from lib import (
    Describe,
    get_median,
    PlotHistOfTotalConfirmed,
    PlotHistTotalConfirmedVsDate,
    PlotScatter,
    LROfTotalConfirmedVsDate,
)

import pandas as pd

def test_main():
    example_csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
    data = pd.read_csv(example_csv)
    result = Describe(data)
    get_median(data['TotalConfirmed'])
    get_median(data['TotalDeaths'])
    get_median(data['DistinctPatientsTested'])
    get_median(data['NewInTheLast14Days'])
    PlotHistOfTotalConfirmed(example_csv)
    PlotHistTotalConfirmedVsDate(example_csv)
    PlotScatter(example_csv)
    LROfTotalConfirmedVsDate(example_csv)



if __name__ == "__main__":
    test_main()