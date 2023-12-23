# Food Hygiene Ratings - Data Analysis

## Introduction

The **Food Hygiene Rating Scheme** is a system that involves food businesses being inspected by environmental health officers, with focuses on food hygiene, cleanliness of premises, and management of food safety. Based on the standards found, an overall rating of **0 to 5** is awarded, with 5 indicating very good standards and 0 indicating urgent improvement is necessary. The official website of the scheme is: https://ratings.food.gov.uk.

**Food safety** is a key priority for most consumers, and Food Hygiene Ratings help consumers make informed decisions regarding where to purchase food whilst ensuring their health is protected.

Whilst most businesses pass inspections and are deemed safe, a small number have inadequate food safety standards and are given a low, failing rating.

Food safety standards indeed vary based on many factors, from location to type of business. This project focuses on analysis of these variations and also exploration of possible reasons for the differences in standards.

In a nutshell, this project consists of the following components:

- A **script to obtain data** from the official Food Hygiene Ratings API (https://api.ratings.food.gov.uk), which when run, obtains all records and saves them to a CSV.
- Code that analyses the **sub-metrics**: Hygiene, Cleanliness and Management, and a corresponding report.
- Code that analyses various **factors** that may affect food safety standards, and a corresponding report.

## Key Insights

Various notable discoveries have been revealed through this data analysis project, but the most significant ones are as follows:

- Businesses score better in **Hygiene** on average, compared to Cleanliness and Management.
- Businesses in **Northern Ireland** have significantly higher average Food Hygiene Ratings than in England and Wales.
- **Schools/Universities** and **Hospitals/Childcare** have extremely high average Food Hygiene Ratings.
- **Takeaways** have by far the lowest average Food Hygiene Ratings compared to other business types.
- **Deprived** areas have significantly lower average Food Hygiene Ratings.

## Reports

There are two reports, one for analysis of sub-metrics and the other for analysis of the various factors affecting food safety standards. If unfamiliar with the technicalities of Food Hygiene Ratings, it is recommended to read the sub-metrics report before the factors report, for contextual knowledge.

- [Sub-metrics - Report](sub_metrics/REPORT.md)
- [Factors affecting food safety - Report](factors/REPORT.md)

## Code

The **Python** programming language has been used throughout the entire project, including the API script and the data analysis modules.

Of course, the API script has been run to collate the data, and each of the data analysis modules have been run to obtain the resulting averages, frequencies, correlations and graphs.

The code can be run, modified and extended freely. To run any code yourself, please note the following:

- The project has been developed in **Python 3.10**, so code may not work on earlier Python versions.
- The `requests` library is used in the API script to fetch the data from the website.
- The `pandas` library is used extensively for seamless data analysis.
- The `matplotlib` library is used to create graphs to visualise particular statistics.

Ensure a suitable Python version alongside the required third party libraries are installed. Python, and all these libraries are used extremely commonly, with millions of users each, so various installation guides are available online if needed.

Here are some points to note about code functionality:
- Upon successfully running the API script, the CSV data is output into the folder called `FoodHygieneData`.
- The **most recently generated** CSV file will be the one used by the analysis code.
- Data analysis can only begin once at least one CSV file of data is inside the folder.
- **JSON files** are also generated storing information on business types and local authorities, but these should **not** be modified or deleted, or this will break the data analysis code.
- Each data analysis module has a dictionary of **function, Boolean pairs**, where the Boolean can be set to True or False to determine which functions to run.

## Disclaimer

Whilst the data, code, methods and reports are to a sensible standard, issues cannot be ruled out. The figures in the reports are based on data as of **12th December 2023**, so the reports may become outdated in the future if trends change. Methods are sensible and controlling of variables is attempted, although may not be perfect. Explanations are sensible, with some level of research performed to ensure reasonable information is provided.

This project is mainly for **real-world data analysis practice**, and is certainly **not an academic project**, hence the lack of sources, so consider doing further research and analysis if taking any insights seriously.

Finally, since data is collected from the https://ratings.food.gov.uk website, all relevant terms and conditions must be followed when handling the data collected by the script: https://www.food.gov.uk/terms-and-conditions

Ultimately, you are free to use the project as you wish, but no legal responsibility will be accepted for errors, omissions and inaccuracies in the code or reports.
