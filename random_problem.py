import random

problems = [
    "26.1", "26.2", "26.3", 
    "27.1", "27.2", "27.3", "27.4", "27.5", "27.6", "27.7", "27.8", "27.9", "27.10", "27.11", "27.12", "27.13", "27.14", "27.15", "27.16", "27.17", "27.18",
    "28.1", "28.2", "28.3", "28.4", "28.5", "28.6", "28.7", "28.8",
    "29.1", "29.2", "29.3", "29.4", "29.5", "29.6", "29.7", "29.8", "29.9"
]

def get_random_problem(arr):
    """
    Returns a random problem from the predefined set of problems.
    """
    return random.choice(arr)

print(get_random_problem(problems))