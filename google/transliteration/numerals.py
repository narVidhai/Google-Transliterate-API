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
    'yue': 'Chinese',
    'zh': 'Chinese',
    
    # African
    'am': 'Geʽez',
    'ti': 'Geʽez',
    
    # More scripts
    'el': 'Greek-Lower',
    'he': 'Hebrew',
    'th': 'Thai',
    
}

EN_NUMERALS = '0123456789'

NATIVE_NUMERALS = {
    # Brahmic scripts
    'Bengali-Assamese'  : '০১২৩৪৫৬৭৮৯',
    'Devanagari'        : '०१२३४५६७८९',
    'Gujarati'          : '૦૧૨૩૪૫૬૭૮૯',
    'Gurmukhi'          : '੦੧੨੩੪੫੬੭੮੯',
    'Kannada'           : '೦೧೨೩೪೫೬೭೮೯',
    'Malayalam'         : '൦൧൨൩൪൫൬൭൮൯',
    'Oriya'             : '୦୧୨୩୪୫୬୭୮୯',
    'Sinhala'           : '෦෧෨෩෪෫෬෭෮෯',
    'Tamil'             : '௦௧௨௩௪௫௬௭௮௯',
    'Telugu'            : '౦౧౨౩౪౫౬౭౮౯',
    'Thai'              : '๐๑๒๓๔๕๖๗๘๙',
    
    # Arabic
    'Eastern-Arabic'    : '۰۱۲۳۴۵۶۷۸۹',
    'Central-Arabic'    : '٠١٢٣٤٥٦٧٨٩',
    
    'Hebrew'            : '0אבגדהוז‎חט',
    
    # TODO: Add Macron diacritic on top?
    'Greek-Lower'      : '0αβγδεϛζηθ',
    'Greek-Upper'      : '0ΑΒΓΔΕϚΖΗΘ',
    'Geʽez'            : '፩፪፫፬፭፮፯፰፱',
    
    'Chinese'          : '〇一二三四五六七八九',
}

NUMERAL_MAP = {
    script: str.maketrans({en: l for en, l in zip(EN_NUMERALS, numerals)})
        for script, numerals in NATIVE_NUMERALS.items()
}

def transliterate_numerals(s: str, lang_code: str) -> str:
    """Convert from standard Hindu-Arabic numerals to native numerals

    Args:
        s (str): The text to transliterate from.
        lang_code (str): The target language's ISO639 code

    Returns:
        str: Returns transliterated text with numerals converted to native form.
    """
    if lang_code == 'en':
        return s
    return s.translate(NUMERAL_MAP[LANG2SCRIPT[lang_code]])
