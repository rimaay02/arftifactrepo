import json

# Load JSON and pretty-print it
with open("semgrep_results_fixed.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Save formatted output to a new file
with open("semgrep_results_pretty.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("✅ JSON formatted successfully! Open 'semgrep_results_pretty.json' to view.")
