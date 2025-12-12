import pandas as pd

# Weekly structure
weekly_schedule = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Focus": [
        "Grammar + Self-Intro",
        "Business Vocab + STAR Answer",
        "Email Writing + Teamwork",
        "Technical English + Project Talk",
        "Resume Language + Strengths",
        "Mock Interview + Business Writing",
        "Review + Culture Immersion"
    ],
    "Tasks": [
        "Present Perfect vs Simple Past + Speak: Tell me about yourself + Listen: TED/Rachel’s English",
        "Learn 15 biz/tech words + Speak STAR: Problem solving + Watch: STAR answers on YouTube",
        "Write follow-up email + Speak: Teamwork example + Watch: The Office clips",
        "Conditionals grammar + Explain a project + Watch tech mock interview",
        "Action verbs + Speak: Strengths & Weaknesses + VOA Podcast (Tech/Business)",
        "Answer 5–6 real interview Qs + Write LinkedIn bio or intro",
        "Review vocab, grammar, writing + Watch U.S. TV show (Shark Tank, Friends)"
    ]
}

# Generate full 16-week schedule
schedule_data = []
for week in range(1, 17):  # 16 weeks
    for i in range(7):  # 7 days per week
        day = weekly_schedule["Day"][i]
        focus = weekly_schedule["Focus"][i]
        tasks = weekly_schedule["Tasks"][i]
        schedule_data.append({
            "Week": f"Week {week}",
            "Day": day,
            "Focus": focus,
            "Daily Tasks": tasks
        })

# Convert to DataFrame
df = pd.DataFrame(schedule_data)

# Save to Excel file
file_name = "4_Month_English_Interview_Schedule.xlsx"
df.to_excel(file_name, index=False)

print(f"✅ Schedule saved as: {file_name}")
