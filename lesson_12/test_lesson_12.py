import pytest


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    # перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
    # перевірити чи є ключ "value"  і перевірити його значення - 2 теста

    def test_check_icon_url(self):
        assert self.response.json()["icon_url"] != ""

    def test_check_icon_url_picture(self):
        assert self.response.json()["icon_url"][-3:] == "png"

    def test_check_value(self):
        assert self.response.json().get("value")

    def test_check_in_value(self):
        assert len(self.response.json()["value"]) > 20


@pytest.mark.usefixtures("fixture_query")
class TestRandom2:
    # Зробити окремий клас
    # пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
    # зробити класому фікстуру
    # тест на статус код
    # тест на кількість жартів
    # тест на сам жарт
    # + 3 тести

    def test_status_code(self):
        assert self.status_code == 200

    def test_check_total_jokes(self):
        assert self.response.json()["total"] == 148

    def test_check_jokes_value(self):
        result = self.response.json()['result']
        for element in result:
            result2 = element.get('value')
            assert len(result2) > 20
