import random

problems = [
    "26.1", "26.2", "26.3", 
    "27.1", "27.2", "27.3", "27.4", "27.5", "27.6", "27.7", "27.8", "27.9"
]

def get_random_problem(arr):
    """
    Returns a random problem from the predefined set of problems.
    """
    return random.choice(arr)

print(get_random_problem(problems))