from lona.static_files import StyleSheet, Script, SORT_ORDER


STATIC_FILES = [
    # css files
    StyleSheet(
        name='bootstrap.css',
        path='static/bootstrap-5.1.0-dist/css/bootstrap.min.css',
        url='bootstrap.min.css',
        sort_order=SORT_ORDER.FRAMEWORK,
    ),
    StyleSheet(
        name='bootstrap.min.css.map',
        path='static/bootstrap-5.1.0-dist/css/bootstrap.min.css.map',
        url='bootstrap.min.css.map',
        sort_order=SORT_ORDER.FRAMEWORK,
        link=False,
    ),

    # js files
    Script(
        name='bootstrap.bundle.min.js',
        path='static/bootstrap-5.1.0-dist/js/bootstrap.bundle.min.js',
        url='bootstrap.bundle.min.js',
        sort_order=SORT_ORDER.FRAMEWORK,
    ),
    Script(
        name='bootstrap.bundle.js',
        path='static/bootstrap-5.1.0-dist/js/bootstrap.bundle.min.js.map',
        url='bootstrap.bundle.min.js.map',
        sort_order=SORT_ORDER.FRAMEWORK,
        link=False,
    ),

    # widgets
    Script(
        name='lona_bootstrap5.widgets',
        path='static/bootstrap5-widgets.js',
        url='bootstrap-widgets.js',
        sort_order=SORT_ORDER.LIBRARY,
    ),
]