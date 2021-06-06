from behave import use_fixture
from core.driver import get_driver


def before_all(context):
    pass


def before_feature(context, feature):
    if feature.name.startswith('Mobile - '):
        context.is_mobile = True
    else:
        context.is_mobile = False


def before_scenario(context, scenario):
    use_fixture(get_driver, context)


def after_scenario(context, scenario):
    pass


def after_featrue(context, feature):
    pass


def after_all(context):
    pass
