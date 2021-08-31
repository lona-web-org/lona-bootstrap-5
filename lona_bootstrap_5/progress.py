from lona.html import Node, Div

from .static_files import STATIC_FILES


class Progress(Node):
    STATIC_FILES = STATIC_FILES

    TAG_NAME = 'div'
    CLASS_LIST = ['progress']

    def __init__(self, *label, background=None, value=None, percentage=None,
                 striped=False, animated=False, **kwargs):

        super().__init__(**kwargs)

        self.nodes = [
            Div(
                _class='progress-bar',
                _role='progressbar',
                _aria_valuemin='0',
                _aria_valuemax='100',
            ),
        ]

        if label:
            self.set_label(*label)

        if background is not None:
            self.background = background

        if value is not None:
            self.value = value

        if percentage is not None:
            self.set_percentage(percentage)

        self.striped = striped
        self.animated = animated

    # properties ##############################################################
    # value
    @property
    def value(self):
        return int(self.nodes[0].attributes.get('aria-valuenow', '0'))

    @value.setter
    def value(self, new_value):
        with self.lock:
            self._value = int(new_value)

            self.nodes[0].style['width'] = '{}%'.format(self._value)
            self.nodes[0].attributes['aria-valuenow'] = str(self._value)

    # background
    @property
    def background(self):
        with self.lock:
            for class_name in self.nodes[0].class_list:
                if class_name.startswith['bg-']:
                    return class_name

            return ''

    @background.setter
    def background(self, new_value):
        with self.lock:
            for class_name in self.nodes[0].class_list:
                if class_name.startswith('bg-'):
                    self.nodes[0].class_list.remove(class_name)

            if new_value:
                if not new_value.startswith('bg-'):
                    new_value = 'bg-{}'.format(new_value)

                self.nodes[0].class_list.add(new_value)

    # striped
    @property
    def striped(self):
        return 'progress-bar-striped' in self.nodes[0].class_list

    @striped.setter
    def striped(self, new_value):
        if new_value:
            self.nodes[0].class_list.add('progress-bar-striped')

        else:
            self.nodes[0].class_list.remove('progress-bar-striped')

    # animated
    @property
    def animated(self):
        return 'progress-bar-animated' in self.nodes[0].class_list

    @animated.setter
    def animated(self, new_value):
        if new_value:
            self.nodes[0].class_list.add('progress-bar-animated')

        else:
            self.nodes[0].class_list.remove('progress-bar-animated')

    # methods #################################################################
    def set_label(self, *nodes):
        self.nodes[0].set_text()

    def set_percentage(self, percentage):
        with self.lock:
            self.value = percentage
            self.nodes[0].set_text('{}%'.format(percentage))
