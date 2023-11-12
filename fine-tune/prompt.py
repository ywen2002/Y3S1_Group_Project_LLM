import csv
import json

# Read CSV data
csv_file = "Heart_Disease_Prediction.csv"  # Replace with the actual path to your CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Define a function to generate completion text
def generate_completion(patient_data):
    completion_template = (
        "Patient Information:\n"
        "Age: {Age}\n"
        "Sex: {Sex}\n"
        "Chest pain type: {Chest pain type}\n"
        "Blood Pressure (BP): {BP}\n"
        "Cholesterol: {Cholesterol}\n"
        "FBS over 120: {FBS over 120}\n"
        "EKG results: {EKG results}\n"
        "Max Heart Rate: {Max HR}\n"
        "Exercise angina: {Exercise angina}\n"
        "ST depression: {ST depression}\n"
        "Slope of ST: {Slope of ST}\n"
        "Number of vessels fluro: {Number of vessels fluro}\n"
        "Thallium: {Thallium}\n"
        "Heart Disease: {Heart Disease}\n"
    )

    return completion_template.format(**patient_data)

# Generate prompt and completion pairs
prompt_completion_pairs = []
for patient in data:
    prompt = "Patient with Age {} and Sex {}".format(patient['Age'], 'Male' if patient['Sex'] == '1' else 'Female')
    completion = generate_completion(patient)
    pair = {"prompt": prompt, "completion": f"<is=deal>{completion}"}
    prompt_completion_pairs.append(pair)

# Export to JSON file
json_file = "output.json"
with open(json_file, 'w') as json_output:
    json.dump(prompt_completion_pairs, json_output, indent=2)

print(f"Prompt and completion pairs have been exported to {json_file}.")
