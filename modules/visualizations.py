import streamlit as st
import altair as alt
import pandas as pd

class Visualizer:
    def show_map(self, df: pd.DataFrame):
        # Check for the existence of the required latitude and longitude columns.
        if "Latitude" in df.columns and "Longitude" in df.columns:
            # Rename columns to match Streamlit's expected names.
            map_data = df.rename(columns={"Latitude": "lat", "Longitude": "lon"})
            # Only pass the necessary columns to the st.map
            st.map(map_data[['lat', 'lon']])
        else:
            st.write("Map visualization not available. Data is missing latitude/longitude information.")

    def show_simulation_graph(self, df: pd.DataFrame):
        # Create an Altair bar chart for simulation data.
        if not df.empty and "Intervention" in df.columns and "Number of Schools Covered" in df.columns:
            chart = alt.Chart(df).mark_bar().encode(
                x='Intervention',
                y='Number of Schools Covered',
                tooltip=['Intervention', 'Number of Schools Covered', 'Estimated Cost']
            ).properties(width=600, height=400)
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write("Simulation graph data is not available or incomplete.")

    def show_performance_table(self, df: pd.DataFrame):
        st.dataframe(df) 
        