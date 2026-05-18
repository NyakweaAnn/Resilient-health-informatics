import pandas as pd
import numpy as np

# 1. Simulate 8 weeks of historical surveillance data for a single health post
# Notice the massive spike in Week 8 (potential Cholera outbreak)
data = {
    "epi_week": [1, 2, 3, 4, 5, 6, 7, 8],
    "acute_watery_diarrhea_cases": [12, 14, 11, 15, 13, 14, 16, 45] 
}

df = pd.DataFrame(data)

def run_surveillance_pipeline(dataframe):
    # 2. Calculate a 4-week rolling mean (baseline) and standard deviation
    # shift(1) ensures we are only looking at past history to evaluate the current week
    dataframe['baseline_mean'] = dataframe['acute_watery_diarrhea_cases'].shift(1).rolling(window=4).mean()
    dataframe['baseline_std'] = dataframe['acute_watery_diarrhea_cases'].shift(1).rolling(window=4).std()
    
    # 3. Define the threshold: Mean + 2 Standard Deviations
    dataframe['alert_threshold'] = dataframe['baseline_mean'] + (2 * dataframe['baseline_std'])
    
    # 4. Evaluate trigger condition (Flag as 1 if true, 0 if false)
    dataframe['alert_triggered'] = np.where(
        (dataframe['acute_watery_diarrhea_cases'] > dataframe['alert_threshold']) & (dataframe['baseline_mean'].notna()), 
        1, 
        0
    )
    
    return dataframe

# Run the automated pipeline
monitored_df = run_surveillance_pipeline(df)

print("--- Automated Epidemiological Surveillance Dashboard ---")
print(monitored_df[['epi_week', 'acute_watery_diarrhea_cases', 'baseline_mean', 'alert_threshold', 'alert_triggered']])

# 5. Trigger System Alert System Call
if monitored_df['alert_triggered'].iloc[-1] == 1:
    print("\n🚨 ALERT: Outbreak anomaly detected in the current Epidemiological Week! Dispatching Rapid Response Team protocols.")
