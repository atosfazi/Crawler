from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from Helpers.HtmlReader import HtmlReader
from random import randint
from Helpers.DataSaver import DataSaver
from selenium.common.exceptions import WebDriverException


class BooksCrawler(HtmlReader, DataSaver):

    def __init__(self):
        DataSaver.__init__(self)
        HtmlReader.__init__(self)

        self.driver_path = r'C:\Users\karolina.stempien\Documents\_Karolina\studia\Crawler\geckodriver.exe'
        self.domain = "https://lubimyczytac.pl"
        self.page_address = "https://lubimyczytac.pl/katalog?page="
        self.options = Options()
        self.options.page_load_strategy = 'none'
        self.options.add_argument("--headless")
        self.records = []

    def get_books_data(self, start_page, last_page):
        for i in range(start_page, last_page):

            website_address = '{}{}'.format(self.page_address, i)

            html = self.__get_website_html(website_address)

            if not html:
                continue

            book_links = self.get_book_links(html)

            for book_link in book_links:
                book_link = self.domain + book_link

                book_html = self.__get_website_html(book_link)

                if not book_html:
                    continue

                title, author, genre, tags, description = self.get_book_data(book_html)

                record = {'page_nb': i, 'title': title, 'author': author,
                          'genre': genre, 'tags': tags, 'description': description}

                self.records.append(record)

            self.save_data(self.records)
            self.records = []

    def __get_website_html(self, website_address):
        driver = webdriver.Firefox(executable_path=self.driver_path,
                                   options=self.options)

        driver.set_page_load_timeout(8)

        try:
            driver.get(website_address)
            html = driver.page_source
            driver.quit()
            del driver
            return html

        except WebDriverException as e:
            driver.quit()
            del driver
            return None

    @staticmethod
    def __scrapping_delay(min_delay=1, max_delay=3):
        delay = randint(min_delay, max_delay)
        time.sleep(delay)
