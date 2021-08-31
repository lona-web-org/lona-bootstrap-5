try:
    from .progress import Progress  # NOQA
    from .modal import Modal  # NOQA
    from .nodes import *  # NOQA

except ImportError:
    # this happens while packaging and can be ignored

    pass

VERSION = (0, 1)
VERSION_STRING = '{}'.format('.'.join([str(i) for i in VERSION]))
