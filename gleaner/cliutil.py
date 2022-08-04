from functools import update_wrapper
from typing import Type, Callable

from click import pass_context


def make_pass_decorator(type: Type) -> Callable[[Callable], Callable]:
    def decorator(f: Callable):
        @pass_context
        def new_func(ctx, *args, **kwargs):
            obj = ctx.find_object(dict) or None
            if not type in obj:
                raise Exception("Context {} not found".format(type.__name__))
            return ctx.invoke(f, obj[type], *args, **kwargs)
        return update_wrapper(new_func, f)
    return decorator