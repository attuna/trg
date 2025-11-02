from pages.careers_site.components.header_component import CareersHeader
from pages.careers_site.life_at_trg_page import LifeAtTrgPage
from pages.main_site.home_page import HomePage
from utils.file_utils import download_images_named_by_headline, save_json
from utils.text_utils import count_exclamation_marks


def test_core_values_extraction(page):
    home_page = HomePage(page)
    careers_header = CareersHeader(page)
    life_at_trg_page = LifeAtTrgPage(page)

    home_page.open_homepage()
    home_page.header.click_careers()
    careers_header.click_life_at_trg()

    life_at_trg_page.scroll_to_core_values()
    core_values = life_at_trg_page.extract_core_values()
    save_json(core_values)
    download_images_named_by_headline(core_values)

    exclamations = count_exclamation_marks(core_values)
    print(f"Found {exclamations} exclamation marks across core values")

    assert len(core_values) == 4
