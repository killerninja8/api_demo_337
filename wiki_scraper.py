# File: wiki_scraper.py
import wikipedia
import wptools
import pandas as pd

def get_wiki_search(company):
    return [{'company': wikipedia.search(company)}]

def print_wiki_search(wiki_search):
    for index, company in enumerate(wiki_search):
        for i, j in company.items():
            print('{}. {} :\n{}'.format(index + 1, i, ', '.join(j)))
            print('\n')

def scrape_wiki_data(companies, features):
    wiki_data = []

    for company in companies:
        page = wptools.page(company)  # create a page object
        try:
            page.get_parse()  # call the API and parse the data
            if page.data['infobox'] is not None:
                # if infobox is present
                infobox = page.data['infobox']
                # get data for the interested features/attributes
                data = {feature: infobox[feature] if feature in infobox else ''
                        for feature in features}
            else:
                data = {feature: '' for feature in features}

            data['company_name'] = company
            wiki_data.append(data)

        except KeyError:
            pass

    return pd.DataFrame(wiki_data).replace('{{|}}', '', regex=True).replace('nowrapl', '').T
