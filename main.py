import panel as pn
import hvplot.pandas
import pandas as pd

# Load the datasets
train_df = pd.read_csv('train.csv')

# Interactive table for train dataset
train_table = train_df.hvplot.table(columns=['id', 'keyword', 'location', 'text', 'target'], 
                                    sortable=True, selectable=True, width=700)

layout = pn.Column(train_table)
layout.servable()
