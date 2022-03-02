from lona.html import CheckBox, Widget, Div


class Switch(Widget):
    def __init__(self, **kwargs):
        self.nodes = [
            Div(
                CheckBox(**kwargs),
            ),
        ]

        self.nodes[0].class_list.extend(['form-check', 'form-switch'])
        self.nodes[0][0].class_list.append('form-check-input')
        self.check_box = self.nodes[0][0]

    # value
    @property
    def value(self):
        return self.check_box.value

    @value.setter
    def value(self, new_value):
        self.check_box.value = new_value

    # value
    @property
    def disabled(self):
        return self.check_box.disabled

    @disabled.setter
    def disabled(self, new_value):
        self.check_box.disabled = new_value