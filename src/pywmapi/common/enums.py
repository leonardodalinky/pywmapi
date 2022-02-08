from enum import Enum


class Platform(Enum):
    pc = "pc"
    xbox = "xbox"
    ps4 = "ps4"
    switch = "switch"


class Language(Enum):
    en = "en"
    ru = "ru"
    ko = "ko"
    de = "de"
    fr = "fr"
    pt = "pt"
    zh_hans = "zh-hans"
    zh_hant = "zh-hant"
    es = "es"
    it = "it"
    pl = "pl"


class OrderType(Enum):
    sell = "sell"
    buy = "buy"


class IncludeOption(Enum):
    item = "item"
