with open("idor2.json", "rb") as file:
    content = file.read()

with open("semgrep_results_fixed.json", "w", encoding="utf-8") as file:
    file.write(content.decode("utf-16", errors="ignore"))

print("✅ Converted JSON to UTF-8. Try running the script again.")
