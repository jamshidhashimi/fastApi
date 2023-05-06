import urllib3
import rich

http = urllib3.PoolManager()
response = http.request('GET', 'https://openlibrary.org/search/authors.json?q=adam%20grant')
result = response.data.decode('utf-8')
rich.print(result)