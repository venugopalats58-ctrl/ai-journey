
# Store the study hours for 7 days
study_hours = [2, 3.5, 4, 1, 5, 2.5, 3]

# Print each day's study hours
print("Daily Study Hours")

for i, hours in enumerate(study_hours, start=1):
    print(f"Day {i}: {hours} hours")

# Calculate total study hours
total = sum(study_hours)

# Calculate average study hours
average = total / len(study_hours)

# Find the day with the most study hours
max_hours = max(study_hours)
best_day = study_hours.index(max_hours) + 1

# Display results
print("\nTotal study hours:", total)
print("Average study hours:", round(average, 2))
print("Most study hours:", max_hours)
print("Day with most study hours:", best_day)
