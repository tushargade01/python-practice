from pathlib import Path

word = Path('learning_python.txt')
conetnt = word.read_text()
print(conetnt)