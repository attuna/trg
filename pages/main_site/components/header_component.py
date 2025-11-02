from playwright.sync_api import Page


class MainHeader:
    """Header for https://www.trgint.com/"""

    def __init__(self, page: Page):
        self.page = page

    def click_careers(self):
        self.page.get_by_role("link", name="Careers", exact=True).click()
