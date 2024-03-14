import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog


f = open('files/catalog.json')
data_json = json.load(f)

books = []
magazines = []
dvds = []
cds = []

for item in data_json:
    if item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                upc=item['upc'],
                subject=item['subject'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            Magazine(
                title=item['title'],
                upc=item['upc'],
                subject=item['subject'],
                volume=item['volume'],
                issue=item['issue']
            )
        )
    elif item['source'] == 'dvd':
        dvds.append(
            Dvd(
                title=item['title'],
                upc=item['upc'],
                subject=item['subject'],
                actors=item['actors'],
                genre=item['genre'],
                directors=['directors']
            )
        )
    elif item['source'] == 'cd':
        cds.append(
            Cd(
                title=item['title'],
                upc=item['upc'],
                subject=item['subject'],
                artist=item['artist']
            )
        )

catalog_all = [books, magazines, dvds, cds]
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'Result ke-{index+1} | {result}')

# print(books)
# print(magazines)
# print(dvds)
# print(cds)
