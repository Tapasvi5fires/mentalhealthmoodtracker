# 🧠 MoodTracker AI  
### **A Lightweight AI‑Style Mental Health Mood Tracking System**  
*Created by Tapasvi Panchagnula*

---

## 📛 Badges  
![Python](https://img.shields.io/badge/Python-3.x-blue)  
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)  
![CLI](https://img.shields.io/badge/Interface-CLI-orange)  
![AI Logic](https://img.shields.io/badge/AI-Rule%20Based-green)  
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🧩 Overview  
**MoodTracker AI** is a simple, fast, and offline mental‑health mood tracker that:  
- Logs your daily mood  
- Stores entries using SQLite  
- Analyzes mood trends over time  
- Generates AI‑style recommendations  
- Runs fully on terminal (no dependencies except Python)

This project demonstrates **AI-like reasoning without real ML**, using *pattern‑based analysis* to create real‑world functionality — a strong point for recruiters evaluating problem‑solving capability.

---

## 🚀 Features  
### ✔ Mood Logging  
- Asks user for their current mood  
- Automatically timestamps the entry  
- Stores data in a SQLite database

### ✔ Trend Analysis  
Analyzes last few days of moods:  
- Checks if moods are improving or declining  
- Detects repeated negative patterns (sad, anxious, stressed)  
- Detects positive streaks (happy, calm, energetic)

### ✔ Smart Recommendations (Rule‑Based AI)  
Based on mood patterns, the system suggests:  
- Relaxation ideas  
- Productivity resets  
- Mental health tips  
- Small actionable tasks  

### ✔ Database Persistence  
All logs saved to `mood_logs.db`, created automatically.

### ✔ Clean Architecture  
Code is divided into **four modules**, following maintainable software‑engineering practice.

---

## 🗂 Project Structure  
```
mentalhealthmoodtracker/
│── main.py            # App entry point (user interaction)
│── mood_db.py         # SQLite DB operations (CRUD)
│── analyzer.py        # Mood trend analyzer
│── recommender.py     # AI-style recommendations
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```

---

## 🛠 Installation  
```bash
git clone https://github.com/Tapasvi5fires/mentalhealthmoodtracker.git
cd mentalhealthmoodtracker
pip install -r requirements.txt
```

---

## ▶️ Run the Application  
```bash
python main.py
```

---

## 🔍 Internal Working (Detailed Explanation)

### **1️⃣ Input Flow (main.py)**  
- Takes user mood input  
- Sends mood to database module  
- Fetches entire mood history  
- Sends mood list to analyzer  
- Displays final recommendation  

**Recruiter Highlight:**  
Shows clear separation of concerns + orchestrator pattern.

---

### **2️⃣ Database Handling (mood_db.py)**  
- Creates table automatically (`mood_logs`)  
- Inserts new mood entries  
- Retrieves full mood history  

Table fields:
| Field | Type | Description |
|-------|------|-------------|
| id | INT | Primary key |
| mood | TEXT | User mood |
| timestamp | TEXT | Auto‑generated time |

**Recruiter Highlight:**  
Clean micro‑ORM style implementation.

---

### **3️⃣ Mood Analytics Engine (analyzer.py)**  
Logic includes:  
- Counting mood frequencies  
- Detecting negative streaks  
- Detecting improvements  
- Detecting fluctuations  

Returns:
```python
{
  'trend': "improving / declining / consistent",
  'most_frequent': "stressed",
  'recent_sequence': ["sad", "sad", "stressed"]
}
```

**Recruiter Highlight:**  
Demonstrates analytical thinking and pseudo‑AI reasoning.

---

### **4️⃣ Recommendation Engine (recommender.py)**  
Uses rule-based mapping like:

- If negative streak → relaxation tips  
- If inconsistent → routine suggestions  
- If positive → reinforcement message  

**Recruiter Highlight:**  
AI-style mapping logic demonstrates problem‑solving & user-oriented design.

---

## 📊 Example Output  
```
Enter your mood: stressed
Saved to database!

Analyzing mood trends...
Trend: You seem to be having repeated stressed moods recently.
Most frequent mood: stressed

Recommendation:
Try a 5-minute breathing exercise or take a short walk.
```

Another example:
```
Enter your mood: happy
Great! It looks like your mood has improved compared to recent days.
Keep doing what makes you happy!
```

---

## 🎯 Why This Project is Recruiter-Friendly  
This project demonstrates:

### ⭐ End‑to‑end application design  
Input → Database → Analysis → AI Recommendation → Output

### ⭐ Understanding of AI logic  
Even without ML, the reasoning pipeline is clear.

### ⭐ Clean modular structure  
Industry-level separation of modules.

### ⭐ Practical real‑world use-case  
Mental health tools are high-impact and relatable.

### ⭐ No heavy dependencies  
Lightweight, readable, and easy to run in interviews.

---

## 🤝 Future Improvements  
- Add sentiment classification using HuggingFace  
- Dashboard using Streamlit  
- Graphs (mood trends) using Matplotlib  
- Mood categories & intensity score  
- Export data as CSV/JSON  
- Mobile-friendly UI using Kivy  

---

## 📜 License  
MIT License

---

## 🧑‍💻 Author  
**Tapasvi Panchagnula**  
Feel free to connect and collaborate!
