# Haochong-Individual-Project-1 [![CI](https://github.com/nogibjj/Individual-Project-1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Individual-Project-1/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Individual Project 1. First of all, I find a new csv about covid, which have record of data like total confirmed for days begin from 2020-04-16 to 2022-02-13. Secondly, I define functions called "polars_describe" and "get_median" to return the descriptive statistics of the dataset. After that, I use the Colab to print the data and plot histagrams and then use assert in the test.py to test my function. Finally, I use Action to run Makefile and got a 100% pass. 

# Purpose
To generate descriptive statistics and visualization on datasets using Polars, which is similar to week 2. 

## Preparation 
1. open codespaces 
2. open Colab
3. wait for container to be built with requiremnts.txt installed

## Check format and test errors
1. Format code `make format`
2. Lint code `make lint`
   <img width="964" alt="截屏2023-09-12 下午9 28 23" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/1b6a52e1-961c-4f53-9699-c445690b792e">

3. Test code `make test`

There is just one problem that stucked me. At the beginning, I thought that we should use the same method to get access to the specific data we want in a polar dataframe, but is not. Hence, First I got this:
<img width="590" alt="截屏2023-09-12 下午9 33 21" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/887b849d-3259-4119-a9cb-90414481dfe4">

After quickly print the polar describe, I found out that methods for polar are defferent. Therefore, I change `assert result.loc['mean', 'Shape_Area'] == 228153453.41946846` to  
`assert result[["describe", "Shape_Area"]][2, 1] == 228153453.41946846`. Then this problem is fixed.

Then, I got failed again, and I noticed an interesting thing is that when I using polars, I got `assert result[["describe", "Shape_Leng"]][2, 1] == 60622.470193439854`. However, I got `assert result.loc['mean', 'Shape_Leng'] == 60622.47019343987` last week while using pandas. Looks like polars is doing a more accurate job. After fixing these, I got all pass.
<img width="580" alt="截屏2023-09-12 下午9 40 12" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/3c605bc9-318d-4fa8-ac9e-4344b696cba8">


## Visualization
Two histagrams of two data in the dataframe can be visualized by `PlotShapeLeng` and `PlotShapeArea` and here are them:
<img width="873" alt="截屏2023-09-12 下午9 42 03" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/54cafbfa-e201-4dfd-aa96-7034fd0d9709">
<img width="862" alt="截屏2023-09-12 下午9 42 22" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/fa3537b8-fdc0-42b3-b408-86c203e1671b">


## Summary statistics
Describe:
<img width="630" alt="截屏2023-09-12 下午9 43 34" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/d9cc37d1-a38f-4974-89de-aadbccb26b4e">

Median:
<img width="243" alt="截屏2023-09-12 下午9 45 48" src="https://github.com/nogibjj/706-Week3-mini-project/assets/89813704/59d93e8b-d8da-4d99-bdf8-09a265c82728">



