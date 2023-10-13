import panel as pn
import hvplot.pandas
import pandas as pd

# Load the datasets
train_df = pd.read_csv('train.csv')

# Interactive table for train dataset
train_table = train_df.hvplot.table(columns=['id', 'keyword', 'location', 'text', 'target'], 
                                    sortable=True, selectable=True, width=700)

layout = pn.Column(train_table)

location_distribution = train_df['location'].value_counts().nlargest(20).hvplot.bar(title='Top 20 Locations', height=300, width=600)
keyword_distribution = train_df['keyword'].value_counts().nlargest(20).hvplot.bar(title='Top 20 Keywords', height=300, width=600)

# Panel layout
exploration_panel = pn.Row(train_table, location_distribution, keyword_distribution)

exploration_panel.servable()
