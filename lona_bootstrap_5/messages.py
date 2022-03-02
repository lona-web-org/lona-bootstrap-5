from lona._json import dumps


def show_alert(
        lona_view,
        text,
        type='info',
        timeout=None,
        broadcast=False,
        filter_connections=lambda connection: True,
        wait=True,
):

    string = 'lona_bootstrap_5:' + dumps(['alert', type, text, timeout])

    return lona_view.send_str(
        string=string,
        broadcast=broadcast,
        filter_connections=filter_connections,
        wait=wait,
    )
