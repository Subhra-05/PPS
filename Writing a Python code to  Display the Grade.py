# Input marks for 5 subjects
marks = []
for i in range(5):
    subject_marks = float(input(f"subject {i + 1}: "))
    marks.append(subject_marks)

# Calculate average marks
average_marks = sum(marks) / len(marks)

# Display average marks
print(f"Average Marks: {average_marks:.2f}")
if 90 <= average_marks <= 100:
	grade = "A"
elif 80 <= average_marks <=89:
	grade = "B"
elif 70 <= average_marks <=79:
	grade = "C"
elif 60 <= average_marks <=69:
	grade = "D"
else:
	grade = "F"
print(f"Grade: {grade}")
