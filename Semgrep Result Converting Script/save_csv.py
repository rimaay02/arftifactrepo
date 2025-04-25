import json
import csv

# Load the JSON file
with open('semgrep_results_pretty.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Define output CSV file
csv_file = 'semgrep_results_clean.csv'
csv_columns = [
    'check_id', 'path', 'start_line', 'start_col', 'end_line', 'end_col',
    'message', 'category', 'cwe', 'owasp', 'severity'
]

# Prepare data
csv_data = []
for result in data.get('results', []):
    csv_data.append({
        'check_id': result.get('check_id'),
        'path': result.get('path'),
        'start_line': result['start']['line'],
        'start_col': result['start']['col'],
        'end_line': result['end']['line'],
        'end_col': result['end']['col'],
        'message': result['extra'].get('message', '').strip(),
        'category': result['extra']['metadata'].get('category'),
        'cwe': result['extra']['metadata'].get('cwe'),
        'owasp': result['extra']['metadata'].get('owasp'),
        'severity': result['extra'].get('severity')
    })

# Write CSV with proper quoting
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(csv_data)

print(f"Clean CSV file saved as '{csv_file}'")
