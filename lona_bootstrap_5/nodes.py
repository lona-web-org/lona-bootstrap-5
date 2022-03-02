from lona.html import (
    NumberInput as BaseNumberInput,
    TextInput as BaseTextInput,
    TextArea as BaseTextArea,
    Button as BaseButton,
    Select as BaseSelect,
    Div as BaseDiv,
    Span,
)

from .static_files import STATIC_FILES


class BootstrapDiv(BaseDiv):
    STATIC_FILES = STATIC_FILES


# Grow Spinners
class GrowPrimarySpinner(BootstrapDiv):
    CLASS_LIST = ['spinner-grow', 'text-primary']

    def __init__(self, *args, **kwargs):
        hidden_text = 'Loading...'
        if len(args) > 0:
            hidden_text = args[0]
        super().__init__(*args, **kwargs)

        self.nodes = [
            BootstrapDiv(
                Span(hidden_text, _class='visually-hidden'),
                _role='status',
            )
        ]


class GrowSecondarySpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-secondary']


class GrowSuccessSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-success']


class GrowDangerSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-danger']


class GrowWarningSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-warning']


class GrowInfoSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-info']


class GrowLightSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-light']


class GrowDarkSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-grow', 'text-dark']


# Border Spinners
class BorderPrimarySpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-primary']


class BorderSecondarySpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-secondary']


class BorderSuccessSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-success']


class BorderDangerSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-danger']


class BorderWarningSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-warning']


class BorderInfoSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-info']


class BorderLightSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-light']


class BorderDarkSpinner(GrowPrimarySpinner):
    CLASS_LIST = ['spinner-border', 'text-dark']


# Badges
class PrimaryBadge(Span):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['badge', 'bg-primary']


class SecondaryBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-secondary']


class SuccessBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-success']


class DangerBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-danger']


class WarningBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-warning']


class InfoBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-info']


class LightBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-light']


class DarkBadge(PrimaryBadge):
    CLASS_LIST = ['badge', 'bg-dark']


# Alerts
class PrimaryAlert(BootstrapDiv):
    CLASS_LIST = ['alert', 'alert-primary']
    ATTRIBUTES = {'role': 'alert'}


class SecondaryAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-secondary']


class SuccessAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-success']


class DangerAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-danger']


class WarningAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-warning']


class InfoAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-info']


class LightAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-light']


class DarkAlert(PrimaryAlert):
    CLASS_LIST = ['alert', 'alert-dark']


# inputs ######################################################################
class TextInput(BaseTextInput):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['form-control']


class NumberInput(BaseNumberInput):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['form-control']


class TextArea(BaseTextArea):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['form-control']


class Select(BaseSelect):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['form-select']


# buttons #####################################################################
class Button(BaseButton):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-primary']


class PrimaryButton(Button):
    pass


class SecondaryButton(Button):
    CLASS_LIST = ['btn', 'btn-secondary']


class SuccessButton(Button):
    CLASS_LIST = ['btn', 'btn-success']


class DangerButton(Button):
    CLASS_LIST = ['btn', 'btn-danger']


class WarningButton(Button):
    CLASS_LIST = ['btn', 'btn-warning']


class InfoButton(Button):
    CLASS_LIST = ['btn', 'btn-info']


class LightButton(Button):
    CLASS_LIST = ['btn', 'btn-light']


class DarkButton(Button):
    CLASS_LIST = ['btn', 'btn-dark']


class LinkButton(Button):
    CLASS_LIST = ['btn', 'btn-link']


# grid system #################################################################
class Row(BootstrapDiv):
    CLASS_LIST = ['row']


class Col(BootstrapDiv):
    CLASS_LIST = ['col']


# XS ##################################
class ColXsAuto(BootstrapDiv):
    CLASS_LIST = ['col-xs-auto']


class ColXs1(BootstrapDiv):
    CLASS_LIST = ['col-xs-1']


class ColXs2(BootstrapDiv):
    CLASS_LIST = ['col-xs-2']


class ColXs3(BootstrapDiv):
    CLASS_LIST = ['col-xs-3']


class ColXs4(BootstrapDiv):
    CLASS_LIST = ['col-xs-4']


class ColXs5(BootstrapDiv):
    CLASS_LIST = ['col-xs-5']


class ColXs6(BootstrapDiv):
    CLASS_LIST = ['col-xs-6']


class ColXs7(BootstrapDiv):
    CLASS_LIST = ['col-xs-7']


class ColXs8(BootstrapDiv):
    CLASS_LIST = ['col-xs-8']


class ColXs9(BootstrapDiv):
    CLASS_LIST = ['col-xs-9']


class ColXs10(BootstrapDiv):
    CLASS_LIST = ['col-xs-10']


class ColXs11(BootstrapDiv):
    CLASS_LIST = ['col-xs-11']


class ColXs12(BootstrapDiv):
    CLASS_LIST = ['col-xs-12']


# SM ##################################
class ColSmAuto(BootstrapDiv):
    CLASS_LIST = ['col-sm-auto']


class ColSm1(BootstrapDiv):
    CLASS_LIST = ['col-sm-1']


class ColSm2(BootstrapDiv):
    CLASS_LIST = ['col-sm-2']


class ColSm3(BootstrapDiv):
    CLASS_LIST = ['col-sm-3']


class ColSm4(BootstrapDiv):
    CLASS_LIST = ['col-sm-4']


class ColSm5(BootstrapDiv):
    CLASS_LIST = ['col-sm-5']


class ColSm6(BootstrapDiv):
    CLASS_LIST = ['col-sm-6']


class ColSm7(BootstrapDiv):
    CLASS_LIST = ['col-sm-7']


class ColSm8(BootstrapDiv):
    CLASS_LIST = ['col-sm-8']


class ColSm9(BootstrapDiv):
    CLASS_LIST = ['col-sm-9']


class ColSm10(BootstrapDiv):
    CLASS_LIST = ['col-sm-10']


class ColSm11(BootstrapDiv):
    CLASS_LIST = ['col-sm-11']


class ColSm12(BootstrapDiv):
    CLASS_LIST = ['col-sm-12']


# MD ##################################
class ColMdAuto(BootstrapDiv):
    CLASS_LIST = ['col-md-auto']


class ColMd1(BootstrapDiv):
    CLASS_LIST = ['col-md-1']


class ColMd2(BootstrapDiv):
    CLASS_LIST = ['col-md-2']


class ColMd3(BootstrapDiv):
    CLASS_LIST = ['col-md-3']


class ColMd4(BootstrapDiv):
    CLASS_LIST = ['col-md-4']


class ColMd5(BootstrapDiv):
    CLASS_LIST = ['col-md-5']


class ColMd6(BootstrapDiv):
    CLASS_LIST = ['col-md-6']


class ColMd7(BootstrapDiv):
    CLASS_LIST = ['col-md-7']


class ColMd8(BootstrapDiv):
    CLASS_LIST = ['col-md-8']


class ColMd9(BootstrapDiv):
    CLASS_LIST = ['col-md-9']


class ColMd10(BootstrapDiv):
    CLASS_LIST = ['col-md-10']


class ColMd11(BootstrapDiv):
    CLASS_LIST = ['col-md-11']


class ColMd12(BootstrapDiv):
    CLASS_LIST = ['col-md-12']


# LG ##################################
class ColLgAuto(BootstrapDiv):
    CLASS_LIST = ['col-lg-auto']


class ColLg1(BootstrapDiv):
    CLASS_LIST = ['col-lg-1']


class ColLg2(BootstrapDiv):
    CLASS_LIST = ['col-lg-2']


class ColLg3(BootstrapDiv):
    CLASS_LIST = ['col-lg-3']


class ColLg4(BootstrapDiv):
    CLASS_LIST = ['col-lg-4']


class ColLg5(BootstrapDiv):
    CLASS_LIST = ['col-lg-5']


class ColLg6(BootstrapDiv):
    CLASS_LIST = ['col-lg-6']


class ColLg7(BootstrapDiv):
    CLASS_LIST = ['col-lg-7']


class ColLg8(BootstrapDiv):
    CLASS_LIST = ['col-lg-8']


class ColLg9(BootstrapDiv):
    CLASS_LIST = ['col-lg-9']


class ColLg10(BootstrapDiv):
    CLASS_LIST = ['col-lg-10']


class ColLg11(BootstrapDiv):
    CLASS_LIST = ['col-lg-11']


class ColLg12(BootstrapDiv):
    CLASS_LIST = ['col-lg-12']


# XL ##################################
class ColXlAuto(BootstrapDiv):
    CLASS_LIST = ['col-xl-auto']


class ColXl1(BootstrapDiv):
    CLASS_LIST = ['col-xl-1']


class ColXl2(BootstrapDiv):
    CLASS_LIST = ['col-xl-2']


class ColXl3(BootstrapDiv):
    CLASS_LIST = ['col-xl-3']


class ColXl4(BootstrapDiv):
    CLASS_LIST = ['col-xl-4']


class ColXl5(BootstrapDiv):
    CLASS_LIST = ['col-xl-5']


class ColXl6(BootstrapDiv):
    CLASS_LIST = ['col-xl-6']


class ColXl7(BootstrapDiv):
    CLASS_LIST = ['col-xl-7']


class ColXl8(BootstrapDiv):
    CLASS_LIST = ['col-xl-8']


class ColXl9(BootstrapDiv):
    CLASS_LIST = ['col-xl-9']


class ColXl10(BootstrapDiv):
    CLASS_LIST = ['col-xl-10']


class ColXl11(BootstrapDiv):
    CLASS_LIST = ['col-xl-11']


class ColXl12(BootstrapDiv):
    CLASS_LIST = ['col-xl-12']


# XXL #################################
class ColXxlAuto(BootstrapDiv):
    CLASS_LIST = ['col-xxl-auto']


class ColXxl1(BootstrapDiv):
    CLASS_LIST = ['col-xxl-1']


class ColXxl2(BootstrapDiv):
    CLASS_LIST = ['col-xxl-2']


class ColXxl3(BootstrapDiv):
    CLASS_LIST = ['col-xxl-3']


class ColXxl4(BootstrapDiv):
    CLASS_LIST = ['col-xxl-4']


class ColXxl5(BootstrapDiv):
    CLASS_LIST = ['col-xxl-5']


class ColXxl6(BootstrapDiv):
    CLASS_LIST = ['col-xxl-6']


class ColXxl7(BootstrapDiv):
    CLASS_LIST = ['col-xxl-7']


class ColXxl8(BootstrapDiv):
    CLASS_LIST = ['col-xxl-8']


class ColXxl9(BootstrapDiv):
    CLASS_LIST = ['col-xxl-9']


class ColXxl10(BootstrapDiv):
    CLASS_LIST = ['col-xxl-10']


class ColXxl11(BootstrapDiv):
    CLASS_LIST = ['col-xxl-11']


class ColXxl12(BootstrapDiv):
    CLASS_LIST = ['col-xxl-12']
