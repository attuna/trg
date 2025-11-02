from pages.base_page import BasePage


class LifeAtTrgPage(BasePage):
    POSTERS_LOCATOR = "img[alt^='Poster']"

    def extract_core_values(self):
        posters = self.page.locator(self.POSTERS_LOCATOR)
        count = posters.count()

        data = []
        for i in range(count):
            img = posters.nth(i)
            headline = img.locator("xpath=following::h5").first.text_content(timeout=5000).strip()
            description = img.locator("xpath=following::p").first.text_content(timeout=5000).strip()
            img_url = img.get_attribute("src")

            data.append({"headline": headline, "description": description, "image_url": img_url})
        return data
