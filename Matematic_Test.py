import random

# Генератор случайного математического примера

def generate_math_question(a, b):
    operators = '/*-+'
    operator = random.choice(operators)
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    primer = f"{num1} {operator} {num2}"
    print(primer)
    return primer

# Проверка ответа пользователя на правильность
def check_answer(a, b):
    try:
        otvet = int(b)
        primer = str(a)
        # print(primer)
        result = eval(primer)
        # print(result)
        # print(otvet)
        if result == otvet:
            # print(8)
            return True
        else:
            # print(7)
            return False
    except ValueError:
        # print(9)
        return False

# print(check_answer("2 + 3", "5"))
# print(check_answer("5 * 3", "10"))
# print(check_answer("10-3", "семь"))

def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        primer = generate_math_question(0, 10)
        otvet = input('Ответ: ')
        True_or_False = check_answer(primer, otvet)
        if True_or_False == True:
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    # процент от числа = (правельные ответы / всего вопросов) * 100
    prothent = (correct_answers/number_of_questions) * 100

    if prothent > 80:
        print("Отлично! Вы получаете оценку A.") # > 80%
    elif prothent > 60:
        print("Хорошо! Вы получаете оценку B.") # > 60%
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(7)