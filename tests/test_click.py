from typing import Type
from click.globals import push_context, pop_context
from click import Context


from unittest import TestCase
from unittest.mock import patch

class TestDecorator(TestCase):
    def test_make_pass_decorator(self):
        """
        When ctx.obj is a dict, make_pass_decorator allows to retrieve
        a value from dict based on a key value.
        """
        from gleaner.cliutil import make_pass_decorator
        try:
            with patch("click.Context") as Context:
                # setup a click context; obj is a dictionary
                # with a int key
                ctx = Context()
                context_object = dict()
                context_object[int] = 5
                ctx.find_object.return_value = context_object
                push_context(ctx)

                # setup a decorator to extract int key from dict object
                def f(context_obj):
                    pass
                # decorate and call function
                make_pass_decorator(int)(f)()
                
                # decorated function is called with expected context value
                ctx.invoke.assert_called_with(f, 5)
        finally:
            pop_context()
    

    def test_make_pass_decorator_failure(self):
        """
        If expected key cannot be extracted from ctx.obj, it throws an Exception.
        """
        from gleaner.cliutil import make_pass_decorator
        try:
            with patch("click.Context") as Context:
                with self.assertRaises(Exception) as raised:
                    # setup a click context; obj is a dictionary
                    # with a int key
                    ctx = Context()
                    context_object = dict()
                    context_object[int] = 5
                    ctx.find_object.return_value = context_object
                    push_context(ctx)

                    # setup a decorator to extract int key from dict object
                    def f(context_obj):
                        pass
                    # decorate and call function
                    make_pass_decorator(dict)(f)()
                assert str(raised.exception) == "Context dict not found"
        finally:
            pop_context()  
        