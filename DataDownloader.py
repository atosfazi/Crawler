from Core.BooksCrawler import BooksCrawler


crawler = BooksCrawler()


if __name__ == "__main__":
    crawler.get_books_data(start_page=0, last_page=10)