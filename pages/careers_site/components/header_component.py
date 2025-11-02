from playwright.sync_api import Page


class CareersHeader:
    """Header for https://careers.trgint.com/"""

    def __init__(self, page: Page):
        self.page = page

    def click_life_at_trg(self):
        self.page.get_by_role("link", name="Life at TRG", exact=True).click()
