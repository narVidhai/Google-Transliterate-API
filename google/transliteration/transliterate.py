import requests
import json
import sys
from .numerals import transliterate_numerals

G_API_DEFAULT = 'https://inputtools.google.com/request?text=%s&itc=%s-t-i0&num=%d'
G_API_CHINESE = 'https://inputtools.google.com/request?text=%s&itc=%s-t-i0-%s&num=%d'

CHINESE_LANGS = {'yue-hant', 'zh', 'zh-hant'}

def transliterate_word(word: str, lang_code: str, max_suggestions: int = 6, input_scheme='pinyin') -> list:
    """Transliterate a given word to the required language.

    Args:
        word (str): The word to transliterate from Latin/Roman (English) script
        lang_code (str): The target language's ISO639 code
        max_suggestions (int, optional): Maximum number of suggestions to fetch. Defaults to 6.
        input_scheme(str, optional): Romanization scheme (Only for Chinese)

    Returns:
        list: List of suggested transliterations.
    """
    if lang_code in CHINESE_LANGS:
        api_url = G_API_CHINESE % (word.lower(), lang_code, input_scheme, max_suggestions)
    else:
        api_url = G_API_DEFAULT % (word.lower(), lang_code, max_suggestions)
        
    response = requests.get(api_url, allow_redirects=False, timeout=5)
    r = json.loads(response.text)
    if 'SUCCESS' not in r[0] or response.status_code != 200:
        print('Request failed with status code: %d\nERROR: %s' % (response.status_code, response.text), file=sys.stderr)
        return []
    return r[1][0][1]

def transliterate_text(text: str, lang_code: str, convert_numerals: bool = False) -> str:
    """[Experimental] Transliterate a given sentence or text to the required language.

    Args:
        text (str): The text to transliterate from Latin/Roman (English) script.
        lang_code (str): The target language's ISO639 code
        convert_numerals (bool): Transliterate numerals. Defaults to False.

    Returns:
        str: Transliterated text.
    """
    result = []
    for word in text.split():
        result.append(transliterate_word(word, lang_code, 1)[0])
    result = ' '.join(result)
    if convert_numerals:
        result = transliterate_numerals(result, lang_code)
    return result
