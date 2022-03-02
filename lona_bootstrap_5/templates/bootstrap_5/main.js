// setup lona context ---------------------------------------------------------
var lona_context = new Lona.LonaContext({
    target: '#lona',
    title: '{{ settings.BOOTSTRAP_5_TITLE }}',
    update_address_bar: true,
    update_title: true,
    follow_redirects: true,
    follow_http_redirects: true,
});

var _lona_bootstrap = {
    settings: JSON.parse('{{ dumps(settings) }}'),
    disconnected_before: false,
    dots: 0,
};

// alerts ---------------------------------------------------------------------
function show_alert(type, message, timeout) {

    // generate html alert
    var template = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;

    var root = document.createElement('div');

    root.innerHTML = template;

    var alert_node = root.firstElementChild;

    // add alert to message stack
    var message_stack = document.querySelector('#message-stack');

    message_stack.appendChild(alert_node);

    // remove message from message stack
    if(timeout !== undefined && timeout !== null) {
        setTimeout(function() {
            alert_node.remove();
        }, timeout);
    };
};

// connect --------------------------------------------------------------------
lona_context.add_connect_hook(function(lona_context, event) {

    // reconnect message
    if(_lona_bootstrap.disconnected_before) {
        show_alert('success', 'Server reconnected', 3000);
    }

    // navigation
    lona_context.patch_input_events('#navigation');
});

// disconnect -----------------------------------------------------------------
lona_context.add_disconnect_hook(function(lona_context, event) {
    _lona_bootstrap.disconnected_before = true;

    // disable navigation links
    document.querySelectorAll('#navigation a').forEach(function(element) {
        element.onclick = function(event) {
            event.preventDefault();

            show_alert(
                'danger',
                'Server disconnected',
                _lona_bootstrap.settings.BOOTSTRAP_5_ALERT_DEFAULT_TIMEOUT,
            );

            return false;
        };
    });

    // show disconnect message
    if(!_lona_bootstrap.settings.BOOTSTRAP_5_AUTO_RECONNECT) {
        document.querySelector('#lona').innerHTML = `
            <h1>Server disconnected</h1>
        `;

        return;
    }

    // auto reconnect
    document.querySelector('#lona').innerHTML = `
        <h1>Server disconnected</h1>
        Trying to reconnect<span id="dots">${'.'.repeat(_lona_bootstrap.dots)}</span>
    `;

    _lona_bootstrap.dots += 1;

    if(_lona_bootstrap.dots > 3) {
        _lona_bootstrap.dots = 0;
    }

    setTimeout(function() {
        lona_context.setup();
    }, _lona_bootstrap.settings.BOOTSTRAP_5_AUTO_RECONNECT_INTERVAL);
});

// timeouts -------------------------------------------------------------------
lona_context.add_view_timeout_hook(function(lona_context, lona_window) {
    lona_window.set_html('Waiting for server...');
});

lona_context.add_input_event_timeout_hook(function(lona_context, lona_window) {
    show_alert(
        'info',
        'Waiting for server...',
        _lona_bootstrap.settings.BOOTSTRAP_5_ALERT_DEFAULT_TIMEOUT,
    );
});

// custom messages ------------------------------------------------------------
lona_context.add_message_handler(function(lona_context, raw_message) {
    var prefix = 'lona_bootstrap_5:';

    if(!raw_message.startsWith(prefix)) {
        return raw_message;
    };

    try {
      raw_message = raw_message.substring(prefix.length);

      var message = JSON.parse(raw_message);

    } catch {
      return raw_message;

    };

    // alerts
    if(message[0] == 'alert') {
        show_alert(
            message[1],
            message[2],
            message[3],
        );

    // unknown message type
    } else {
        return raw_message;
    };

});

// init -----------------------------------------------------------------------
lona_context.setup();