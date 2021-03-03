# Google Input Tools - Transliteration scripts

Transliterate from romanized text to any of the following languages.

Note:  
- Google Input Tools actually uses back-transliteration models for conversion.
  - Hence it might not produce good results for English language words, because English is phonetically impure (In English, pronounciations vary from the way we write it in Latin alphabet)

## Languages Supported

([Source](https://www.google.com/intl/en/inputtools/help/languages.html))

### Indic scripts

|Language|ISO639 Code|
|--------|-----------|
|Assamese (অসমীয়া)|as|
|Bengali (বাংলা)|bn|
|Gujarati (ગુજરાતી)|gu|
|Hindi (हिन्दी)|hi|
|Kannada (ಕನ್ನಡ)|kn|
|Malayalam (മലയാളം)|ml|
|Marathi (मराठी)|mr|
|Nepali (नेपाली)|ne|
|Oriya (ଓଡ଼ିଆ)|or|
|Punjabi (ਪੰਜਾਬੀ)|pa|
|Sanskrit (संस्कृतम्)|sa|
|Sinhala (සිංහල)|si|
|Tamil (தமிழ்)|ta|
|Telugu (తెలుగు)|te|

### Cyrillic scripts

|Language|ISO639 Code|
|--------|-----------|
|Belarusian (беларуски)|be|
|Bulgarian (български)|bg|
|Russian (русский)|ru|
|Serbian (српски)|sr|
|Ukranian (украї́нська)|uk|

### PersoArabic scripts

|Language|ISO639 Code|
|--------|-----------|
|Arabic (عَرَبِيّ)|ar|
|Persian (فارسی)|fa|
|Urdu (اُردُو)|ur|

### More scripts

|Language|ISO639 Code|
|--------|-----------|
|Amharic (አማርኛ)|am|
|Greek (ελληνικά)|el|
|Hebrew (עִבְרִית‎)|he|
|Japanese (日本語)|ja|
|Thai (ภาษาไทย)|th|
|Tigrinya (ትግርኛ)|ti|

### Chinese scripts

|Language|Usage Code|Supported Input Schemes|
|--------|-----------|------------|
|Simplified Chinsese (Zhōngwén)|zh|`pinyin`, `pinyin-x0-shuangpin-abc`, `pinyin-x0-shuangpin-ms`, `pinyin-x0-shuangpin-flypy`, `pinyin-x0-shuangpin-jiajia`, `pinyin-x0-shuangpin-ziguang`, `pinyin-x0-shuangpin-ziranma`, `wubi-1986`|
|Traditional Chinese (Taiwan)|zh-hant|`pinyin`, `cangjie-1982`|
|Yue (HongKong Chinese)|yue-hant|`jyutping`, `und`|

Note:  
- `und` means undefined, by which Google uses default transliterator.

#### Chinese Usage

```py
from google.transliteration import transliterate_text
result = transliterate_text('Zen', lang_code='zh', input_scheme='pinyin')
print(result)
```
