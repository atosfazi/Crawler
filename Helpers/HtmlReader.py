from bs4 import BeautifulSoup
import re


class HtmlReader:

    def get_book_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        links = []

        for link in soup.findAll('a'):
            link = link.get('href')
            if link:
                if self.__is_book_link(link):
                    links.append(link)
        return links

    def get_book_data(self, book_html):
        soup = BeautifulSoup(book_html, "html.parser")
        title = soup.find('h1', class_='book__title').text.strip()
        author = soup.find(class_='link-name')
        if author is not None:
            author = author.text.strip()
        genre = soup.find(class_="book__category d-sm-block d-none").text.strip()
        tags = soup.find_all(class_="btn btn-outline-primary tag mt-2 mb-0")
        tags = [tag.text.strip() for tag in tags]
        tags = ' '.join(tags)
        description = soup.find(class_="collapse-content")
        if description is not None:
            description = description.text.strip()
        return title, author, genre, tags, description

    @staticmethod
    def __is_book_link(link):
        regex = r"(\/ksiazka\/\d+)"
        return bool(re.search(regex, link))
