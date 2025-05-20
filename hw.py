# Student Report Card Generator with Personality

# Input collection and cleaning
full_name = input("Enter the student's full name: ").strip().title()
class_grade = input("Enter the class/grade: ").strip().capitalize()

# Collect subjects and marks
subjects = []
marks = []

for i in range(1, 4):
    subject = input(f"Enter subject {i}: ").strip().title()
    score = int(input(f"Enter marks for {subject} (0–100): ").strip())
    subjects.append(subject)
    marks.append(score)

teacher_comment = input("Enter a comment from the teacher: ").strip()

# Generate Student ID using initials
names = full_name.split()
initials = '.'.join([name[0].upper() for name in names])
student_id = f"{initials}_{class_grade.replace(' ', '')}"

# Calculate average
average = sum(marks) / len(marks)

# Determine performance remark
if average >= 80:
    remark = "Outstanding performance!"
elif 60 <= average < 80:
    remark = "Keep it up, but work harder."
else:
    remark = "Needs improvement."

# Report card formatting
print("\n" + "=" * 40)
print("         STUDENT REPORT CARD")
print("=" * 40)
print(f"\nName      : {full_name}")
print(f"Student ID: {student_id}")
print(f"Class     : {class_grade}\n")

print("Subjects and Scores:")
for subject, score in zip(subjects, marks):
    print(f"- {subject.ljust(15)}: {score}")

print(f"\nAverage Score: {average:.1f}\n")

print("Teacher's Comment:")
print(f"\"{teacher_comment}\"\n")

print("Performance Remark:")
print(remark)

print("=" * 40)