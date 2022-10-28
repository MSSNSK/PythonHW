# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


txt = input('Enter the text through the gap:\n')
print(f'Source text: {txt}')
find_txt = 'абв'
lst = [i for i in txt.split() if find_txt not in i]
print(f'Result: {" ".join(lst)}')
