from lona.html import Widget, HTML, CLICK

from .static_files import STATIC_FILES


class Modal(Widget):
    STATIC_FILES = STATIC_FILES
    FRONTEND_WIDGET_CLASS = 'lona_bootstrap5.Modal'

    def __init__(self):
        # setup html
        self.nodes = HTML("""
            <div class="modal fade" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-hidden="true">
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

        self._modal_header = self.query_selector('div.modal-header')
        self._modal_title = self.query_selector('h5.modal-title')
        self._close_button = self.query_selector('button')
        self._modal_body = self.query_selector('div.modal-body')
        self._modal_footer = self.query_selector('div.modal-footer')

        self.close_button = self._modal_header.query_selector(
            'button.btn-close')

        # set events
        self.close_button.events.add(CLICK)

        # setup data
        self.data = {
            'modal_options': {
                'focuse': True,
            },
            'visible': False,
        }

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
