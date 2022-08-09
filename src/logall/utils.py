from typing import Callable


def apply_on_dict(
    dict_obj: dict,
    fn: Callable,
    return_as_dict: bool = False,
    *args,
    **kwargs
):
    """ applies an operation defined by a function on each key, value pair in a given
    dictionary.

    Args:
        dict_obj (Dict): dictionary to apply a function on
        fn (Callable): function to apply on (key, value) pairs of the `dict_obj`.
        return_as_dict (bool, optional): to return the result as dictionary or not.
            Defaults to False.

        .. note::
            Additional arguments are passed to the function.

    Returns:
        Dict, optional: result of reconstructing the dictionary is returned if
            return_as_dict is set to True, otherwise nothing is returned.
    """
    ans = dict()
    if dict_obj is None:
        return
    for key, value in dict_obj.items():
        x = fn(key, value, *args, **kwargs)
        if return_as_dict:
            ans[key] = x
    if return_as_dict:
        return ans
