# Google Transliteration - Python API

A Python library to use Google Transliterate API which powers the [G Input Tools](https://www.google.com/intl/en/inputtools/try/).

Install using:  
```
pip install google-transliteration-api
```

Note:  
- This is not Google's official library since [Google has deprecated Input Tools API](https://developers.google.com/transliterate/v1/getting_started).
- Do not confuse with Google Translate API

## Usage

Check [here for list of supported languages](https://github.com/narVidhai/Google-Transliteration-API/blob/master/Languages.md).

### Get suggestions for a word

```py
from google.transliteration import transliterate_word
suggestions = transliterate_word('America', lang_code='ja')
print(suggestions)
```

> ['アメリカ', '米国', '米', '亜米利加', '亜墨利加', '米利堅']

The above transliterates the word 'America' into Japanese script and returns a list of possible suggestions.

### Transliterate a sentence or text

(Experimental)

```py
from google.transliteration import transliterate_text
result = transliterate_text('Hello comrade!', 'ru')
print(result)
```

> хелло комраде!

---

## Similar works

- [Google Input Tools Client](https://github.com/KSubedi/transliteration-input-tools)
- [Google Input Tools VS Code Extension](https://github.com/varunkumar/google-input-tools)
- [AksharaMukha](http://aksharamukha.appspot.com/python) - Brahmic scripts (South Asia and South-East Asia) ([list](http://aksharamukha.appspot.com/documentation))
- [Indic-Trans](https://github.com/libindic/indic-trans)
- [Soviet Transliterate](https://pypi.org/project/transliterate/)

---

Please feel free to contribute by Pull Requests or [raise an issue](https://github.com/NarVidhai/Google-Transliteration-API/issues).

---

## DMCA & Disclaimer

If you're Google and want us to take down the API, please raise an issue mentioning the main contributors.
