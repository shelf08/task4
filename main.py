import re

with open('5.txt', 'r', encoding='utf-8') as file:
    text = file.read()

questions = re.findall(r'[^.!?]*\?', text)

if questions:
    print(questions)
else:
    print("Нет вопросительных предложений в файле")