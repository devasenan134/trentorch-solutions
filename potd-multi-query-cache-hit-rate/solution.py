def cache_hit_rate(keys: list[int]) -> tuple[int, int, float]:
    """
    keys: a sequence of request keys in arrival order.

    A request is a hit iff its key has appeared earlier in the sequence
    (the first occurrence of any key is always a miss).

    Return (hits, misses, rate) where rate = hits / len(keys).
    """
    # TODO: track which keys have been seen so far, in order.

    hits = 0
    uks = []
    for key in keys:
        if key not in uks:
            uks.append(key)
        else:
            hits += 1

    return hits, len(uks), hits/len(keys)
