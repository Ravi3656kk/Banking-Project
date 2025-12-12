from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define Indian Timezone
tz = pytz.timezone("Asia/Kolkata")

# Schedule per month (start_date, topic, [(start_time, end_time, title)])
schedule = [
    ("2025-07-01", "Month 1: Python, SQL, Excel", [
        ("08:30", "10:30", "Python: Loops, Functions, Lists"),
        ("10:45", "12:15", "SQL: SELECT, JOIN, GROUP BY"),
        ("12:30", "13:30", "Excel: Formulas, Pivot Tables"),
        ("14:30", "16:30", "Python Practice: HackerRank"),
        ("16:45", "18:00", "Mini Project / Concept Review"),
        ("18:00", "19:30", "Revision / Notes / YouTube"),
    ]),
    ("2025-08-01", "Month 2: Pandas, NumPy, Power BI", [
        ("08:30", "10:30", "Pandas: Data Wrangling"),
        ("10:45", "12:15", "NumPy + Dataset Practice"),
        ("12:30", "13:30", "Power BI: Basics & Interface"),
        ("14:30", "16:00", "Power BI: Dashboard Building"),
        ("16:15", "18:00", "Seaborn / Matplotlib Charts"),
        ("18:00", "19:30", "Mini Project / Case Study"),
    ]),
    ("2025-09-01", "Month 3: Machine Learning", [
        ("08:30", "10:30", "ML Theory: Linear, Logistic, KNN"),
        ("10:45", "12:45", "EDA + Feature Engineering"),
        ("13:45", "15:30", "Scikit-learn: Model Building"),
        ("15:45", "17:30", "Evaluation Metrics"),
        ("17:30", "19:30", "ML Project + Revision"),
    ]),
    ("2025-10-01", "Month 4: Deep Learning & NLP", [
        ("08:30", "10:30", "Neural Nets + TensorFlow/Keras"),
        ("10:45", "12:45", "CNN + OpenCV"),
        ("13:45", "15:30", "NLP + spaCy"),
        ("15:45", "17:30", "Transformers + Hugging Face"),
        ("17:30", "19:30", "AI Project Work"),
    ]),
    ("2025-11-01", "Month 5: Deployment & DevOps", [
        ("08:30", "10:30", "Flask / FastAPI APIs"),
        ("10:45", "12:45", "Docker + Deployment"),
        ("13:45", "15:30", "GitHub + CI/CD"),
        ("15:45", "17:30", "Deploy on Heroku / AWS"),
        ("17:30", "19:30", "Logging + Testing"),
    ]),
    ("2025-12-01", "Month 6: Capstone & Interview", [
        ("08:30", "10:30", "Capstone Project Work"),
        ("10:45", "12:45", "Resume + GitHub Portfolio"),
        ("13:45", "15:30", "Interview Prep: Python/SQL/ML"),
        ("15:45", "17:30", "Mock Interviews + LinkedIn"),
        ("17:30", "19:30", "Final Demo + Docs"),
    ]),
]

cal = Calendar()

# Add weekly study schedule (Mon–Sat) and Sunday review
for start_str, month_name, sessions in schedule:
    start_date = datetime.strptime(start_str, "%Y-%m-%d")
    year = start_date.year
    month = start_date.month
    num_days = Calendar.monthrange(year, month)[1]

    for day_offset in range(num_days):  # 0=Mon to 6=Sun
            day = start_date + timedelta(days=day_offset)

            # If Sunday (day_offset == 6), add Weekly Review only
            if day.weekday() == 6:
                review_start = tz.localize(datetime.strptime(f"{day.date()} 10:00", "%Y-%m-%d %H:%M"))
                review_end = tz.localize(datetime.strptime(f"{day.date()} 12:00", "%Y-%m-%d %H:%M"))
                review_event = Event()
                review_event.name = "[Review] Weekly + Notes Revision + Rest"
                review_event.begin = review_start
                review_event.end = review_end
                cal.events.add(review_event)
            else:
                # Mon–Sat regular schedule
                for start_time, end_time, title in sessions:
                    start_dt = tz.localize(datetime.strptime(f"{day.date()} {start_time}", "%Y-%m-%d %H:%M"))
                    end_dt = tz.localize(datetime.strptime(f"{day.date()} {end_time}", "%Y-%m-%d %H:%M"))
                    event = Event()
                    event.name = title
                    event.begin = start_dt
                    event.end = end_dt
                    cal.events.add(event)

# Write to .ics file
with open("StudySchedule.ics", "w", encoding="utf-8") as f:
    f.writelines(cal)

print("✅ Calendar generated with Sunday review: StudySchedule.ics")
