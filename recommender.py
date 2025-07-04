def suggest(df, anomalies):
    avg = df['mood'].mean()
    print(f"\n📊 Average mood score: {avg:.2f}")

    if avg < 4:
        print("⚠️ Low average mood detected. It may help to talk to someone you trust or seek professional help.")
    elif avg < 7:
        print("ℹ️ Your mood is moderate. Consider regular self-care to improve your well-being.")
    else:
        print("✅ Your mood is generally positive. Keep up your healthy habits!")

    if anomalies is None or anomalies.empty:
        print("✅ No major anomalies found in mood patterns.")
    else:
        print("\n⚠️ Detected mood anomalies on these dates:")
        print(anomalies[['date', 'mood']].to_string(index=False))

def predict_next_mood(df):
    if len(df) < 3:
        print("\nℹ️ Not enough data to predict the next mood. Add more entries to enable prediction.")
    else:
        next_mood = df['mood'].rolling(window=3).mean().iloc[-1]
        print(f"\n🔮 Predicted next mood (3-day moving average): {next_mood:.2f}")
