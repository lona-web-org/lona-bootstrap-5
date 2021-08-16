from lona.html import (
    TextInput as BaseTextInput,
    TextArea as BaseTextArea,
    Button as BaseButton,
    Div,
)

from .static_files import STATIC_FILES


# inputs ######################################################################
class TextInput(BaseTextInput):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['form-control']


class TextArea(BaseTextArea):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['form-control']


# buttons #####################################################################
class Button(BaseButton):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-primary']


class PrimaryButton(Button):
    pass


class SecondaryButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-secondary']


class SuccessButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-success']


class DangerButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-danger']


class WarningButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-warning']


class InfoButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-info']


class LightButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-light']


class DarkButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-dark']


class LinkButton(Button):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['btn', 'btn-link']


# grid system #################################################################
class Row(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['row']


class Col(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col']


# XS ##################################
class ColXsAuto(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-auto']


class ColXs1(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-1']


class ColXs2(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-2']


class ColXs3(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-3']


class ColXs4(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-4']


class ColXs5(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-5']


class ColXs6(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-6']


class ColXs7(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-7']


class ColXs8(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-8']


class ColXs9(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-9']


class ColXs10(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-10']


class ColXs11(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-11']


class ColXs12(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xs-12']


# SM ##################################
class ColSmAuto(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-auto']


class ColSm1(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-1']


class ColSm2(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-2']


class ColSm3(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-3']


class ColSm4(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-4']


class ColSm5(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-5']


class ColSm6(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-6']


class ColSm7(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-7']


class ColSm8(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-8']


class ColSm9(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-9']


class ColSm10(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-10']


class ColSm11(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-11']


class ColSm12(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-sm-12']


# MD ##################################
class ColMdAuto(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-auto']


class ColMd1(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-1']


class ColMd2(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-2']


class ColMd3(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-3']


class ColMd4(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-4']


class ColMd5(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-5']


class ColMd6(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-6']


class ColMd7(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-7']


class ColMd8(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-8']


class ColMd9(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-9']


class ColMd10(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-10']


class ColMd11(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-11']


class ColMd12(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-md-12']


# LG ##################################
class ColLgAuto(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-auto']


class ColLg1(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-1']


class ColLg2(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-2']


class ColLg3(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-3']


class ColLg4(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-4']


class ColLg5(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-5']


class ColLg6(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-6']


class ColLg7(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-7']


class ColLg8(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-8']


class ColLg9(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-9']


class ColLg10(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-10']


class ColLg11(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-11']


class ColLg12(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-lg-12']


# XL ##################################
class ColXlAuto(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-auto']


class ColXl1(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-1']


class ColXl2(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-2']


class ColXl3(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-3']


class ColXl4(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-4']


class ColXl5(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-5']


class ColXl6(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-6']


class ColXl7(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-7']


class ColXl8(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-8']


class ColXl9(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-9']


class ColXl10(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-10']


class ColXl11(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-11']


class ColXl12(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xl-12']


# XXL #################################
class ColXxlAuto(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-auto']


class ColXxl1(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-1']


class ColXxl2(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-2']


class ColXxl3(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-3']


class ColXxl4(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-4']


class ColXxl5(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-5']


class ColXxl6(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-6']


class ColXxl7(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-7']


class ColXxl8(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-8']


class ColXxl9(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-9']


class ColXxl10(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-10']


class ColXxl11(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-11']


class ColXxl12(Div):
    STATIC_FILES = STATIC_FILES
    CLASS_LIST = ['col-xxl-12']
