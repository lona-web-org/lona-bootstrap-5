lona-bootstrap-5
================

This package contains `Lona <http://lona-web.org>`_ nodes and widgets for
`Bootstrap 5 <https://getbootstrap.com/docs/5.1/getting-started/introduction/>`_.

Supported components:

* `Grid System <#grid-system>`_
* `TextInputs and Textareas <#textinputs-and-textareas>`_
* `Buttons <#buttons>`_
* `Modal <#modal>`_
* `Progress <#progress>`_


Grid System
-----------

Upstream documentation: `Link <https://getbootstrap.com/docs/5.0/layout/grid/>`__

.. code-block:: python

    from lona_bootstrap_5 import ColMd6, Col, Row

    Row(
        ColMd6('foo'),
        ColMd6('bar'),
    )

    Row(
        Col('foo'),
        Col('bar'),
        Col('baz'),
    )


TextInputs and TextAreas
------------------------

Upstream documentation: `Link <https://getbootstrap.com/docs/5.1/forms/overview/>`__

``TextInput`` and ``TextArea`` work exactly like
`Lona TextInputs <https://lona-web.org/end-user-documentation/html.html#textinput-textarea>`__
and are just styled by Bootstrap.


.. code-block:: python

    from lona_bootstrap_5 import TextInput, TextAreas


Buttons
-------

Upstream documentation: `Link <https://getbootstrap.com/docs/5.1/components/buttons/>`__

``Button`` works exactly like
`Lona Button <https://lona-web.org/end-user-documentation/html.html#button>`__
and is just styled by Bootstrap.


.. code-block:: python

    from lona_bootstrap_5 import (
        PrimaryButton,
        SecondaryButton,
        SuccessButton,
        WarningButton,
        DangerButton,
        InfoButton,
        LightButton,
        DarkButton,
        LinkButton,
    )


Modal
-----

Upstream documentation: `Link <https://getbootstrap.com/docs/5.1/components/modal/>`__

.. code-block:: python

    from lona_bootstrap_5 import Modal

    Modal(fade=True, scrollable=False, centered=False)


Properties
~~~~~~~~~~

* ``Modal.fade``: (bool) If ``True`` modal is animated
* ``Modal.centered``: (bool) If ``True`` modal is vertically centred
* ``Modal.scrollable``: (bool) If ``True`` modal is scrollable
* ``Modal.buttons``: (list) Contains all buttons added using ``Modal.set_buttons()``


Methods
~~~~~~~

* ``Modal.show()``: Makes the modal visible (modals are invisible by default)
* ``Modal.hide()``: Makes the modal invisible (modals are invisible by default)
* ``Modal.set_title(*nodes)``: Sets the modal title
* ``Modal.set_body(*nodes)``: Sets the modal body
* ``Modal.set_buttons(*buttons)``: Sets the modal buttons (set buttons are available in ``Modal.buttons``)


Example
~~~~~~~

.. code-block:: python

    from lona_bootstrap_5 import Modal, PrimaryButton
    from lona import LonaView, LonaApp
    from lona.html import HTML, H1

    app = LonaApp(__file__)


    @app.route('/')
    class MyModalView(LonaView):
        def handle_request(self, request):
            modal = Modal()

            html = HTML(
                H1('My Modal'),
                PrimaryButton('Open Modal', _id='open-modal'),
                modal,
            )

            self.show(html)

            # wait for button to be clicked
            self.await_click()

            # button was clicked; show modal
            with html.lock:
                modal.set_title('My Modal')
                modal.set_body('Lorem Ipsum')

                modal.set_buttons(
                    PrimaryButton('Close')
                )

                modal.show()

            self.show(html)

            # wait for modal button to be clicked
            self.await_click(modal.buttons)

            # modal button was clicked; hide modal
            modal.hide()

            return html


    app.run(port=8080)


Progress
--------

Upstream documentation: `Link <https://getbootstrap.com/docs/5.1/components/progress/>`__

.. code-block:: python

    from lona_bootstrap_5 import Progress

    Progress(*label, background=None, value=None, percentage=None,
             striped=False, animated=False)


Properties
~~~~~~~~~~

* ``Modal.background``: (str) [''\|success\|info\|warning\|danger]
* ``Modal.value``: (int) Current progress value between ``0`` and ``100``
* ``Modal.striped``: (bool) Enables Bootstraps ``striped`` style
* ``Modal.animated``: (bool) Enables Bootstrap animations


Methods
~~~~~~~

* ``Modal.set_labal(*nodes)``: Sets label
* ``Modal.set_percentage(percentage)``: Sets the value the given value and calls ``Modal.set_label()``
