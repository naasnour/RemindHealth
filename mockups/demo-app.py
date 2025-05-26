# remindhealth_demo.py

def generate_reminder(patient_name, doctor_name, date_time, clinic_name):
    return f"Hello {patient_name}, this is a reminder from {clinic_name}. You have a follow-up with Dr. {doctor_name} on {date_time}. Thank you, and we look forward to seeing you soon!"

# User input
print("📲 Welcome to RemindHealth Prototype")
name = input("Enter patient name: ")
doctor = input("Enter doctor name: ")
appt = input("Enter appointment date/time: ")
clinic = input("Enter clinic name: ")

# Generate message
message = generate_reminder(name, doctor, appt, clinic)
print("\n✅ Message Preview:\n")
print(message)
