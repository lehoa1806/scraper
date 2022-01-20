from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from utils.decorators.do_and_sleep import do_and_sleep

from scraper.common import wait_for_change


class Button:
    def __init__(self, element: WebElement) -> None:
        self.html = element

    @do_and_sleep(level=1)
    def click(self) -> None:
        self.html.click()

    def click_and_wait(self) -> None:
        with wait_for_change(self.html):
            self.html.click()

    @classmethod
    def load_button_by_css_selector(
        cls,
        parent: Union[WebDriver, WebElement],
        css_selector: str,
    ) -> 'Button':
        """
        Locate a button element by css selector.
          dropdown = Button.load_dropdown_by_css_selector('#foo')
        :param parent: a webdriver or the parent web element
        :param css_selector: CSS selector string, ex: '#button'
        :return: WebElement - the button if it was found
        """
        return cls(parent.find_element_by_css_selector(css_selector))
