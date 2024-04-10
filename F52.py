while True:
    def calF51(express):

        if len(express.split()) != 3:
            raise Exception("throws Exception //т.к. строка не является математической операцией")

        a, operator, b = express.split()


        if not (1 <= int(a) <= 10) or not (1 <= int(b) <= 10):
            raise Exception("Числа должны быть от 1 до 10")


        if operator == '+':
            return int(a) + int(b)
        elif operator == '-':
            return int(a) - int(b)
        elif operator == '*':
            return int(a) * int(b)
        elif operator == '/':
            return int(a) // int(b)
        else:
            raise Exception("throws Exception //т.к Неподдерживаемая операция")


    try:
        express = input("Введите математическую операцию(2 Числа и 1 оператор): ")
        result = calF51(express)
        print(result)
    except Exception as e:
        print("Ошибка:", str(e))