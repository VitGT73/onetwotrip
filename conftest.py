import pytest
from playwright.sync_api import Page, sync_playwright

from sites.onetwotrip.pages import HomePage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def home_page(chromium_page: Page) -> HomePage:
    return HomePage(chromium_page)


@pytest.fixture(scope='module')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
