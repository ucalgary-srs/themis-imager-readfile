__version__ = "1.1.3"

from ._themis import read

if (__name__ == "__main__"):
    import multiprocessing
    multiprocessing.freeze_support()
