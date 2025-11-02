from pages.base_page import BasePage


class LifeAtTrgPage(BasePage):
    POSTERS_LOCATOR = "img[alt^='Poster']"


    def scroll_to_core_values(self):
        self.page.wait_for_selector("ul li", state="attached", timeout=8000)
        self.page.wait_for_timeout(1000) #I've tried to get rid of wix autoscroll, no success
        element = self.page.locator(f"text=Whatever it takes!")
        element.scroll_into_view_if_needed()
        element.wait_for(state="visible")

    def extract_core_values(self):
        posters = self.page.locator(self.POSTERS_LOCATOR)
        count = posters.count()

        data = []
        for i in range(count):
            img = posters.nth(i)
            headline_locator = img.locator("xpath=following::h5[1]")
            description_locator = img.locator("xpath=following::p[1]")

            headline = headline_locator.text_content(timeout=5000).strip()
            description = description_locator.text_content(timeout=5000).strip()

            img_url = img.get_attribute("src")
            data.append({"headline": headline, "description": description, "image_url": img_url})
        return data
