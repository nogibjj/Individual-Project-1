# Haochong-Individual-Project-1 [![CI](https://github.com/nogibjj/Individual-Project-1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Individual-Project-1/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Individual Project 1. First of all, I find a new csv about covid, which have record of data like total confirmed for days begin from 2020-04-16 to 2022-02-13. Secondly, I define functions called `Describe` and `get_median` to return the descriptive statistics of the dataset. After that, I use the jupyter notebook to print the descriptive statistics and plot the histagrams of the distribution of the `TotalConfirmed` by count. Next, I plot the histagrams of the distribution of the `TotalConfirmed` by `Date` and simplify it into a scatter plot. Consequently, I noticed that they have linear relation so I did a linear regression. All codes above are first complished in jupyter notebook. After that, I transfered the code into the `lib.py` as self-define functions and I use assert in the `test_lib.py` to test my function definitions and result. Futhermore, I import my functions into both jupyter notebook and `script.py`, use `nbval` to test the jupyter notebook. In addition, I write `test_script.py` to test my `script.py`. Finally, I use Action to run `Makefile` and got a 100% pass. 

Important file:
* `Individual Project 1.ipynb`
* `Makefile`
* `lib.py`
* `script.py`
* `test_lib.py`
* `test_script.py`
* `requirements.txt`

# Purpose
To generate descriptive statistics and visualization on datasets using `Pandas` in both jupyther notebook (.ipynb) and .py files. Use `nbval` plugin for pytest to test jupyther notebook and `test_.py` to test to test library and script. Formats code with Python black. Additionally, Lints code with `Ruff` this time.

## Preparation 
1. open codespaces 
2. open Colab
3. wait for container to be built with requiremnts.txt installed

## Check format and test errors
1. Format code with Python black by using `make format`
2. Lint code with Ruff by using `make lint`. Add `ruff==0.0.284` in `requirements.txt` and `ruff check *.py mylib/*.py` under `lint` in `Makefile`

<img width="616" alt="截屏2023-09-16 上午1 56 51" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/f0cdb336-da4f-4fcd-acaa-235d6410aa16">


4. Test code by using `make test`

In this project, I failed lots of times before I passed all of them. At the beginning, I tried to add a file with `.ipynb` directly in my repo. Nevertheless, it shown as "invalid notebook". After consulting TA, I understanded that we can't use jupyter notebook in this way. Since setting up the environment on github would be redundant, I created a jupyter notebook locally, git clone my repo to local and drag the notebook into my repo then update my repo. Finally, I got vaild notebook.

<img width="169" alt="截屏2023-09-16 上午1 43 18" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/c67ffd16-68ff-450f-9468-464f5b6bccdd">


When I tried to plot the distribution of `TotalConfirmed` by `Date`, after I groupby the dataset by `Date`, I met the second problem: dates were not shown under x-axis. After print the type of Date column, I found out that the type is str. Hence, I use package `datetime` to convert the type into date, then I fixed the problem.

<img width="552" alt="截屏2023-09-16 上午1 52 53" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/563d977d-2618-4620-95b3-2074bfb6e286">


When I tried to do the liner regression, I met the third problem: both date type data and row index are not able to do liner regression. Therefore, first reset the Date index and then I added a new column into the dataframe as Date index, use that column and `TotalConfirmed` to do liner regression. Finally, I got waht I want.

<img width="281" alt="截屏2023-09-16 上午1 54 59" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/bfbcedd3-05f3-4ec3-a928-e9b009abe436">


After fixing all of these, I got all pass.
`test_lib.py` and `test_script.py`:

<img width="653" alt="截屏2023-09-16 上午1 58 01" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/65e3467c-c17a-48f4-8256-f2edfebe8e91">

`nbval`:

<img width="600" alt="截屏2023-09-16 上午1 59 19" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/38de4371-98c1-45e8-a98f-e9aad5bb4647">


## Visualization
The distribution of TotalConfirmed by cout is plotted by `PlotHistOfTotalConfirmed`:

<img width="628" alt="截屏2023-09-16 上午2 03 20" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/a4b140c7-4f29-4781-a7e1-6d9bf0859dd5">

The distribution of TotalConfirmed by Date is plotted by `PlotHistTotalConfirmedVsDate`:

<img width="633" alt="截屏2023-09-16 上午2 03 49" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/8c3a1c9a-715c-4166-8cef-bc41a46b8f33">

Simplify it to a scatter plot is plotted by `PlotScatter`:

<img width="628" alt="截屏2023-09-16 上午2 04 13" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/ddded506-4990-4ed2-add8-8f1c35794615">

The graph indicates a linear relation, do linear regression by `LROfTotalConfirmedVsDate`:

<img width="645" alt="截屏2023-09-16 上午2 04 35" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/069e8565-e694-413e-85c8-6c521eedba41">


## Summary statistics
Describe:

<img width="807" alt="截屏2023-09-16 上午2 05 07" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/76ff59e6-3fc8-456e-8388-0ac22eb4f109">


Median:

<img width="399" alt="截屏2023-09-16 上午2 07 58" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/868c35f9-794a-4a3d-8d42-0cc040652dd8">

## Video





