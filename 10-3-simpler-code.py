from pathlib import Path

path = Path('learning_python.txt')

content = path.read_text()

# i = content.splitlines()
# print(i)

print(content.splitlines())
for i in content.splitlines():
    print(i)
print('\n')
print(content.replace('Python','Java'))    