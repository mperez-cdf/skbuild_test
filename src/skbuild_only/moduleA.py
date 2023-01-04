"""Pure python module in the package"""

import skbuild_only._core as m


def add_five(i: int) -> int:
    """Add five to an integer

    Args:
        i (int): The number to add

    Returns:
        int: The number + 5
    """
    return m.add(i, 5)
