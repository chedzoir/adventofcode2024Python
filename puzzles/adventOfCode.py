"""Module providing useful helper functions"""

def load_content(day) :
    """Load puzzle data for the day requested"""
    filename = f"./data/day{day}.txt"

    print(f"Loading from {filename}") 
    with open(filename, "r", encoding="utf8") as f:
        return list(map(lambda a : a.strip(), f.readlines()))