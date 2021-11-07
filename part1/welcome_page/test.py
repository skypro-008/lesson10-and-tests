import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup


BASENAME = 'lesson10-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class WelcomeTestCase(SkyproTestCase):
    def setUp(self):
        with open("welcome_page.html", 'r') as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Skyprogram',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")

    def test_image(self):
        image = self.main.img
        self.assertIsNotNone(
            image,
            "%@Проверьте, что добавили картинку.")
         
        attributes=image.attrs
        width = attributes.get('width')
        self.assertIsNotNone(
            width,
            "%@Проверьте, что тэг img имеет аттрибут 'width'")
        
        self.assertEqual(
            width, '300',
            "%@Проверьте, что аттрибуту width присвоено значение 300")
        
    def test_paragraph(self):
        paragraph = self.main.p
        self.assertIsNotNone(
            paragraph,
            "%@Проверьте, что добавили тег 'параграф'")
        self.assertEqual(
            paragraph.text, 'У нас тут фоточки и уютно. Смотрите чужие, постите свои.',
            "%@Проверьте что в теле тега <p> содержится правильный текст'"
        )

    def test_ref(self):
        ref1 = self.main.a
        self.assertIsNotNone(
            ref1,
            "%@Проверьте, что добавили ссылки")
        refs = self.main.find_all('a')
        refs_text = [text.text for text in refs]
        search = ['Вход', 'Регистрация']
        for element in search:
            self.assertIn(
                element, refs_text,
                f"%@Проверьте, что одна из ссылок имеет значение {element}"
            )
        refs_attr = [attr.attrs for attr in refs]
        for attr in refs_attr:
            href = attr.get('href')
            self.assertIsNotNone(
                href, "%@Проверьте, что Ваши ссылки имеют аттрибут 'href'"
            )
            self.assertEqual(
                href, '#', 
                "%@Проверьте что аттрибуту href в ссылке присвоено значение заглушки '#'"
                )

    def test_has_hr(self):
        hr = self.main.hr
        self.assertIsNotNone(
            hr, "%@ Проверьте, что не забыли про разделитель"
        )

if __name__ == "__main__":
    unittest.main()