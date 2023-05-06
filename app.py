import urllib3
import rich

resp = urllib3.request('GET', 'https://openlibrary.org/search/authors.json?q=adam grant')
result = resp.json()
rich.print(result)