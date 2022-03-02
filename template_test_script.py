from lona.html import HTML, H1, H2
from lona import LonaApp, LonaView

from lona_bootstrap_5 import (
    TEMPLATE_DIR,
    PrimaryButton,
    MenuItem,
    show_alert,
    Select,
    TextInput,
    NumberInput,
)

app = LonaApp(__file__)


app.settings.TEMPLATE_DIRS = [
    TEMPLATE_DIR,
]

app.settings.FRONTEND_TEMPLATE = 'bootstrap_5/sidebar_left.html'
app.settings.BOOTSTRAP_5_TITLE = 'My Fancy Script'
app.settings.BOOTSTRAP_5_VERSION_STRING = 'v0.1'
app.settings.BOOTSTRAP_5_DARK_NAVIGATION = True

app.settings.BOOTSTRAP_5_MENU = [
    MenuItem(
        title='Home',
        url='/',
    ),
    MenuItem(
        title='Foo',
        route_name='print',
        route_args={'word': 'foo'},
    ),
    MenuItem(
        title='Bar',
        route_name='print',
        route_args={'word': 'bar'},
    ),
]


@app.route('/')
class IndexView(LonaView):
    def handle_request(self, request):
        alert_type = Select(
            values=[
                ('info', 'Info'),
                ('success', 'Success'),
                ('warning', 'Warning'),
                ('danger', 'Danger'),
            ],
        )

        alert_text = TextInput(value='Test Alert')
        alert_timeout = NumberInput(value=3000)

        html = HTML(
            H1('Lona Bootstrap 5'),
            H2('Show Alert'),
            alert_type,
            alert_timeout,
            alert_text,
            PrimaryButton('Send'),
        )

        while True:
            self.await_click(html=html)

            show_alert(
                lona_view=self,
                type=alert_type.value,
                text=alert_text.value,
                timeout=alert_timeout.value,
            )


@app.route('/print/<word>', name='print')
class PrintView(LonaView):
    def handle_request(self, request):
        return request.match_info['word']


app.run()
