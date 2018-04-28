import googleapiclient.discovery
import base64
import nltk
import requests
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from itertools import product
from bs4 import BeautifulSoup
# from google_images_download import google_images_download   # importing the library
import pythonImageSearch
nltk.download('wordnet')
nltk.download('punkt')


USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


def ocr(photo_file):
    # [START authenticate]
    service = googleapiclient.discovery.build('vision', 'v1')
    # [END authenticate]
    # [START construct_request]
    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'DOCUMENT_TEXT_DETECTION',
                    'maxResults': 5
                }]
            }]
        })
    # [END construct_request]
    # [START parse_response]
    response = service_request.execute()
    return response


def word_analysis(word):
    arabList = ['Hommus', 'Baba ghannuge', 'Koosa bil tahine', 'Baba', 'ghannuge', 'Koossa', 'bil', 'tahine', 'Halloum', 'meshouse']
    if word in arabList:
        return True
    else:
        return False


    # data = []
    # menu_word = word + 'Description'
    # try:
    #     results = scrape_google(menu_word, 1, "en")
    #     for result in results:
    #         data.append(result)
    # except Exception as e:
    #     print(e)
    # finally:
    #     time.sleep(10)
    # # (data)
    #
    # dataDescription = ""
    # # arabList = ['Arab', 'Arabic', 'Levant', 'MiddleEast', 'NorthAfrica', 'Levantese', 'Taboula', 'Middle East', 'Tunisia', 'UAE', 'Morocco', 'Tunisia', 'Palestine', 'Tajine', 'Iran', 'Iraq', 'baba']
    # for description in data:
    #     if description['description'] != None:
    #         dataDescription = description['description']
    # if dataDescription != "":
    #     listWords = word_tokenize(dataDescription)[:20]
    #     allsyns1 = set(ss for word in arabList for ss in wordnet.synsets(word))
    #     allsyns2 = set(ss for word in listWords for ss in wordnet.synsets(word))
    #     best = max((wordnet.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in
    #             product(allsyns1, allsyns2))
    #     if best.__getitem__(0) > 0.85:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False


def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')

    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results,
                                                                          language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()

    return search_term, response.text


def parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')

    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:

        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                found_results.append({'keyword': keyword, 'rank': rank, 'title': title, 'description': description})
                rank += 1
    return found_results


def scrape_google(search_term, number_results, language_code):
    try:
        keyword, html = fetch_results(search_term, number_results, language_code)
        results = parse_results(html, keyword)
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")


def imageSearch(keyword):
    response = pythonImageSearch.googleimagesdownload()   # class instantiation
    arguments = {"keywords": keyword, "limit": 1, "la": "Arabic"}   # creating list of arguments
    url = response.download(arguments)   # passing the arguments to the function
    return url
#
#
# if __name__ == '__main__':
#     response = ocr("levant_menu.png")
#     i = 0
#     imageList = []
#     finalResponse = []
#     imageList = []
#     for result in response['responses'][0]['textAnnotations']:
#         if i != 0:
#             isDish = word_analysis(result['description'])
#             if isDish:
#                 finalResponse.append(result)
#                 imageUrl = imageSearch(result['description'])
#                 imageList.append({result['description'], imageUrl})
#
#         i = i + 1
#     print(finalResponse)
#     print(imageList)



