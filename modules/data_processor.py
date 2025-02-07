import pandas as pd

class DataProcessor:
    def load_dummy_data(self) -> pd.DataFrame:
        # Create dummy data for demonstration purposes.
        data = {
            "School Name": [
                "Green High", 
                "Riverdale Prep", 
                "Lakeside Elementary", 
                "Mountainview School"
            ],
            "Latitude": [34.0522, 34.0622, 34.0722, 34.0822],
            "Longitude": [-118.2437, -118.2537, -118.2637, -118.2737],
            "Connectivity": ["Connected", "No Connectivity", "Connected", "No Connectivity"],
            "Region": ["Urban", "Rural", "Urban", "Rural"]
        }
        df = pd.DataFrame(data)
        return df
    
    def filter_by_connectivity_status(self, df: pd.DataFrame, status: str) -> pd.DataFrame:
        # Filter rows where the 'Connectivity' column matches the given status.
        return df[df["Connectivity"] == status]
    
    def generate_dummy_plan(self, df: pd.DataFrame) -> pd.DataFrame:
        # Generate dummy data representing proposed infrastructure sites.
        plan_data = {
            "Proposed Site": ["Site A", "Site B"],
            "Latitude": [34.0550, 34.0750],
            "Longitude": [-118.2450, -118.2650],
            "Estimated Cost": [100000, 120000]
        }
        plan_df = pd.DataFrame(plan_data)
        return plan_df
    
    def generate_dummy_simulation_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # Generate dummy simulation data for scenario analysis.
        simulation_data = {
            "Intervention": ["Current", "Budget Increase 20%"],
            "Number of Schools Covered": [80, 95],
            "Estimated Cost": [500000, 600000]
        }
        simulation_df = pd.DataFrame(simulation_data)
        return simulation_df
    
    def generate_dummy_performance_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # Generate dummy network performance data.
        performance_data = {
            "Region": ["Region X", "Region Y", "Region Z"],
            "Outage Frequency": [5, 2, 3],
            "Average Downtime (hrs)": [2.0, 1.0, 1.5]
        }
        performance_df = pd.DataFrame(performance_data)
        return performance_df 