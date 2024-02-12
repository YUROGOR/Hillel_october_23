import pytest
from lesson_19.ElementsPage import ElementsPage


class TestElementsPage:

    @pytest.mark.parametrize("element", ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons', 'Links',
                                         'Broken Links - Images', 'Upload and Download', 'Dynamic Properties', '', '',
                                         '', '', '', '', '', '', '', '', '',
                                         '', '', '', '', '', '', '', '', '', '', '', '', ''])
    def test_categories(self, chrome, element):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert element in elements
