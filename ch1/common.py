"""a module that has the common functionalities"""

from heapq import heappush, heappop
from typing import List, Tuple

space = "abcdefghijklmnopqrstuvwxyz"

NOT_FOUND = -1

__relative_frequencies = [
    0.0817,
    0.0150,
    0.0278,
    0.0425,
    0.1270,
    0.0223,
    0.0202,
    0.0609,
    0.0697,
    0.0015,
    0.0077,
    0.0403,
    0.0241,
    0.0675,
    0.0751,
    0.0193,
    0.0010,
    0.0599,
    0.0633,
    0.0906,
    0.0276,
    0.0098,
    0.0236,
    0.0015,
    0.0197,
    0.0007,
]

__max_heap = []

char_frequency_ordered = []

for i, char in enumerate(space):
    heappush(__max_heap, (-__relative_frequencies[i], char))

while len(__max_heap) > 0:
    frequency, char = heappop(__max_heap)
    char_frequency_ordered.append((char, -frequency))

# char ordered by the frequency of occurrence
char_ordered = [char for char, _ in char_frequency_ordered]


def count_chars(text: str) -> List[Tuple[str, int]]:
    """computes the frequency of each alpha character in the given text."""
    char_frequency_unordered = {}
    max_heap = []

    for char in space:
        char_frequency_unordered[char] = 0

    for char in text:
        if char_frequency_unordered.get(char, NOT_FOUND) == NOT_FOUND:
            continue
        char_frequency_unordered[char] += 1

    for key, value in char_frequency_unordered.items():
        heappush(
            max_heap,
            (
                -value,
                key,
            ),
        )

    char_frequency_ordered = []

    while len(max_heap) > 0:
        frequency, char = heappop(max_heap)
        char_frequency_ordered.append((char, -frequency))

    return char_frequency_ordered
