def count_exclamation_marks(core_values: list[dict]) -> int:
    return sum(v["headline"].count("!") + v["description"].count("!") for v in core_values)
