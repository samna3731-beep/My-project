import pandas as pd

class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score

    def check_status(self):
        avg = (self.math_score + self.science_score) / 2
        if avg >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"

df = pd.read_csv("raw_grades.csv")
df = df.fillna(0)

students = []

for _, row in df.iterrows():
    s = Student(row["Student_Name"], row["Math_Score"], row["Science_Score"])
    s.check_status()
    students.append({
        "Student_Name": s.name,
        "Math_Score": s.math_score,
        "Science_Score": s.science_score,
        "Status": s.status
    })

new_df = pd.DataFrame(students)
new_df["School_Year"] = "2023-2024"
new_df.to_csv("final_grades.csv", index=False)