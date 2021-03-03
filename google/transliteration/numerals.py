# ISO Language code to numeric script name
LANG2SCRIPT = {
    # Indo-Aryan
    'as': 'Bengali-Assamese',
    'bn': 'Bengali-Assamese',
    'gu': 'Gujarati',
    'hi': 'Devanagari',
    'mr': 'Devanagari',
    'ne': 'Devanagari',
    'or': 'Oriya',
    'pa': 'Gurmukhi',
    'sa': 'Devanagari',
    'si': 'Sinhala',

    # Dravidian
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'ta': 'Tamil',
    'te': 'Telugu',
    
    # South-East Asia
    'bo': 'Tibetan',
    'lo': 'Lao',
    'my': 'Burmese',
    'sat': 'Ol Chiki',
    'th': 'Thai',

    # Cyrllic
    'be': 'Greek-Upper',
    'bg': 'Greek-Upper',
    'ru': 'Greek-Upper',
    'sr': 'Greek-Upper',
    'uk': 'Greek-Upper',
    
    # PersoArabic
    'ar': 'Central-Arabic',
    'fa': 'Eastern-Arabic',
    'ur': 'Eastern-Arabic',
    
    # Chinese family
    'ja': 'Chinese',
    'ko': 'Chinese',
    'yue-hant': 'Chinese',
    'zh-hant': 'Chinese',
    'zh': 'Chinese',
    
    # African
    'am': 'Geʽez',
    'ti': 'Geʽez',
    
    # More scripts
    'el': 'Greek-Lower',
    'he': 'Hebrew',
    
}

EN_NUMERALS = '0123456789'

NATIVE_NUMERALS = {
    # Brahmic scripts
    'Bengali-Assamese'  : '০১২৩৪৫৬৭৮৯',
    'Burmese'           : '၀၁၂၃၄၅၆၇၈၉',
    'Devanagari'        : '०१२३४५६७८९',
    'Gujarati'          : '૦૧૨૩૪૫૬૭૮૯',
    'Gurmukhi'          : '੦੧੨੩੪੫੬੭੮੯',
    'Kannada'           : '೦೧೨೩೪೫೬೭೮೯',
    'Lao'               : '໐໑໒໓໔໕໖໗໘໙',
    'Malayalam'         : '൦൧൨൩൪൫൬൭൮൯',
    'Ol Chiki'          : '᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙',
    'Oriya'             : '୦୧୨୩୪୫୬୭୮୯',
    'Sinhala'           : '෦෧෨෩෪෫෬෭෮෯',
    'Tamil'             : '௦௧௨௩௪௫௬௭௮௯',
    'Telugu'            : '౦౧౨౩౪౫౬౭౮౯',
    'Thai'              : '๐๑๒๓๔๕๖๗๘๙',
    'Tibetan'           : '༠༡༢༣༤༥༦༧༨༩',
    
    'Hindu-Arabic'      : EN_NUMERALS,
    
    # Arabic
    'Eastern-Arabic'    : '۰۱۲۳۴۵۶۷۸۹',
    'Central-Arabic'    : '٠١٢٣٤٥٦٧٨٩',
    
    'Hebrew'            : '0אבגדהוז‎חט',
    
    # TODO: Add Macron diacritic on top?
    'Greek-Lower'      : '0αβγδεϛζηθ',
    'Greek-Upper'      : '0ΑΒΓΔΕϚΖΗΘ',
    'Geʽez'            : '0፩፪፫፬፭፮፯፰፱',
    
    'Chinese'          : '〇一二三四五六七八九',
}

NUMERAL_MAP = {
    script: str.maketrans({en: l for en, l in zip(EN_NUMERALS, numerals)})
        for script, numerals in NATIVE_NUMERALS.items()
}

def transliterate_numerals(text: str, lang_code: str) -> str:
    """Convert standard Hindu-Arabic numerals in given text to native numerals

    Args:
        text (str): The text in which numeral digits should be transliterated.
        lang_code (str): The target language's ISO639 code

    Returns:
        str: Returns transliterated text with numerals converted to native form.
    """
    if lang_code == 'en':
        return text
    return text.translate(NUMERAL_MAP[LANG2SCRIPT[lang_code]])
