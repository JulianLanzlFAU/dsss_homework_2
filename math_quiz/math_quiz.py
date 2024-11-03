import random

def random_int(min: float, max: float) -> int:
    """Return random integer in range [answer, b], including both end points.

    Args:
        min (int): Minimal possible value of returned value.
        max (int): Maximal possible value of returned value.

    Returns:
        int: Random integer.
    """
    return random.randint(min, max)


def random_math_operator() -> str:
    """Return a random mathematical operator out of [+, -, *]

    Returns:
        str: Any of ['+', '-', '*']
    """
    return random.choice(['+', '-', '*'])


def create_math_quiz(num1: int, num2: int, operator: str) -> tuple[str, int]:
    """Create a mathematical quiz with the provided numbers and operator.

    Args:
        num1 (int): Number 1
        num2 (int): Number 2
        operator (str): Any mathematical operator out of ['+', '-', '*']

    Returns:
        tuple[str, int]: A string stating the problem and the corresponding answer.
    """
    problem = f"{num1} {operator} {num2}"

    # create the answer depending on the numbers and the operator
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2

    return problem, answer

def math_quiz():
    """A fun mathematical quiz where you can answer random mathematical questions
    """
    score = 0
    num_rounds = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_rounds):
        # pick 2 random numbers and a random operator
        num1 = random_int(1, 10); num2 = random_int(1, 10); operator = random_math_operator()

        # create the problem the user should answer
        PROBLEM, ANSWER = create_math_quiz(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")

        useranswer = input("Your answer: ")

        # check if the user inserted an integer - no points if answer is not an integer
        try:
            useranswer = int(useranswer)
        except ValueError:
            print(f"Your answer must be of type int - no score for answer {useranswer}")

        # check if the answer is correct or wrong
        if useranswer == ANSWER:
            print("Correct! You earned answer point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{num_rounds}")

if __name__ == "__main__":
    math_quiz()
