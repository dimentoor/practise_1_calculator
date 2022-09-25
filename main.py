'''calculator'''

def main():
    # Выводим сообщение
    print("Это простой калькулятор на Python")

    while True:
        # действия
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")

        action = input("Действие: ")
        # Если action равен q то
        if action == "q":

            print("Выход из программы")
            break
        # Если action равен +, -, *, /, то
        if action in ('+', '-', '*', '/'):
            pass

        else:
            print("thx for using calculator")


if __name__ == '__main__':
    main()

