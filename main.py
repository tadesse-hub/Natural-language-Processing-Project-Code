import requests

from bs4 import BeautifulSoup


def get_bible_books():
    main_url = "https://www.ethiopicbible.com/amharic-bible-books"
    get_books = requests.get(main_url)
    if get_books.status_code == 200:
        book_lists = get_books.content
        soup = BeautifulSoup(
            book_lists, 'html5lib')
        li = soup.select("ol > li > a")
        books_of_bible = []
        for link in li:
            books_of_bible.append(link.get('href'))
        print("We have found " + str(len(books_of_bible)) + " books of bible")
        return books_of_bible


def content_crawl():
    books = get_bible_books()
    for item in books:
        book_iterator = 1
        while book_iterator < 151:
            print('https://www.ethiopicbible.com/' + item + "-" + str(book_iterator))
            get_content = requests.get('https://www.ethiopicbible.com/' + item + "-" + str(book_iterator))
            if get_content.status_code == 200:
                book_content = get_content.content
                soup2 = BeautifulSoup(book_content, 'html5lib')

                amharic_content = soup2.findAll("div", {"class": "amharicBibleChapterContainer"}) or None
                geez_content = soup2.findAll("div", {"class": "geezBibleChapterContainer"}) or None
                english_content = soup2.findAll("div", {"class": "kjvBibleChapterContainer"}) or None

                if amharic_content:
                    amharic_book = open("amharic/" + item + "-" + str(book_iterator) + ".txt", "w+")
                    amharic_table = amharic_content[0].find('table').find_all('tr')
                    for each in amharic_table:
                        amharic_verse = each.text
                        amharic_verse = amharic_verse.replace('\n', ' ')
                        amharic_book.write(amharic_verse.strip() + "\n")
                        print(amharic_verse)
                if geez_content:
                    geez_book = open("geez/" + item + "-" + str(book_iterator) + ".txt", "w+")
                    geez_table = geez_content[0].find('table').find_all('tr')
                    for each in geez_table:
                        geez_verse = each.text
                        geez_verse = geez_verse.replace('\n', ' ')
                        geez_book.write(geez_verse.strip() + "\n")
                        print(geez_verse)
                if english_content:
                    english_book = open("english/" + item + "-" + str(book_iterator) + ".txt", "w+")
                    english_table = english_content[0].find('table').find_all('tr')
                    for each in english_table:
                        english_verse = each.text
                        english_verse = english_verse.replace('\n', ' ')
                        english_book.write(english_verse.strip() + "\n")
                        print(english_verse)
                else:
                    print("false")
                    break
            book_iterator += 1


if __name__ == '__main__':
    print(content_crawl())
