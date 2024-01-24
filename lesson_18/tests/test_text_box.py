from lesson_18.TextBoxPage import TextBoxPage
import time


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Yurii")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Yurii"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_name_field("test@ukr.net")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_email()
        assert name_field.replace("Email:", "") == "test@ukr.net"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_text_area_field("Hello!")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_current_address()
        assert name_field.replace("Current Address :", "") == "Hello!"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_text_area_field("Hello world!")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_permanent_address()
        assert name_field.replace("Permananet Address :", "") == "Hello world!"
