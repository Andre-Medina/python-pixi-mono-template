from pixi_py.hello import hello
from rich import print

MAX = 10


def say_hello():
    """Say hello."""
    print(*hello())


def testing_pre_commit():
    """Tests some special cases."""
    test = MAX
    if test >= MAX:
        print("a")
    if test == 0:
        print("b")
