"""
Collect Patient information from user input
"""
from patient import Patient

required_vitals = [
    "blood_pressure",
    "bmi",
    "weight",
    "height",
    "temperature",
    "pulse",
    "respiration",
    "oxygen_saturation"
]

patient = Patient()
#---------------------
# Patient Demographics
#---------------------
name = input("Enter the patient name: ")
patient.name = name

age = int(input("Enter the patient's age: "))
patient.age = age

#---------------
# Patient Vitals
#---------------

vitals = {}

print("\nEnter patient vitals")
for vital in required_vitals:
    if vital == "blood_pressure":
        blood_pressure = input(
            "Blood pressure (e.g 114/63): "
        )

        systolic, diastolic = blood_pressure.split("/")
        vitals[vital] = (
            int(systolic),
            int(diastolic)
        )
    else:

        value = input(
            f"{vital.replace('_', ' '.title())}: "
        )
        vitals[vital] = value
patient.vitals = vitals

#----------
# Symptoms
# ---------
has_symptoms = input(
    "\nIs the patient experiencing symptoms? Y/N: "
).lower()

if has_symptoms == "y":

    while True:

        symptom = input(
            "Enter symptom or type done: "
        )

        if symptom.lower() == "done":
            break

        patient.symptoms = set()
        patient.symptoms.add(symptom)
#-------------
# Medications 
#-------------

total = int(
    input("\nHow many medications does the patient take? ")
)
patient.medications = []
for i in range(total):
    medication = input(
        f"Medication {i + 1}: "
    )

    patient.medications.append(medication)

#----------
# Allergies
#----------
has_allergies = input(
    "\nDoes the patient have any allergies? Y/N: "
).lower()

if has_allergies == "y":

    while True:

        allergy = input(
            "Enter allergy or type done: "
        )

        if allergy.lower() == "done":
            break

        patient.allergies = set()
        patient.allergies.add(allergy)


#-----------------
# Display patient
#-----------------
print("\nPatient Record")
print(patient)