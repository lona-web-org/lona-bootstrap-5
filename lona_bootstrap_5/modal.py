from lona.html import Widget, HTML

from .static_files import STATIC_FILES


class Modal(Widget):
    STATIC_FILES = STATIC_FILES
    FRONTEND_WIDGET_CLASS = 'lona_bootstrap5.Modal'

    def __init__(self, fade=True, scrollable=False, centered=False):
        # setup html
        self.nodes = HTML("""
            <div class="modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title"></h5>
                            <button type="button" class="btn-close" aria-label="Close"></button>
                        </div>
                        <div class="modal-body"></div>
                        <div class="modal-footer"></div>
                    </div>
                </div>
            </div>
        """)[0]  # NOQA

        self._modal_dialog = self.query_selector('div.modal-dialog')
        self._modal_header = self.query_selector('div.modal-header')
        self._modal_title = self.query_selector('h5.modal-title')
        self._close_button = self.query_selector('button')
        self._modal_body = self.query_selector('div.modal-body')
        self._modal_footer = self.query_selector('div.modal-footer')

        self.close_button = self._modal_header.query_selector(
            'button.btn-close')

        # setup data
        self.data = {
            'modal_options': {
                'focuse': True,
            },
            'visible': False,
        }

        # properties
        self.fade = fade
        self.scrollable = scrollable
        self.centered = centered

    # properties ##############################################################
    # fade
    @property
    def fade(self):
        return 'fade' in self.nodes[0].class_list

    @fade.setter
    def fade(self, new_value):
        if new_value:
            self.nodes[0].class_list.add('fade')

        else:
            self.nodes[0].class_list.remove('fade')

    # scrollable
    @property
    def scrollable(self):
        return 'modal-dialog-scrollable' in self._modal_dialog.class_list

    @scrollable.setter
    def scrollable(self, new_value):
        if new_value:
            self._modal_dialog.class_list.add('modal-dialog-scrollable')

        else:
            self._modal_dialog.class_list.remove('modal-dialog-scrollable')

    # centered
    @property
    def centered(self):
        return 'modal-dialog-centered' in self._modal_dialog.class_list

    @centered.setter
    def centered(self, new_value):
        if new_value:
            self._modal_dialog.class_list.add('modal-dialog-centered')

        else:
            self._modal_dialog.class_list.remove('modal-dialog-centered')

    # methods #################################################################
    def hide(self):
        self.data['visible'] = False

    def show(self):
        self.data['visible'] = True

    def set_title(self, *nodes):
        self._modal_title.nodes = list(nodes)

    def set_body(self, *nodes):
        self._modal_body.nodes = list(nodes)

    def set_buttons(self, *buttons):
        self.buttons = list(buttons)
        self._modal_footer.nodes = self.buttons
