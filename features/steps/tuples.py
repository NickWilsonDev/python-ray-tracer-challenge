#tuples.py  test steps for tuples feature
from behave import *


@given('a tuple(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    pass

@then('a.x = 4.3')
def step_impl(context):
    a = Tuple(4.3, -4.2, 3.1, 1.0)
    assert a.x == 4.3


