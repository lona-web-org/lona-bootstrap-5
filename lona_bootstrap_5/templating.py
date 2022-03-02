from __future__ import annotations

from dataclasses import dataclass

DEFAULTS = {
    # styling
    'BOOTSTRAP_5_PAGE_WIDTH': '',
    'BOOTSTRAP_5_TITLE': 'Lona',
    'BOOTSTRAP_5_ICON': '',
    'BOOTSTRAP_5_VERSION_STRING': '',
    'BOOTSTRAP_5_DARK_NAVIGATION': True,
    'BOOTSTRAP_5_DARK_PAGE': False,

    # frontend features
    'BOOTSTRAP_5_AUTO_RECONNECT': True,
    'BOOTSTRAP_5_AUTO_RECONNECT_INTERVAL': 1000,
    'BOOTSTRAP_5_ALERT_DEFAULT_TIMEOUT': 3000,

    # sidebar
    'BOOTSTRAP_5_SIDEBAR_WIDTH': '280px',
}


@dataclass
class MenuItem:
    title: str = ''
    url: str = ''
    route_name: str = ''
    route_args: dict | None = None
    icon: str = ''
    divider: bool = False


def get_settings(lona):
    settings = {}

    for name, default_value in DEFAULTS.items():
        value = lona.server.settings.get(name, default_value)
        settings[name] = value

    return settings


def get_menu(lona):
    return lona.server.settings.get('BOOTSTRAP_5_MENU', [])
