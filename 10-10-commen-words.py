from pathlib import Path

file_path = Path('whats_python.txt')

file_content = file_path.read_text()

print(file_content.lower().count('the '))