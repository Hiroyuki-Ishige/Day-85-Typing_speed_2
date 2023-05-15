import requests
import wikipediaapi
import difflib

'''
# basic format to get API
responce = requests.get(url="http://api.open-notify.org/iss-now.json")
responce.raise_for_status()
data = responce.json()
print(data)

# Wikipedia API
https://pypi.org/project/Wikipedia-API/

'''

def get_wiki(words_serch):
    wiki_wiki = wikipediaapi.Wikipedia(
                language="en",
                extract_format=wikipediaapi.ExtractFormat.WIKI)
    p_wiki = wiki_wiki.page(words_serch)
    print(f'Page - Title: {p_wiki.title}')
    print(f'page - Summary: {p_wiki.summary}')
    print(f'type: {type(p_wiki.summary)}')

    w_summary = p_wiki.summary.replace(",", ",\n")
    return w_summary
