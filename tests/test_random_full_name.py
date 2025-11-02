from utils.data_generator import random_full_name


def test_random_full_name_uniqueness():
    names = [random_full_name() for _ in range(1000000)]
    assert len(names) == len(set(names)), "Duplicate names generated"
