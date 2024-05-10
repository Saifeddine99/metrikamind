import plotly.graph_objects as go
from datetime import datetime
import streamlit as st

def time_series_plot(dates, test_results):

    # Create a Plotly figure
    fig = go.Figure()

    # Add a scatter plot for the time series
    fig.add_trace(go.Scatter(x=dates, y=test_results, mode='lines+markers', name= "Scores Evolution"))

    # Update layout for better readability
    plot_title= "Scores Evolution Time Series"
    fig.update_layout(title= plot_title,
                    xaxis_title='Date', 
                    yaxis_title= "Scores",
                    hovermode='x unified')

    # Show the plot
    st.plotly_chart(fig, use_container_width=True)      