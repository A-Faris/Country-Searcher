def reverse_words(text: str) -> str:
    return " ".join([i[::-1] for i in text.split()])
