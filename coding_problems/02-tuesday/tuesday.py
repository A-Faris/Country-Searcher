from collections import Counter


def duplicate_count(text: str) -> int:
    return sum([1 for value in Counter(text.lower()).values() if value > 1])


duplicate_count("abcdeaB")
