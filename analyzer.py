import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

def plot_mood(df, anomalies):
    plt.figure(figsize=(10, 5))

    # All moods
    plt.plot(df['date'], df['mood'], marker='o', linestyle='-', color='blue', label='Mood')

    # Anomalies
    if anomalies is not None and not anomalies.empty:
        plt.scatter(anomalies['date'], anomalies['mood'], color='red', s=100, label='Anomaly')

    # Average mood line
    avg = df['mood'].mean()
    plt.axhline(avg, color='green', linestyle='--', label=f'Average ({avg:.1f})')

    plt.title("Mood Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mood (1-10)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def detect_anomalies(df):
    if len(df) < 5:
        return pd.DataFrame(columns=df.columns)
    model = IsolationForest(contamination=0.2, random_state=42)
    df['anomaly'] = model.fit_predict(df[['mood']])
    return df[df['anomaly'] == -1]
