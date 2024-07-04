#!/usr/bin/env python3
"""
Module: Lockbox Unlocker
"""
from typing import List

"""
Module: Lockbox Unlocker

This module provides a function to determine if all boxes can be unlocked
starting from the first box (boxes[0]).

Functions:
- canUnlockAll(boxes): Determine if all boxes can be unlocked.

"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked starting from the first box (boxes[0]).

    Args:
    boxes (List[List[int]]): A list of lists where each inner list contains
    integers representing keys to other boxes.

    Returns:
    bool: True if all boxes can be opened starting from the first box, False otherwise.

    Notes:
    - A key with the same number as a box opens that box.
    - The function assumes all keys will be positive integers.
    - There can be keys that do not have corresponding boxes.

    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key < n and key not in visited:
                    queue.append(key)

    return len(visited) == n
