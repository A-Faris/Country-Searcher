def missing(nums: list[int], s: str) -> str:
    code = "".join(s.lower().split())

    if len(code) <= max(nums):
        return "No mission today"

    return "".join([code[num] for num in sorted(nums)])
