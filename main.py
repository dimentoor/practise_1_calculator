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
            # add +; -
            x = float(input("x = "))

            y = float(input("y = "))

            if action == '+':
                print('%.2f + %.2f = %.2f' % (x, y, x + y))

            elif action == '-':
                print('%.2f - %.2f = %.2f' % (x, y, x - y))
                # add *; /
            elif action == '*':
                print('%.2f * %.2f = %.2f' % (x, y, x * y))

            elif action == '/':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x / y))
                else:
                    print("Деление на ноль!")
        else:
            print("thx for using calculator")


if __name__ == '__main__':
    main()

