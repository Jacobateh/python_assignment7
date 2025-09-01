"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
	if student_id not in attendance:
		attendance[student_id] = {
			"name": name,
			"present_days": [],
			"absent_days" : []
		}
	else:
		print(f"Student{student_id} already exist")
register_student("101", "Jay")
register_student("102", "Ruth")
    pass

def mark_present(student_ids):
    """Mark multiple students as present for today."""
	today = str(datetime.date.today())
    # implement logic
	for sid in student_ids:
		if sid in attendance:
			if today not attendance[sid]["present_days"]:
				attendance[sid]["present_days"].append(today)
		else:
			print(f"Student {sid} not registered")

    pass

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
	for sid in student_ids:
		if sid in attendance:
			if today not in attendance[sid]["absent_days"]:
			if today in attendance[sid]["present_days"].remove(today)
		else:
			print(f"Student {sid} not registered")
    #implement logic
    pass

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
	today = str(datetime.date.today())
	report = {}
	for sid, record in attendance.items():
		present_today = today in record["present_todays"]
		absent_today = today in record["absent_days"]
		if kwargs.get("only_present") and not present_today:
		continue
		if kwargs.get("only_absent") and not absent_today:		
		continue
		report[sid] = record
	return report
    # implement logic


    return report
print("Full Report:", get_report())
print("Present Only:", get_report(only_present=True))
print("Absent Only:", get_report(only_absent=True))

