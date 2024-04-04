def second_symbol(s: str, symbol: str) -> int:
    if s.count(symbol) < 2:
        return -1

    start_search = s.find(symbol)+1
    return s[start_search:].find(symbol) + start_search
