questions = [
    {
        "question": "Столица Казахстана?",
        "options": ["Алматы", "Астана", "Атырау", "Шымкент"],
        "answer": 2
    },
    {
        "question": "Сколько будет 5 × 6?",
        "options": ["25", "30", "35", "40"],
        "answer": 2
    },
    {
        "question": "Какой язык используется в этом проекте?",
        "options": ["Java", "Python", "C#", "PHP"],
        "answer": 2
    },
    {
        "question": "Сколько дней в неделе?",
        "options": ["5", "6", "7", "8"],
        "answer": 3
    },
    {
        "question": "Git используется для...",
        "options": [
            "Просмотра фильмов",
            "Контроля версий",
            "Монтажа видео",
            "Рисования"
        ],
        "answer": 2
    }
]


def get_answer():
    while True:
        try:
            ans = int(input("Ваш ответ: "))
            if 1 <= ans <= 4:
                return ans
            print("Введите число от 1 до 4.")
        except ValueError:
            print("Введите только число.")


def run_quiz():
    score = 0

    print("=== Викторина ===")

    for i, q in enumerate(questions, start=1):
        print(f"\nВопрос {i}: {q['question']}")

        for j, option in enumerate(q["options"], start=1):
            print(f"{j}. {option}")

        answer = get_answer()

        if answer == q["answer"]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно.")

    print("\n===== Результат =====")
    print(f"Правильных ответов: {score} из {len(questions)}")

    percent = score / len(questions) * 100
    print(f"Процент: {percent:.0f}%")

    if percent == 100:
        print("Превосходный результат!")
    elif percent >= 60:
        print("Хороший результат.")
    else:
        print("Попробуйте ещё раз.")


run_quiz()