from __future__ import absolute_import
from . import main


# function to set path to current folder (py 2 to 3)
def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))


def main():
    import_modify()
    main.main()
