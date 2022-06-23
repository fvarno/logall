def apply_on_dict(dict_obj, fn, return_as_dict=False, *args, **kwargs):
    ans = dict()
    if dict_obj is None:
        return
    for key, value in dict_obj.items():
        x = fn(key, value, *args, **kwargs)
        if return_as_dict:
            ans[key] = x
    if return_as_dict:
        return ans
