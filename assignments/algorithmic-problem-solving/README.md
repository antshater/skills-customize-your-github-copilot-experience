# 📘 Assignment: Algorithmic Problem Solving with Python

## 🎯 Objective

Practice structured problem solving and algorithm design by implementing Python functions that search, match, and analyze number sequences.

## 📝 Tasks

### 🛠️ Linear Search and Counting

#### Description
Write a function called `find_positions()` that searches a list of numbers and returns every index where a target value appears.

#### Requirements
Completed program should:

- Accept a list of integers and a target integer.
- Return a list of all 0-based indexes where the target appears.
- Return an empty list when the target does not exist in the list.
- Example:
  ```python
  find_positions([4, 7, 4, 1, 4], 4)  # [0, 2, 4]
  ```

### 🛠️ Subsequence Matching

#### Description
Write a function called `find_subsequence()` that checks whether a smaller sequence appears inside a larger list.

#### Requirements
Completed program should:

- Accept a main list and a subsequence list.
- Return the starting index of the first matching subsequence.
- Return `-1` if the subsequence does not appear.
- Example:
  ```python
  find_subsequence([1, 2, 3, 4, 5], [3, 4])  # 2
  find_subsequence([1, 2, 3, 4, 5], [4, 2])  # -1
  ```

### 🛠️ Smallest Missing Positive

#### Description
Write a function called `first_missing_positive()` that finds the smallest positive integer not present in a list.

#### Requirements
Completed program should:

- Accept a list of integers.
- Return the smallest positive integer greater than 0 that is not in the list.
- Handle repeated and negative values correctly.
- Example:
  ```python
  first_missing_positive([3, 4, -1, 1])  # 2
  first_missing_positive([1, 2, 0])      # 3
  ```
