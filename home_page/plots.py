import plotly.graph_objects as go
from datetime import datetime
import streamlit as st

def time_series_plot(all_responses_with_titles):

    for title, value in all_responses_with_titles.items():

        dates = value["dates"]
        test_results = value["scores"]
        # Create a Plotly figure
        fig = go.Figure()

        # Add a scatter plot for the time series
        fig.add_trace(go.Scatter(x=dates, y=test_results, mode='lines+markers', name= "Scores Evolution"))

        # Update layout for better readability
        plot_title= f"Scores Evolution Time Series For {title}"
        fig.update_layout(title= plot_title,
                        xaxis_title='Date',
                        yaxis_title= "Scores",
                        hovermode='x unified')

        # Show the plot
        st.plotly_chart(fig, use_container_width=True)      