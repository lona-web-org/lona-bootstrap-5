from lona_bootstrap_5 import (
    ColMd6,
    Col,
    Row,
    TextInput,
    TextArea,
    PrimaryButton,
    SecondaryButton,
    SuccessButton,
    WarningButton,
    DangerButton,
    InfoButton,
    LightButton,
    DarkButton,
    LinkButton,
    Progress,
    Modal,
)

from lona import LonaApp, LonaView
from lona.html import H1, H2, HTML

app = LonaApp(__file__)

app.add_static_file('lona/style.css', """
#lona {
    max-width: 60em;
    margin: 0 auto;
}
""")


@app.route('/')
class MyView(LonaView):
    def handle_request(self, request):
        # modal
        self.modal_trigger = PrimaryButton('Show Modal', _id='show-modal')
        self.modal = Modal()

        html = HTML(
            H1('Bootstrap 5'),

            # grid system
            H2('Grid System'),
            Row(
                ColMd6('foo'),
                ColMd6('bar'),
            ),
            Row(
                Col('foo'),
                Col('bar'),
                Col('baz'),
            ),

            # inputs
            H2('Inputs'),
            TextInput(),
            TextArea(),

            # Buttons
            H2('Buttons'),
            PrimaryButton('PrimaryButton'),
            SecondaryButton('SecondaryButton'),
            SuccessButton('SuccessButton'),
            WarningButton('WarningButton'),
            DangerButton('DangerButton'),
            InfoButton('InfoButton'),
            LightButton('LightButton'),
            DarkButton('DarkButton'),
            LinkButton('LinkButton'),

            # Modal
            H2('Modal'),
            self.modal_trigger,
            self.modal,

            # Progress
            H2('Progress'),
            Progress(percentage=35, background='success'),
        )

        while True:
            self.show(html)

            input_event = self.await_input_event()

            # modal
            if input_event.node is self.modal_trigger:
                with html.lock:
                    self.modal.set_title('Test Title')
                    self.modal.set_body('Test Body')

                    self.modal.set_buttons(
                        PrimaryButton('PrimaryButton', _id='primary'),
                        SecondaryButton('SecondaryButton', _id='secondary'),
                    )
                    self.modal.show()

            elif input_event.node is self.modal.close_button:
                print('modal close button clicked')

                self.modal.hide()

            elif input_event.node in self.modal.buttons:
                print(input_event.node, 'was clicked')

                self.modal.hide()


app.run(port=8080)
