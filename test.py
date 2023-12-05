def min_carrots_to_equalize_bunnies(N, X, carrots):
    total_carrots = sum(carrots)
    sorted_carrots = sorted(carrots, reverse=True)

    target_bunnies = N - X
    extra_carrots = sum(sorted_carrots[:target_bunnies])

    return max(extra_carrots, max(sorted_carrots)) if target_bunnies > 0 else max(sorted_carrots)

test_cases = [
    (4, 3, [2, 5, 9, 19]),  # 11
    (4, 2, [2, 5, 9, 10]),  # 1
    (4, 3, [2, 5, 9, 19]),  # 11
    (4, 4, [2, 5, 9, 19]),  # 19
    (5, 3, [2, 5, 9, 10, 20]),  # 11
    (5, 4, [2, 5, 9, 10, 20]),  # 19
]

for N, X, carrots in test_cases:
    result = min_carrots_to_equalize_bunnies(N, X, carrots)
    print(result)
