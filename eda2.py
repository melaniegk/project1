import dash
from dash import dcc
from dash import html

import plotly.express as px
import pandas as pd
import matplotlib.pylab as pylab
import seaborn as sns
sns.set(palette="pastel")
pylab.rcParams[ 'figure.figsize' ] = 16,9
import warnings
warnings.filterwarnings('ignore')

app = dash.Dash()            
df=pd.read_csv("cleaned_fraud.csv")
height = df['type']
points = df['amount']

fig = px.scatter(x = height,y= points)
graph = dcc.Graph(figure=fig)

fig2 =px.pie(df,df['type'],values=df['isFraud'])
graph2 = dcc.Graph(figure=fig2)

#Fraud rate
# isFraudCount = df['isFraud'].value_counts()
# fig4=px.pie(isFraudCount,names=['non-fraud','fraud'],values=isFraudCount,labels=['non-fraud','fraud'])
# graph4 = dcc.Graph(figure=fig4)

#Fraud rate
fig4='pie1.html'
graph4 = dcc.Graph(figure=fig4)

#isFlagged rate
# isFlaggedFraudCount = df['isFlaggedFraud'].value_counts()
# print(isFlaggedFraudCount)
# fig5=px.pie(isFlaggedFraudCount,names=['not flagged fraud','flagged fraud'],values=isFlaggedFraudCount)
# graph5= dcc.Graph(figure=fig5)

#Type of transactions
# typecount = df['type'].value_counts()
# fig6=px.pie(typecount,names=['PAYMENT','CASH_OUT','CASH_IN ','TRANSFER','DEBIT'],values=typecount,labels=['PAYMENT','CASH_OUT','CASH_IN ','TRANSFER','DEBIT'])
# graph6= dcc.Graph(figure=fig6)

#Type of transactions
fig6='pie2.html'
graph6= dcc.Graph(figure=fig6)

#Count of Fraud and Non-Fraud Transactions in each type of Transaction
# fig7=px.bar(df,x=df['type'],y=df['amount'],color=df['amount'])
# graph7= dcc.Graph(figure=fig7)

#Count of Fraud and Non-Fraud Transactions in each type of Transaction
fig7='bar1.html'
graph7= dcc.Graph(figure=fig7)

data = df.drop(df[(df.type == 'PAYMENT') | (df.type == 'DEBIT') | (df.type == 'CASH_IN')].index)
fraud = data[data["isFraud"] == 1]
valid = data[data["isFraud"] == 0]
groupby_step = fraud.groupby('step').size()
groupby_step.sum()
px.line_polar()
# print(groupby_step)
data1=data[data["isFraud"] == 1]
fig8=px.line(data1,data1['step'],data1['amount'])
graph8=dcc.Graph(figure=fig8)

#Confusion matrix between oldbalanceOrg & newbalanceOrig
data_num = df[['oldbalanceOrg','newbalanceOrig']]
fig9 = px.scatter_matrix(data_num,
                        height=600, 
                        width=600,
                        title= "Correlation between oldbalanceOrg & newbalanceOrig"
                        )
fig9.update_traces(diagonal_visible=False)
graph9 = dcc.Graph(figure=fig9)

#Confusion matrix between oldbalanceDest & newbalanceDest
data_num = df[['oldbalanceDest','newbalanceDest']]
fig10 = px.scatter_matrix(data_num,
                        height=600, 
                        width=600,
                        title= "Correlation between oldbalanceDest & newbalanceDest"
                        )
fig10.update_traces(diagonal_visible=False)
graph10 = dcc.Graph(figure=fig10)

#fraudulent transactions
fig11 = px.box(df, x="isFraud", 
             y="amount", 
             color="type",
             log_y="True",
             title="Concentration of Fraudulent and Non-Fraudulent Amounts")
graph11 = dcc.Graph(figure=fig11)

#Count of fraud and non-fraud transactions by account type


app.layout = html.Div(children=[
html.H1(children='Proportion of Fraud in Transactions'),
    graph4,
#     # graph5,
html.H1(children='Transaction Type'),
    graph6,
html.H1(children='Transactions Amount in Each Type of Transaction'),
    graph7,
html.H1(children='Confusion matrix between oldbalanceOrg & newbalanceOrig'),
    graph9,
html.H1(children='Confusion matrix between oldbalanceDest & newbalanceDest'),
    graph10,
html.H1(children='Fraudulent Transactions'),
    graph11,
html.Div([
    html.H1('Checking Fraudulent Transactions by step'),
    graph8
])
])

if __name__=='__main__':
    app.run_server(debug=True)