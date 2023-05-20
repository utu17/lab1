
#Name- Utsav Jiteshkumar Bhanderi
#Student Id - 159776202

# Function 1: wins_rock_scissors_paper
def wins_rock_scissors_paper(player_throw, opponent_throw):
    player_throw = player_throw.lower()
    opponent_throw = opponent_throw.lower()

    if player_throw == opponent_throw:
        return False
    elif (
        (player_throw == "rock" and opponent_throw == "scissors")
        or (player_throw == "paper" and opponent_throw == "rock")
        or (player_throw == "scissors" and opponent_throw == "paper")
    ):
        return True
    else:
        return False


# Function 2: factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# Function 3: fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# Function 4: sum_to_goal
def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0


# Python Class: UpCounter
class UpCounter:
    def __init__(self, step_size=1):
        self.counter = 0
        self.step_size = step_size

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.step_size


# Python Class: DownCounter (Inherited from UpCounter)
class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.step_size
