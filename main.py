#1
alphabet = ["a","b","c","d","e","f","g","h","i","j", "k","l","m","n","o","p","q","r","s","t", "u","v","w","x","y","z"," "]

def get_data():
    word = input('Введите текст: ').lower()
    num = int(input('Введите число(1-26): '))
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input('Вне диапазона,введите число(1-26): '))
    data = (word, num)
    return data

def make_code(word, num):
    new_word = ""
    for i in word:
        j = alphabet.index(i)
        j += num
        if j > 26:
            j = j - 27
        char = alphabet[j]
        new_word = new_word + char
    print(f'Шифр текста {word} -> {new_word}')
    print()

def decode(word, num):
    new_word = ""
    for i in word:
        j = alphabet.index(i)
        j -= num
        if j < 0:
            j = j + 27
        char = alphabet[j]
        new_word = new_word + char
    print(f'{word} -> {new_word}')
    print()

def main():
    isAgain = True
    while isAgain:
        print('Перешифровать текст - 1')
        print('Расшифровать код - 2')
        print('Выйти из программы - 3')
        selection = input('Выберите опцию: ')
        if selection == '1':
            (word, num) = get_data()
            make_code(word, num)
        elif selection == '2':
            (word, num) = get_data()
            decode(word, num)
        elif selection == '3':
            print('Вы вышли из программы, Спасибо!')
            isAgain = False
        else:
            raise TypeError('Вы выбрали не тот вариант. Пожалуйста попробуйте еще раз!')

if __name__ == '__main__':
    main()


"""def hiText():
    return 'Hello','Text','World'

a,b,c = hiText()
print(a,b,c)"""