import streamlit as st
from modules.ai_agent import AIAgent
from modules.data_processor import DataProcessor
from modules.visualizations import Visualizer

def main():
    # Configure the Streamlit page
    st.set_page_config(
        page_title="AI-Driven Network Optimization for School Connectivity",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("AI-Driven Network Optimization for School Connectivity")
    st.markdown("**Optimizing school connectivity using AI and geospatial analysis.**")
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose Mode", [
        "Connectivity Gaps",
        "Network Planning",
        "Scenario Simulation",
        "Network Performance"
    ])
    
    # Initialize modules
    agent = AIAgent()
    data_processor = DataProcessor()
    visualizer = Visualizer()
    
    # Load dummy data (replace with real data source as needed)
    df = data_processor.load_dummy_data()
    
    if app_mode == "Connectivity Gaps":
        st.header("Identify Connectivity Gaps")
        st.markdown("Analyze geospatial data to identify schools lacking connectivity.")
        query = st.text_input("Enter your query", "Show me schools in rural Kenya with no internet access.")
        if st.button("Analyze Connectivity Gaps"):
            # Run LLM analysis
            response = agent.analyze_connectivity(query)
            st.subheader("LLM Analysis Response")
            st.write(response)
            st.subheader("Visualizing Connectivity Gaps on Map")
            df_gap = data_processor.filter_by_connectivity_status(df, "No Connectivity")
            visualizer.show_map(df_gap)
            
    elif app_mode == "Network Planning":
        st.header("Optimize Network Planning")
        st.markdown("Generate recommendations for new infrastructure placement.")
        query = st.text_input("Enter your query", "Where should we build new cell towers to maximize coverage for schools in Uganda?")
        if st.button("Generate Network Plan"):
            response = agent.generate_infrastructure_plan(query)
            st.subheader("LLM Recommendation")
            st.write(response)
            st.subheader("Proposed Infrastructure Locations")
            plan_df = data_processor.generate_dummy_plan(df)
            visualizer.show_map(plan_df)
            st.table(plan_df)
            
    elif app_mode == "Scenario Simulation":
        st.header("Scenario Simulation")
        st.markdown("Simulate the impact of different network interventions.")
        query = st.text_input("Enter your simulation query", "What happens if we increase the budget for satellite internet by 20%?")
        if st.button("Simulate Scenario"):
            response = agent.simulate_scenario(query)
            st.subheader("Scenario Analysis")
            st.write(response)
            simulation_df = data_processor.generate_dummy_simulation_data(df)
            visualizer.show_simulation_graph(simulation_df)
            st.table(simulation_df)
            
    elif app_mode == "Network Performance":
        st.header("Monitor and Maintain Networks")
        st.markdown("Monitor real-time network performance and detect issues.")
        query = st.text_input("Enter your query", "Show me areas with frequent network outages in Nigeria.")
        if st.button("Monitor Network"):
            response = agent.monitor_network(query)
            st.subheader("Network Performance Analysis")
            st.write(response)
            performance_df = data_processor.generate_dummy_performance_data(df)
            visualizer.show_performance_table(performance_df)
    
if __name__ == "__main__":
    main() 