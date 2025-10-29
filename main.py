import pandas as pd
import datetime
import os
import matplotlib.pyplot as plt

moods = {
    "1": ("😄", "Happy"),
    "2": ("😐", "Neutral"),
    "3": ("😔", "Sad"),
    "4": ("😡", "Angry"),
    "5": ("😌", "Relaxed")
}

def log_mood():
    print("Πώς νιώθεις σήμερα;\n")
    for key, (emoji, mood) in moods.items():
        print(f"{key}. {emoji} {mood}")
    
    choice = input("\nΔιάλεξε (1-5): ")
    if choice not in moods:
        print("Μη έγκυρη επιλογή.")
        return

    emoji, mood = moods[choice]
    date = datetime.date.today()

    entry = {"Date": date, "Mood": mood, "Emoji": emoji}
    file_exists = os.path.isfile("mood_data.csv")
    df = pd.DataFrame([entry])
    df.to_csv("mood_data.csv", mode="a", header=not file_exists, index=False)

    print(f"\n✅ Καταγράφηκε: {emoji} {mood} ({date})")

def plot_moods():
    if not os.path.isfile("mood_data.csv"):
        print("⚠️ Δεν υπάρχουν καταγραφές ακόμα.")
        return

    df = pd.read_csv("mood_data.csv")
    mood_counts = df["Mood"].value_counts().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    mood_counts.plot(kind="bar", color="skyblue")
    plt.title("Mood Tracker Summary")
    plt.xlabel("Mood")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("mood_plot.png")
    plt.show()

if __name__ == "__main__":
    print("\n🎯 MOOD TRACKER")
    print("1. Καταγραφή διάθεσης")
    print("2. Προβολή στατιστικών")

    option = input("Διάλεξε (1/2): ")

    if option == "1":
        log_mood()
    elif option == "2":
        plot_moods()
    else:
        print("Μη έγκυρη επιλογή.")