"""
This program is used to check Lemma 4.5, in which we need to proof that m = 21 is the only
m-value with more than one minimal Fibonacci triple. Given the indexes of the Fibonacci
elements (a,b,c), this program checks all triples up to c=500.

First, we generate a dictionary with the Fibonacci sequence, where the key is the index
of the sequence and the value is the corresponding number.

Then, we generate all possible combinations of indexes to generate Fibonacci triples. 
We preprocess each combination, as based on Lemma 2.3, we only need to analyse triples with
the minimality condition c >= a + b + 1.

Finally, we store in a dictionary all minimal Fibonacci triples assigned to their respective
m-value. With this we can check if m = 21 is trully the only positive m-value that has more
than one minimal Fibonacci triple.
"""

from itertools import combinations_with_replacement as combinations


def generate_fibonacci(n: int) -> dict:
    """
    This function calculates a fibonacci sequence up to the nth number. It returns
    a dictionary where the key is the index of the sequence and the value is the
    corresponding number.

    Parameters:
    - n: int

    Returns:
    - dict
    """
    fibonacci_sequence = {}
    a, b = 0, 1
    for idx in range(n):
        fibonacci_sequence[idx] = a
        a, b = b, a + b
    return fibonacci_sequence


def combinations_idx(c: int):
    """
    This function calculates all combinations of 3 numbers from a range of 2 to a
    given number.

    Parameters:
    - c: int

    Returns:
    - Generator of tuple[int, int, int]
    """
    all_combinations = combinations(range(2, c), 3)
    return all_combinations


def process_indexes(all_combs: list[tuple[int, int, int]]):
    """
    This function processes the combinations of indexes considering the minimality
    condition c >= a + b + 1, given the combination (a,b,c).

    Parameters:
    - all_combs: list[tuple[int, int, int]]

    Returns:
    - Generator of tuple[int, int, int]
    """
    for a, b, c in all_combs:
        if c >= a + b + 1:
            yield a, b, c


def process_combinations(indexes: list[tuple[int, int, int]], all_fibs: dict) -> dict:
    """
    This function calculates m-values for all Fibonacci triples, given the processed
    indexes and the dictionary containing the Fibonacci sequence. It returns a
    dictionary where the key is the m-value and the value is the list of minimal triples
    that satisfy that m-value (both indexes and Fibonacci values).

    Parameters:
    - indexes: list[tuple[int, int, int]]

    Returns:
    - dict
    """
    dict_m = {}
    for a, b, c in indexes:
        fa, fb, fc = all_fibs[a], all_fibs[b], all_fibs[c]
        m = fa * fa + fb * fb + fc * fc - 3 * fa * fb * fc
        if m > 0:
            if m not in dict_m:
                dict_m[m] = [((a, b, c), (fa, fb, fc))]
            else:
                dict_m[m] += [((a, b, c), (fa, fb, fc))]
    return dict_m


def print_dict(dict_m: dict) -> None:
    """
    This function prints all m-values that have more than one minimal Fibonacci
    triple.

    Parameters:
    - dict_m: dict[int, list[tuple[tuple[int, int, int], tuple[int, int, int]]]]
    """
    for m in dict_m:
        if len(dict_m[m]) > 1:
            print("m = {}, count = {}".format(m, len(dict_m[m])))


if __name__ == "__main__":
    c_max = 500
    all_combs = combinations_idx(c_max)
    all_fibs = generate_fibonacci(c_max)
    processed_indexes = process_indexes(all_combs)
    dict_m = process_combinations(processed_indexes, all_fibs)

    print_dict(dict_m)
    print(dict_m[21])
