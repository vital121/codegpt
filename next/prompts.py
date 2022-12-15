from enum import Enum

class PromptKeys(Enum):
    COMMENT = 'comment'
    VARNAMES = 'varnames'
    UGH = 'ugh'
    BUGS = 'bugs'
    VULNS = 'vulns'

prompts = {
    "comment": '''Add or update comments according to the Sphinx format. For example:

.. code-block:: python

   def divide(a, b):
       """
       This is a sample comment for a function.

       :param a: The numerator.
       :param b: The denominator.
       :return: The result of dividing a by b.
       """
       return a / b''',
    "varnames": "Change variable names, but nothing else, to make the code more readable. For example, instead of using 'x' and 'y', use 'width' and 'height'.",
    "ugh": "Do anything you can to make this code more readable. Add comments, change variable and function names, add whitespace, whatever",
    "bugs": """Find any bugs you can, note them in comments prefixed with BUG:

Before:
def divide(a, b):
    return a / b

After:
def divide(a, b):
    # BUG: This function should check for division by zero.
    return a / b
""",
    "vulns": """Find any vulnerabilities you can, note them in comments prefixed with VULN:

Before:
def set_username(username):
    this.username = username

After:
def set_username(username):
    # VULN: This function should validate the input to prevent injection attacks.
    this.username = username
""",
}
