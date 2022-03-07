import os

try:
    from .templating import MenuItem  # NOQA
    from .messages import show_alert  # NOQA
    from .progress import Progress  # NOQA
    from .switch import Switch  # NOQA
    from .modal import Modal  # NOQA
    from .nodes import *  # NOQA

except ImportError:
    # this happens while packaging and can be ignored

    pass

VERSION = (0, 3)
VERSION_STRING = '{}'.format('.'.join([str(i) for i in VERSION]))

TEMPLATE_DIR = os.path.join(
    os.path.dirname(__file__),
    'templates',
)
