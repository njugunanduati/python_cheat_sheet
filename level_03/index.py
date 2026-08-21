"""
LEVEL 3 - Data Types
"""
# Built-in Types
# int - Integer (Whole numbers without decimals)
patient_age = 72
heart_rate = 80
number_of_patients = 25

print(type(patient_age))

patients_today = 15
patients_yesterday = 12
total = patients_today + patients_yesterday
print(total)

# float - Numbers containing decimals
temperature = 98.6
weight = 75.5
blood_glucose = 105.7
print(type(temperature))

# complex numbers: Contains a real and imaginary component
numbers = 3 + 4j
print(numbers.real)
print(numbers.imag)

# bool - Boolean -  Only two possible values
True
False

# Example
has_fever = True
has_allergy = False

if has_fever:
    print("Check patient's temperature" )

temperature = 101.2
has_fever = temperature > 100.4
print(has_fever)

# str - String - Represents text
patient_name = "Mary Johnson"
diagnosis = "Hypertension"
medication = "Lisinoplril"

# Strings have many useful methods

diagnosis = "hypertension"
print(diagnosis.upper())
print(diagnosis.capitalize())
# string slicing
print(diagnosis[:5])
print(diagnosis[5:])
print(diagnosis[-1])

# lists - List - An ordered and mutable collection
medications = [
    "Metformin",
    "Lisinopril",
    "Asprin"
]
# Access elements
print(medications[0])
#  Modify the list
medications.append("Ibuprofen")

# tuple = Tuple - Similar to a list, but genaraly used for data that should not change.
blood_pressure = (120, 80)
# you can unpack it
systolic, diastolic = blood_pressure
print(systolic)
print(diastolic)

# NB: tuples are immutable and blood_pressure[0] = 130 will produce an error

# set - Set - A collection of unique elements
symptoms = {
    "fever",
    "cough",
    "headache"
}
print(symptoms)
# Duplicates automatically disappear 
symptoms = {
    "fever",
    "cough",
    "fever",
    "headache"
}
print(symptoms)

if "fever" in symptoms:
    print("Patient has fever")


# frozenset -- Immutable Set
required_fields = frozenset({
    "name",
    "dob",
    "medications"
})
# frozensets are immutable

# dict - Dictionary - One of the most important python data structures
# especially for APIs, JSON-like data, ML pipelines and backend development.
# It stores in key-value pairs.
patient = {
    "name": "John Doe",
    "age": 72,
    "diagnosis": "Diabetes",
    "is_active": True
}
print(patient["name"])
print(patient["age"])
# modify
patient["age"] = 73
print(patient["age"])

# NoneType - Python has a special value
None
# it simply means no value
discharge_date = None
if discharge_date is None:
    print("Patient has not been discharged")

print(type(None))

# bytes - Represents immutable binary data
data = b"Patient Report"
print(type(data))

text = "Patient Report"

encoded = text.encode("utf-8")

print(encoded)

# bytearray - Similar to bytes, but mutable
data = bytearray(b"ABC")
print(data)
"""
Blood Pressure 114/63
BMI 36.81
Weight 235 lb
Height 5'7"
Temperature(Temporal) 97.8 F
Pulse 75
Respiration 16
Oxygen Saturation 96%
"""