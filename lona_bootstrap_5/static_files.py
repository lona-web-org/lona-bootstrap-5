from lona.static_files import StyleSheet, Script, SORT_ORDER


STATIC_FILES = [
    # css files
    StyleSheet(
        name='bootstrap5.css',
        path='static/bootstrap-5.1.0-dist/css/bootstrap.min.css',
        url='bootstrap5.min.css',
        sort_order=SORT_ORDER.FRAMEWORK,
    ),
    StyleSheet(
        name='bootstrap5.css',
        path='static/bootstrap-5.1.0-dist/css/bootstrap.min.css',
        url='bootstrap5.min.css.map',
        sort_order=SORT_ORDER.FRAMEWORK,
        link=False,
    ),

    # js files
    Script(
        name='bootstrap5.bundle.js',
        path='static/bootstrap-5.1.0-dist/js/bootstrap.bundle.min.js',
        url='bootstrap5.bundle.min.js',
        sort_order=SORT_ORDER.FRAMEWORK,
    ),
    Script(
        name='bootstrap5.bundle.js',
        path='static/bootstrap-5.1.0-dist/js/bootstrap.bundle.min.js.map',
        url='bootstrap5.bundle.min.js.map',
        sort_order=SORT_ORDER.FRAMEWORK,
        link=False,
    ),

    # widgets
    Script(
        name='lona_bootstrap5.widgets',
        path='bootstrap5-widgets.js',
        url='bootstrap5-widgets.js',
        sort_order=SORT_ORDER.LIBRARY,
    ),
]