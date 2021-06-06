import time

from behave import fixture
from selenium.webdriver import (
    Remote,
    ChromeOptions,
)

from core.browsers import (
    FIREFOX,
    CHROME,
)
from core.exceptions import DriverSetupException
from core.mobile_emulation import device_iphone8
from core.settings import SELENOID_REMOTE_URL


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(Remote, metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicitly_wait(5)  # default time waiting for a locator


@fixture
def get_driver(context):
    # driver setup start

    browser = context.config.userdata.get('browser')
    vnc = bool(context.config.userdata.get('vnc') == 'true')
    video = bool(context.config.userdata.get('video') == 'true')

    browser_capabilities = None

    if browser == 'chrome':
        chrome_options = ChromeOptions()
        if context.is_mobile:
            chrome_options.add_experimental_option('mobileEmulation', device_iphone8)
        browser_capabilities = chrome_options.to_capabilities()
        browser_capabilities['version'] = CHROME['browserVersion']

    elif browser == 'firefox':
        browser_capabilities = FIREFOX
        if context.is_mobile:
            raise DriverSetupException('Unable to use mobile emulation with Firefox - use Chrome instead')

    if vnc:
        browser_capabilities['enableVNC'] = True
    if video:
        browser_capabilities['enableVideo'] = True
    browser_capabilities['name'] = f'{browser}:{time.ctime()}'

    context.webdriver = Driver(command_executor=SELENOID_REMOTE_URL, desired_capabilities=browser_capabilities)
    context.webdriver.set_window_size(1920, 1080)
    # driver setup end

    yield context.webdriver

    # driver teardown
    try:
        context.webdriver.quit()
    finally:
        context.webdriver.__class__._instances = {}