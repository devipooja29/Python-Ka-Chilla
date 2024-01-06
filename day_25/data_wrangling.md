# Data Wrangling Report

## Introduction

The 2019–20 coronavirus pandemic is an ongoing global pandemic of coronavirus disease 2019 (COVID-19) caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The virus first emerged in Wuhan, Hubei, China, in December 2019. On 11 March 2020, the World Health Organization declared the outbreak a pandemic. As of 11 March 2020, over 126,000 cases have been confirmed in more than 110 countries and territories, with major outbreaks in mainland China, Italy, South Korea, and Iran. More than 4,600 have died from the disease and 67,000 have recovered.

2019 Novel Coronavirus (2019-nCoV) is a virus (more specifically, a coronavirus) identified as the cause of an outbreak of respiratory illness first detected in Wuhan, China. Early on, many of the patients in the outbreak in Wuhan, China reportedly had some link to a large seafood and animal market, suggesting animal-to-person spread. However, a growing number of patients reportedly have not had exposure to animal markets, indicating person-to-person spread is occurring. At this time, it’s unclear how easily or sustainably this virus is spreading between people.

The dataset has information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.

Dataset link : <https://www.kaggle.com/datasets/whenamancodes/covid-19-coronavirus-pandemic-dataset>

The EDA has been performed on dataset and following hypotheses have been made:

H0: The number of recoveries is equal to the total number of tests conducted.\
H1: The number of recoveries is less than the total number of tests conducted.\
H2: The number of recoveries is more than the total number of tests conducted.

## Author & Data

Author: Pooja Dinani\
Date: 16/12/2023

## Handling Missing Values

There are missing values in almost all columns. The column named 'New Deaths' has 98.695652% of missing values so it was dropped from dataset. Missing values in the columns of interest (Total Cases, Total Tests, and Total Recovered) were filled with the mean of respective column.

## Outliers in Data

The number of outliers in each column is relatively small so there is no need of removing outliers from data. Besides, removing outliers means exlcuding rows from analysis and exlcuding rows means excluding data of entire country from the data.

## Data Normalization

The variables of interest were not normalized so they have been normalized using Log Transformation. After log transformation, results are as follow:

![Log_Transformation](../pic1.png)

The results of Shapiro tests are as follow:

Total Cases: Statistic=0.9745823740959167, p-value=0.00037419056752696633\
Total Tests: Statistic=0.9895334243774414, p-value=0.09418582916259766\
Total Recovered: Statistic=0.9607686996459961, p-value=6.019584816385759e-06

Shapiro results suggests that there is not enough evidence to accept null hypothesis (Data is normal). Further, Boxcox transformation was applued on log transformed data to normalize the data. After Boxcox, results are as follow:

![Boxcox_Transformation](../pic2.png)

The results of Shapiro test are as follow:

Total Cases: Statistic=0.9891136884689331, p-value=0.07978564500808716\
Total Tests: Statistic=0.9902926683425903, p-value=0.12694963812828064\
Total Recovered: Statistic=0.9895999431610107, p-value=0.09669016301631927

Now there is enough evidence to accept null hypothesis and say data is normal as in all variables p-value > 0.05.

## Hypothesis Testing

For hypothesis testing student's t-test was used and obtained results are t-statistic: -24.543878818949526, p-value: 4.716233178429569e-66.
The extremely small p-value (close to zero) indicates strong evidence to reject the null hypothesis (H0) that the number of recoveries is equal to the total number of tests conducted. Given the negative sign of the t-statistic (-24.54), it suggests that the mean of 'Total Recoveries' is significantly lower than the specified value (mean of 'Total Tests'). Therefore, there is enough evidence to support the alternative hypothesis (H1) that the number of recoveries is less than the total number of tests conducted.

## Feature Scaling

It is necessary for all variables/features in dataset to be on scale to perform linear regression. In current dataset variables are not in same scale, thereby, MinMaxScaler was used.
