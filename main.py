from mood_db import init_db, add_entry, get_entries
from analyzer import plot_mood, detect_anomalies
from recommender import suggest, predict_next_mood


def main():
    print("🧠 Welcome to the Mood Tracker System")
    init_db()

    while True:
        print("\nOptions:\n1. Add Mood\n2. View Analysis\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                mood = int(input("Enter today's mood (1-10): "))
                if 1 <= mood <= 10:
                    add_entry(mood)
                    print("✅ Mood saved.")
                else:
                    print("❌ Enter a number between 1 and 10.")
            except ValueError:
                print("❌ Invalid input. Please enter a number between 1 and 10.")
        elif choice == '2':
            df = get_entries()
            if df.empty:
                print("No data available.")
            else:
                anomalies = detect_anomalies(df)
                plot_mood(df, anomalies)
                suggest(df, anomalies)
                predict_next_mood(df)

        elif choice == '3':
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
