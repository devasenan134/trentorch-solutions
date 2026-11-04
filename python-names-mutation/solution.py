def mutate_list(lst: list) -> None:
    """
    Mutate `lst` in place by appending the value 4 to it.
    Do not reassign lst to a new object. Return nothing.
    """
    lst.append(4)


def reassign_list(lst: list) -> list:
    """
    Create a brand-new list [9, 9, 9] and return it, without
    mutating the original `lst` in any way.
    """
    return [9, 9, 9]


def observe_through_alias(original: list) -> dict:
    """
    Inside this function:
      1. Create `alias = original` (a second variable pointing
         at the same object).
      2. Mutate `original` by appending 100 to it.
      3. Reassign `original` to a brand-new list [0, 0, 0]
         (do not mutate this new list into alias's object).

    Return a dictionary:
      {
        "alias_after_mutation": <contents of alias right after step 2>,
        "alias_after_reassignment": <contents of alias right after step 3>,
        "original_final": <contents of original at the end>
      }
    """
    res = {
        "alias_after_mutation": 0,
        "alias_after_reassignment": 0,
        "original_final": 0
    }
    alias = original
    original.append(100)
    res["alias_after_mutation"] = alias
    original = [0, 0, 0]
    res["alias_after_reassignment"] = alias
    res["original_final"] = original

    return res


def is_mutable_type(value) -> bool:
    """
    Return True if the type of `value` is mutable (list, dict,
    set, or a typical custom object instance), False if it's
    immutable (int, float, bool, str, tuple, frozenset).
    """
    if isinstance(value, (int, float, bool, str, tuple, frozenset)):
        return False
    return True


def tuple_inner_mutation_check(t: tuple) -> dict:
    """
    Given a tuple `t` whose first element is a list, mutate that
    inner list by appending the value 100 to it. Do NOT attempt
    to reassign any slot of the tuple itself.

    Return a dictionary:
      {
        "tuple_id_before": <id of t before mutation>,
        "tuple_id_after": <id of t after mutation>,
        "inner_list_after": <contents of t[0] after mutation>
      }
    tuple_id_before and tuple_id_after should be equal, since the
    tuple itself was never reassigned.
    """
    res = {
        "tuple_id_before": id(t),
        "tuple_id_after": 0,
        "inner_list_after": 0
      }
    t[0].append(100)
    res["tuple_id_after"] = id(t)
    res["inner_list_after"] = t[0]

    return res
