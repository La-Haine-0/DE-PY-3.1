#Написать программу, которая удаляет из списка все элементы, стоящие на четных позициях.#
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [list[i] for i in range(len(list)) if i % 2 != 0]
print(new_list)

#Написать программу, которая считывает список слов и находит слова, содержащие более трех гласных букв.#
def count_vowels(word):
    vowels = 'aeiou'
    return sum(1 for char in word if char in vowels)

words = ['apple', 'banana', 'elephant', 'python', 'cat']
result = [word for word in words if count_vowels(word) > 3]
print(result)

#Написать программу, которая находит второй по величине элемент в списке.#
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_list = sorted(list, reverse=True)
second_largest = sorted_list[1]
print(second_largest)

#Написать программу, которая удаляет из списка все дубликаты.#
list = [1, 2, 2, 3, 4, 4, 5, 5]
new_list = list(set(list))
print(new_list)

#Написать программу, которая считывает данные из CSV-файла и создает словарь, где ключами являются значения в столбце «Name», а значениями — соответствующие им словари с информацией о поле, возрасте и зарплате.#
import csv

with open('file.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = {row['Name']: {'gender': row['Gender'], 'age': row['Age'], 'salary': row['Salary']} for row in reader}
    print(data)

#Написать программу, которая запрашивает у пользователя строку и выводит на экран все ее подстроки длиной не менее трех символов.#
string = input("Введите строку: ")
substrings = [string[i:j] for i in range(len(string)) for j in range(i + 3, len(string) + 1)]
print(substrings)
