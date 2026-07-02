import pandas as pd

# Load dataset
df = pd.read_excel("AI_Career_Navigator_Dataset.xlsx")

print("========== DATASET OVERVIEW ==========\n")

print("Total Jobs:", len(df))
print("Total Companies:", df["Company"].nunique())
print("Total Cities:", df["City"].nunique())

print("\nAverage Salary (LPA):", round(df["Salary_LPA"].mean(), 2))

print("\nHighest Salary:")
print(df["Salary_LPA"].max())

print("\nLowest Salary:")
print(df["Salary_LPA"].min())

print("\nMost Hiring Companies")
print(df["Company"].value_counts().head(10))

print("\nTop Hiring Cities")
print(df["City"].value_counts())

print("\nWork Mode")
print(df["Work_Mode"].value_counts())

print("\nExperience Levels")
print(df["Experience"].value_counts())
print(df.describe())

print("\nTop 10 Most Demanded Skills")

skills = df["Skills"].str.split(", ").explode()

print(skills.value_counts().head(10))

import matplotlib.pyplot as plt

# Split the skills column into individual skills
skills = df["Skills"].str.split(", ").explode()

# Count each skill
top_skills = skills.value_counts().head(10)

# Create bar chart
plt.figure(figsize=(10,6))
top_skills.plot(kind="bar")

plt.title("Top 10 Most Demanded Skills")
plt.xlabel("Skills")
plt.ylabel("Number of Job Postings")

plt.tight_layout()
plt.show()

city_jobs = df["City"].value_counts()

plt.figure(figsize=(10,6))
city_jobs.plot(kind="bar")

plt.title("Jobs Available by City")
plt.xlabel("City")
plt.ylabel("Number of Jobs")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n========== INSIGHTS ==========")

print(f"📍 The city with the highest job openings is {city_jobs.idxmax()} with {city_jobs.max()} jobs.")

print(f"📍 The city with the lowest job openings is {city_jobs.idxmin()} with {city_jobs.min()} jobs.")

print("📍 This analysis helps identify cities with higher demand for Data Analyst roles.")

company_jobs = df["Company"].value_counts().head(10)

plt.figure(figsize=(10,6))
company_jobs.plot(kind="bar")

plt.title("Top 10 Hiring Companies")
plt.xlabel("Company")
plt.ylabel("Number of Jobs")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n========== COMPANY INSIGHTS ==========")

print(f"🏢 The highest hiring company is {company_jobs.idxmax()} with {company_jobs.max()} job postings.")

print("🏢 These companies have the highest recruitment activity in the dataset.")

plt.figure(figsize=(10,6))

df["Salary_LPA"].plot(kind="hist", bins=10)

plt.title("Salary Distribution")
plt.xlabel("Salary (LPA)")
plt.ylabel("Number of Jobs")

plt.tight_layout()
plt.show()

print("\n========== SALARY INSIGHTS ==========")

print(f"💰 Average Salary: {round(df['Salary_LPA'].mean(),2)} LPA")
print(f"💰 Highest Salary: {df['Salary_LPA'].max()} LPA")
print(f"💰 Lowest Salary: {df['Salary_LPA'].min()} LPA")

work_mode = df["Work_Mode"].value_counts()

plt.figure(figsize=(6,6))

work_mode.plot(kind="pie", autopct="%1.1f%%")

plt.title("Work Mode Distribution")

plt.ylabel("")

plt.show()

print("\n========== WORK MODE INSIGHTS ==========")

print(work_mode)

salary_exp = df.groupby("Experience")["Salary_LPA"].mean()

plt.figure(figsize=(8,5))

salary_exp.plot(kind="bar")

plt.title("Average Salary by Experience")

plt.xlabel("Experience")

plt.ylabel("Average Salary (LPA)")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()
print("\n========== EXPERIENCE INSIGHTS ==========")

print(salary_exp)