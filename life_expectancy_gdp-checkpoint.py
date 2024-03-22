#!/usr/bin/env python
# coding: utf-8

# PROJECT SCOPING
# 
# 1. Project Objectives:
#    - To etermine the relationship between GDP and life expectancy across different countries.
#    - Identify factors influencing this relationship.
#    - Build predictive models to forecast life expectancy based on GDP and other relevant features.
# 
# 2. Data Collection:
#    - The data for this project is from WHO and World Bank on GDP and life expectancy
#    - Collect additional variables like healthcare expenditure, education levels, access to clean water, sanitation, etc., which may influence life expectancy.
#    
# 3. Data Cleaning and Preparation:
#    - Handle missing values, outliers, and inconsistencies in the data.
#    - Standardize the data formats and units if necessary.
#    - Merge datasets based on common identifiers like country names or codes.
# 
# 4. Exploratory Data Analysis (EDA):
#    - Visualize the distributions of GDP and life expectancy.
#    - Explore correlations between GDP, life expectancy, and other variables.
#    - Identify any interesting patterns or outliers in the data.
#    - Has life expectancy increased over time in the six nations?
#    - Has GDP increased over time in the six nations?
#    - Is there a correlation between GDP and life expectancy of a country?
#    - What is the average life expectancy in these nations?
#    - What is the distribution of that life expectancy?
# 
# 5. Feature Engineering:
#    - Create new features if needed, such as GDP per capita.
#    - Consider transforming variables or encoding categorical features.
# 
# 6. Statistical Analysis:
#    - Conduct statistical tests to quantify the relationship between GDP and life expectancy.
#    - Use techniques like regression analysis to model this relationship and assess its significance.
# 
# 7. Machine Learning Models:
#    - Develop predictive models to forecast life expectancy based on GDP and other relevant features.
#    - Evaluate various algorithms such as linear regression, decision trees, random forests, or gradient boosting.
#    - Use techniques like cross-validation to assess model performance and prevent overfitting.
#    
# 8. Interpretation and Insights:
#    - Interpret the results of the analysis and models.
#    - Identify key factors influencing life expectancy beyond GDP.
#    - Provide actionable insights for policymakers or healthcare professionals.
# 
# 9. Visualization and Reporting:
#    - Create visualizations (e.g., scatter plots, heatmaps, etc.) to communicate findings effectively.
#    - Prepare a comprehensive report summarizing the project methodology, findings, and recommendations.
#    - Present results in a clear and understandable manner for stakeholders.
# 
#  Tools and Technologies:
#    - Programming Languages: Python
#    - Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
#    - Data Visualization: Tableau
# 
# 

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


gdp_data = pd.read_csv('all_data.csv')
print(gdp_data.head())


# In[32]:


#Data Cleaning and Preparation 
#numerical summarization
print(gdp_data.describe(include= 'all'))

#check for missing values
print(gdp_data.info())
#there are no missing values

#renaming an individual coulumn 'Life Expectancy at birth (years)'
gdp_data.columns =['country','year', 'life_expectancy','gdp']
print(gdp_data.columns)

#standardize data formats
...

# #Split datasets based on common identifiers like country names
# unique_countries = gdp_data['country'].unique()

# # Create an empty dictionary to store DataFrames for each country
# country_dfs = {}

# # Split the merged DataFrame into separate DataFrames based on country name
# for country in unique_countries:
#     country_dfs[country] = gdp_data[gdp_data['country'] == country]

# print(country_dfs)

#there are 6 countries in this data set with info on life expectancy and GDP spanning a 15 year period(2000-2015)


# In[46]:


# Exploratory Data Analysis (EDA):
# Visualize the distributions of GDP and life expectancy (two quantitative varibles)
#distributions of GDP for each country (create a for loop and how to create axes on either side of a graph to accommodate the different ranges)
plt.subplot(2,3,1)
plt.plot('year','life_expectancy',data= gdp_data[gdp_data.country=='Chile'], color = 'green')
plt.plot('year','gdp',data= gdp_data[gdp_data.country=='Chile'], color = 'red')
plt.title('Chile')
#
plt.subplot(2,3,2)
plt.plot('year','life_expectancy',data= gdp_data[gdp_data.country=='China'], color = 'green')
plt.plot('year','gdp',data= gdp_data[gdp_data.country=='China'], color = 'red')
plt.title('China')
# plt.plot('year','life_expectancy',hue= gdp,data= gdp_data[gdp_data.country=='Germany'], color = 'blue')
# plt.plot('year','life_expectancy',data= gdp_data[gdp_data.country=='Mexico'], color = 'orange')
# plt.plot('year','life_expectancy',data= gdp_data[gdp_data.country=='United States of America'], color = 'pink')
# plt.plot('year','life_expectancy',data= gdp_data[gdp_data.country=='Zimbabwe'], color = 'black')

# plt.axis([2000, 2015, 4.000000e+09, 2.000000e+13])
# plt.xlabel('Year')
# plt.ylabel('Gross Domestic Product')
plt.show()

#comparing the 6 countries



# In[43]:


#    - Explore correlations between GDP, life expectancy, and other variables.
#    - Identify any interesting patterns or outliers in the data.
#    - Has life expectancy increased over time in the six nations?
#    - Has GDP increased over time in the six nations?
#    - Is there a correlation between GDP and life expectancy of a country?
#    - What is the average life expectancy in these nations?
#    - What is the distribution of that life expectancy?


# In[44]:


# Select 6 countries for visualization
countries = ['Chile','China','Germany','Mexico','United States of America','Zimbabwe']

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

# Flatten the axes for easy iteration
axes = axes.flatten()

# Plot GDP and life expectancy for each country
for i, country in enumerate(countries):
    # Filter data for the current country
    country_data = gdp_data[gdp_data['country'] == country]
    
    # Plot GDP
    axes[i].plot(country_data['year'], country_data['gdp'], label='GDP')
    axes[i].set_title(country)
    axes[i].set_xlabel('Year')
    axes[i].set_ylabel('GDP')
    
    # Create a twin Axes for life expectancy
    ax2 = axes[i].twinx()
    
    # Plot life expectancy
    ax2.plot(country_data['year'], country_data['life_expectancy'], color='red', label='Life Expectancy')
    ax2.set_ylabel('Life Expectancy')
    
    # Display legend for both axes
    axes[i].legend(loc='upper left')
    ax2.legend(loc='upper right')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()


# In[ ]:




