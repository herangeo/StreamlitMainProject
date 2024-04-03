import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')


st.sidebar.header('Dashboard')


def display_chart(data, chart_type, x_column, y_column):
    if chart_type == 'Bar':
        st.markdown('### Bar chart')
        fig = px.bar(data, x=x_column, y=y_column, title=f'{y_column} vs {x_column}')
    elif chart_type == 'Scatter':
        st.markdown('### Scatter plot')
        fig = px.scatter(data, x=x_column, y=y_column, title=f'{y_column} vs {x_column}')
    elif chart_type == 'Pie':
        st.markdown('### Pie chart')
        fig = px.pie(data, values=y_column, names=x_column, title=f'{y_column} distribution by {x_column}')
    st.plotly_chart(fig, use_container_width=True)


uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    columns = list(data.columns)
    columns.insert(0, None) 
    

    chart_type = st.sidebar.selectbox('Select chart type', options=['Bar', 'Scatter', 'Pie'])
    x_column = st.sidebar.selectbox('Select x-axis column', options=columns)
    if x_column is not None:
        columns.remove(None) 
        y_column = st.sidebar.selectbox('Select y-axis column', options=columns)
        if y_column is not None:
            display_chart(data, chart_type, x_column, y_column)
