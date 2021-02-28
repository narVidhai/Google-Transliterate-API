import requests
import json
import sys

G_API = 'https://inputtools.google.com/request?text=%s&itc=%s-t-i0-und&num=%d'
G_API_PINYIN = 'https://inputtools.google.com/request?text=%s&itc=%s-t-i0-pinyin&num=%d'

PINYIN_LANGS = {'zh'}

def transliterate_word(word: str, lang_code: str, max_suggestions: int = 6) -> list:
    """Transliterate a given word to the required language.

    Args:
        word (str): The word to transliterate from Latin/Roman (English) script
        lang_code (str): The target language's ISO639 code
        max_suggestions (int, optional): Maximum number of suggestions to fetch. Defaults to 6.

    Returns:
        list: List of suggested transliterations.
    """
    api_url = G_API_PINYIN if lang_code in PINYIN_LANGS else G_API
    response = requests.get(api_url % (word.lower(), lang_code, max_suggestions), allow_redirects=False, timeout=5)
    r = json.loads(response.text)
    if 'SUCCESS' not in r[0] or response.status_code != 200:
        print('Request failed with status code: %d\nERROR: %s' % (response.status_code, response.text), file=sys.stderr)
        return []
    return r[1][0][1]

def transliterate_text(text: str, lang_code: str) -> str:
    """[Experimental] Transliterate a given sentence or text to the required language.

    Args:
        text (str): The text to transliterate from Latin/Roman (English) script.
        lang_code (str): The target language's ISO639 code

    Returns:
        str: Transliterated text.
    """
    result = []
    for word in text.split():
        # TODO: Handle punctuations and numbers?
        result.append(transliterate_word(word, lang_code, 1)[0])
    return ' '.join(result)
