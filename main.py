#1
alphabet = ["a","b","c","d","e","f","g","h","i","j", "k","l","m","n","o","p","q","r","s","t", "u","v","w","x","y","z"," "]

def get_data():
    pass

def make_code():
    pass

def decode():
    pass

def main():
    isAgain = True
    while isAgain:
        print('Перешифровать текст - 1')
        print('Расшифровать код - 2')
        print('Выйти из программы - 3')
        selection = input('Выберите опцию: ')
        if selection == '1':
            make_code()
        elif selection == '2':
            decode()
        elif selection == '3':
            print('Вы вышли из программы, Спасибо!')
            isAgain = False
        else:
            raise TypeError('Вы выбрали не тот вариант. Пожалуйста попробуйте еще раз!')

if __name__ == '__main__':
    main()