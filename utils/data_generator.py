import random
import string


def random_full_name() -> str:
    letters = string.ascii_letters  # a-zA-Z
    first_part = "".join(random.choice(letters) for _ in range(6))
    digits = "".join(random.choice(string.digits) for _ in range(3))
    combined = first_part + digits
    return combined[::-1]
