from typing import List


def find_positions(numbers: List[int], target: int) -> List[int]:
    """Return all indexes where target appears in numbers."""
    positions: List[int] = []
    for index, value in enumerate(numbers):
        if value == target:
            positions.append(index)
    return positions


def find_subsequence(sequence: List[int], pattern: List[int]) -> int:
    """Return the starting index of the first matching subsequence or -1."""
    if not pattern:
        return 0

    for start in range(len(sequence) - len(pattern) + 1):
        match = True
        for index in range(len(pattern)):
            if sequence[start + index] != pattern[index]:
                match = False
                break
        if match:
            return start

    return -1


def first_missing_positive(numbers: List[int]) -> int:
    """Return the smallest positive integer not found in the list."""
    current = 1
    while True:
        if current not in numbers:
            return current
        current += 1


if __name__ == "__main__":
    sample_numbers = [3, 4, -1, 1]
    print("Positions of 4:", find_positions([4, 7, 4, 1, 4], 4))
    print("Subsequence index:", find_subsequence([1, 2, 3, 4, 5], [3, 4]))
    print("First missing positive:", first_missing_positive(sample_numbers))
