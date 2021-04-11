from collections import Counter
import re

synonyms = {
    'хагрид': re.compile(r'''
        hagrid
        |
        хагри+[тдл]
    ''', re.VERBOSE),

    'толстой': re.compile(r'''
        т[ао]ль?сто[йг]
        |
        левниколаевич
        |
        описаниедуба
        |
        войнуимир
    ''', re.VERBOSE),

    'карлмаркс': re.compile(r'''
        карламарла
        |
        маркс
        |
        капитал
        |
        правойрукемарс
    ''', re.VERBOSE),

    'распутин': re.compile(r'''
        распут[иі]н
    ''', re.VERBOSE),

    'бэбэй': re.compile(r'''
        б[эе]б[эес]й?
    ''', re.VERBOSE),

    'дамблдор': re.compile(r'''
        дамбл[дб]ор
    ''', re.VERBOSE),

    'мэнсон': re.compile(r'''
        менсон
    ''', re.VERBOSE),

    'пронька': re.compile(r'''
        пронька
    ''', re.VERBOSE),

    'перельман': re.compile(r'''
        перельман
    ''', re.VERBOSE),
    
    'достоевский': re.compile(r'''
        достоевский?
    ''', re.VERBOSE),

    'батюшка': re.compile(r'''
        батюшка
    ''', re.VERBOSE),

    'гендальф': re.compile(r'''
        гендальф
    ''', re.VERBOSE),

    'иисус': re.compile(r'''
        и?исус
    ''', re.VERBOSE),

    'бакунин': re.compile(r'''
        бакунин
    ''', re.VERBOSE),

    'менделеев': re.compile(r'''
        менделеев
    ''', re.VERBOSE),
}


def replace_with_synonym(text: str) -> str:
    '''Replace text with synonym
    '''
    for (s, r) in synonyms.items():
        if r.search(text):
            return s
    return text


def construct_with_synonyms(comments: list[str]) -> dict[str, int]:
    c = Counter()
    for (s, r) in synonyms.items():
        for text in comments:
            c[s] += 1 if r.search(text) else 0
    return c
