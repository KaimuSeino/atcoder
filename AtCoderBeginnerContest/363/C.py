def is_palindrome(s):

    return s == s[::-1]

def has_k_palindrome(s, K):

    for start in range(len(s) - K + 1):

        if is_palindrome(s[start:start + K]):

            return True

    return False

def count_avoid_k_palindrome_permutations(S, K):

    from collections import Counter
    import math

    char_count = Counter(S)

    factorial = math.factorial

    total_permutations = factorial(len(S))

    for count in char_count.values():

        total_permutations //= factorial(count)

    def backtrack(path, remaining):

        nonlocal valid_count

        if not remaining:

            if not has_k_palindrome(path, K):

                valid_count += 1

            return

        previous_char = None

        for char in list(remaining):

            if char != previous_char:

                path.append(char)

                remaining[char] -= 1

                if remaining[char] == 0:

                    del remaining[char]

                backtrack(path, remaining)

                remaining[char] = remaining.get(char, 0) + 1

                path.pop()

            previous_char = char

    valid_count = 0

    backtrack([], char_count)

    return valid_count

N, K = map(int, input().split())

S = input()

print(count_avoid_k_palindrome_permutations(S, K))