from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = '/wiki/Special:Random'
target_page = '/wiki/Philosophy'
first_link_only = True

def get_first_link(first_link_only):
    html = urlopen('https://en.wikipedia.org{}'.format(page)).read()
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find('div', {'id': 'bodyContent'}).findAll('p')
    if page == '/wiki/Special:Random':
        print(str(soup.title.string))
    for paragraph in paragraphs:
        # outside_parenthesis = ''
        # for q in [p.split(')')[-1] for p in paragraph.split('(')]:
            # outside_parenthesis += q
        # for link in outside_parenthesis.findAll(
        for link in paragraph.findAll(
                'a', href=re.compile('^(/wiki/)((?!:).)*$')):
            if 'href' in link.attrs:
                first_link = link.attrs['href']
                if first_link in bread_crumbs:
                    if first_link_only:
                        print('\n!!! infinite loop!')
                        return None
                    else:
                        continue
                return first_link

if __name__ == '__main__':
    bread_crumbs = []
    count = 0
    while page != target_page:
        if page != '/wiki/Special:Random':
            print(page, flush=True)
        if page == None:
            print('\n!!! no more links')
            break
        bread_crumbs.append(page)
        page = get_first_link(first_link_only)
        count += 1
    print('\n{}{} in {}'.format(
        '!!! ' if page != target_page else '', page, count))
