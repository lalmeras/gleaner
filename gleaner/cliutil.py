from functools import update_wrapper

from click import pass_context


def make_pass_decorator(type):
    def decorator(f):
        @pass_context
        def new_func(ctx, *args, **kwargs):
            obj = ctx.find_object(dict)[type] or None
            if obj is None:
                raise Exception("Context {} not found".format(type.__name__))
            return ctx.invoke(f, obj, *args, **kwargs)
        return update_wrapper(new_func, f)
    return decorator