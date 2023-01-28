# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:44:55 2023

@author: Home PC
"""

import pandas as pd
import streamlit as st
import matplotlib as plt
file = "C:\\Users\\Home PC\\Downloads\\class 2\\Billionaire.csv"
df = pd.read_csv('Billionaire.csv')
df['NetWorth'] = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))

#st.header('Billionaire Dataset')




all_countries = sorted(df['Country'].unique())

col1, col2 = st.columns(2)

#column 1
#display on streamlit
selected_country = col1.selectbox('Select Your Country', all_countries)
#subset on selected country
subset_country = df[df['Country'] == selected_country]

#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())

#display multi select option on source
selected_source = col1.multiselect('Select Source of income', sources)

#subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]

main_string = '{} - Billionaire'.format(selected_country)
col2.header(main_string)
col2.table(subset_country)
col2.header('Source wise Info')
col2.table(subset_source)

#selection = st.selectbox('Select Country', all_countries)
#subset = df[df['Country'] == selection]
#st.dataframe(subset)
#st.table(subset)

# find count of billionaire by countries
#bill= df.groupby('Country')['Name'].count().sort_values(ascending= False).head(10)


#st.bar_chart(bill)

# find the most popular source of income

#df.groupby('Source')['Name'].count().sort_values(ascending=False).head(1)
# Get the cumulative wealth of billionaire belonging to US

#import pandas as pd

# Assuming your data is in a DataFrame called 'billionaires'
#df['NetWorth'] = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))
#us_billionaires = df[df['Country'] == 'United States']
#us_cumulative_wealth = us_billionaires['NetWorth'].cumsum()
#print("Cumulative wealth of billionaires belonging to US: ", us_cumulative_wealth)


